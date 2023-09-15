# A place for Drew's notes

Commands I used to create this repo initially:

```sh
[  7:20PM ]  [ jac494@hp-laptop:~/Projects ]
 $ mkch jm_python
[  7:20PM ]  [ jac494@hp-laptop:~/Projects/jm_python ]
 $ git init
Initialized empty Git repository in /home/jac494/Projects/jm_python/.git/
[  7:20PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✔) ]
 $ touch README.md
[  7:20PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✗) ]
 $ echo "# jm_python" >> README.md
[  7:21PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✗) ]
 $ printf "\nA repo for some study code"

A repo for some study code%                                           
[  7:21PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✗) ]
 $ printf "\nA repo for some study code\n\n"

A repo for some study code

[  7:21PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✗) ]
 $ printf "\nA repo for some study code\n\n" >> README.md
[  7:21PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✗) ]
 $ touch drew_notes.md
[  7:21PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✗) ]
 $ touch first.py
[  7:21PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✗) ]
 $ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        drew_notes.md
        first.py

nothing added to commit but untracked files present (use "git add" to track)
[  7:21PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✗) ]
 $ git add .
[  7:21PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✗) ]
 $ git commit -m "created repo and initial files"
[main (root-commit) 03761f4] created repo and initial files
 3 files changed, 4 insertions(+)
 create mode 100644 README.md
 create mode 100644 drew_notes.md
 create mode 100644 first.py
[  7:22PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✔) ]
 $ history | grep "gh repo"
 1003  gh repo create --source=. --public
 1005  gh repo create --source=. --public
 2025  gh repo create --source=. --public
 2033  gh repo create --source=. --public
 2656  gh repo create --source=. --public
 2663  gh repo --help
 3501  gh repo create --source=. --public
 4001  gh repo create --source=. --public
[  7:22PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✔) ]
 $ gh repo create --source=. --public
✓ Created repository jac494/jm_python on GitHub
✓ Added remote git@github.com:jac494/jm_python.git
[  7:22PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✔) ]
 $
```
