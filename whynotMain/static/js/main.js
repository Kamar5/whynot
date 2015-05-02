$(function() {
    console.log("starting...");
    var thumbsoup = "fa-thumbs-o-up";
    var thumbsup = "fa-thumbs-up";
    var good = "Good Job!";
    var awesome = "Awesome Effort!";
    var unbelivable = "I am going to cry!";
    $(".vote-button").hover(
        function() {
            $(this).addClass(thumbsup).removeClass(thumbsoup);
            $(this).prev().addClass(thumbsup).removeClass(thumbsoup);
            $(this).prev().prev().addClass(thumbsup).removeClass(thumbsoup);
            var index = $(this).index();
            console.log(index);

            if (index == 0) {
                $(this).siblings(".vote-message").html(good);
            } else if (index == 1) {
                $(this).siblings(".vote-message").html(awesome);
            } else if (index == 2) {
                $(this).siblings(".vote-message").html(unbelivable);
            }
        },
        function() {
            $(this).removeClass(thumbsup).addClass(thumbsoup);
            $(this).prev().removeClass(thumbsup).addClass(thumbsoup);
            $(this).prev().prev().removeClass(thumbsup).addClass(thumbsoup);
            $(this).siblings(".vote-message").html("");
        }
    );

    $(".vote-button").click(function() {
            var voteup = $(this).attr("voter-value");
            console.log(voteup);

            var value = $(this).parent(".vote-buttons").siblings(".effort-results").children(".effort-score").children(".value");
            var currentValue = value.html();
            console.log(currentValue);

            var increment = parseInt(currentValue) + parseInt(voteup);
            console.log(increment);
            value.html(increment);
        });
});
