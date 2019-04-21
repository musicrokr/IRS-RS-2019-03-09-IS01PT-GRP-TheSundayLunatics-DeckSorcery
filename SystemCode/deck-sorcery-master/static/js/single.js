$(document).ready(function(){
    $('#cards-for-hero-div').lightGallery();
    const urlParams = new URLSearchParams(window.location.search);
    const heroName = urlParams.get('heroClass');
    console.log(heroName)
    cardsForHero = {
          heroClass: heroName
    }
    $("#hero-class").append("<h2 class=\"site-section-heading text-center\">"+heroName+"</h2>")
    
    $.ajax({
      url: "/getCardsForHero",
      type: "Get", 
      dataType: "json", // type of content being received
      data:cardsForHero,
      success: function(data) {
        console.log("single")
        console.log(data[0]['id'])
        for(var i =0;i<data.length;i++){
          $("#cards-for-hero-div").append("<div class=\"col-sm-6 col-md-4 col-lg-3 col-xl-2 item\" data-aos=\"fade\" data-src=\"/static/images/"+data[i]['id']+".png><a href=\"#\"><img src=\"/static/images/"+data[i]['id']+".png\" alt=\"IMage\" class=\"img-fluid\"></a></div>")
        }
      }
    });	
  });