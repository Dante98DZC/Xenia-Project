$(function () {
    function get_formated_date() {
        let current_datetime = new Date();
        let formatted_date =
            ("0" + current_datetime.getDate()).slice(-2) +
            "/" +
            ("0" + (current_datetime.getMonth() + 1)).slice(-2) +
            "/" +
            current_datetime.getFullYear() +
            " " +
            ("0" + current_datetime.getHours()).slice(-2) +
            ":" +
            ("0" + current_datetime.getMinutes()).slice(-2);
        return formatted_date;
    }
    $("div.solved").each(function () {
        if (!$(this).find("div").first().find("input").prop("checked")) {
            $("." + $(this).data("disable")).addClass("disabledbutton");
            $("." + $(this).data("disable-date")).addClass("disabledbutton");
        }
    });
    $("div.solved").on("change", "input", function () {
        if ($(this).prop("checked")) {
            if ($(this).val()=="true") {
                $("." + $(this).parent().parent().data("disable")).removeClass(
                    "disabledbutton"
                );
                $(
                    "." + $(this).parent().parent().data("disable-date")
                ).removeClass("disabledbutton");
            } else {
                $("." + $(this).parent().parent().data("disable")).addClass(
                    "disabledbutton"
                );
                $(
                    "." + $(this).parent().parent().data("disable-date")
                ).addClass("disabledbutton");
                $("input", $("." + $(this).data("disable-date"))).val(
                    get_formated_date()
                );
            }
        }
    });
});
