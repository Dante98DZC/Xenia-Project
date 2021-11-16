$(function () {
    var $table = $("#table");
    $("#toolbar")
        .find("select")
        .change(function () {
            $table.bootstrapTable("destroy").bootstrapTable({
                exportDataType: $(this).val(),
                exportTypes: ["excel"],
            });
        })
        .trigger("change");
    $(
        "div.dropdown-menu.dropdown-menu-right>label.dropdown-item.dropdown-item-marker>input.toggle-all+span"
    ).html("Alternar");
    $(
        "div.dropdown-menu.dropdown-menu-right>label.dropdown-item.dropdown-item-marker:first-child+div.dropdown-divider+label.dropdown-item.dropdown-item-marker"
    ).hide();
    function getStorageFixedUrl(url) {
        let pos = url.indexOf("?", url.lastIndexOf("/"));
        if (pos > 0) {
            pos = url.indexOf("search=", pos);
            if (pos > 0) {
                return url.substring(0, pos);
            } else {
                return url + "&";
            }
        } else {
            return url + "?";
        }
    }
    function getFixedUrl(url) {
        let pos = url.indexOf("?", url.lastIndexOf("/"));
        if (pos > 0) {
            pos = url.indexOf("search=", pos);
            if (pos > 0) {
                return url.substring(0, pos - 1);
            } else {
                return url;
            }
        } else {
            return url;
        }
    }
    $("#blitzCrudSearchInput").keyup(function (e) {
        let textSearch = $(this).val();
        let storageUrl =
            getStorageFixedUrl(window.location.href) + "search=" + textSearch;
        let url = getFixedUrl(window.location.href);
        window.history.pushState({ href: storageUrl }, "", storageUrl);
        $.ajax({
            method: "GET",
            url: url,
            data: { search: textSearch },
            success: function (response) {
                $("ul.pagination").html($("ul.pagination", response).html());
                $("#table").bootstrapTable("destroy");
                $("table").html($("table", response).html());
                $("#table").bootstrapTable({
                    exportDataType: null,
                    exportTypes: ["excel"],
                });
                $(
                    "div.dropdown-menu.dropdown-menu-right>label.dropdown-item.dropdown-item-marker>input.toggle-all+span"
                ).html("Alternar");
                $(
                    "div.dropdown-menu.dropdown-menu-right>label.dropdown-item.dropdown-item-marker:first-child+div.dropdown-divider+label.dropdown-item.dropdown-item-marker"
                ).hide();
            },
        });
    });
});

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
