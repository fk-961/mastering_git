**This file is of markdown format or whatever**

<h1>It is dedicated to this project of getting back in the game boss</h1>
## This is coming from dev-1
//Trying stuff//

So when we create a local rep we want to link the project to the cloud so everyone can access it, to do this we have to:
- Create a new repo on the cloud (GitHub in this case)
- Link the cloud repo to the local repo by using the command:  
<code>git remote add origin repo.link</code>
Here we use the name origin to refer to the link when using our terminal
- Push any changes from a branch by using:  
<code>git push -u origin master</code>

Branching  
The typical way things happen is someone needs to develop a new feature on the new project.  
They will need to create a new branch where they will update the code and then maybe merge it to the master. They need to also connect their branch to the remote repo so people can either review their changes or start coding and branching from their created branch.  
<code>git branch branch_name source_branch</code> creates a branch `branch_name` starting from the branch `source_branch`. Usually, we dont specify the source branch since we just want to branch from where we are currently in  
<code>git checkout branch_name</code> is used to jump to another branch. If we add the option -b we simultaneously create a branch and move to it.  
<code>git push --set-upstream origin branch_name</code> syncs our branch with the remote repo. Either use this or <code>git push -u origin branch_name</code> like the above.  

When everything is set up, we can start using <code>git push</code> to directly push our changes to the remote repo and <code>git pull</code> to pull any changes made by someone (which have been pushed to the remote).