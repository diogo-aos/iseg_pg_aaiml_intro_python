Installation of reveal.js with basic setup:
https://revealjs.com/installation/

build.py receives the source index.html and replaces some tags by the content of the files they reference.

```
# setup revealjs - download revealjs, unzip and remove zip
curl -L https://github.com/hakimel/reveal.js/archive/master.zip -o temp.zip && unzip temp.zip && rm temp.zip

# build
python3 build.py --src index_src.html --loop True

# serve
python3 -m http.server 8000
```