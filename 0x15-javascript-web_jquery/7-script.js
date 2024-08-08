//JavaScript script that fetches the character from url
const  name = $('#character');

$.ajax({
	type: 'GET',
	url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
	success: (data) => {
		name.text(data.name);
	}
});
