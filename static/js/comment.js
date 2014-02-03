var $commentarea = $('.commentarea');

$commentarea.on('click', '.noncollapsed .expand', function (){
    hide($(this).closest('.thing'));
});

$commentarea.on('click', '.collapsed .expand', function (){
    show($(this).closest('.thing'));
});

function hide($thing) {
    var $entry = $thing.find('.entry');

    $entry.find('.noncollapsed').hide();
    $thing.find('.child').hide();

    $entry.find('.collapsed').show();
}

function show($thing) {
    var $entry = $thing.find('.entry');

    $entry.find('.collapsed').hide();

    $entry.find('.noncollapsed').show();
    $thing.find('.child').show();
}