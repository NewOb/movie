// 评分
var config1 = liquidFillGaugeDefaultSettings();
// 票房
var config2 = liquidFillGaugeDefaultSettings();


config1.circleColor = "#178BCA";
config1.textColor = "#045681";
config1.waveTextColor = "#A4DBf8";
config1.waveColor = "#178BCA";
config1.maxValue = 10;

config2.circleColor = "#178BCA";
config2.textColor = "#045681";
config2.waveTextColor = "#A4DBf8";
config2.waveColor = "#178BCA";

var chart1 = loadLiquidFillGauge("fillgauge1", 5.0, config1);
var chart2 = loadLiquidFillGauge("fillgauge2", 100000000.0, config2);

d3.select("#stext")
    .append("h3")
    .attr("class", "result")
    .text("评分：" + "5.0");

d3.select("#btext")
    .append("h3")
    .attr("class", "result")
    .text("票房：" + "1亿");