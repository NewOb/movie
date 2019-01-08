// 评分
var config1 = liquidFillGaugeDefaultSettings();
// 票房
var config2 = liquidFillGaugeDefaultSettings();

var colors = get_color();
var massages = get_massage();

// console.log();
console.log(massages);
// circlecolor
var circlecor = [];
// wavecolor
var wavecor = [];
// textcolor
var textcor = [];
// wavetextcolor
var wtcor = [];

config1.circleColor = "#178BCA";
config1.textColor = "#045681";
config1.waveTextColor = "#A4DBf8";
config1.waveColor = "#178BCA";
config1.maxValue = 10;

config2.circleColor = "#178BCA";
config2.textColor = "#045681";
config2.waveTextColor = "#A4DBf8";
config2.waveColor = "#178BCA";

var chart1 = loadLiquidFillGauge("fillgauge1", 5.0, config1);
var chart2 = loadLiquidFillGauge("fillgauge2", 100000000.0, config2);

for (var q=0;q <massages.type.length;q++) {
    for (var p=0;p <colors.length;p++) {
        if (colors[p].name == massages.type[q]) {
            circlecor.push(colors[p].Color);
            wavecor.push(colors[p].Color);
            textcor.push(colors[p].textColor);
            wtcor.push(colors[p].waveTextColor)
        }
    }
}

function ups() {
        var i = 0;
        while (wtcor[i]) {
            config1.circleColor = circlecor[i];
            config1.textColor = textcor[i];
            config1.waveTextColor = wtcor[i];
            config1.waveColor = wavecor[i];
            config1.value = massages.result[0].toFixed(1);

            config2.circleColor = circlecor[i];
            config2.textColor = textcor[i];
            config2.waveTextColor = wtcor[i];
            config2.waveColor = wavecor[i];
            config2.value = massages.result[1].toFixed(1);

            chart1.update(config1.circleColor);
            chart1.update(config1.textColor);
            chart1.update(config1.waveColor);
            chart1.update(config1.waveTextColor);
            chart1.update(config1.value);

            chart2.update(config2.circleColor);
            chart2.update(config2.textColor);
            chart2.update(config2.waveColor);
            chart2.update(config2.waveTextColor);
            chart2.update(config2.value);

            i++;

            if (i==wtcor.length){
                i=0
            }
        }
}
if (massages){
    setInterval("ups()", 5000);
}
