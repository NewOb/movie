height = 420;

datasets = {
  "d1": [100000, 100000, 100000, 100000],
  "d2": [20000, 60000, 40000, 90000],
  "d4": [60000, 80000, 10000, 40000],
    "names":["导演", "主演1", "主演2", "主演3"]
};

var lab = ["最高值","平均值","当前值"];
var colors = ["#f98e86","#455d7a","#f95959"];

// var data1 = [100000, 100000, 100000, 100000];   //导演，主演的最高值
// var data2 = [20000, 60000, 40000, 90000];       //当前导演，主演的受欢迎程度
// var data3 = [60000, 80000, 10000, 40000];       //导演，主演的平均值
var names = ["导演", "主演1", "主演2", "主演3"];

console.log(datasets.names);
var svg = d3.select("#bullet")
    .append("svg")
    .attr("id", "bsvg")
    .attr("width", "100%")
    .attr("height", height)
    .append("g");

var yScale = d3.scale.ordinal()
    .domain(names)
    .rangeRoundBands([0, height - 90]);

svg.selectAll(".rlabel")
    .data(colors)
    .enter()
    .append("rect")
    .attr("width",30)
    .attr("height",30)
    .attr("class",".rlabel")
    .attr("fill",function (d) {
        return d
    })
    .attr("transform",function (d,i) {
        return "translate("+(i*150+180)+",340)"
    });

svg.selectAll(".rltext")
    .data(lab)
    .enter()
    .append("text")
    .attr("class",".rltext")
    .text(function (d) {
        return d
    })
    .attr("fill","white")
    .attr("transform",function (d,i) {
        return "translate("+(i*150+173)+",390)"
    })
    .attr("font-size","15px");

var tip1 = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<strong>最高值:</strong> <span style='color:#f98e86'>" + d + "</span>" ;
  });

var tip2 = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<strong>当前值:</strong> <span style='color:#f95959'>" + d + "</span>" ;
  });

var tip3 = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<strong>平均值:</strong> <span style='color:#455d7a'>" + d + "</span>" ;
  });

svg.call(tip1);
svg.call(tip2);
svg.call(tip3);
// var xAxis = d3.svg.axis()
//     .scale(xScale)
//     .orient("bottom");

// var yAxis = d3.svg.axis()
//     .scale(yScale)
//     .orient("left");

var lbar = svg.selectAll(".lbar")
    .data(datasets.d1)
    .enter()
    .append("rect")
    .attr("class", "lbar")
    .attr("y", function (d,i) {
        return yScale(names[i])
    })
    .attr("transform", "translate(110,30)")
    .attr("fill", "#f98e86")
    .attr("rx", 20)
    .attr("ry", 20)
    .attr("width", 500)
    .attr("height", 40)
    .on('mouseover',tip1.show)
    .on('mouseout',tip1.hide);

var zbar = svg.selectAll(".zbar")
    .data(datasets.d2)
    .enter()
    .append("rect")
    .attr("class", "zbar")
    .attr("y", function (d, i) {
        return yScale(names[i])
    })
    .attr("fill", "#f95959")
    .attr("width", function (d, i) {
        return (d / datasets.d1[i]) * 500;
    })
    .attr("rx", 20)
    .attr("ry", 20)
    .attr("transform", "translate(110,30)")
    .attr("height", 40)
.on('mouseover',tip2.show)
    .on('mouseout',tip2.hide);

var qbar = svg.selectAll(".qbar")
    .data(datasets.d4)
    .enter()
    .append("rect")
    .attr("class", "qbar")
    .attr("y", function (d, i) {
        return yScale(names[i])
    })
    .attr("fill", "#455d7a")
    .attr("width",10)
    .attr("rx", 5)
    .attr("ry", 5)
    .attr("transform", function (d,i) {
        var result = (d/datasets.d1[i])*500+110;
        return "translate("+result+",30)"
    })
    .attr("height", 40)
.on('mouseover',tip3.show)
    .on('mouseout',tip3.hide);

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
    lbar.data(d1);

zbar.data(d2)
    .transition()
    .duration(1000)
    .ease("linear")
    .attr("width", function (d, i) {
        return (d / d1[i]) * 500;
    });

qbar.data(d4)
    .transition()
    .duration(1000)
    .ease("linear")
    .attr("transform", function (d,i) {
        var result = (d/d1[i])*500+110;
        return "translate("+result+",30)"
    });
}