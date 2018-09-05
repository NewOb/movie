d3.json("/l_data/", function (error, type_data) {
        var i = 0;
        var type = [];
        var type_like = [];
        var color = [];
        var t_color = [];
        var rect_data = [];
        if (error)
            console.log(error);
        // console.log(type_data);
        // console.log(type_data[0].zh);
        while (i < 16) {
            // console.log(tabs[i].zh);
            type[i] = type_data[i].en;
            type_like[i] = type_data[i].like;
            color[i] = type_data[i].Color;
            t_color[i] = "#B3B6B6";
            i++;
        }
        for (var a = 0; a < type_data[16].length; a++) {
            var p = 0;
            while (p < type.length) {
                // console.log(type_data[16][a]);
                // console.log(type_data[p].en);
                if (type_data[p].en == type_data[16][a]) {
                    t_color[p] = color[p];
                }
                p++;
            }
        }
        console.log(type);
        console.log(t_color);
        // var fill = d3.scale.category20();
        // for (var a= 0;a<color.length;a++){
        //
        // }

        var cloud = d3.layout.cloud()
            .size([600, 500])  // 宽高
            .words(type.map(function (d, i) {
                return {text: d, size: (type_like[i] / 10) + 0.2 * 90, color: t_color[i]};
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

        d3.selectAll(".cloud_text")
            .on("mouseover",function () {
                $.post("/cloud_rect/",this.innerHTML,function (data,status) {
                    for (i = 0;i<data.length;i++){
                        rect_data[i] = data[i]
                    }
                    console.log(data)
                });
            });

        function draw(type) {

            d3.select("#cloud").append("svg")
                .attr("width", 525)
                .attr("height", 450)
                .append("g")
                .attr("transform", "translate(" + 525 / 2 + "," + 450 / 2 + ")")
                .selectAll("text")
                .data(type)
                .enter().append("text")
                .attr("class","cloud_text")
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
    }
);