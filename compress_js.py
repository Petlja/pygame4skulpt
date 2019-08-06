import os
import fileinput
import token
import tokenize
from pathlib import Path
from typing import NoReturn, Union

dist_path = Path("./pygame_dist")


def main() -> NoReturn:
    """
    compress all js file
    :return:
    """
    pygame_path = "./pygame/"
    file_list = (i for i in Path(pygame_path).iterdir() if i.is_file() and i.glob("*.js|*.py"))
    dist_path.mkdir(exist_ok=True)

    for file in file_list:
        res_file_path = dist_path / file.name
        if res_file_path.exists():
            res_file_path.unlink()
        if file.match("*.js"):
            compress_js(file)
            print(f"file: {file} finish compress success")
        elif file.match("*.py"):
            res_file_path = dist_path / file.name
            try:
                remove_file_comment(file, res_file_path)
                print(f"success move {file.as_posix()}, and remove comment")
            except IOError:
                print(f"Permission denied, please try again: {file.as_posix()}")


def compress_js(file: Path) -> NoReturn:
    """
    now compress
    babel --> make es6 -> es5
    uglifyjs --> get compress js file (must use es5 js file)
    :param file:
    :return:
    """
    res_file_path = dist_path / file.name
    res_file_name = res_file_path.as_posix()
    es6_to_5_cmd = f"babel {file.as_posix()} -o {res_file_name}"
    os.system(es6_to_5_cmd)

    # remove first line
    [print(line, end="") for line in fileinput.input(res_file_name, inplace=1) if not fileinput.isfirstline()]
    compress_cmd = f"uglifyjs {res_file_name} -m -o {res_file_name}"
    os.system(compress_cmd)


def remove_file_comment(fname: Union[str, Path], r_fname: Union[str, Path]) -> NoReturn:
    """ Run on just one file.

    """
    source = open(fname, encoding="u8")
    mod = open(r_fname, "w", encoding="u8")

    prev_toktype = token.INDENT
    last_lineno = -1
    last_col = 0

    tokgen = tokenize.generate_tokens(source.readline)
    for toktype, ttext, (slineno, scol), (elineno, ecol), _ in tokgen:
        if slineno > last_lineno:
            last_col = 0
        if scol > last_col:
            mod.write(" " * (scol - last_col))
        if toktype == token.STRING and prev_toktype == token.INDENT:
            # Docstring
            continue
        elif toktype == tokenize.COMMENT:
            # Comment
            continue
        else:
            mod.write(ttext)
        prev_toktype = toktype
        last_col = ecol
        last_lineno = elineno
    mod.close()
    source.close()


if __name__ == "__main__":
    main()
