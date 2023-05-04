$(function () {
	const h = $('#hello');
	$.ajax({
		type: 'GET',
		url: 'https://fourtonfish.com/hellosalut/?lang=fr',
		success: (data) => {
			h.text(data.hello);	
		}
	});
});
