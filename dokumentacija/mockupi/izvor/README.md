# Vir mockupov

Vsi zasloni so v `gen.py` (vsako besedilo kot `L("makedonsko", "slovensko")`), videz v `style.css`.

```bash
python3 gen.py                       # ustvari out/mk.html in out/sl.html
node shot.js $PWD/out/sl.html ../sl  # PNG 860×1800 (potreben puppeteer)
node shot.js $PWD/out/mk.html ../mk
```
