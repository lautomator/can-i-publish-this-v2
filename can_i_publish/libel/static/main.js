var libel_main_script = {
    button_click: function (e) {
        var choice = e.target.dataset.choice;
        var url_path = "/";

        if (choice === "None") {
            url_path += "libel/summary/";
        } else if (choice === "metrics") {
            url_path += "libel/metrics/";
        } else {
            url_path += "libel/" + choice;
        }

        window.location.pathname = url_path;
    },
    disable_back_browsing: function () {
        window.history.pushState(null, null, window.location.href);
        window.onpopstate = function () {
            window.history.go(1);
        };
    },
    init: function () {
        // listen for button clicks
        var index = 0;
        if (this.targets.choices.length > 0) {

            while (index < this.targets.choices.length) {
                this.targets.choices[index].onclick = this.button_click;
                index += 1;
            }
        }

        this.disable_back_browsing();
    },
    targets: {
        choices: document.querySelectorAll(".choice")
    }
};

libel_main_script.init();
