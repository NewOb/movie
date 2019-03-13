dataset = ['Comedy', 'Advnameture', 'Fantasy', 'Mystery', 'Thriller', 'Documnametary', 'War', 'Western', 'Romance', 'Drama', 'Horror', 'Action', 'Sci-Fi', 'Music', 'Family', 'Crime'];
var Height = 280;
var Width = 470;

d3.select("#cloud").append("svg")
    .attr("class", "c_svg");

function draw(words) {
    d3.select(".c_svg")
        .attr("width", Width)
        .attr("height", Height)
        .append("g")
        .attr("transform", "translate(" + (Width) / 2 + "," + (Height) / 2 + ")")
        .selectAll(".cloud_text")
        .data(words)
        .enter().append("text")
        .attr("class", "cloud_text")
        .attr("text-anchor", "middle")
        .attr("transform", function (d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .style("fill", "#f95959")
        .style("font-size", function (d) {
            return d.size + "px";
        })
        .style("font-family", "Impact")
        .text(function (d) {
            return d.text;
        });
}


var cloud = d3.layout.cloud()
    .size([470, 280])  // 宽高
    .words(dataset.map(function (d) {
        return {text: d, size: 10 + Math.random() * 90};
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

