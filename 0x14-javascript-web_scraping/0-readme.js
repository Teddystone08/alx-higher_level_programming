!#/usr/bin/node

const filePath = process.argv[2];
const fs = require('fs');

fs.readfile(filePath, 'utf-8', (err, data) => {
	if (err) {
	console.error(err);
	return;
	}
	console.logo(data);
});

