#!/usr/bin/env python3

from flask import Flask
from dotenv import load_dotenv
from os import getenv

from utils.db import init_db, insert_test

load_dotenv()

SECRET_TOKEN = getenv("JWT_SECRET", None)
BIND_ADDRESS = getenv("BIND_ADDRESS", "0.0.0.0")
PORT = getenv("PORT", 9999)
DEBUG = getenv("DEBUG", True)


def start():
    engine = init_db()
    insert_test(engine)
    # app = Flask(__name__)

    # app.run(BIND_ADDRESS, PORT, DEBUG, True)


if __name__ == "__main__":
    if not SECRET_TOKEN:
        print("Aie aie pas de secret token")
        exit(1)
    start()
