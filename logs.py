#!/usr/bin/env python3

import os
import logging
from logging import handlers

# BOILERPLATE (que deve ser encapulado em uma função posteriormente)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("bruno", log_level)
# ch = logging.StreamHandler()  # Console/terminal/stderr
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=300,  # 10**6
    backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s  %(name)s  %(levelname)s " "l:%(lineno)d f:%(filename)s: %(message)s"
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)
# log.addHandler(ch)
log.addHandler(fh)


"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
