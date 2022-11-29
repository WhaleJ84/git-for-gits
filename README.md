# Git for Gits

A project to teach the usage of Git and related technologies.

![Success Kid meme saying 'I hated Git. Now I hate it less'](https://miro.medium.com/max/640/0*Gb3B1-Xk5qHaxU7v.jpg)

## Markdown for Morons

This document is written in Markdown[^1] and named `README.md`.
Following this format will have it rendered in the repository's directory.
Most IDEs[^ide] will render the file in realtime, removing the need to push your changes to a repository to see how it looks.
If you're a :nerd_face: using a Debian based system, you can render it locally with:

```shell
# Install dependencies (only needs to be done once)
sudo apt install -y pandoc w3m w3m-img

# Render and view markdown
pandoc README.md | w3m -T text/html

# Inside Vim
:! pandoc % | w3m -T text/html -o confirm_qq=false
```

You may question why Markdown is relevant to learning Git;
It is important to document what your projects are about and how to use them.
You are not just writing documentation for others, *you are also writing it for yourself*.
There will come a time where you return to a project after a long period and have no idea where to resume without it.

## Initialising for Idiots

You may question: '*What is the difference between Microsoft file history and a VCS*[^vcs]?'.
In that regard, there is very little difference - both will allow snapshots of documents at particular points, and both will show who made the changes.
Where they differ is as such[^2]:
- + Microsoft file history only works with Windows systems | VCSs are system agnostic
- + Microsoft's implmentation has people working on the original document | VCSs uses copies of the document
- - Microsoft allows collaborating in realtime | VCS does not

There are a few different VCSs, but Git is the most popular and is what we will be using.
You can add and remove version control at any point by running `git init` inside your desired directory.
This will create a Git repository for that directory and its child directories.
Consider the following:

```
├── my_other_project
│   ├── src
│   │   └── main.py
│   └── test
└── my_project        # we are here
    ├── .git
    ├── src
    │   └── main.py
    └── test
``` 

Initialising inside `my_project` creates the hidden directory `.git` (you can see with `ls -a`).
We can only add files inside that directory like `src/main.py`, but trying to add something above the directory will fail:

```
$ git add ../my_other_project/src/main.py
fatal: ../my_other_project/src/main.py: '../my_other_project/src/main.py' is outside repository at '/tmp/test/my_project'
```

Only files that are *added* will be tracked.
Tracked items are added to what is called the **staging area**, which can be seen by running `git status`:

```
$ git init
Reinitialised existing Git repository in /tmp/my_project/.git/
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        src/                                                                   # <---- Untracked

nothing added to commit but untracked files present (use "git add" to track)
$ git add src
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   src/main.py                                                # <---- Tracked

$
```

Manually adding files allows granularity in tracking.
However, if you are sure everything in the directory can be added, then you can run `git add *`.

## Committing for Cronies

Just adding files to the staging area does nothing to 'save' their progress.
In Git, each *save* is a called a commit and requires a message to explain what the change was.
It is commonplace for a repository's first commit to be *'Initial commit'*, but subsequent should have meaningful messages.

```
$ git commit -m 'initial commit'
[main (root-commit) ba9e827] initial commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 src/main.py
$ echo "print('Hello world!')" >> src/main.py
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   src/main.py

no changes added to commit (use "git add" and/or "git commit -a")
$ git add src/main.py
$ git commit -m 'apended print statement to file'
[main 7e493bd] appended print statement to file
 1 file changed, 1 insertion(+)
$
```

Note that every time a change is made to a file, it needs to be re-added to the staging area.
It is good practice to make one commit per change.
For example, if you have to modify 20 files to change "It's coming home!" to "It's coming home next time", make the changes, add all the files, then write a meaningful commit like `git commit -m 'adjusted statement to reflect that ludicrous display last night'`.
There is no need to make 20 separate commits all saying the same thing.

You may have noticed there was a typo in the commit message.
You can edit the message with `git commit --amend`.

## Logging for Lobotomites

A good reason why you write meaningful commit messages is to provide a clear timeline what has happened.
Returning to a project after a long while can leave you wondering where you left off.
The command `git log` will show the history of all commits:

```
$ git log
commit cc754c71428cae9708c338a7ec2692e936c2df3e (HEAD -> main, origin/main)
Author: James Whale <james@james-whale.com>
Date:   Tue Nov 29 18:52:43 2022 +0000

    added committing example to readme

commit 8540bdabbfa08a76de4315a03f011dc4122639ac
Author: James Whale <james@james-whale.com>
Date:   Tue Nov 29 18:33:15 2022 +0000

    updated README

:
```

You can see that the commit message *'updated README'* is rather ambiguous and does not describe *how* it was updated.
In situations such as that, if you wish to view the change, you have to use the commit hash[^hash].
Using at least 7 characters of any hash should be unique enough to refer to that change:

```
$ git diff 8540bda
diff --git a/README.md b/README.md
index f5beb6d..11d4372 100644
--- a/README.md
+++ b/README.md
@@ -96,7 +96,60 @@ However, if you are sure everything in the directory can be added, then you can
 ## Committing for Cronies

 Just adding files to the staging area does nothing to 'save' their progress.
-In Git, each *save* is a called a commit.
+In Git, each *save* is a called a commit and requires a message to explain what the change was.
+It is commonplace for a repository's first commit to be *'Initial commit'*, but subsequent should have meaningful messages.
:
```

Each commit will note who made what changes when.
While working in teams, this can be important for accounting purposes.

## Pushing for Pillocks

Until now, everything has been done on your local machines.
If you were to lose your machine, the work would be lost.
Git allows *pushing* to a *remote* repository using `git push`:

```
$ git push
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>

$
```

The error points out there is no remote configured; so what is a remote?
You may have heard of [GitHub](https://github.com/), [GitLab](https://gitlab.com/), [Gitea](https://gitea.com), and others.
Each require an account to begin creating repositories (GitHub is the most popular so it's best to go with that).
The repository will provide you with the commands required to begin pushing to it, but lets break it down:

- `git remote add *<name>* <url>`
By default, the name provided to you will be **origin** which is standard, but the name *origin* is meaningless.
You could change the name to reflect your actual remote (e.g. *github*), or anything like 'whaaaah' to inform developers the correct way to cry when they break things - it does not matter.

- `git remote add <name> *<url>*`
The URL will typically follow the following format: '<method><service>:<username>/<repository>.git'.
For example, my repo on GitHub would be 'git@github.com:WhaleJ84/git-for-gits.git'.
The caveat would be whether you use SSH or HTTPS as the connection method;
SSH is 'git@' and HTTPS is 'https://'.
Regardless, the repository will provide you the correct commands and you can then push your work:

```
$ git push -u gitea main
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (8/8), 833 bytes | 833.00 KiB/s, done.
Total 8 (delta 1), reused 0 (delta 0), pack-reused 0
remote: . Processing 1 references
remote: Processed 1 references in total
To git.james-whale.com:james/test.git
 * [new branch]      main -> main
branch 'main' set up to track 'gitea/main'.
$
```

There is no requirement to push after every commit or at any interval at all.
Keep in mind that if your repository is public, then what you push can be seen by everyone, so push whwhen you are happy with that work.

## Branching for Baboons

Git utilises *branches* to allow for easier development and cooperation.
By default, the '*main*' branch is created, but similar to remote names, it is entirely meaningless.
Conceptually, the main branch is supposed to always house working code that anyone can use without issue.
While making changes to files, it is best to create a new branch for that specifc task.

```
$ git branch WhaleJ84/proof-reading
$ git branch
* main
  WhaleJ84/proof-reading
$ git checkout WhaleJ84/proof-reading
Switched to branch 'WhaleJ84/proof-reading'
$ git branch
  main
* WhaleJ84/proof-reading
$
```

Note that when creating the branch, I prefixed the task with my username `WhaleJ84/proof-reading`.
This means if myself and another both work on the *proof-reading* task, then the task of merging in changes later will be made easier.

Any changes made in this branch will not affect any other branch.
This allows for experimentation of different features while always ensuring the *main* branch is working.
The branch will also remain local only until it is pushed to the remote `git push -u WhaleJ84/proof-reading` (the `-u` part onward is only needed the first push).

[^1]: [This guide](https://www.markdownguide.org/basic-syntax) provides a handy link to learning the syntax.
[^2]: I don't use Windows. Do not sue me if this is not all 100% correct.
[^ide]: Integrated Development Environment
	: Software for building applications that combines common developer tools into a single graphical user interface.
[^vcs]: Version Control System
	: A system that records changes to a file or set of files over time so that you can recall specific versions later.
[^hash]: Hash
	: A fixed-length, unpredictable, and irreversible representation of a given input,

