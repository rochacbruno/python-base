"""An Open Trivia Database TUI Client

Click on the proper answer
or select with arrows and press enter

----------------------------------
| What CPU stands for?           |
----------------------------------
| Common Process Unit            |
----------------------------------
| Central Process Uniform        |
----------------------------------
| Central Processing Unit        |
----------------------------------

"""
import html
import random
import sys
from asyncio import sleep
from typing import Optional

import httpx
from rich import print, prompt
from rich.console import RenderableType
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from textual.widgets import Button, ButtonPressed
from textual.widgets import Footer as BaseFooter
from textual.widgets import Header as BaseHeader

CATEGORIES = [
    ("any", "Any Category"),
    ("9", "General Knowledge"),
    ("10", "Entertainment: Books"),
    ("11", "Entertainment: Film"),
    ("12", "Entertainment: Music"),
    ("13", "Entertainment: Musicals; Theatres"),
    ("14", "Entertainment: Television"),
    ("15", "Entertainment: Video Games"),
    ("16", "Entertainment: Board Games"),
    ("17", "Science; Nature"),
    ("18", "Science: Computers"),
    ("19", "Science: Mathematics"),
    ("20", "Mythology"),
    ("21", "Sports"),
    ("22", "Geography"),
    ("23", "History"),
    ("24", "Politics"),
    ("25", "Art"),
    ("26", "Celebrities"),
    ("27", "Animals"),
    ("28", "Vehicles"),
    ("29", "Entertainment: Comics"),
    ("30", "Science: Gadgets"),
    ("31", "Entertainment: Japanese Anime; Manga"),
    ("32", "Entertainment: Cartoon; Animations"),
]
LEVELS = ("any", "easy", "medium", "hard")

API_BASE_URL = "https://opentdb.com/api.php"


def request_questions(amount=20, level=None, category=None):
    """returns a list[dict] of questions"""

    params = {
        "amount": amount,
        "type": "multiple",
        "cache_bypass": random.randint(1, 10000),
    }
    if level:
        params["difficulty"] = level
    if category:
        params["category"] = category

    response = httpx.get(
        API_BASE_URL,
        params=params,
    )
    response.raise_for_status()
    return response.json()["results"]


class Question(Widget):
    def __init__(self, text: str, name: Optional[str] = None) -> None:
        self.text = html.unescape(text)
        super().__init__(name)

    def render(self) -> Panel:
        return Panel(f"{self.text}", style=("on blue"))

    def update(self, text):
        self.text = html.unescape(text)
        self.refresh()


class Option(Button):
    mouse_over = Reactive(False)

    def __init__(self, text: str, name: Optional[str] = None) -> None:
        text = html.unescape(text)
        self.panel = Panel(f"{text}")
        super().__init__(name)

    def render(self) -> Panel:
        self.panel.style = "on cyan" if self.mouse_over else ""
        return self.panel

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def update(self, text, name):
        self.panel.renderable = html.unescape(text)
        self.name = name
        self.refresh()

    async def set_status(self):
        status = "✅" if self.name == "correct" else "❌"
        self.update(f"{status} {self.panel.renderable}", self.name)
        await sleep(1)


class Header(BaseHeader):
    def render(self) -> RenderableType:
        header_table = Table.grid(padding=(0, 1), expand=True)
        header_table.style = self.style
        header_table.add_column(justify="left", ratio=0, width=8)
        header_table.add_column("status", justify="center", ratio=1)
        header_table.add_column("title", justify="center", ratio=1)
        header_table.add_column("clock", justify="right", width=8)
        header_table.add_row(
            "💡",
            f"{self.app.current_question + 1}/{len(self.app.questions)}",
            self.full_title,
            self.get_clock() if self.clock else "",
        )
        return header_table


class Footer(BaseFooter):
    def render(self) -> RenderableType:
        footer_table = Table.grid(padding=(0, 0), expand=True)
        footer_table.add_column(justify="left", ratio=1)
        footer_table.add_column(justify="right", ratio=1)
        footer_table.add_row(
            Text.assemble(
                ("Quit", "reverse"),
                meta={"@click": "app.press('q')", "key": "q"},
                style="white on dark_green",
            ),
            Text(
                f"✅{self.app.correct_answers}  ❌{self.app.wrong_answers}",
                style="white on dark_green",
            ),
        )
        return footer_table


class TriviaApp(App):
    answers: list
    questions: dict
    current_question: int = 0
    finished: bool = False
    amount: int
    level: Optional[str]
    category: Optional[str]

    def __init__(self, amount=20, level=None, category=None, *args, **kwargs):
        self.amount = amount
        self.level = level
        self.category = category
        super().__init__(*args, **kwargs)

    @property
    def correct_answers(self):
        return len([item for item in self.answers if item == "correct"])

    @property
    def wrong_answers(self):
        return len([item for item in self.answers if item != "correct"])

    @property
    def completed(self):
        return len(self.answers) >= len(self.questions)

    async def on_load(self, event):
        self.answers = []
        self.questions = request_questions(self.amount, self.level, self.category)
        await self.bind("q", "quit")
        question = self.questions[self.current_question]
        self.question = Question(question["question"])
        self.options = [
            Option(question["correct_answer"], name="correct"),
            Option(question["incorrect_answers"][0], name="in_0"),
            Option(question["incorrect_answers"][1], name="in_1"),
            Option(question["incorrect_answers"][2], name="in_2"),
        ]
        random.shuffle(self.options)

    async def handle_button_pressed(self, message: ButtonPressed) -> None:
        """A message sent by the button widget"""
        if self.finished:
            await self.action_quit()
        self.answers.append(message.sender.name)
        await message.sender.set_status()
        if not self.completed:
            self.current_question += 1
            self.next_question()
        else:
            self.finish_screen()

        self.header.refresh()
        self.footer.refresh()

    def finish_screen(self):
        self.finished = True
        self.question.update("🤚🏻🤚🏻 Finished!!! 🤚🏻🤚🏻")
        question_texts = [item["question"] for item in self.questions]
        score = list(zip(self.answers, question_texts))
        right = [item[1] for item in score if item[0] == "correct"]
        self.options[0].update(f"Right anwers: {right}", "")
        wrong = [item[1] for item in score if item[0] != "correct"]
        self.options[1].update(f"Wrong anwers: {wrong}", "")
        self.options[2].update("", "")
        self.options[3].update("🎉 Congrats" if not wrong else "Try Again", "")

    def next_question(self):
        question = self.questions[self.current_question]
        self.question.update(question["question"])
        new_options = [
            (question["correct_answer"], "correct"),
            (question["incorrect_answers"][0], "in_0"),
            (question["incorrect_answers"][1], "in_1"),
            (question["incorrect_answers"][2], "in_2"),
        ]
        random.shuffle(new_options)
        for index, option in enumerate(new_options):
            self.options[index].update(*option)

    async def on_mount(self) -> None:
        await self.view.dock(*self.get_widgets(), edge="top")

    def get_widgets(self):
        self.header = Header(tall=False)
        self.footer = Footer()
        return [self.header, self.question, *self.options, *[self.footer]]


def main(amount=None, category=None, level=None):
    if not amount:
        amount = prompt.Prompt.ask("Number of questions? [20]") or 20

    if not category:
        cat_table = Table()
        cat_table.add_column("number")
        cat_table.add_column("name")
        for number, name in CATEGORIES:
            cat_table.add_row(number, name)
        print(cat_table)
        category = prompt.Prompt.ask("Category Number? [any]").lower() or None
        if category == "any":
            category = None

    if not level:
        print(*LEVELS)
        level = prompt.Prompt.ask("Difficult level? [any]").lower() or None
        if level == "any":
            level = None

    TriviaApp.run(
        title="Trivia",
        level=level,
        category=category,
        amount=amount,
        # log="trivia.log"
    )


if __name__ == "__main__":
    _, *args = sys.argv
    main(*args)
