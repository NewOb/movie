var i = 0;


function action() {
    i++;
    if (i == 1) {
        $("#Mbtn").fadeIn(500);
    }
    if (i == 2) {
        $("#Mbtn").fadeOut(3500);
        i = 0;
    }
    setTimeout(action(), 10000);
}

action();
