Installation of reveal.js with basic setup:
https://revealjs.com/installation/

build.py receives the source index.html and replaces some tags by the content of the files they reference.

```
python build.py --src index_src.html --loop True
python content\slides\iseg_python\build.py --src content\slides\iseg_python\index_src.html --loop True
python -m http.server 8000
```