const express=require('express');
const bodyParser=require('body-parser');
var http = require('http');
const puppeteer = require('puppeteer');
(async () => {
    const browser = await puppeteer.launch({args: ['--no-sandbox'], headless: true})
const page = await browser.newPage();
await page.goto('https://m.ctrip.com/webapp/hotel/shanghai2/');
solve=async (data) =>{
    const dimensions = await page.evaluate(function (data){
        eval(data["_s"]);
        var getEleven;
        eval("var "+'____casf1'+" = function(a){getEleven = a}");
        eval(data["_s"]);
        var getEleven;
        eval("var "+'____casf1'+" = function(a){getEleven = a}");
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
            key:getEleven()
        };
    },data);
    return dimensions['key']
}
var server=express();
server.listen(8080);
server.use(bodyParser.urlencoded({
    extended: false,                 //扩展模式
    limit:    2*1024*1024           //限制-2M
}));
server.use('/', async function (req, res){
    var data=await req.body
    console.log(data); //POST
    var key=await solve(data)
    console.log(key)
    res.send(JSON.stringify({'key':key}));
    // res.end(JSON.stringify({'key':key}))
    //req.query   GET
    //req.body    POST
});
})()