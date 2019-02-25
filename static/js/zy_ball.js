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

var svg1 = d3.select("#stext")
    .append("svg")
    .attr("id", "st")
    .attr("width", "100%")
    .attr("height", 190);


var svg2 = d3.select("#btext")
    .append("svg")
    .attr("id", "bt")
    .attr("width", "100%")
    .attr("height", 190);

var result1 = svg1.append("text")
    .attr("class", "result")
    .attr("transform", "translate(100,100)")
    .attr("fill", "#eb586f")
    .text("评分：" + score);

var result2 = svg2.append("text")
    .attr("class", "result")
    .attr("transform", "translate(100,100)")
    .attr("fill", "#eb586f")
    .text("票房：" + box_office);

var chart1 = loadLiquidFillGauge("fillgauge1", 0, config1);
var chart2 = loadLiquidFillGauge("fillgauge2", 0, config2);

function Result(score, box_office) {
    config1.value = score;
    config2.value = box_office;

    chart1.update(config1.value);
    chart2.update(config2.value);

        result1.transition()
        .duration()
        .ease("linear")
        .text("评分" + score);

        result2.transition()
        .duration(1000)
        .tween("text", function () {
            var that = d3.select("this"),
                i = d3.interpolate(that.text(), score);
            return function (t) {
                that.text("评分："+i(t));
            }
        });
}