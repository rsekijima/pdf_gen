"""
pdf_gen base module.
"""

from dotenv import load_dotenv

from pdf_gen.gui import MainWindow

NAME = "pdf_gen"

load_dotenv()


def main():  # pragma: no cover
    app = MainWindow()
    app.mainloop()
