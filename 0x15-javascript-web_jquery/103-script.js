$(function() {
	const langCode = $('#language_code');
	const translate = $('#btn_translate');
	const hello = $('div#hello');

	translate.on('click', () => {
		$.ajax({
			type: 'GET',
			url: 'https://www.fourtonfish.com/hellosalut/hello/',
			data: {
				lang: `${langCode}`
			},
			success: (data) => {
				hello.text(data)
			}
		});
	});

	langCode.on('keypress', (event) => {
		if (event.keyCode === 13) {
			$.ajax({
				type: 'GET',
				url: 'https://www.fourtonfish.com/hellosalut/hello/',
				data: {
					lang: `${langCode}`
				},
				success: (data) => {
					hello.text(data);
				}
			});
		}
	});
});
