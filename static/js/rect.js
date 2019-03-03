height = 420;

var data1 = [100000, 100000, 100000, 100000];
var data2 = [20000, 60000, 40000, 90000];
var data3 = [50000, 50000, 50000, 50000];
var name = ["导演", "主演1", "主演2", "主演3"];

var svg = d3.select("#bullet")
    .append("svg")
    .attr("id", "bsvg")
    .attr("width", "100%")
    .attr("height", height);

var yScale = d3.scale.ordinal()
    .domain(name)
    .rangeRoundBands([0, height - 20]);

// var xAxis = d3.svg.axis()
//     .scale(xScale)
//     .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(yScale)
    .orient("left");

// svg.append("g")
//     .attr("class",baxis)
//     .call(yAxis);

svg.selectAll(".lbar")
    .data(data1)
    .enter()
    .append("rect")
    .attr("class", "lbar")
    .attr("y", function (d, i) {
        return yScale(name[i])
    })
    .attr("transform","translate(110,30)")
    .attr("fill", "#EB9FA0")
    .attr("rx",20)
    .attr("ry",20)
    .attr("width", 500)
    .attr("height", 40);

svg.selectAll(".zbar")
    .data(data2)
    .enter()
    .append("rect")
    .attr("class", "zbar")
    .attr("y", function (d, i) {
        return yScale(name[i])
    })
    .attr("fill", "#EB586F")
    .attr("width", function (d,i) {
        return (d/data1[i])*500;
    })
    .attr("rx",20)
    .attr("ry",20)
    .attr("transform","translate(110,30)")
    .attr("height", 40);