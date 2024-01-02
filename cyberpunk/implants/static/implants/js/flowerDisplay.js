function myCallback() {
  var txt;
  if (confirm("Send response?")) {
    txt = "Wait our callback..";
  } else {
    txt = "Canceled!";
  }
  document.getElementById("demo").innerHTML = txt;
}

