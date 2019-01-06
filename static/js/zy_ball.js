// 评分
var config1 = liquidFillGaugeDefaultSettings();
// 票房
var config2 = liquidFillGaugeDefaultSettings();

var colors = get_color();
var massages = get_massage();

// console.log();
console.log(colors);
// circlecolor
var circlecor = [];
// wavecolor
var wavecor = [];
// textcolor
var textcor = [];
// wavetextcolor
var wtcor = [];

for (i in massages.type) {
    for (p in colors) {
        if (p.name == i) {
            circlecor.push(p.Color);
            wavecor.push(p.Color);
            textcor.push(p.textColor);
            wtcor.push(p.waveTextColor)
        }
    }
}
config1.circleColor = circlecor[0];
config1.textColor = textcor[0];
config1.waveTextColor = wtcor[0];
config1.waveColor = wavecor[0];

config2.circleColor = circlecor[0];
config2.textColor = textcor[0];
config2.waveTextColor = wtcor[0];
config2.waveColor = wavecor[0];

var chart1 = loadLiquidFillGauge("fillgauge1", massages.resut[0].toFixed(1), config1);
var chart2 = loadLiquidFillGauge("fillgauge2", massages.resut[1].toFixed(1), config2);

function ups() {
    if (wtcor.length > 1) {
        var i = 0;
        while (wtcor[i]) {
            i++;
            config1.circleColor = circlecor[i];
            config1.textColor = textcor[i];
            config1.waveTextColor = wtcor[i];
            config1.waveColor = wavecor[i];

            config2.circleColor = circlecor[i];
            config2.textColor = textcor[i];
            config2.waveTextColor = wtcor[i];
            config2.waveColor = wavecor[i];

            chart1.update(config1.circleColor);
            chart1.update(config1.textColor);
            chart1.update(config1.waveColor);
            chart1.update(config1.waveTextColor);

            chart2.update(config2.circleColor);
            chart2.update(config2.textColor);
            chart2.update(config2.waveColor);
            chart2.update(config2.waveTextColor);
        }
    }
}

setTimeout("ups()", 5000);
