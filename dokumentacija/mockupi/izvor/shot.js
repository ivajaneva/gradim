const puppeteer = require('puppeteer');
(async () => {
  const [,, html, outDir] = process.argv;
  const b = await puppeteer.launch({args:['--no-sandbox']});
  const p = await b.newPage();
  await p.setViewport({width:430, height:900, deviceScaleFactor:2});
  await p.goto('file://' + html, {waitUntil:'networkidle0'});
  await p.evaluateHandle('document.fonts.ready');
  const ids = await p.$$eval('.wrap', els => els.map(e => e.id));
  for (const id of ids) { const el = await p.$('#' + id); await el.screenshot({path: `${outDir}/${id}.png`, omitBackground:true}); }
  await b.close();
})();
