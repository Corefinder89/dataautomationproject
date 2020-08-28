## Pre-requisites
* `Linux` or `mac` platform
* `zsh` or `bash`.
* `python` should be installed within the system.
* Recommended python version should be greater than `2.7` as the python version `2.7` is not supported any more.
* Any one of the IDE (`vscode`, `pycharm`, `atom` or `sublime`) to visualize the code.

## Setup
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
* Run command
```bash
pip install -r requirements.txt
```
* The api key provided in the documentation is not there in the project. Python reads the apikey from the environment variable. As a standard practice no authorization token or key should be present there in the repository. The apikey has been set as an environment variable in the z-shell of my system. In order to set it up in your shell go to `.zshrc` or `.bashrc` and write
```bash
export apikey='<apikey>'
```
* Create a `report` directory inside the project directory to store all the execution reports.

## Execution
* Run this command from the root directory
```bash
pytest --html=report/report.html
```
