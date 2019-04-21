$(document).ready(function(){
  $('#cards-for-hero-div').lightGallery();
  console.log(window.location.search)
  var urlParams = new URLSearchParams(window.location.search);
  var heroName = urlParams.get("services-hero");
  var useLibrary = urlParams.get("useLibrary");
  console.log(heroName)
  cardsForHero = {
    heroClass: heroName,
    isLibrary: useLibrary
  }
  $("#hero-class").append("<h2 class=\"site-section-heading text-center\">Result For "+heroName+"</h2>")
  $.ajax({
    url: "/getTheDeckForHero",
    type: "Get", 
    dataType: "json", // type of content being received
    data:cardsForHero,
    success: function(data) {
      console.log("result")
      console.log(data)
      for(var i =0;i<data.length;i++){
        $("#cards-for-hero-div").append("<div class=\"col-sm-6 col-md-4 col-lg-3 col-xl-2 item\" data-aos=\"fade\" data-src=\"/static/images/"+data[i]+".png><a href=\"#\"><img src=\"/static/images/"+data[i]+".png\" alt=\"IMage\" class=\"img-fluid\"></a></div>")
      }
    }
  });	
});