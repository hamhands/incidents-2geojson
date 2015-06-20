# incidents2geojson

Takes Pittsburgh crime incidents from [OpenPGH's json repo](https://github.com/openpgh/jsonIncidents2015), outputs geojson. 

### Installation
To get the json data, make sure to clone recursively by running ``` git clone --recursive ```. If you've already cloned normally, ``` git submodule init ``` should work fine as well.

### Keeping submodule up-to-date
This will probably/should be automated in the future, but for now the easiest way is to ``` git fetch ``` + ``` git pull ``` from jsonIncidents2015 subdirectory. If you notice the repo doesn't have the newest data, feel free to open a pull request.

### Requirements
Includes ipython notebook for development. Install by running from the project directory: ``` pip install requirements.txt ```
