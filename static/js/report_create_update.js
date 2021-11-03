$(function () {
function update_report_ui(element,responsed){
    if(responsed){
        $(element).parent().parent().parent().siblings(".report-response-conditional").removeClass("disabledbutton");
        $(element).parent().parent().parent().parent().siblings(".report-response-conditional").removeClass("disabledbutton");
    }else{
        $(element).parent().parent().parent().siblings(".report-response-conditional").addClass("disabledbutton");
        $(element).parent().parent().parent().parent().siblings(".report-response-conditional").addClass("disabledbutton");
    }
}
$("div.responsed").find("div").first().find("input").click(function(){
    update_report_ui($(this),true);
});
$("div.responsed").find("div").last().find("input").click(function(){
    update_report_ui($(this),false);
});
let element = $("div.responsed").find("div").first().find("input");
update_report_ui(element, element.prop("checked"));
});