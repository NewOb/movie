// 评分
var config1 = liquidFillGaugeDefaultSettings();
// 票房
var config2 = liquidFillGaugeDefaultSettings();

config1.circleColor = "#eb586f";
config1.textColor = "#eb586f";
config1.waveTextColor = "#eb8b8b";
config1.waveColor = "#eb586f";

config2.circleColor = "#eb586f";
config2.textColor = "#eb586f";
config2.waveTextColor = "#eb8b8b";
config2.waveColor = "#eb586f";

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
    .attr("transform", "translate(50,100)")
    .attr("fill", "#eb586f")
    .text("评分：" + score);

var result2 = svg2.append("text")
    .attr("class", "result")
    .attr("transform", "translate(30,100)")
    .attr("fill", "#eb586f")
    .text("票房：" + box_office);

var chart1 = loadLiquidFillGauge("fillgauge1", 0, config1);
var chart2 = loadLiquidFillGauge("fillgauge2", 0, config2);

function Result(score, box_office,max_box) {
    // 传入参数“评分”“票房”“最高票房”

    var bf = box_office/100000000;
    //将票房单位改为亿
    config1.value = score*10;
    config2.value = (box_office/max_box)*100;

    chart1.update(config1.value);
    chart2.update(config2.value);

    result1.transition()
        .duration(1000)
        .tween("text",function () {
            var i = d3.interpolate(this.textContent,parseFloat(score).toFixed(1));
            return function (t) {
                this.textContent = "评分：" + i(t)
            }
        })

    result2.transition()
        .duration(1000)
        .tween("text",function () {
            var i = d3.interpolate(this.textContent,parseFloat(bf).toFixed(2));
            return function (t) {
                this.textContent = "票房：" + i(t) + "亿"
            }
        })
}