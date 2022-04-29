# Can I Publish This?
### Web Browser Application (Django prototype version)

## Overview
Can I Publish This? is an interactive, online decision tree that will guide student journalists through self-pre publication review. This was created for the [Foundation for Individual Rights in Education](https://www.thefire.org) (FIRE).

This version of the application is a prototype. It was created using [Django](https://www.djangoproject.com/). The live version was created with a javascript backend. The live production site is here: [https://canipublishthis.com/](https://canipublishthis.com/).

## Modules

* Libel (the module used for this prototype)

* Privacy & Leaked Information

* Copyright & Trademark

* Prior Review/Prior Restraint

## Development
You will need:

* Python 3 (venv module and PIP): see `requirements.txt`

* Django

* nodejs v12.22.5

* npm v6.14.14

You can use node [NVM](https://github.com/nvm-sh/nvm#about) -- node version control -- to emulate this environment.

`libel/package.json` has all of the listed dependencies and build details. The dependencies are:

* minify

* npm-watch

* sass

### Setup/Virtual Environment
Download this repository. To get the virtual environment running, cd into `can-i-publish-this-v2` and run `python3 -m venv env`. Check the [Python docs](https://docs.python.org/3/library/venv.html) for more information about the *venv* module.

Run the virtual environment: `. env/bin/activate`.

Install the dependencies (including Django): `pip install -r requirements.txt`.

cd into `libel/` and run `npm install` to install all the of the node modules needed for development.

To run the Django server, cd back into the top directory and run `python manage.py runserver`. You can then navigate to the url displayed in the console.

### CSS and SASS
Don't edit any `.css` files. The CSS files are auto-generated when you run the build script or watch scripts. Make all edits to the SASS files in `libel/static/scss/` directory.
