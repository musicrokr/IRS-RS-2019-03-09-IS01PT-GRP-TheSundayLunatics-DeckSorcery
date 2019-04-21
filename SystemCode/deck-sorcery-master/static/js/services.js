$(document).ready(function(){
  $.ajax({
    url: "/getHeroes",
    type: "Get", 
    dataType: "json", // type of content being received
    success: function(data) {
          console.log(data.length)
          for(var i =0;i<data.length;i++){
            if(data[i]!="NEUTRAL")
            $("#radio-hero").append("<div><input type=\"radio\" id=\""+data[i]+"-radio\" name=\"services-hero\" value=\""+data[i]+"\" class=\"form-control\">"+data[i]+"<img height=\"200\" width=\"140\" src=\"/static/images/heroes/"+data[i]+".png\"></div>")
          }
        }
  });
});

function setCheckboxValue() {
  if(document.myForm.useLibrary.checked) {
    document.getElementById("library-check-box").setAttribute('value', true);
  }
  else {
    document.getElementById("library-check-box").setAttribute('value', false);
  }
}