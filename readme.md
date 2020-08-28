Table of contents
=================

<!--ts-->
   * [Pre-requisites](#Pre-requisites)
   * [Setup](#Setup)
   * [Installation](#Installing python modules)
   * [Execution](#Execution)
   * [Project parameters](#Configuring project parameters)
   * [Test data](#Configuring test data)
<!--te-->

# Pre-requisites
* `Linux` or `mac` platform.
* `zsh` or `bash`.
* `python` should be installed within the system.
* Recommended python version should be greater than `2.7` as the python version `2.7` is not supported any more.
* Any one of the IDE (`vscode`, `pycharm`, `atom` or `sublime`) to visualize the code.
* Chrome version should be `85` as the browser driver uses the latest chrome version.

# Setup
* `Homebrew` should be installed within your system. If homebrew is not installed use this documentation to install [Homebrew](https://brew.sh/).
* If python version is `2.7` then you can use this command to install python version above 2.7 using
```bash
brew install python3
```
* Install virtualenv in your system at first using
```bash
pip3 install virtualenv
```
* Clone the project from bitbucket.
* Navigate to the project directory.
* Run command
```bash
python3 -m virtualenv venv
```
* Then activate virtual environment using
```bash
source venv/bin/activate
```

* The api key provided in the documentation is not there in the project. Python reads the apikey from the environment variable. As a standard practice no authorization token or key should be present there in the repository. The apikey has been set as an environment variable in the z-shell of my system. In order to set it up in your shell go to `.zshrc` or `.bashrc` and write
```bash
export apikey='<apikey>'
```
* Create a `report` directory inside the project directory to store all the execution reports.

# Installing python modules
* Use pip to install python modules
```bash
pip install -r requirements.txt
```

# Execution
* Run this command from the root directory
```bash
pytest --html=report/report.html
```

# Configuring project parameters
Project parameters are configured in the `config.json` file. These parameters would be basically utilised across the project. This basically consist of
* API parameters which can be used to make a specific API request.
* Driver paths for specific browser drivers based on the platform.
* Upper bound and the lower bound values that is required to find out the variance

# Configuring test data
Test data can be configured in the `test_data.py` file. The `Testdata` class consists of the following
* The query parameters based on the parameter types that we want to pass to the API endpoint. These are basically
    * `city name`
    * `zip code`
    * `co-ordinates`
* The `city name` for which the data needs to be fetched from the web
