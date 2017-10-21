$(document).ready(function(){
	$("#cv :file").filestyle({buttonText: 'Nahraj svoje CV', input:true, buttonBefore :true});
	$("#list :file").filestyle({buttonText: 'Nahraj svoj motivačný list', input:true, buttonBefore :true});
	/*
	$('.trigger').click(function(){
		$('nav').toggleClass('opened');
		$(this).toggleClass('opened');
	});
	$('.go-to').click(function(){
		var whereToGo = $(this).data("id");
		$('html,body').animate({scrollTop: $('#' + whereToGo).offset().top-50},1000);
	});
	*/
	
	$('.subpage-form-1 .main-form .form-line input[type="submit"]').click(function(){
		if (!$('input#id_udaje').prop('checked')) {
			$('.subpage-form-1 .main-form .form-line #id_udaje_error.hidden').removeClass('hidden');
		}
	});

	$('.carousel').carousel({
	  interval: 8000
	});
});
/*
function nazevFunkce(){
	
}
*/