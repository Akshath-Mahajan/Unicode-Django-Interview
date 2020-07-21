function getCookie(name) {//helper function
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function tabulate(data){ //helper function
    data = data.substring(1, data.length-1)
    data = data.split(',')
    tablerow1 = "<tr><th>Number:</th>"
    tablerow2 = "<tr><th>Value:</th>"
    for (let i = 0; i < data.length; i++)
    {
        var temp = data[i].split(':')
        tablerow1+="<td>"+temp[0]+"</td>"
        tablerow2+="<td>"+temp[1]+"</td>"
    }
    tablerow1+="</tr>"
    tablerow2+="</tr>"
    tablestring = '<table class="table table-responsive">'+tablerow1+tablerow2+'</table>'
    return tablestring
}
function taskTwoAJAX()
{
    document.getElementById("rawResponseResult").innerHTML = '<div class="spinner-border text-info"></div>'
    document.getElementById("tabResponseResult").innerHTML = '<div class="spinner-border text-info"></div>'
    var xhttp = new XMLHttpRequest();
    var start = document.getElementById("start").value
    var end = document.getElementById("end").value
    if(start=="" || end=="")
    {return}
    var url = "/taskTwo/"+start+"-"+end;
    var csrftoken = getCookie('csrftoken');
    xhttp.open("POST", url, async=true);
    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xhttp.send()
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200)
        {
            document.getElementById("rawResponseResult").innerHTML = this.responseText
            document.getElementById("tabResponseResult").innerHTML = tabulate(this.responseText)
        }
    }
}
function taskThreeAJAX()
{
    document.getElementById("rawApiResponseResult").innerHTML = '<div class="spinner-border text-info"></div>'
    var xhttp = new XMLHttpRequest();
    var cityName = document.getElementById("city").value
    var countryCode = document.getElementById("country-code").value
    if(cityName=="" || countryCode==""){return}
    var url = "/taskThree";
    var parameters = "city="+cityName+"&country="+countryCode
    var csrftoken = getCookie('csrftoken');
    xhttp.open("POST", url, async=true);
    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(parameters)
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200)
        {
            let index = this.responseText.lastIndexOf('<div class="container">')+("<div class='container'>".length)
            document.getElementById("rawApiResponseResult").innerHTML = this.responseText.substring(index).trim()
        }
    }
}
function taskFourAAJAX()
{
    document.getElementById("DBResponseAResult").innerHTML = '<div class="spinner-border text-info"></div>'
    var xhttp = new XMLHttpRequest();
    var cityName = document.getElementById("dbCity").value
    var date = document.getElementById("dbDate").value
    if(cityName=="" || date==""){return}
    var url = "/taskFourA";
    var parameters = "city="+cityName+"&date="+date
    var csrftoken = getCookie('csrftoken');
    xhttp.open("POST", url, async=true);
    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(parameters)
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200)
        {
            let index = this.responseText.lastIndexOf('<div class="table-responsive">')
            document.getElementById("DBResponseAResult").innerHTML = this.responseText.substring(index).trim()
        }
    }
}
function taskFourBAJAX()
{
    document.getElementById("DBResponseBResult").innerHTML = '<div class="spinner-border text-info"></div>'
    var xhttp = new XMLHttpRequest();
    var url = "/taskFourB";
    xhttp.open("GET", url, async=true);
    xhttp.send()
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200)
        {
            let index = this.responseText.lastIndexOf('<div class="table-responsive">')
            document.getElementById("DBResponseBResult").innerHTML = this.responseText.substring(index).trim()
        }
    }
}