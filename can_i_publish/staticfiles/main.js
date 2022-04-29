var libel_main_script = {
    choice_button_click: function (e) {
        var choice = e.target.dataset.choice;
        var submit_btn = document.getElementById("submit_choice");
        var url_path = "/libel/";

        if (choice === "None") {
            // go to the summary
            window.location.pathname = url_path + "summary/";
        } else if (choice === "metrics") {
            // go to the metrics page
            window.location.pathname = url_path + "metrics/";
        } else if (choice === "Q1") {
            // start over
            window.location.pathname = url_path + "Q1/";
        } else {
            if (submit_btn !== null) {
                submit_btn.removeAttribute("disabled");
                submit_btn.classList.add("is_active");

                // clicking the continue button will initiate the new request
                submit_btn.onclick = function () {
                    window.location.pathname = url_path + choice;
                };
            } else {
                // next button
                window.location.pathname = url_path + choice;
            }
        }
    },
    disable_back_browsing: function () {
        window.history.pushState(null, null, window.location.href);
        window.onpopstate = function () {
            window.history.go(1);
        };
    },
    init: function () {
        // listen for choice button clicks
        var index = 0;
        if (this.targets.choices[0] !== null) {
            while (index < this.targets.choices.length) {
                this.targets.choices[index].onclick = this.choice_button_click;
                index += 1;
            }
        }

        // disable back browsing so the metrics don't get repeated
        this.disable_back_browsing();
    },
    targets: {
        choices: document.querySelectorAll(".choice")
    }
};

libel_main_script.init();
