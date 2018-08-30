  /*
   * 更改：d3.js的引用路径；
   * colorScheme 线条颜色数组
   * 425行 d3.csv（）需要更改
   * */
    let margin = {top: 30, bottom: 30, left: 70, right: 150};
    let width = 640 - margin.left - margin.right;
    let height = 400 - margin.top - margin.bottom;
    let nest_data;
    let type_data;
    let colorScheme = ["#E57373", "#BA68C8", "#7986CB", "#A1887F", "#90A4AE", "#AED581", "#9575CD", "#FF8A65", "#4DB6AC", "#FFF176", "#64B5F6", "#00E676"];
    let hashColor = [];
    let chart_type = ['评分', '票房'];
    let y_label = ['/score', '/dollar'];
    let zone_state01 = [];
    let zone_state02 = [1, 0];
    //添加line的svg（本质g）
    let lineSvg;
    //这将添加我们的工具提示元素
    let focus;
    let new_data = {};
    let yName = 'IMDB';  //当前展示的评分还是票房的字段名；
   //line_data表的字段名称
   let film_grade='IMDB';
   let film_boxoffice='Box_office';


    let svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    let x = d3.scale.linear()
        .range([0, width]);
    let y = d3.scale.linear()
        .range([height, 0]);


    let xAxis = d3.svg.axis().scale(x)
        .orient("bottom");

    let yAxis = d3.svg.axis().scale(y)
        .orient("left");

    let bisectDate = d3.bisector(function (d) {
        return d.years;
    }).left;

    //线生成器
    let line_generator_grade = d3.svg.line()
        .x(function (d) {
            return x(d.years);
        })
        .y(function (d) {
            return y(d.IMDB);
        });

    //线生成器
    let line_generator_box = d3.svg.line()
        .x(function (d) {
            return x(d.years);
        })
        .y(function (d) {
            return y(d.Box_office);
        });

    //底部标签
    svg.append("g")
        .attr("class", "x label")
        .append("text")
        .text("/year")
        .attr("transform", "translate(" + (width) + "," + (height + 15) + ")");

    //y轴标签
    svg.append("g")
        .append("text")
        .attr("class", "y label y_label")
        .text(y_label[0])
        .attr("transform", `translate(${18 - margin.left},${0 - 10})`)
        .attr("dy", ".7em");

    //顶部标签
    svg.append("g")
        .attr("class", "title")
        .append("text")
        .attr("x", width / 2)
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")
        .text("Trends for ratings and box office");

    //线条类型标签
    let state01 = svg.append("g")
        .attr("id", "state01")
        .attr("transform", `translate(${width},${margin.top})`);

    //纵轴类型标签
    let state02 = svg.append('g')
        .attr('id', 'state02')
        .attr("transform", `translate(${0},${height + margin.bottom})`);


    focus = svg.append('g')
        .style("display", "none");

    //Add x-line
    focus.append("line")
        .attr("class", "x")
        .style("stroke", "blue")
        .style("stroke-dasharray", "3,3")
        .style("opacity", 0.5)
        .attr("y1", 0)
        .attr("y2", height);

    //绘制一次，主要为监听；
    function draw_state02() {
        let color = ['black', '#b3b3b3'];
        for (let i = 0; i < chart_type.length; i++) {
            state02.append('text')
                .attr('class', 'state02_' + i)
                .attr('x', width / 2 - 40 + 60 * i)
                .attr('y', 0)
                .attr('dx', 8)
                .attr('dy', '-.3em')
                .text(chart_type[i])
                .style('fill', color[i])
                .style('font-size', 12)
                .on('click', function () {
                    zone_state02[0]++;
                    zone_state02[1]++;
                    yName = checkYName();
                    drawYAxis(new_data);
                    switch (yName) {
                        case film_grade: {
                            d3.select('.state02_0').style('fill', color[0]);
                            d3.select('.state02_1').style('fill', color[1]);
                            d3.select('.y_label').text(y_label[0]);
                            break;
                        }
                        case film_boxoffice: {
                            d3.select('.state02_0').style('fill', color[1]);
                            d3.select('.state02_1').style('fill', color[0]);
                            d3.select('.y_label').text(y_label[1]);
                            break;
                        }
                    }
                    drawLine(new_data[0], new_data[1], chooseGenerator());
                    drawTiptool(new_data[0]);
                    rectListener(new_data[0], new_data[1]);
                });
        }
    }

    function drawYAxis(new_data) {
        d3.selectAll('.yAxisG').remove();
        let arr = d3.extent(new_data[1], function (d) {
            return d.values.map(function (dd, i) {
                return parseFloat(dd[yName]);
            });
        });
        let min_num = 10000000, max_num = 0;
        for (let i = 0; i < new_data[1].length; i++) {
            let a1 = d3.extent(arr[i]);
            if (min_num > a1[0]) {
                min_num = a1[0];
            }
            if (max_num < a1[1]) {
                max_num = a1[1];
            }
        }
        y.domain([min_num, max_num]);
        console.log(min_num, max_num);

        yAxis.scale(y);
        svg.append('g')
            .attr('class', 'y axis yAxisG')
            .call(yAxis);
    }

    function chooseGenerator() {
        if (yName === film_grade) {
            return line_generator_grade;
        } else {
            return line_generator_box;
        }
    }

    function checkYName() {
        if (zone_state02[0] % 2 === 1) {
            return film_grade;
        }
        else {
            return film_boxoffice;
        }
    }

    function bindColor() {
        for (let i = 0; i < type_data.length; i++) {
            hashColor[type_data[i]] = colorScheme[i];
        }
    }

    function drawLine(type_data, nest_data, line_generator) {
        //对nest_data数据排序；
        //对分组g删除；
        d3.selectAll('.line_g').remove();
        lineSvg = svg
            .selectAll('.path_g')  //尽量选择空类，避免不必要的坑；
            .data(type_data)
            .enter()
            .append('g')
            .attr('class', 'line_g');
        //添加line_generator路径。
        lineSvg.each(function (d, i) {
            let element = d3.select(this);
            element.append("path")
                .attr("class", "line state01_" + i)
                .style('stroke', hashColor[type_data[i]])
                .attr("d", line_generator(nest_data[i].values));
        });
    }

    //绘制一次，主要是监听
    function draw_state01(type_data) {
        for (let i = 0; i < type_data.length; i++) {
            let g1 = state01.append('g')
                .attr('class', 'state01_g_' + i);
            g1.append('rect')
                .attr('y', i * 15)
                .attr('width', 10)
                .attr('height', 10)
                .attr('class', 'state01_rect_' + i)
                .style('fill', hashColor[type_data[i]]);
            g1.append('text')
                .text(type_data[i])
                .attr('class', 'state01_text_' + i)
                .attr('y', i * 15)
                .attr('dx', 15)
                .attr('dy', 10)
                .attr('font-size', 12)
                .style('fill', 'black')
                .on('click', function (d) {
                    let id = d3.select(this).attr('class');
                    let index = parseInt(id.split('_')[2]);
                    zone_state01[0][index]++;
                    if (zone_state01[0][index] % 2 === 0) {
                        d3.select(this).style('fill', '#b3b3b3');
                        d3.select('.state01_rect_' + index).style('fill', '#b3b3b3');
                    } else {
                        d3.select(this).style('fill', 'black');
                        d3.select('.state01_rect_' + index).style('fill', hashColor[type_data[index]]);
                    }
                    new_data = getNewData();
                    drawYAxis(new_data);
                    //need check generator state
                    switch (zone_state02[0] % 2) {
                        case 0:
                            drawLine(new_data[0], new_data[1], line_generator_box);
                            break;
                        case 1:
                            drawLine(new_data[0], new_data[1], line_generator_grade);
                            break;
                    }
                    drawTiptool(new_data[0]);
                    rectListener(new_data[0], new_data[1]);
                });
        }

        function getNewData() {
            let arr = [], arr1 = [], arr2 = [];
            for (let i = 0; i < type_data.length; i++) {
                if (zone_state01[0][i] % 2 === 1) {
                    arr1.push(type_data[i]);
                    nest_data.map(function (d, j) {
                        if (d.key === type_data[i]) {
                            arr2.push(d);
                        }
                    })
                }
            }
            arr.push(arr1);
            arr.push(arr2);
            return arr;
        }
    }

    function drawTiptool(type_data) {
        //need to delete circle ,text
        d3.selectAll('.tip_text').remove();
        d3.selectAll('circle').remove();
        let row = type_data.length / 2;
        for (let i = 0; i < type_data.length + 1; i++) {
            focus.append("text")
                .attr("class", "tip_text tip_" + i)
                .style("stroke", "blue")
                .style("stroke-width", "0.51px")
                .style("font", "6px")
                .attr("dx", 6)
                .attr("dy", (i - row) + 'em');
        }

        // Add circle to graph
        focus.selectAll('circle')
            .data(type_data)
            .enter()
            .append("circle")
            .attr("class", "y")
            .style("fill", "none")
            .style("stroke", "blue")
            .attr("r", 4);
    }

    function rectListener(type_data, nest_data) {
        if (d3.select('.listener_rect')) {
            d3.selectAll('.listener_rect').remove();
        }
        //设置区域以捕获鼠标移动
        svg.append("rect")
            .attr("width", width)
            .attr("height", height)
            .attr('class', 'listener_rect')
            .style("fill", "none")
            .style("pointer-events", "all")
            .on("mouseover", function () {
                focus.style("display", null);
            })
            .on("mouseout", function () {
                focus.style("display", "none");
            })
            .on("mousemove", mousemove);

        function mousemove() {
            let x0 = x.invert(d3.mouse(this)[0]); //光标对应的标准实际值
            //找到最接近鼠标光标的数据数组的索引
            //返回高于光标位置的第一个日期的索引号
            // i = bisectDate(data, x0, 1);
            let i_arr = [];
            nest_data.forEach(function (d) {
                let index = bisectDate(d.values, x0, 1);
                i_arr.push(index);
            });
            let arr = [], i, min_dis = Number.MAX_VALUE, min_index = 0;
            nest_data.forEach(function (d, index) {
                i = i_arr[index];
                //两个变量保持光标值上下的日期
                let d0 = (d.values)[i - 1],
                    d1 = (d.values)[i],
                    dd = 0;
                let diff = x0 - d0.years - (d1.years - x0);
                diff > 0 ? dd = d1 : dd = d0;
                if (min_dis > Math.abs(diff)) {
                    min_dis = Math.abs(diff);
                    min_index = index;
                }
                //声明一个dd，它保存光标最接近的数据点
                arr.push(dd);
            });

            //the content of tiptool
            function chooseTip(yName) {
                focus.selectAll("circle.y").each(function (d, i) {
                    let e = d3.select(this);
                    e.attr('transform', `translate(${x(arr[i].years)},${y(arr[i][yName])})`)
                        .style('stroke', hashColor[type_data[i]])
                });

                let uniq = arr[min_index];
                for (let i = 0; i < type_data.length; i++) {
                    let ee = d3.select("text.tip_" + i);
                    ee.each(function (d, j) {
                        let e = d3.select(this);
                        e.attr("transform", "translate(" + x(uniq.years) + "," + y(uniq[yName]) + ")")
                            .text(type_data[i] + ':' + arr[i][yName]);
                    })
                }
                focus.select('text.tip_' + type_data.length)
                    .attr("transform", "translate(" + x(uniq.years) + "," + y(uniq[yName]) + ")")
                    .text('Date:' + uniq.years);

                // d3.selectAll('tip_text').attr('transform',`translate(${},${})`);

                focus.select(".x")
                    .attr("transform", "translate(" + x(uniq.years) + "," + 0 + ")")
                    .attr("y2", height);
            }

            chooseTip(checkYName())
        }
    }

    d3.csv("C:\\Users\\虚拟现实实验室\\PycharmProjects\\movie\\line_data.csv", type, function (data) {
        console.log(data);
        x.domain(d3.extent(data, function (d) {
            return d.years
        }));

        nest_data = d3.nest()
            .key(function (d) {
                return d.type;
            })
            .entries(data);

        type_data = nest_data.map(function (d) {
            return d.key;
        });
        if (type_data[1] === "") {
            nest_data.pop();
            type_data.pop();
        }
        let a = [];
        for (let i = 0; i < type_data.length; i++) {
            a[i] = 1;
        }
        zone_state01.push(a);
        zone_state01.push([1, 1]);

        new_data = [];
        new_data[0] = type_data;
        new_data[1] = nest_data;

        bindColor();
        drawYAxis(new_data);

//在此绘制必要组件；
        drawLine(type_data, nest_data, line_generator_grade);
        drawTiptool(type_data);
        rectListener(type_data, nest_data);
        draw_state01(type_data);
        draw_state02();
//在变化评分票房数据时重绘制一下；
        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis)
            .selectAll(".tick text")
            .style("text-anchor", "start")
            // .attr('transform', 'translate(rotate(60))')
            .attr("x", 2)
            .attr("y", 6);

        svg.append("g")
            .attr("class", "y axis yAxisG")
            .call(yAxis);
    });

    function type(d) {
        d.IMDB = +d.IMDB;
        d.Box_office = +d.Box_office;
        d.years = +d.years;
        return d
    }
