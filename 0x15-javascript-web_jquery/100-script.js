function updateHeaderColor () {
	const h = document.querySelector('header');
	h.style.color = '#FF0000';
}

if (document.readyState === 'complete') {
	updateHeaderColor();
} else {
	if (window.addEventListener) {
		window.addEventListener('load', updateHeaderColor, false);
	} else {
		window.attachEvent('onload', updateHeaderColor);
	}
}
