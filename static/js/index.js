var f_massage;

// console.log(type_color);

$("#submit").click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/massage/",
        async:false,
        data: $("#data").serialize(),
        success: function (result) {
            // console.log(result);
            console.log(result);
            var score = result.result[0];
            var box_office = result.result[1]*10;
            var max_box = result.max_box;
            Result(score,box_office,max_box);
            // alert("成功");
            $.get("/rect/",function (data,status) {
                console.log(data);
                rup(data.d1,data.d2,data.d4)
            })
        },
        error: function () {
            alert("输入数据异常！")
        }
    })
});
