dataset = ['Comedy', 'Advnameture', 'Fantasy', 'Mystery', 'Thriller', 'Documnametary', 'War', 'Western', 'Romance', 'Drama', 'Horror', 'Action', 'Sci-Fi', 'Music', 'Family', 'Crime'];

d3.select("#cloud").append("svg")
    .attr("class", "c_svg");

function draw(words) {
    d3.select(".c_svg")
        .attr("width", layout.size()[0])
        .attr("height", layout.size()[1])
        .append("g")
        .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
        .selectAll("text")
        .data(words)
        .enter().append("text")
        .attr("class", "cloud_text")
        .attr("text-anchor", "middle")
        .attr("transform", function (d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .style("fill", function (d) {
            return d.color;
        })
        .transition()
        .duration(1000)
        .ease("linear")
        .style("font-size", function (d) {
            return d.size + "px";
        })
        .style("font-family", "Impact")
        .text(function (d) {
            return d.text;
        });
}


var cloud = d3.layout.cloud()
    .size([600, 500])  // 宽高
    .words(dataset.map(function (d, i) {
        return {text: d, size: 10 + Math.random() * 90, color: t_color[i]};
    }))  // 数据
    .padding(5)  // 内间距
    .rotate(function () {
        return ~~(Math.random() * 2) * 90;
    })
    .font("Impact")
    .fontSize(function (d) {
        return d.size;
    })
    .on("end", draw);

cloud.start();

