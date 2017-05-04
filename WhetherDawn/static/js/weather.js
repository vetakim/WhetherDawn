function dms2grad(dms) {
    var dms = dms.split("°");
    var ms = dms[1].split("\′");
    var m = ms[0];
    var s = ms[1].split("\″")[0];
    return parseInt(dms) + parseInt(m) / 60 + parseInt(s) / 3600;
}

function getInfo(json) {
    var info = "<br>" +  json.name + "</br>";
    info += "<br> Wind " + json.wind.speed + " m/s </br>";
    info += "<br> Temperature " + json.main.temp + " °C </br>";
    info += "<br> Cloudiness " + json.clouds.all + " % </br>";
    return info;
}

function getWeatherData(cityId, lat, lon) {
    var apireq = new XMLHttpRequest();
    var apiref = "http://api.openweathermap.org/data/2.5/weather?";
    if ( cityId === 0 ) {
        apiref += "lat=" + dms2grad(lat) + "&";
        apiref += "lon=" + dms2grad(lon) + "&";
    } else {
        apiref += "id=" + cityId + "&";
    }
    apiref += "units=metric&";
    apiref += "APPID=30a72912a9f6bc40e2a104bf3f853556";
    apireq.open("GET", apiref, false);
    apireq.send();
    var wdata = JSON.parse(apireq.response);
    return wdata;
}

function drawMoscow() {
    var mdata = getWeatherData(524901, 0, 0);
    document.getElementById("moscow").innerHTML  = getInfo(mdata);
}
