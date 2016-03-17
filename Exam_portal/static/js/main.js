$(document).ready(function () {


    $('#previous').click(function(event){
        event.preventDefault();
        console.log("Element have been subitted for previous");

        $.ajax({
            type:"GET",
            url:"http://127.0.0.1:8000/exam/previous/",
            success:function(data){
                console.log("Ajax on previous have been called");
                console.log(data);
                console.log(data['question']);
                $('#1').text(data['question']);
                $('#2').text(data['choices'][0]);
                $('#3').text(data['choices'][1]);
                $('#4').text(data['choices'][2]);
                $('#5').text(data['choices'][3]);

            }
        })
    });




    $('#next').click(function (event) {
        event.preventDefault();
        console.log("Element have been submitted for next ");
        //console.log($('#test').val());
        //console.log($('#test2').val());
        //console.log($('#test3').val());
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/exam/next/",
            success: function (data) {
                console.log("success");
                console.log(data);
                console.log(data['question']);
                console.log(data['choices']);

                //console.log(data[0]['models']);
                $('#1').text(data['question']);
                $('#2').text(data['choices'][0]);
                $('#3').text(data['choices'][1]);
                $('#4').text(data['choices'][2]);
                $('#5').text(data['choices'][3]);


            }
        });

    });




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
    $('.check').click(function (event) {
        event.preventDefault();
        console.log('post request via ajax');
        console.log($("#test").val());
        $.ajax({
            type: "POST",
            url: "/exam/postajax/",
            dataType: "json",
            data: {"item": $("#test").val()},
            success: function (data) {
                console.log("hello success ajax post request");
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
