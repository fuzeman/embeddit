var $commentarea = $('.commentarea');

$commentarea.on('click', '.noncollapsed .expand', function (){
    var $thing = $(this).closest('.thing'),
        $entry = $thing.find('.entry');

    $entry.find('.noncollapsed').hide();

    $thing.find('.child').addClass('collapsed')
                         .hide();

    $entry.find('.collapsed').show();
});

$commentarea.on('click', '.collapsed .expand', function (){
    var $thing = $(this).closest('.thing'),
        $entry = $thing.find('.entry'),
        $child = $thing.find('.child');

    $entry.find('.collapsed').hide();
    $entry.find('.noncollapsed').show();


    $child.removeClass('collapsed');

    // Only show if the children have been expanded
    if(!$child.hasClass('expander-collapsed')) {
        $child.show();
    }
});

$('.child-expander', $commentarea).click(function() {
    var $child = $('.child', $commentarea);

    $(this).hide();

    $child.removeClass('expander-collapsed');

    // Only show if the comment hasn't been collapsed
    if(!$child.hasClass('collapsed')) {
        $child.show();
    }
});

$('.comment .usertext-body a').attr('target', '_blank');