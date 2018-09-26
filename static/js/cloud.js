d3.json("/l_data/", function (error, type_data) {
    var i = 0;
    var type = [];
    var type_like = [];
    var color = [];
    var t_color = [];
    var rect_year = [];
    var rect_like = [];
    var width = "100%", height = 450;
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
    // console.log(type);
    // console.log(t_color);
    // var fill = d3.scale.category20();
    // for (var a= 0;a<color.length;a++){
    //
    // }

    d3.select("#cloud").append("svg")
            .attr("class", "c_svg");

    function draw(type) {
        d3.select(".c_svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
            .selectAll("text")
            .data(type)
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

        d3.selectAll(".cloud_text").on('click', function () {
        $.post("/cloud_rect/", this.innerHTML, function (data, status) {
            console.log(data);
            console.log(status);
            for (var i = 0; i < data.length; i++) {
                rect_year[i] = data[i].year;
                rect_like[i] = data[i].like;
            }
            var us_r_color = color[r_color(data[0].type)];
            console.log(d3.max(rect_like));
            cloud_remove();
            rect(data, rect_year, rect_like, us_r_color);
        });
    });
    }


    function cloud() {
        var cloud = d3.layout.cloud()
            .size([600, 500])  // 宽高
            .words(type.map(function (d, i) {
                return {text: d, size: (type_like[i] / 10) + 0.1 * 90, color: t_color[i]};
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
    }

    function cloud_remove() {
        d3.selectAll(".cloud_text")
            .transition()
            .duration(1000)
            .ease("linear")
            .style("font-size", function () {
                return "0px"
            })
            .remove()
    }

    function rect(r_data, year, like, r_color) {
        var x = d3.scale.ordinal()
            .domain(year)
            .rangeRoundBands([0, width - 50], 1);

        var y = d3.scale.linear()
            .domain([0, d3.max(like)])
            .range([height - 115, 0]);

        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom");

        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left");

        var tip = d3.tip()
            .attr("class", "d3-tip")
            .offset([-10, 0])
            .html(function (d) {
                return "<strong style='color: crimson'>like:</strong>" + "<strong>" + d.like + "</strong>"
            });

        var svg = d3.select(".c_svg")
            .append("g")
            .attr("transform", "translate(50,30)");

        svg.call(tip);

        svg.append("g")
            .attr("class", "r_axis")
            .attr("transform", "translate(0,350)")
            .transition()
            .duration(1000)
            .ease("linear")
            .call(xAxis);

        svg.append("g")
            .attr("class", "r_axis")
            .attr("transform", "translate(0,15)")
            .transition()
            .duration(1000)
            .ease("linear")
            .call(yAxis);

        svg.selectAll(".bar")
            .data(r_data)
            .enter()
            .append("rect")
            .attr("transform", "translate(-13,14)")
            .attr("class", "bar")
            .attr("fill", r_color)
            .attr("width", "0")
            .attr("height", function (d) {
                return height - y(d.like) - 115
            })
            .transition()
            .duration(1000)
            .ease("linear")
            .attr("x", function (d) {
                return x(d.year)
            })
            .attr("y", function (d) {
                return y(d.like)
            })
            .attr("width", "26");

        d3.selectAll(".bar").on("mouseover", tip.show)
            .on("mouseout", tip.hide)
            .on("click",function () {
                rect_remove();
                cloud();
            })

    }

    function rect_remove() {
        d3.selectAll(".r_axis")
            .transition()
            .duration(1000)
            .ease("linear")
            .attr("transform", "translate(0,-800)")
            .remove();

        d3.selectAll(".bar")
            .transition()
            .duration(1000)
            .ease("linear")
            .attr("width", "0")
            .remove();

        d3.selectAll(".d3-tip")
            .remove();
    }

    function r_color(r_color) {
        for (var i = 0; i < type.length; i++) {
            if (r_color == type[i]) {
                return i
            }
        }
    }

    cloud();



});