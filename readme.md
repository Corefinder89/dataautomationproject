# Table of contents

   * [Pre-requisites](#Pre-requisites)
   * [Setup](#Setup)
   * [Installation](#Installing python modules)
   * [Execution](#Execution)
   * [Project parameters](#Configuring project parameters)
   * [Test data](#Configuring test data)


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
* Run this command from the root directory to execute the test suite
```bash
pytest
```

# Configuring project parameters
Project parameters are configured in the `config.json` file.
These parameters would be basically utilised across the project. This basically consist of
* API parameters which can be used to make a specific API request.
* Driver paths for specific browser drivers based on the platform.
* Upper bound and the lower bound values that is required to find out the variance.
* Logging configurations are done in `pytest.ini` file. Without this configuration logging will not be done in the report or in the console.
* For maintaining coding standards the `pre-commit` configurations were used. The configurations are there in the `.pre-commit-config.yaml` file. The python coding standards are maintained in the `.style.yapf` file. For more information on pre-commit follow this [doc](https://dzone.com/articles/utility-of-the-pre-commit-hook).

# Configuring test data
Test data can be configured in the `test_data.py` file. The `Testdata` class consists of the following
* The query parameters based on the parameter types that we want to pass to the API endpoint. These are basically
    * `city name`
    * `zip code`
    * `co-ordinates`
* The `city name` for which the data needs to be fetched from the web

# Reporting
The test suite is configured to support both the report libraries
* For getting reports in pytest-html run the command
```bash
pytest --html=report/<report directory>
```
There will be a html file inside the directory. Open the report to get the detailed test execution details.
* For getting reports in allure run the command
```bash
pytest --alluredir = <report directory>
allure serve <report directory>
```

# Pipeline
To configure pipeline for bitbucket have used the `bitbucket-pipelines.yml` configuration file. it consists of
   * The platform configurations.
   * Project configurations.
   * Test execution.
 The CI will trigger when pushing the code to the `develop` branch and also while merging code to the `master` branch.
