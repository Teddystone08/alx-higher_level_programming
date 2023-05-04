const header = $('header');
const updateHeader = $('#update_header');

updateHeader.on('click', () => {
	header.text('New Header!!!');
});
