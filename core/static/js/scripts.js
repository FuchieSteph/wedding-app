$('#sortBy').on('change', function() {
    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set('o', $(this).val());
    window.location.search = urlParams;
});

$('.form-check-input').on('click', function() {
    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set($(this).attr('id'), $(this).val() == 'on' ? 'true' : 'false');
    window.location.search = urlParams;
});

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const order = urlParams.get('o')

var params = {'o':'#sorBy', 'menu':'', 'echoppes':'', 'buffet':'', 'dishes_included':''};

urlParams.forEach(function(value, key) {
    if(params.hasOwnProperty(key)) {
        if(params[key] != '') $(params[key]).val(value);
        else $('#'+key).val(value);

        $('#'+key).val(value);
    }
});
