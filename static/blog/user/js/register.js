function check() {
    var $password_input = $("#password_input");
    var password = $password_input.val().trim();
    console.log(password);
    var $password_confirm_input = $("#password_confirm_input");
    var password_confirm_input = $password_confirm_input.val().trim();
    console.log(password_confirm_input);
    if (password_confirm_input == password){
        $(".btn btn-success btn-block").removeAttr("disabled");
        console.log("111");
    }
    else {
        $(".btn btn-success btn-block").attr("disabled", "disabled");
        console.log("222");
    }

}
