const h = $('header');
const red = $('div#red_header');

red.on('click', () => {
	h.css('color', '#FF0000');
});
