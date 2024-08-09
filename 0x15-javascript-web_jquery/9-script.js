//JavaScript script that fetches from url from tag DIV#hello.
$(document).ready(function() {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        $('#hello').text(data.hello);
    });
});
