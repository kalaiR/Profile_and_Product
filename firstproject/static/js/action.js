$(document).ready(function(){
	var Height = $(window).height();
	$(".login_holder ").css({'height': Height+ "px"});
	var theHeight = $(".login_holder form").height();
    var theWidth = $(".login_holder form").width();
	$(".login_holder form").css({'margin-top': -theHeight / 2 + "px", 'margin-left': -theWidth / 2 + "px",'border':"1px solid"});
	
	var height = $(document).height();
	$(".register_holder ").css({'height': height+ "px"});
	var theHeight = $(".register_holder form").height();
    var theWidth = $(".register_holder form").width();
	$(".register_holder form").css({'margin-top': -theHeight / 2 + "px", 'margin-left': -theWidth / 2 + "px",'border':"1px solid"});

});