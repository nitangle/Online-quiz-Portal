$(document).ready(function () {

    


    $.ajax({
        type: "GET",
        datatype: 'json',
        url: 'http://127.0.0.1:8000/exam/timer',

        success: function (data) {
            var h = data['time'][0];
            var m = data['time'][1];
            var s = data['time'][2];
            var now = new Date();
            console.log(now.toString());
            var test_time = new Date(now.getFullYear(), now.getMonth(), now.getDate(), h, m, s);
            var epoch = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 0, 0, 0);
            var test_duration = Math.floor(Date.parse(test_time) - Date.parse(epoch));
            console.log(test_duration);
            var today = new Date();
            var stop = setInterval(function () {
                var current = new Date();
                var diff = Math.floor(Date.parse(current) - Date.parse(today));
                console.log(diff);
                if (diff == test_duration) {
                    clearInterval(stop);

                    window.location.replace("http://127.0.0.1:8000/exam/end");

                }
                var seconds = Math.floor(diff / 1000) % 60;
                var minutes = Math.floor(diff / 1000 / 60) % 60;
                var hours = Math.floor(diff / 1000 / 60 / 60) % 24;


                document.getElementById("time").innerHTML = hours + ':' + minutes + ':' + seconds;

            }, 1000);
        }
    });

    $('#mark').click(function(event){
        event.preventDefault();
        console.log(event.target.class);
        console.log("Element have been subitted for mark");
        selectedVal = null;

        var selected = $("input[type='radio'][name='choice']:checked");

        if (selected.length > 0) {
            selectedVal = selected.val();
            console.log(selectedVal);
        }
        $.ajax({
            type:"POST",
            url:"http://127.0.0.1:8000/exam/next/",
            datatype:'json',
            data:{'answer':selectedVal},
            success: function (data) {
                console.log("success");
                $('input[type="radio"]').each(function(){
                     $(this).checked = false;
                 });
                     if(data['color']){
                         $('#'+data['color'].toString()).css("background-color",'#F71B1B');
                        }
                     loaddata(data);
                }
            });
            
        

    });


    $('#grid').find('li').click(function(event){
        event.preventDefault();
        console.log("changing question via grid");
        id = event.target.id;
        console.log(id);
        $.ajax({
            type:"GET",
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
        console.log(event.target.class);
        console.log("Element have been subitted for previous");

        //selectedVal = null;
        //
        //var selected = $("input[type='radio'][name='choice']:checked");
        //if (selected.length > 0) {
        //    selectedVal = selected.val();
        //    console.log(selectedVal);
        //}

        $.ajax({
            type:"GET",
            //datatype:'json',
            //data:{'answer':selectedVal},
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
                
                console.log("success");
                console.log(data);
                console.log(data['question']);
                console.log(data['choices']);
                console.log(data['color']);

                if(data['color']){
                    $('#'+data['color'].toString()).css("background-color",'#3CC541');
                }
                var color = '#3CC541';
                $('input[type="radio"]').each(function(){
                    $(this).checked = false;
                    });
                loaddata(data);
                var color = '#3CC541';





            }

        });

    });




    function loaddata(data){
        $('#question').text(data['question']);

        console.log(data['choice_data'][0][0]);
        console.log(data['choice_data'][0][1]);
        console.log("hello "+data['question_no'].toString());
        // $('#choices').text(" ")

        $('span #question_no').text(data['question_no']+".");


        for(i=0;i<data['choice_data'].length;i++) {
            
            id = '#q'+ (i+1).toString();
            $('#test'+(i+1).toString()).attr({'value':data['choice_data'][i][1],'checked':false});
            $(id).text(data['choice_data'][i][0]);
            
            // $('#choices').append('<li class="collection=item"><input name="choice" type="radio" id="test"'+ toString(i+1)+'value="'+ toString(data['choice_data'][i][1])+'"/><label style="color:black;font-style: normal;" for="test'+toString(i+1)+'" id="q'+toString(i+1)+'">'+data['choice_data'][i][0]+'</label></li>');

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
