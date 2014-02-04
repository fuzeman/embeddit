$('.link .expando-button').on('click', function (){
    if($(this).hasClass('collapsed')) {
        $(this).removeClass('collapsed').addClass('expanded');
        $(this).parent().find('.expando').show();
    } else {
        $(this).removeClass('expanded').addClass('collapsed');
        $(this).parent().find('.expando').hide();
    }
});

$('.link .usertext-body a').attr('target', '_blank');