// 评分
var config1 = liquidFillGaugeDefaultSettings();
// 票房
var config2 = liquidFillGaugeDefaultSettings();

config1.circleColor = "#eb586f";
config1.textColor = "#eb586f";
config1.waveTextColor = "#eb8b8b";
config1.waveColor = "#eb586f";
config1.maxValue = 10;

config2.circleColor = "#eb586f";
config2.textColor = "#eb586f";
config2.waveTextColor = "#eb8b8b";
config2.waveColor = "#eb586f";
config2.maxValue = 10000000000;

var score = 0;
var box_office = 0;

d3.select("#stext")
    .append("h3")
    .attr("class", "result")
    .attr("id","stext")
    .text("评分：" + score);

d3.select("#btext")
    .append("h3")
    .attr("class", "result")
    .attr("id","btext")
    .text("票房：" + box_office);

var chart1 = loadLiquidFillGauge("fillgauge1", 0, config1);
var chart2 = loadLiquidFillGauge("fillgauge2", 0, config2);

function Result(score, box_office) {
    config1.value = score;
    config2.value = box_office;

    chart1.update(config1.value);
    chart2.update(config2.value);

    d3.select("#stext")
        .transition()
        .duration()
        .ease("linear")
        .text("评分"+score);

    d3.select("#btext")
        .transition()
        .duration()
        .ease("linear")
        .text("评分"+box_office);
}