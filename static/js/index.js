var f_massage;
$("#submit").click(function form() {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/massage/",
        data: $("#data").serialize(),
        success: function (result) {
            // console.log(result);
            f_massage = result;
            console.log(f_massage)
            // alert("成功");
        },
        error: function () {
            alert("输入数据异常！")
        }
    })
});

function get_massage() {
    return f_massage;
}