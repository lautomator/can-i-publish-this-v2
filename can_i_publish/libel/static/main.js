var libel_main_script = {
    targets: {
        choices: document.querySelectorAll(".choice")
    },
    button_click: function (e) {
        var choice = e.target.dataset.choice;
        var slug = e.target.dataset.slug;
        var url_path = "/libel/" + choice;

        if (choice === "None") {
            url_path = "libel/" + slug + "/summary/";
        }

        window.location.pathname = url_path;
    },
    init: function() {
        // listen for button clicks
        var index = 0;
        var len = 0;
        if (this.targets.choices.length > 0) {
            len = this.targets.choices.length;

            while (index < this.targets.choices.length) {
                this.targets.choices[index].onclick = this.button_click;
                index += 1;
            }
        }
    }
};

libel_main_script.init();
