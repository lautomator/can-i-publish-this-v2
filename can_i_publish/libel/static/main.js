var libel_main_script = {
    init_question: "Q1",
    targets: {
        card_slug: document.querySelector("#card-slug"),
    },
    store_card_slug(slug) {
        var history = localStorage.getItem("card_history");
        // console.log(typeof(history), history);
        history = history + ", " + slug;
        localStorage.setItem("card_history", history);
    },
    reset: function(slug) {
        localStorage.clear();
        localStorage.setItem("card_history", slug);
    },
    init: function() {
        // setup local storage for the card history (first time only)
        if (localStorage.getItem("card_history") === null) {
            this.reset(this.init_question);
        }

        // get the current card slug
        if (this.targets.card_slug !== null) {
            // first, check for a reset: the visitor started over
            if (this.targets.card_slug.dataset.slug === this.init_question) {
                this.reset(this.init_question)
            } else {
                // add the current card slug to the history
                this.store_card_slug(this.targets.card_slug.dataset.slug);
            }
        }

        console.log(localStorage);
    }


};

// libel_main_script.init();