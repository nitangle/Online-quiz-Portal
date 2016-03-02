


$(document).ready(function () {

    // AJAX GET
    $('li').click(function () {

        //url_data = "https://127.0.0.1:8000/exam/"+$('li').val()+"/";
        //console.log(url_data);

        // console.log("am i called a get method");
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/exam/ajaxdisplay/",
            success: function (data) {

                //console.log("am i called a get method");
                //console.log(data)
                //var jdata = jQuery.parseJSON(data);
                // var arr = $.map(data, function(el) { return el });
                //console.log(jdata);
                //var parsed = jQuery.parseJSON(data);


                //console.log(parsed)
                //var arr = [];
                //
                //for (var x in parsed) {
                //    arr.push(parsed[x]);
                //}
                // console.log(arr);
                console.log(data[0]['model']);
                console.log(data[0]['fields']['name'])
                console.log(data[0]['fields'])

                var num = data[0]['fields']['name']

                $('.ul').append("<li >" + num + "</li>");


                //for (i = 0; i < data.length; i++) {
                //    console.log(data)
                //    $('li').append('<li >'+data[i]+'</li>');
                //    $('li').css("color", "red");
                //}
            }
        });

    });


    // AJAX POST
    $('.add-todo').click(function () {
        console.log('am i called');

        $.ajax({
            type: "POST",
            url: "/ajax/add/",
            dataType: "json",
            data: {"item": $(".todo-item").val()},
            success: function (data) {
                alert(data.message);
            }
        });

    });


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
