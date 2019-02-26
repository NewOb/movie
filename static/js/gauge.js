var svg = d3.select("#gauge1")
    .append("svg")
    .attr("width", "100%")
    .attr("height", 250);

var svg1 = d3.select("#gauge2")
    .append("svg")
    .attr("width", "100%")
    .attr("height", 250);

var gauge = iopctrl.arcslider()
    .radius(105)   //仪表盘的半径
    .events(false)
    .indicator(iopctrl.defaultGaugeIndicator);
gauge.axis().orient("in")
    .normalize(true)
    .ticks(12)  //数字之间的刻度大小
    .tickSubdivide(2)   //当前刻度与下一刻度之间的格挡个数
    .tickSize(10, 8, 10)
    .tickPadding(10)   //数字距离刻度的距离
    .scale(d3.scale.linear()
        .domain([0, 15])   //刻度范围，投资级数，内圈
        .range([-3 * Math.PI / 4, 3 * Math.PI / 4]));  //刻度盘的周长

var gauge1 = iopctrl.arcslider()
    .radius(105)   //仪表盘的半径
    .events(false)
    .indicator(iopctrl.defaultGaugeIndicator);
gauge1.axis().orient("in")
    .normalize(true)
    .ticks(12)  //数字之间的刻度大小
    .tickSubdivide(3)   //当前刻度与下一刻度之间的格挡个数
    .tickSize(10, 8, 10)
    .tickPadding(10)   //数字距离刻度的距离
    .scale(d3.scale.linear()
        .domain([-5, 10])   //刻度范围,回报率,外圈
        .range([-3 * Math.PI / 4, 3 * Math.PI / 4]));  //刻度盘的周长

var segDisplay = iopctrl.segdisplay()
    .width(80)  //蓝色数字的宽度
    .digitCount(5)   //蓝色数字的位数
    .negative(false)
    .decimals(0);

svg.append("g")
    .attr("class", "segdisplay")
    .attr("transform", "translate(80, 200)")
    .call(segDisplay);

var segDisplay1 = iopctrl.segdisplay()
    .width(80)  //蓝色数字的宽度
    .digitCount(5)   //蓝色数字的位数
    .negative(false)
    .decimals(0);

svg1.append("g")
    .attr("class", "segdisplay")
    .attr("transform", "translate(75, 200)")
    .call(segDisplay1);

svg.append("g")
    .attr("class", "gauge")
    .attr("transform", "translate(-35,0)")    //位置=两个圆盘半径之差
    .call(gauge);

svg1.append("g")
    .attr("class", "gauge")
    .attr("transform", "translate(-35,0)")
    .call(gauge1);


segDisplay.value(350);  //内盘蓝色数字的值,投资数
segDisplay1.value(100000000 / (350 * 10000));  //外盘蓝色数字的值，回报率


gauge.value(350 / 100);   //内盘指针当前指向的值，投资级数
gauge1.value(100000000 / (350 * 10000));   //外盘指针当前指向的值,回报率
