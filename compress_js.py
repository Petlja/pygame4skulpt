import os
from pathlib import Path
import fileinput


def main() -> None:
    pygame_path = "./pygame/"
    file_list = (i for i in Path(pygame_path).iterdir() if i.is_file() and i.glob("*.js"))
    dist_path = Path("./pygame_dist")
    dist_path.mkdir(exist_ok=True)

    for file in file_list:
        compress_js(file)
        print(f"file: {file} finish compress")


def compress_js(file: Path):
    dist_path = Path("./pygame_dist")
    res_file_path = dist_path / file.name
    res_file_name = res_file_path.as_posix()
    es6_to_5_cmd = f"babel {file.as_posix()} -o {res_file_name}"
    os.system(es6_to_5_cmd)

    # remove first line
    [print(line, end="") for line in fileinput.input(res_file_name, inplace=1) if not fileinput.isfirstline()]
    compress_cmd = f"uglifyjs {res_file_name} -m -o {res_file_name}"
    os.system(compress_cmd)


if __name__ == "__main__":
    main()
