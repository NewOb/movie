d3.json("/data/", function (error, type_data) {
        var i = 0;
        var type = [];
        var type_like = [];
        var color = ['#CDAA7D', '#178BCA', '#008B00', '#9ACD32', '#8EE5EE', '#AA7D39', '#696969', '#DB7093', '#FF8C00', '#20B2AA', '#000000', '#CD2626', '#FFD700', ' #9932CC', '#CD96CD', '#CCCC33'];
        var t_color = [];
        if (error)
            console.log(error);
        // console.log(type_data[16]);
        // console.log(type_data[0].zh);
        while (i < 16) {
            // console.log(tabs[i].zh);
            type[i] = type_data[i].zh;
            type_like[i] = type_data[i].like;
            i++;
        }
        for (var a = 0;a<type_data[16].length;a++){
            var p =0;
            while (p<type.length){
                console.log(type_data[16][a]);
                console.log(type[p]);
                if (type_data[16][a] == type[p]){
                    t_color[p] = color[p];
                    }else {
                    t_color[i] = "#B3B6B6";
                }
                p++;
            }
        }
        // console.log(t_color);
        // var fill = d3.scale.category20();
        // for (var a= 0;a<color.length;a++){
        //
        // }

        var cloud = d3.layout.cloud()
            .size([600, 400])  // 宽高
            .words(type.map(function (d, i) {
                return {text: d, size: (type_like[i] / 10) + Math.random() *90};
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

        function draw(words) {

            d3.select("#cloud").append("svg")
                .attr("width", cloud.size()[0])
                .attr("height", cloud.size()[1])
                .append("g")
                .attr("transform", "translate(" + cloud.size()[0] / 2 + "," + cloud.size()[1] / 2 + ")")
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .attr("text-anchor", "middle")
                .attr("transform", function (d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .style("fill", function (d, i) {
                     return color[i];
                })
                .transition()
                .duration(1000)
                .ease("linear")
                .style("font-size", function (d, i) {
                    return d.size + "px";
                })
                .style("font-family", "Impact")
                .text(function (d) {
                    return d.text;
                });
        }
    }
);