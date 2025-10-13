Merge conflicts usually happen when 2 people are working on the same file or feature on 2 separate branches coming from the same branch.

Imagine someone is working on branch A on a specific line and pushes his changes and merges it to master.
Before the merge, someone was working on branch B on the same line and pushed his changes on github, github will detect that it can't merge branch B to master since changes to the code modified had been already merged to master by branch A.

The guy working on branch B has to now pull the changes done on master to his local repo then merge them into his branch where he would resolve the conflicts.