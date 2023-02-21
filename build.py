import argparse
from pathlib import Path
import re

parser = argparse.ArgumentParser(
    description='render RevealJS presentation')
parser.add_argument(
    '--src', default="index_src.html", type=Path,
    help='the file with the source index')
args = parser.parse_args()


print(args)

src_html_file: Path = args.src

src_html = src_html_file.read_text()


def replace_code(txt: str, txt_file: Path):
    matches = re.finditer(".*\{\{code:.*\}\}", txt)
    for m in matches:
        print(m.group().strip())
        # get path to code
        match_txt = m.group()
        code_path = match_txt[match_txt.find("{{code:")+7:-2]
        code_file = txt_file.parent.joinpath(code_path)
        # read code
        code = code_file.read_text()
        # replace
        txt = txt.replace(match_txt, code)
        #txt = txt[:m.start()] + code + txt[m.end()+1:]
    return txt

src_html = replace_code(src_html, src_html_file)

out_file = src_html_file.parent.joinpath("index.html")
out_file.write_text(src_html)