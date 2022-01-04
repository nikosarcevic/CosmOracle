from pathlib import Path

def read_markdown(markdown_file):
        return Path(markdown_file).read_text()

def read_eq(equation_file):
        return Path(equation_file).read_text()
