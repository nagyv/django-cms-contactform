var contactForm = function(formID) {
    var currentForm = document.getElementById(formID);
    //var this.successMessage = document.querySelector('.form-messages .success');

    function messageSentDone(){
        $('button', currentForm).html(document.querySelector('.form-messages .success').innerHTML)
        window.setTimeout(function(){
            currentForm.reset();
            $('button', currentForm).html(currentForm.original_value)
        }, 2000);
    }

    function showError(data, textStatus, jqXHR){
        var errorHolder = $('.form-messages .error');
        var errorMessage = "Some error occured. Please try again later!"
        try{
            var responseJSON = JSON.parse(data.responseText);   
        } catch(e) {
            responseJSON = '';
        }
        
        errorHolder.empty();

        if(data.status == 400){
            errorMessage = "";
            for(var error in responseJSON) {
               errorMessage += responseJSON[error][0]+'<br>';
            }
        }

        errorHolder.append(errorMessage);
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