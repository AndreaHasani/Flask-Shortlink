$(function() {
    $('#search').submit(function(event) {

	var search = $.trim($('#input-text').val());
	event.preventDefault(); // Prevent the form from submitting via the browser


	var form = $(this);
	if ( search != '' ) {
	    $.ajax({
		type: form.attr('method'),
		url: form.attr('action'),
		data: form.serialize(),
	    }).done(function(response) {
		console.log(response.code);
		if (response.code == 1) {
		    $("#result p").remove();
		    $( "#result" ).append(response.result).animate({opacity:1});

		}
		else {
		    console.log(response)

		}
	    }).fail(function(response) {
		console.log(response.code)
	    });
	}
	else {

	    $("#result p").remove();
	    $('input-text').val('').focus();
	    $( "#result" ).append("<p>Search Empty</p>").animate({opacity:1});
	}
    });
});
