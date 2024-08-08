//script script that updates the text <header> element to New Header!!! when clicks on DIV#update_header
const header = $('header');
const updateHeader = $('#update_header');

updateHeader.on('click', () => {
	header.text('New Header!!!');
});
