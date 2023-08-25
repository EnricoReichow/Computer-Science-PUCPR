function compare() {
    var value1 = parseInt((document.getElementById("value1").value));
    var value2 = parseInt((document.getElementById("value2").value));

    if (value1 > value2) {
        alert(value1 + " o primeiro valo é maior!")
    } else if(value2 > value1) {
        alert(value2 + " o segundo valor é maior")
    } else {
        alert("Os números são iguais")
    }
}