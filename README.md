Installation of reveal.js with basic setup:
https://revealjs.com/installation/

build.py receives the source index.html and replaces some tags by the content of the files they reference.

```
while true; do sleep 2; python3 build.py --src reveal.js-master/index_src.html; done
```