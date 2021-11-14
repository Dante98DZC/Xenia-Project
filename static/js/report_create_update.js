$(function () {
    function update_report_ui(element, solved) {
        if (solved) {
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
            $(
                "input",
                $(element)
                    .parent()
                    .parent()
                    .parent()
                    .parent()
                    .siblings(".report-response-conditional")
            ).val(formatted_date);
            $(element)
                .parent()
                .parent()
                .parent()
                .siblings(".report-response-conditional")
                .removeClass("disabledbutton");
            $(element)
                .parent()
                .parent()
                .parent()
                .parent()
                .siblings(".report-response-conditional")
                .removeClass("disabledbutton");
        } else {
            $(element)
                .parent()
                .parent()
                .parent()
                .siblings(".report-response-conditional")
                .addClass("disabledbutton");
            $(element)
                .parent()
                .parent()
                .parent()
                .parent()
                .siblings(".report-response-conditional")
                .addClass("disabledbutton");
        }
    }
    $("div.solved")
        .find("div")
        .first()
        .find("input")
        .click(function () {
            update_report_ui($(this), true);
        });
    $("div.solved")
        .find("div")
        .last()
        .find("input")
        .click(function () {
            update_report_ui($(this), false);
        });
    let element = $("div.solved").find("div").first().find("input");
    update_report_ui(element, element.prop("checked"));
});
