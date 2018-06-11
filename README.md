Kakar Advocates - Law ERP
===

This is the official code repository for Kakar Law ERP system.

## Contributing Code
All codes written should follow [Odoo 10's code guidelines](https://www.odoo.com/documentation/10.0/reference/guidelines.html). Below are the steps push code to Kakar Law ERP's repo.

### Step 1
Code to this repository can only be pushed through **Pull Requests**. Therefore, fork this repository and create pull requests.

### Step 2
Add two remote git repositories and name them however you like. One git repo should refer to base Kakar Law ERP remote repo [https://github.com/NETLINKSAF/kakar-erp]() and another should refer to your forked repo. **Always pull from Kakar Law ERP repo and push to your own forked repo**.

### Step 3
Before doing anything with code, **pull** the **latest changes** from Kakar Law ERP's repo. Then, make changes to code and before committing do not forget to run `autopep8` in the root directory of the project.

To install `autopep8`, first make sure that you have `pip` installed on your machine, then you can the below command to install it:

```
pip install autopep8
```

Once installed, before pushing any commit to remote, run the below command from the root of project to auto fix everything according to `pep8` specifications.

```
autopep8 --in-place --ignore E501 --recursive .
```

Check if nothing is broken after your run the above command.

### Step 4
Once you commit the code, then push your changes to your forked repo.

### Step 5 - Final Step
Now create a pull request from your forked repo's specific git branch to base repo which is Kakar Law ERP's remote repo. Read this [GitHub Article](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) on how create PRs from a fork repo.

### Help on Pull Request Process
This stackoverflow answer can help with understanding PR process: https://stackoverflow.com/a/14680805/2169355
