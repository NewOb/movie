var i = 0;


function action() {
    i++;
    if (i == 1) {
        $("#Mbtn").fadeOut(600);
    }
    if (i == 2) {
        $("#Mbtn").fadeIn(3500);
        i = 0;
    }
    setTimeout(action(), 10000);
}

action();
