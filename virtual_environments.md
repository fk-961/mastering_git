A typical workflow scenario is where a team wants to work on the same data science project and each member of the team may have different versions of desired packages used in the project on their machine.  
A good way to handle this is to have a virtual environment defined for the project (usually in a "requirements.txt" file) where people pull it from the remote repo and create the correct virtual environment on their machine depending on this file.

Usually the create environments folder is ignored by git (adding .gitigonre file with * in it) since the user will create the environment on their machine directly using the requirements.txt file.

To install a virtual environment we can use either python or conda.

In python, <code>python3 -m venv env_name</code> is used to create the environment env_name.

To activate an environment, on windows we use <code>env_name\Scripts\activate.ps1</code> for powershell (check documentation).

<code>pip list</code> shows us the installed libraries and dependencies in the current environment.

<code>pip freeze > requirements.txt</code> creates the requirements file with the needed dependencies in it.

Now when someone clones a repo on their machine, all they have to do is create a new virtual environment and then run <code>pip install -r requirements.txt</code>.

We can also specify the name of the virtual environment in the requirements file.