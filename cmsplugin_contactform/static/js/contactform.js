var contactForm = function(formID) {
    var currentForm = document.getElementById(formID);
    //var this.successMessage = document.querySelector('.form-messages .success');

    function messageSentDone(){
        $('button', currentForm).html($('.success', currentForm).innerHTML)
        window.setTimeout(function(){
            currentForm.reset();
            $('button', currentForm).html(currentForm.original_value)
        }, 2000);
    }

    function showError(data, textStatus, jqXHR){
        var errorHolder = $('.error', currentForm);
        try{
            var responseJSON = JSON.parse(data.responseText);   
        } catch(e) {
            errorHolder.show();
        }

        if(typeof responseJSON != 'undefined' && data.status == 400){
            for(var error in responseJSON) {
                //$('label.' + error).addClass('error');
                errorHolder = $('label.' + error + ' .error', currentForm);
                var errorMessage = "";
                for(var message in responseJSON[error]) {
                    errorMessage += responseJSON[error][message];
                }
                errorHolder.html(errorMessage);
                errorHolder.show();
            }
        }
        $('button', currentForm).html(currentForm.original_value)
    }

    currentForm.addEventListener('submit', function(evt){
        evt.preventDefault()
        var formData = $(currentForm).serialize();
        var submitBtn = $('button', currentForm)
        currentForm.original_value = submitBtn.html()
        submitBtn.html("Processing...")
        $.ajax({
            type: "POST",
            url: evt.target.action,
            data: formData,
            dataType: 'json',
            accept: 'application/json'
        })
        .done(messageSentDone)
        .fail(showError);
    });
};