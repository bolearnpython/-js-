const puppeteer = require('puppeteer');
(async () => {
    const browser = await puppeteer.launch({args: ['--no-sandbox'], headless: false})
const page = await browser.newPage();
await page.goto('http://wsjs.saic.gov.cn/txnT01.do?y7bRbP=KaltkM10zh10zh10triDHWegi3_iGKEpBPgY7GGba.A');
})()