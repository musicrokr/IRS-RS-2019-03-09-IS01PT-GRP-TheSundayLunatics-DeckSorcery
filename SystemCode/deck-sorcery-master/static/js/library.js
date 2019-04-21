$(document).ready(function(){
  $('#cards-for-hero-div').lightGallery();
  $.ajax({
    url: "/getCardsLibrary",
    type: "Get", 
    dataType: "json", // type of content being received
    success: function(data) {
      console.log("library")
      var libraryIds = data
      console.log(libraryIds)
      $("#hero-class").append("<h2 class=\"site-section-heading text-center\">My Library(total "+libraryIds.length+" cards)</h2>")

      for(var i =0;i<libraryIds.length;i++){
        $("#cards-for-hero-div").append("<div class=\"col-sm-6 col-md-4 col-lg-3 col-xl-2 item\" data-aos=\"fade\" data-src=\"/static/images/"+libraryIds[i]+".png><a href=\"#\"><img src=\"/static/images/"+libraryIds[i]+".png\" alt=\"IMage\" class=\"img-fluid\"></a></div>")
      }
    }
  });	
});