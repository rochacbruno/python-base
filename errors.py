#!/usr/bin/env python3
import time
import logging

log = logging.Logger("errors")


# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)


def try_to_open_a_file(filepath, retry=1) -> list:
    """Tries to open a file, if error, retries n times."""
    if retry > 999:
        raise ValueError("Retry cannot be above 999")

    try:
        return open(filepath).readlines()  # FileNotFoundError
    except FileNotFoundError as e:
        log.error("ERRO: %s", e)
        time.sleep(2)
        if retry > 1:
            # recursão
            return try_to_open_a_file(filepath, retry=retry - 1)
    else:
        print("Sucesso!!!")
    finally:
        print("Execute isso sempre!")

    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)
