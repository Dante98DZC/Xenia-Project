function anyRowSelected() {
    let selected = false;
    $(".blitzCheck").each(function(){
        if ($(this).prop('checked')){
            selected= true;
            return;
        }
    });
    return selected;
}
function crudElementsAction(url){
    let selection = [];
    $(".blitzCheck").each(function(){
        if($(this).prop('checked') == true){
            $(this).parent().siblings("input").each(function(){
                selection.push($(this).val());
            });
        }
    });
    window.location = url + "?item=" + selection.join("&item=");
}
$(function () {
    $("table").on('change', "td.bs-checkbox>label>input",function(){
        let value = $(this).prop('checked');
        $(this).parent().parent().siblings("td.blitz-checkbox").each(function(){
            $(this).find("input.blitzCheck").prop('checked', value);
        });
    });
    $("table").on('change', "thead>tr>th.bs-checkbox>div>label>input",function(){
        let value = $(this).prop('checked');
        $(this).closest("table").find("tbody").children().each(function(){
            $(this).find("td.blitz-checkbox>div>input").prop('checked', value);
        });
    });
});
