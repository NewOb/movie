var f_massage;

// console.log(type_color);

$("#submit").click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/massage/",
        async: false,
        data: $("#data").serialize(),
        success: function (result) {
            // console.log(result);
            console.log(result);
            var score = result.result[0];
            var box_office = result.result[1] * 10;
            var max_box = result.max_box;
            var addnames = [];
            addnames[0] = result.director;
            addnames[1] = result.act1;
            addnames[2] = result.act2;
            addnames[3] = result.act3;
            addname(addnames);
            Result(score, box_office, max_box);
            // alert("成功");
            upgauge(result.result[1],result.invest);
            $.get("/rect/", function (data, status) {
                console.log(data);
                rup(data.d1, data.d2, data.d4)
            });
            d3.selectAll(".cloud_text")
                        .transition()
                        .duration(1000)
                        .ease("linear")
                        .style("fill", function () {
                            var color = "#838289";
                            for (var i=0;i<result.type.length;i++){
                                if(this.textContent == result.type[i]){
                                    color =  "#f95959"
                                }
                            }
                            return color;
                        });

            d3.selectAll(".cloud_text")
                .on("click", function () {
                    console.log(this.textContent);
                    $.post('/line/', {"this_type": this.textContent},
                        function (data, status) {
                            console.log(data);
                            like = [];
                            for (var i = 0; i < data.length; i++) {
                                if (data[i].times != 0){
                                    like[i] = data[i].like/data[i].times
                                } else {
                                    like[i] = data[i].like
                                }
                            }
                            lineup(like)
                        });           //向后端发送类型，以便给予折线图数据

                    d3.selectAll(".cloud_text")
                        .transition()
                        .duration(300)
                        .ease("linear")  //
                        .style("fill", function () {
                            var color = "#838289";
                            for (var i=0;i<result.type.length;i++){
                                if(this.textContent == result.type[i]){
                                    color =  "#f95959"
                                }
                            }
                            return color;
                        });

                    d3.select(this)
                        .transition()
                        .duration(500)
                        .ease("linear")
                        .style("fill", "#f98e86");
                })
        },
        error: function () {
            alert("输入数据异常！")
        }
    })
});
