height = 420;

var data1 = [100000, 100000, 100000, 100000];
var data2 = [20000, 60000, 40000, 90000];
var data3 = [60000, 80000, 10000, 40000];
var names = ["导演", "主演1", "主演2", "主演3"];

console.log(names[0]);
var svg = d3.select("#bullet")
    .append("svg")
    .attr("id", "bsvg")
    .attr("width", "100%")
    .attr("height", height);

var yScale = d3.scale.ordinal()
    .domain(names)
    .rangeRoundBands([0, height - 20]);

// var xAxis = d3.svg.axis()
//     .scale(xScale)
//     .orient("bottom");

// var yAxis = d3.svg.axis()
//     .scale(yScale)
//     .orient("left");

var lbar = svg.selectAll(".lbar")
    .data(data1)
    .enter()
    .append("rect")
    .attr("class", "lbar")
    .attr("y", function (d, i) {
        return yScale(names[i])
    })
    .attr("transform", "translate(110,30)")
    .attr("fill", "#EB9FA0")
    .attr("rx", 20)
    .attr("ry", 20)
    .attr("width", 500)
    .attr("height", 40);

var zbar = svg.selectAll(".zbar")
    .data(data2)
    .enter()
    .append("rect")
    .attr("class", "zbar")
    .attr("y", function (d, i) {
        return yScale(names[i])
    })
    .attr("fill", "#EB586F")
    .attr("width", function (d, i) {
        return (d / data1[i]) * 500;
    })
    .attr("rx", 20)
    .attr("ry", 20)
    .attr("transform", "translate(110,30)")
    .attr("height", 40);

var qbar = svg.selectAll(".qbar")
    .data(data3)
    .enter()
    .append("rect")
    .attr("class", "qbar")
    .attr("y", function (d, i) {
        return yScale(names[i])
    })
    .attr("fill", "#2e2e2e")
    .attr("width",10)
    .attr("rx", 5)
    .attr("ry", 5)
    .attr("transform", function (d,i) {
        var result = (d/data1[i])*500+110;
        return "translate("+result+",30)"
    })
    .attr("height", 40);

svg.selectAll(".rtext")
.data(names)
.enter()
.append("text")
.attr("class","rtext")
.attr("fill","#F8FFF7")
.text(function (d) {
    return d;
})
    .attr("y", function (d) {
        return yScale(d)
    })
    .attr("font-size",30)
.attr("transform","translate(20,60)");


//zbar的宽度需要改变
//qbat的translate改变
function rup(d1,d2,d4) {
zbar.transition()
    .duration(1000)
    .ease("linear")
    .data(d2)
    .attr("width", function (d, i) {
        return (d / d1[i]) * 500;
    });

qbar.transition()
    .duration(1000)
    .ease("linear")
    .data(d4)
    .attr("transform", function (d,i) {
        var result = (d/d1[i])*500+110;
        return "translate("+result+",30)"
    })
}