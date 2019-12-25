$("#button").click(function () {
    event.preventDefault();
    var $title = $("#title").val().trim();
    var $article = $("#article").val().trim();
    console.log($title);
    console.log($article);
    $.post("/blog/createarticle/", {"article": $article, "title": $title}, function (data) {
        console.log(data)

        if (data["status"] === 200){
            window.open('/blog/mine/', target="_self")
        }
    })
})



