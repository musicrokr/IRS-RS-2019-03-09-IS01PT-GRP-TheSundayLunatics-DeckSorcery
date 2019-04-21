

function loadMe() {
	console.log("loadMe")
	$.ajax({
		url: "/getHeroes",
		type: "Get", 
		dataType: "json", // type of content being received
		success: function(data) {
					console.log(data.length)
					for(var i =0;i<data.length;i++){
						$("#hero-class-div").append("<div class=\"swiper-slide\"><div class=\"image-wrap\"><div class=\"image-info\"><h2 class=\"mb-3\">"+data[i]+"</h2><a onclick=\"displayCardsForHero('"+data[i]+"')\" value=\""+data[i]+"\" class=\"btn btn-outline-white py-2 px-4\">More Photos</a></div><img src=\"/static/images/heroes/"+data[i].toLowerCase()+".png\" alt=\"Image\"></div></div></div>")
					}
				}
	});
}

function displayCardsForHero(heroName){
	window.location = "/single?heroClass="+heroName	
}

