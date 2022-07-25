import os
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")


os.system("git init")
os.system("git remote rm origin")
os.system("git remote add origin git@github.com:Akarsha1994/IADT_Assignment7.git")
os.system('git config --global user.email "sudheer.a@northeastern.edu"')
os.system('git config --global user.name "Akarsha1994"')
os.system("git rm -r --cached .")
os.system("git add .")
git_commit_with_time = f'git commit -m "added index.html file"'
os.system(git_commit_with_time)
os.system("git push -f --set-upstream origin main")
