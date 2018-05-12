<a href="https://pyup.io/repos/github/9l1ves/GithubExportIssuesCSV/"><img src="https://pyup.io/repos/github/9l1ves/GithubExportIssuesCSV/shield.svg" alt="Updates" /></a>
<a href="https://pyup.io/repos/github/9l1ves/GithubExportIssuesCSV/"><img src="https://pyup.io/repos/github/9l1ves/GithubExportIssuesCSV/python-3-shield.svg" alt="Python 3" /></a>

# GithubExportIssuesCSV
A Python Tool for Exporting Issues in a Github Repo to a csv

# Parameters
> usage: GithubExportCSV.exe [-h] --username GITHUBUSERNAME --password <br />
                          GITHUBPASSWORD --repo REPO [--filepath PATH] <br />
optional arguments: <br />
-h, --help            show this help message and exit <br />
--username GITHUBUSERNAME, -u GITHUBUSERNAME <br />
                      Github Username <br />
--password GITHUBPASSWORD, -p GITHUBPASSWORD <br />
                      Github Personal Access Token. Can be created here: <br />
                      https://github.com/settings/tokens <br />
--repo REPO, -r REPO  The Repository to connect to in the format <br />
                    username/repo (e.g. 9l1ves/GithubExportIssuesCSV) <br />
--filepath PATH, -f PATH <br />
                     The path where you want the CSV file stored <br />
                       
# Usage Build executable from Source
- pip install cx_freeze
- navigate to the directory of the files
- python setup.py build

# Usage Pre-built Exe - Windows
- Download the build folder
- Place the exe.win32-3.6 somewhere on your pc
- Open Command Prompt
- Navigate to the exe.win32-3.6 folder on the pc
- execute githubexportcsv.exe with the above mentioned parameters.
