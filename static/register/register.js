$(function () {

    var $username = $("#username_input");

    $username.change(function () {
        var username = $username.val().trim();

        if (username.length) {

            //    将用户名发送给服务器进行预校验
            $.getJSON('/movie/checkuser/', {'username': username}, function (data) {

                console.log(data);

                var $username_info = $("#username_info");

                if (data['status'] === 200){
                    $username_info.html("用户名可用").css("color", 'green');
                }else  if(data['status'] ===901){
                    $username_info.html("用户已存在").css('color', 'red');
                }

            })

        }

    })


});


function check() {
    var $username = $("#username_input");

    var username = $username.val().trim();

    if (!username){
        return false
    }

    var info_color = $("#username_info").css('color');

    console.log(info_color);

    if (info_color == 'rgb(255, 0, 0)'){
        return false
    }

    return true
}


/*  预校验邮箱 */
$(function () {

    var $email = $("#email_input");

    $email.change(function () {
        var email = $email.val().trim();

        if (email.length) {

            //    将邮箱发送给服务器进行预校验
            $.getJSON('/movie/checkemail/', {'email': email}, function (data) {

                console.log(data);

                var $email_info = $("#email_info");

                if (data['status'] === 200){
                    $email_info.html("邮箱可用").css("color", 'green');
                }else  if(data['status'] ===901){
                    $email_info.html("该邮箱已注册!").css('color', 'red');
                }

            })

        }

    })


})


function checkemail() {
    var $email = $("#email_input");

    var email = $username.val().trim();

    if (!email){
        return false
    }

    var info_color = $("#email_info").css('color');

    console.log(info_color);

    if (info_color == 'rgb(255, 0, 0)'){
        return false
    }

    return true
}
/* 密码非空预校验 */
$(function () {

    var $password = $("#password_input");
    var $password1 = $("#password_info");
    $password.change(function () {
        var password = $password.val().trim();
        if (password.length < 6) {
            console.log(password.length);

            $password1.html("密码格式不正确!").css('color', 'red');
        }
        else {
            $password1.html("密码可用").css("color", 'green');
        }
    })
});




/* 确认密码预校验 */
$(function () {
    var $password_again = $("#password_confirm_input");
    var $password = $("#password_input");

    var $password_again_info = $("#password_again_info");

    $password_again.change(function () {
        var passwordagain = $password_again.val().trim();
        var password = $password.val().trim();
        if (passwordagain === password) {

            $password_again_info.html("密码输入正确").css("color", 'green');

        }
        else {
            $password_again_info.html("两次密码输入不相同!").css('color', 'red');
        }
    })
});



