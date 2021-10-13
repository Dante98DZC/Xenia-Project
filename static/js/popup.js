function showEditPopup(clicked) {
    const field_id = clicked.id.replace("_edit", "");
    const val = $("#"+field_id).val();
    href = clicked.href + val + "/change?_popup=1";
    let win = window.open(href, "Edit",
        'height=500,width=800,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}
function showAddPopup(triggeringLink) {
    const text_id = triggeringLink.id.replace("_add", "")
    href = triggeringLink.href + "?_popup=1&_field_to_add=" + text_id;
    var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}
function closePopup(win, newID, newRepr, id) {
    $(id).append(new Option(newRepr, newID)).val(newID).trigger("input");
    win.close();
}
