$(function () {
    var $table = $("#table");
    $("#toolbar")
        .find("select")
        .change(function () {
            $table.bootstrapTable("destroy").bootstrapTable({
                exportDataType: $(this).val(),
                exportTypes: ["xml", "csv", "txt", "excel", "pdf"],
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
function crudElementsAction(url) {
    let selection = [];
    $(".blitzCheck").each(function () {
        if ($(this).prop("checked") == true) {
            $(this)
                .parent()
                .siblings("input")
                .each(function () {
                    selection.push($(this).val());
                });
        }
    });
    window.location = url.substring(0, url.length - 5) + `${selection[0]}/`;
}
var currentScript = document.currentScript;
function buttons() {
    return {
        btnAdd: {
            text: "Crear registro",
            icon: "fa-plus",
            event: function () {
                window.location = currentScript.getAttribute("create-url");
            },
            attributes: {
                title: "Crear registro",
            },
        },
        btnDelete: {
            text: "Eliminar elemento(s)",
            icon: "fa-trash",
            event: function () {
                if (anyRowSelected()) {
                    crudElementsAction(
                        currentScript.getAttribute("delete-url")
                    );
                }
            },
            attributes: {
                title: "Eliminar elemento(s)",
            },
        },
        btnEdit: {
            text: "Editar registro(s)",
            icon: "fa-edit",
            event: function () {
                if (anyRowSelected()) {
                    crudElementsAction(
                        currentScript.getAttribute("update-url")
                    );
                }
            },
            attributes: {
                title: "Editar registro(s)",
            },
        },
    };
}

function formatYesNo(value, row, index) {
    return value == "False" ? "No" : "Yes";
}
