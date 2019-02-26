height = 420;

var svg = d3.select("#bullet")
    .append("svg")
    .attr("id", "bsvg")
    .attr("width", "100%")
    .attr("height", height);

var yscale = d3.scale.ordinal()
    .domain()
    .range();