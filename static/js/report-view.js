$(function () {
    var $table = $("#table");
    var currentScript = document.currentScript;
    $("#toolbar")
        .find("select")
        .change(function () {
            $table.bootstrapTable("destroy").bootstrapTable({
                exportDataType: $(this).val(),
                exportTypes: ["xml", "csv", "txt", "excel", "pdf"],
            });
        })
        .trigger("change");
    function buttons() {
        return {
            btnAdd: {
                text: "Add new row",
                icon: "fa-plus",
                event: function () {
                    window.location = currentScript.getAttribute("create-url");
                },
                attributes: {
                    title: "Add a new row to the table",
                },
            },
            btnDelete: {
                text: "Remove item(s)",
                icon: "fa-trash",
                event: function () {
                    getSelected(currentScript.getAttribute("delete-url"));
                },
                attributes: {
                    title: "Remove item(s)",
                },
            },
        };
    }
});
