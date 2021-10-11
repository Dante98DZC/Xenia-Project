$(function () {
    var $table = $("#table");
    $("#toolbar")
        .find("select")
        .change(function () {
            $table.bootstrapTable("destroy").bootstrapTable({
                exportDataType: $(this).val(),
                exportTypes: ["xml", "csv", "txt", "excel", "pdf"]
            });
        })
        .trigger("change");
    $(
        "div.dropdown-menu.dropdown-menu-right>label.dropdown-item.dropdown-item-marker>input.toggle-all+span"
    ).html("Alternar");
    $(
        "div.dropdown-menu.dropdown-menu-right>label.dropdown-item.dropdown-item-marker:first-child+div.dropdown-divider+label.dropdown-item.dropdown-item-marker"
    ).hide();
});
var currentScript = document.currentScript;
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
                if (anyRowSelected()) {
                    crudElementsAction(
                        currentScript.getAttribute("delete-url")
                    );
                }
            },
            attributes: {
                title: "Remove item(s)",
            },
        },
        btnEdit: {
            text: "Update item(s)",
            icon: "fa-edit",
            event: function () {
                if (anyRowSelected()) {
                    crudElementsAction(
                        currentScript.getAttribute("update-url")
                    );
                }
            },
            attributes: {
                title: "Update item(s)",
            },
        },
        btnDetail: {
            text: "Show detail from item(s)",
            icon: "fa-eye",
            event: function () {
                if (anyRowSelected()) {
                    crudElementsAction(
                        currentScript.getAttribute("detail-url")
                    );
                }
            },
            attributes: {
                title: "Show detail from item(s)",
            },
        },
    };
}
