function wordCount(form_line) {
    var text = form_line.find('textarea').val();
    if (text === undefined) { return 0 }
    return form_line.find('textarea').val().split(/\s+/).filter(function (v) {return /\w+/.test(v)}).length;
}

function setCounter(form_line, current, limit) {
  form_line.find('.text-counter').text(current + '/' + limit + ' slov');
}

function setWarning(form_line, warning) {
  form_line.find('.warning').text(warning);
}

function getSoftLimit(form_line) {
  return parseInt(form_line.find('textarea').attr('soft_limit'));
}


function setLineCounter(form_line) {
    var wc = wordCount(form_line);
    var softLimit = getSoftLimit(form_line);
    setCounter(form_line, wc, softLimit);
    return {current: wc, limit: softLimit}
}



$(document).ready(function(){
	$("#cv :file").filestyle({buttonText: 'Nahraj svoje CV', input:true, buttonBefore :true});
	$("#list :file").filestyle({buttonText: 'Nahraj svoj motivačný list', input:true, buttonBefore :true});

	$('.subpage-form-1 .main-form .form-line input[type="submit"]').click(function(){
		if (!$('input#id_udaje').prop('checked')) {
			$('.subpage-form-1 .main-form .form-line #id_udaje_error.hidden').removeClass('hidden');
		}
	});

	$('.carousel').carousel({
	  interval: 8000
	});

	$('#reg_final .form-line').each(function () {
		setLineCounter($(this));
    });

	$('#reg_final textarea').bind('input propertychange', function() {
		var formLine = $(this).parent();
		var count = setLineCounter(formLine);
        setWarning(formLine, '');
  		if (count.current > count.limit) {
      		setWarning(formLine, 'Pokús sa prosím vyjadriť svoju myšlienku na menej ako ' + count.limit + ' slov.');
		}
}	);

});
