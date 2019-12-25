$("#button").click(function () {
    event.preventDefault();
    var $comment = $("#comment").val().trim();


    console.log($comment);

    $.post("/blog/comment/", {"c_content": $comment}, function (data) {
        console.log(data);

        if (data["status"] === 200) {
            window.location.reload()
        }}
    )
})