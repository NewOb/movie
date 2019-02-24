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
            console.log(result)
            var score = result.result[0];
            var box_office = result.result[1];
            Result(score,box_office);
            // alert("成功");
        },
        error: function () {
            alert("输入数据异常！")
        }
    })
});

