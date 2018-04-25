# GithubExportIssuesCSV
A Python Tool for Exporting Issues in a Github Repo to a csv

# Parameters
> usage: GithubExportCSV.exe [-h] --username GITHUBUSERNAME --password
>                           GITHUBPASSWORD --repo REPO [--filepath PATH]
> optional arguments:
>  -h, --help            show this help message and exit
>  --username GITHUBUSERNAME, -u GITHUBUSERNAME
>                        Github Username
>  --password GITHUBPASSWORD, -p GITHUBPASSWORD
>                        Github Personal Access Token. Can be created here:
>                        https://github.com/settings/tokens
>  --repo REPO, -r REPO  The Repository to connect to in the format
>                        username/repo (e.g. 9l1ves/GithubExportIssuesCSV)
>  --filepath PATH, -f PATH
>                        The path where you want the CSV file stored
                       
# Usage Build executable from Source
- pip install cx_freeze
-navigate to the directory of the files
- python setup.by build

# Usage Pre-built Exe - Windows
- Download the build folder
- Place the exe.win32-3.6 somewhere on your pc
- Open Command Prompt
- Navigate to the exe.win32-3.6 folder on the pc
- execute githubexportcsv.exe with the above mentioned parameters.
