# A place for Drew's notes

Commands I used to create this repo initially:

```sh
mkch jm_python
git init
touch README.md
echo "# jm_python" >> README.md
printf "\nA repo for some study code\n\n" >> README.md
touch drew_notes.md
touch first.py
git status
git add .
git commit -m "created repo and initial files"
gh repo create --source=. --public
```

And the full session with output:

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

Testing the examples in `first.py` with doctest in Python repl:

```sh
[  7:47PM ]  [ jac494@hp-laptop:~/Projects/jm_python(main✗) ]
 $ python3
Python 3.11.4 (main, Jun  7 2023, 00:00:00) [GCC 12.3.1 20230508 (Red Hat 12.3.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import doctest
>>> import first
>>> doctest.testmod(first)
**********************************************************************
File "/home/jac494/Projects/jm_python/first.py", line 21, in first.ip_to_site
Failed example:
    ip_to_site("11.12.34.0")
Expected:
    '1234'
Got nothing
**********************************************************************
File "/home/jac494/Projects/jm_python/first.py", line 3, in first.site_to_ip
Failed example:
    site_to_ip("1234")
Expected:
    '11.12.34.0'
Got:
    '11...0'
**********************************************************************
2 items had failures:
   1 of   1 in first.ip_to_site
   1 of   1 in first.site_to_ip
***Test Failed*** 2 failures.
TestResults(failed=2, attempted=2)
>>>
```

After this you'll want to delete the generated `__pycache__` directory:

```sh
rm -rf __pycache__
```

**OR** I just learned that it is possible to tell Python not to generate it in the first place with:

```sh
export PYTHONDONTWRITEBYTECODE=1
```
