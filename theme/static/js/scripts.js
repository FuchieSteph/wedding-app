var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl,{html: true})
});

$(document).on('click', '.modal-backdrop', function() { $('.modal').modal('hide') });