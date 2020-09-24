$(function() {
    // 하단 롤링배너
    
    $("#arrow_right").click(function(){
        $(".food1").eq(0).insertAfter(".food1:last-child");
        $(".food2").eq(0).insertAfter(".food2:last-child");
    });

    $("#arrow_left").click(function(){
        $(".food1").eq(-1).insertBefore(".food1:first-child");
        $(".food2").eq(-1).insertBefore(".food2:first-child");
    });

    // 롤링배너 클릭 시 클릭 효과

    $(".food").click(function() {
        if ($(this).hasClass("clicked") == false) {
            $(this).addClass("clicked");
            $(this).css({"border": "5px solid blue"});
        }
        else {
            $(this).removeClass("clicked");
            $(this).css({"border": "1px solid blue"});
        };
    });

    // 클릭한 데이터 값 저장

    $("#food1").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input1").val($(this).text());
        }
        else {
            $("#input1").val("");
        }
    })

    $("#food2").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input2").val($(this).text());
        }
        else {
            $("#input2").val("");
        }
    })

    $("#food3").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input3").val($(this).text());
        }
        else {
            $("#input3").val("");
        }
    })

    $("#food4").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input4").val($(this).text());
        }
        else {
            $("#input4").val("");
        }
    })

    $("#food5").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input5").val($(this).text());
        }
        else {
            $("#input5").val("");
        }
    })

    $("#food6").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input6").val($(this).text());
        }
        else {
            $("#input6").val("");
        }
    })

    $("#food7").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input7").val($(this).text());
        }
        else {
            $("#input7").val("");
        }
    })

    $("#food8").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input8").val($(this).text());
        }
        else {
            $("#input8").val("");
        }
    })

    $("#food9").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input9").val($(this).text());
        }
        else {
            $("#input9").val("");
        }
    })

    $("#food10").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input10").val($(this).text());
        }
        else {
            $("#input10").val("");
        }
    })

    $("#food11").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input11").val($(this).text());
        }
        else {
            $("#input11").val("");
        }
    })

    $("#food12").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input12").val($(this).text());
        }
        else {
            $("#input12").val("");
        }
    })

    $("#food13").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input13").val($(this).text());
        }
        else {
            $("#input13").val("");
        }
    })

    $("#food14").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input14").val($(this).text());
        }
        else {
            $("#input14").val("");
        }
    })

    $("#food15").click(function() {
        if ($(this).hasClass("clicked")) {
            $("#input15").val($(this).text());
        }
        else {
            $("#input15").val("");
        }
    })
})