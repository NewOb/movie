var f_massage;
var type_color;
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

d3.json("/color/",function (error,data) {
    if (error)
        console.log(error);
    console.log(data);
    type_color=data
});

function get_massage() {
    return f_massage;
}
function get_color() {
    return type_color;
}