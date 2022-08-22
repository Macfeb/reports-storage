from git import Repo

import os                       #For getting script's path

scriptPath = os.path.dirname(os.path.abspath(__file__))
commitMessage = "Auto commit via script"
os.environ['GIT_USERNAME'] = "pawey"
os.environ['GIT_PASSWORD'] = "lalala"

def git_push():
    try:
        repo = Repo(scriptPath)
        repo.git.add(update=True)
        repo.index.commit(commitMessage)
        origin = repo.remote(name='origin')
        print("DEbug")
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()
