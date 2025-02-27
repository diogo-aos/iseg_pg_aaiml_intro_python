import argparse
from pathlib import Path
import re

parser = argparse.ArgumentParser(
    description='render RevealJS presentation')
parser.add_argument(
    '--src', default="index_src.html", type=Path,
    help='the file with the source index')

parser.add_argument(
    '--loop', default=False, type=bool,
    help='the file with the source index')
args = parser.parse_args()

#print(args)


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

markdown_template_slide = '\n<section data-markdown="{md_path}" \n' \
                          'data-separator="^\r?\n---\r?\n$" \n' \
				          'data-separator-vertical="^\r?\n--\r?\n$" \n' \
				          '> \n'

def insert_markdown(md_src: Path, html_file: Path):
    raise NotImplemented
    # md_src is assumed to be at the same level as html file

    # get all markdown files
    all_paths = sorted(markdown_src_dir.iterdir())
    md_files = [p for p in all_paths if p.is_file() and '.md' in str(p).lower()]

    # compile markdown insertion code
    html_md = ...
    for files in md_files:
         ...


def run():
    src_html_file: Path = args.src

    src_html = src_html_file.read_text()

    new_html = replace_code(src_html, src_html_file)

    out_file = src_html_file.parent.joinpath("index.html")
    out_file.write_text(new_html)

if args.loop:
    import time
    import datetime
    while True:
        run()
        print(f"executed at {datetime.datetime.now()}")
        time.sleep(2)
else:
    run()
