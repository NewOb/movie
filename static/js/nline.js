var years = [];
var datasets = [];
for (var i = 1990; i <= 2016; i++) {
    years.push(i);
    datasets.push(Math.ceil(Math.random()*600));
}
console.log(datasets);
var height = 280;
var width = 470;

var lsvg = d3.select("#line")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("class", "l_svg");

var xscale = d3.scale.ordinal()
    .domain(years)
    .rangeRoundPoints([0, width - 30]);

var yscale = d3.scale.linear()
    .domain([0, 600])
    .range([height - 30, 0]);

var xa = d3.svg.axis()
    .scale(xscale)
    .orient("bottom")
    .tickValues([1990, 1995, 2000, 2005, 2010, 2015]);

var ya = d3.svg.axis()
    .scale(yscale)
    .orient("left");

var gxAxis = lsvg.append("g")
    .attr("class", "xaxis")
    .attr("transform", "translate(40," + (height - 20) + ")")
    .call(xa)
    .append("text")
    .attr("x", width - 40)
    .attr("y", -5)
    .style("text-anchor", "end")
    .attr("fill", "#ffffff")
    .text("年份");

var gyAxis = lsvg.append("g")
    .attr("class", "yaxis")
    .attr("transform", "translate(40,10)")
    .call(ya)
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("x", 4)
    .attr("y", 15)
    .style("text-anchor", "end")
    .attr("fill", "#ffffff")
    .text("点赞量");

 var line = d3.svg.line()
        .x(function (d, i) {
            return xscale(i + 1990);
        })
        .y(function (d) {
            return yscale(d);
        })
     .interpolate("basis");

   lsvg.append("path")
        .attr("class", "line_path")
        .attr("d", line(datasets))
        .attr("transform", "translate(40,0)")
        .attr("fill", "none")
        .attr("stroke", "#f95959")
        .attr("stroke-width", "4px");