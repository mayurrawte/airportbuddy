/**
 * Created by someone on 4/1/17.
 */
$(document).ready(function()
{
   $('#staff-login-formbtn').on('click',function(event)
   {
      event.preventDefault();
       var tempdata = $('#staff-login-form').serializeArray();
       var jsondata = {};

       $.each(tempdata,function(i,v)
        {
           jsondata[v.name] = v.value;
        });

       $.ajax({
            type: "POST",
            url: "/getuser/",
            data : {
              username : jsondata['username'],
                password : jsondata['password']
            },
            success: function (data) {
                if(data == "OK")
                {
                    window.location = "/dash";
                }
            },
            error: function (xhr, errmsg, err) {
                alert(xhr.status + ": " + xhr.responseText);
            }
        });

        /*
        var jsondata = {};
        jsondata['is_admin'] = false;
        jsondata['username'] = "Someone";
        jsondata['email'] = "somoeone@gmail.com";
        jsondata['emailVerified'] = "yes";
        jsondata['password'] = "random";
        jsondata['mobile_no'] = 564654;
        jsondata['realm'] = "sdfkj";

        $.ajax({
            type: "POST",
            url: "http://www.typingkeeda.in:8000/api/users",
            data: jsondata,
            success: function (data)
            {
                alert(data);
            },
            error: function (xhr, errmsg, err)
            {
                alert(xhr.status + ": " + xhr.responseText);
            }
        });
        */

   });


   $('#staff-register-formbtn').on('click',function(event)
   {
      event.preventDefault();
      var tempdata = $('#staff-form-register').serializeArray();
       var jsondata = {};

       $.each(tempdata,function(i,v)
        {
           jsondata[v.name] = v.value;
        });

       jsondata['realm'] = "ok";
       jsondata['is_admin'] = true;


        $.ajax({
            type: "POST",
            url: "http://www.typingkeeda.in:8000/api/users",
            data: jsondata,
            success: function (data)
            {
                alert(JSON.stringify(data));
            },
            error: function (xhr, errmsg, err)
            {
                alert(xhr.status + ": " + xhr.responseText);
            }
        });

   });

   function login()
   {

   }

    $('#mqtt-test').on('click',function(event) {
        event.preventDefault();
        var topic = document.getElementById('topic').value;
        var message_h = document.getElementById('message').value;

        $.ajax({
            type : "POST",
            url : "../admin/sos",
            data : {
                topic : topic,
                message: message_h,
            },
            success : function(data)
            {
                console.log(data);
            },
            error: function (xhr, errmsg, err)
            {
                alert(xhr.status + ": " + xhr.responseText);
            }
        });
    });

});