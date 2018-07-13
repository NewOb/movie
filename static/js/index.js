d3.json("/data/", function (error, type_data) {
        var i = 0;
        var type = [];
        var type_like = [];
        var color = ['#FFCC99', '#FFCC00', '#006633', '#99CC33', '#3399CC', '#805615', '#666666', '#FF9999', '#FF9900', '#339999', '#000000', '#CC3333', '#99CCFF', ' #663399', '#9999CC', '#CCCC33']
        if (error)
            console.log(error);
        console.log(type_data);
        console.log(type_data[0].zh);
        while (i < 16) {
            // console.log(tabs[i].zh);
            type[i] = type_data[i].zh;
            type_like[i] = type_data[i].like;
            i++;
        }
        console.log(type);
        // var fill = d3.scale.category20();

        var layout = d3.layout.cloud()
            .size([500, 500])  // 宽高
            .words(type.map(function (d,i) {
                return {text: d, size: type_like[i]%50 + 30};
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

        layout.start();

        function draw(words) {

            d3.select("#cloud").append("svg")
                .attr("width", layout.size()[0])
                .attr("height", layout.size()[1])
                .append("g")
                .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", function (d) {
                    return d.size + "px";
                })
                .style("font-family", "Impact")
                .style("fill", function (d, i) {
                    return color[i];
                })
                .attr("text-anchor", "middle")
                .attr("transform", function (d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .text(function (d) {
                    return d.text;
                });
        }
    }
);