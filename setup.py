from cx_Freeze import setup, Executable


base = None    

executables = [Executable("GithubExportCSV.py", base=base)]
packages = ['os', 'requests', 'argparse', 'csv','asyncio']
options = {
    'build_exe': {    
        'packages':packages, 'includes': ['backoff']
    },    
}

setup(
    name = "GithubExport",
    options = options,
    version = "1.0",
    description = 'Used to Export Github Repos',
    executables = executables
)
