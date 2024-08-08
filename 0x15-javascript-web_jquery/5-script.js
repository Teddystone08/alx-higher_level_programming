//javaScript  that adds a <li> element to a list when clicks on DIV#add_item
$('#add_item').click(function() {
    $('UL.my_list').append('<li>Item</li>');
});
