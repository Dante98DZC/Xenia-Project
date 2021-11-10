(function ($) {
    "use strict";
    $(".delete-notifications").on("click", function (e) {
        e.preventDefault();
        $.post($(this).data("url"), {
            csrfmiddlewaretoken: $(this).data("token"),
        });
        $(this).parent().hide();
        $(".notifications-count").html(
            parseInt($(".notifications-count").html()) - 1
        );
    });
    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }

    function createSkinBlock(colors, callback, noneSelected) {
        var $block = $("<select />", {
            class: noneSelected
                ? "custom-select mb-3 border-0"
                : "custom-select mb-3 text-light border-0 " +
                  colors[0].replace(/accent-|navbar-/, "bg-"),
        });

        if (noneSelected) {
            var $default = $("<option />", {
                text: "None Selected",
            });
            if (callback) {
                $default.on("click", callback);
            }

            $block.append($default);
        }

        colors.forEach(function (color) {
            var $color = $("<option />", {
                class: (typeof color === "object" ? color.join(" ") : color)
                    .replace("navbar-", "bg-")
                    .replace("accent-", "bg-"),
                text: capitalizeFirstLetter(
                    (typeof color === "object" ? color.join(" ") : color)
                        .replace(/navbar-|accent-|bg-/, "")
                        .replace("-", " ")
                ),
            });

            $block.append($color);

            $color.data("color", color);

            if (callback) {
                $color.on("click", callback);
            }
        });

        return $block;
    }

    var $sidebar = $(".control-sidebar");
    var $container = $("<div />", {
        class: "p-3 control-sidebar-content",
    });

    $sidebar.append($container);

    // Checkboxes

    $container.append(
        '<div class="row"> <i class="fa fa-angle-double-right mt-1 ml-3" data-widget="control-sidebar" data-slide="true" role="button" ></i>  <h5 class="ml-auto mr-2">Configuración</h5></div><hr class="mb-2"/>'
    );

    var $dark_mode_checkbox = $("<input />", {
        type: "checkbox",
        value: 1,
        checked: localStorage.getItem("blitz-dark-mode"),
        class: "mr-1",
    }).on("click", function () {
        if ($(this).is(":checked")) {
            localStorage.setItem("blitz-dark-mode", true);
            $(document.body)
                .removeClass("bootstrap")
                .addClass("bootstrap-dark");
        } else {
            localStorage.setItem("blitz-dark-mode", false);
            $(document.body)
                .removeClass("bootstrap-dark")
                .addClass("bootstrap");
        }
    });
    var $dark_mode_container = $("<div />", { class: "mb-4" })
        .append($dark_mode_checkbox)
        .append("<span>Dark Mode</span>");
    $container.append($dark_mode_container);

    if (localStorage.getItem("blitz-dark-mode") === "true") {
        $dark_mode_checkbox.prop("checked", true);
        $(document.body).removeClass("bootstrap").addClass("bootstrap-dark");
    } else {
        $dark_mode_checkbox.prop("checked", false);
        $(document.body).removeClass("bootstrap-dark").addClass("bootstrap");
        localStorage.setItem("blitz-dark-mode", false);
    }

    $container.append("<h6>Header Options</h6>");

    var $header_fixed_checkbox = $("<input />", {
        type: "checkbox",
        value: 1,
        checked: localStorage.getItem("xenia-layout-navbar-fixed"),
        class: "mr-1",
    }).on("click", function () {
        if ($(this).is(":checked")) {
            localStorage.setItem("xenia-layout-navbar-fixed", true);
            $(document.body).addClass("layout-navbar-fixed");
        } else {
            localStorage.setItem("xenia-layout-navbar-fixed", false);
            $(document.body).removeClass("layout-navbar-fixed");
        }
    });
    var $header_fixed_container = $("<div />", { class: "mb-1" })
        .append($header_fixed_checkbox)
        .append("<span>Fixed</span>");
    $container.append($header_fixed_container);

    if (localStorage.getItem("xenia-layout-navbar-fixed") === "true") {
        $header_fixed_checkbox.prop("checked", true);
        $(document.body).addClass("layout-navbar-fixed");
    } else {
        $header_fixed_checkbox.prop("checked", false);
        $(document.body).removeClass("layout-navbar-fixed");
        localStorage.setItem("xenia-layout-navbar-fixed", false);
    }

    $container.append("<h6>Sidebar Options</h6>");

    var $sidebar_collapsed_checkbox = $("<input />", {
        type: "checkbox",
        value: 1,
        checked: localStorage.getItem("xenia-sidebar-collapse"),
        class: "mr-1",
    }).on("click", function () {
        if ($(this).is(":checked")) {
            localStorage.setItem("xenia-sidebar-collapse", true);
            $(document.body).addClass("sidebar-collapse");
            $(window).trigger("resize");
        } else {
            localStorage.setItem("xenia-sidebar-collapse", false);
            $(document.body).removeClass("sidebar-collapse");
            $(window).trigger("resize");
        }
    });
    var $sidebar_collapsed_container = $("<div />", { class: "mb-1" })
        .append($sidebar_collapsed_checkbox)
        .append("<span>Collapsed</span>");
    $container.append($sidebar_collapsed_container);

    if (localStorage.getItem("xenia-sidebar-collapse") === "true") {
        $sidebar_collapsed_checkbox.prop("checked", true);
        $(document.body).addClass("sidebar-collapse");
        $(window).trigger("resize");
    } else {
        $sidebar_collapsed_checkbox.prop("checked", false);
        $(document.body).removeClass("sidebar-collapse");
        $(window).trigger("resize");
        localStorage.setItem("xenia-sidebar-collapse", false);
    }

    $(document).on(
        "collapsed.lte.pushmenu",
        '[data-widget="pushmenu"]',
        function () {
            localStorage.setItem("xenia-sidebar-collapse", true);
        }
    );
    $(document).on(
        "shown.lte.pushmenu",
        '[data-widget="pushmenu"]',
        function () {
            localStorage.setItem("xenia-sidebar-collapse", false);
        }
    );

    var $no_expand_sidebar_checkbox = $("<input />", {
        type: "checkbox",
        value: 1,
        checked: localStorage.getItem("xenia-sidebar-no-expand"),
        class: "mr-1",
    }).on("click", function () {
        if ($(this).is(":checked")) {
            localStorage.setItem("xenia-sidebar-no-expand", true);
            $(".main-sidebar").addClass("sidebar-no-expand");
        } else {
            localStorage.setItem("xenia-sidebar-no-expand", false);
            $(".main-sidebar").removeClass("sidebar-no-expand");
        }
    });
    var $no_expand_sidebar_container = $("<div />", { class: "mb-4" })
        .append($no_expand_sidebar_checkbox)
        .append("<span>Disable Hover/Focus Auto-Expand</span>");
    $container.append($no_expand_sidebar_container);

    if (localStorage.getItem("xenia-sidebar-no-expand") === "true") {
        $no_expand_sidebar_container.prop("checked", true);
        $(".main-sidebar").addClass("sidebar-no-expand");
    } else {
        $no_expand_sidebar_container.prop("checked", false);
        $(".main-sidebar").removeClass("sidebar-no-expand");
        localStorage.setItem("xenia-sidebar-no-expand", false);
    }
})(jQuery);
