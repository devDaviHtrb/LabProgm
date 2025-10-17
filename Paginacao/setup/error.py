# setup/register_handlers.py
import pkgutil
from flask import Flask, render_template
from typing import Tuple

def register_handlers(app: Flask) -> None:
    error_codes = [403, 404, 401]

    def handle_error(err: object) -> Tuple[str, int]:
        print("erro")
        code = getattr(err, "code")
        return render_template("error.html", erro=code), code

    for code in error_codes:
        app.register_error_handler(code, handle_error)