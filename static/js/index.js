var f_massage;
var type_color=[];

d3.json("/color/", function (error, data) {
    console.log(data);
    for (var i=0;i<data.length;i++){
        type_color[i]=data[i]
    }
});

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
            f_massage = result;
            // alert("成功");
        },
        error: function () {
            alert("输入数据异常！")
        }
    })
});

function get_massage() {
    // $.ajax({
    //     type: "POST",
    //     dataType: "json",
    //     url: "/massage/",
    //     async:false,
    //     data: $("#data").serialize(),
    //     success: function (result) {
    //         f_massage = result;
    //         // alert("成功");
    //     },
    //     error: function () {
    //         alert("输入数据异常！")
    //     }
    // });
    return f_massage;
}

function get_color() {
    return type_color;
}
