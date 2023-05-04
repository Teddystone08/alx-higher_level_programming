const h = $('header');
const r = $('div#red_header');

r.on('click', () => {
	h.addClass('red')
});
