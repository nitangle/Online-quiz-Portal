$(document).ready(function () {
    $('#grid').find('li').click(function(event){
        event.preventDefault();
        console.log("changing question via grid");
        id = event.target.id;
        console.log(id);
        $.ajax({
            type:"POST",
            datatype:'json',
            data:{'id':id},
            url:"http://127.0.0.1:8000/exam/grid/",
            success:function(data){
                console.log("successful request");
                loaddata(data);
            }
        });
    });



    $('#previous').click(function(event){
        event.preventDefault();
        console.log("Element have been subitted for previous");

        selectedVal = null;

        var selected = $("input[type='radio'][name='choice']:checked");
        if (selected.length > 0) {
            selectedVal = selected.val();
            console.log(selectedVal);
        }

        $.ajax({
            type:"POST",
            datatype:'json',
            data:{'answer':selectedVal},
            url:"http://127.0.0.1:8000/exam/previous/",
            success:function(data){

                console.log("Ajax on previous have been called");
                console.log(data);
                console.log(data['question']);
                loaddata(data)


            }
        })
    });



    $('#next').click(function (event) {
        event.preventDefault();
        console.log("Element have been submitted for next ");

        selectedVal = null;

        var selected = $("input[type='radio'][name='choice']:checked");

        if (selected.length > 0) {
            selectedVal = selected.val();
            console.log(selectedVal);
        }

        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/exam/next/",
            datatype:'json',
            data:{'answer':selectedVal},
            success: function (data) {
                $('input[type="radio"]').each(function(){
                     $(this).checked = false;
                });
                console.log("success");
                console.log(data);
                console.log(data['question']);
                console.log(data['choices']);

                loaddata(data);




            }
        });

    });




    function loaddata(data){
        $('#question').text(data['question']);

        for(i=0;i<data['choices'].length;i++) {
            id = '#q'+ (i+1).toString();
            $('#test'+(i+1).toString()).attr({'value':data['choices'][i],'checked':false});
            $(id).text(data['choices'][i]);

        }
    }




    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


});
