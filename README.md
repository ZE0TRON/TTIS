# Things That I Should (TTIS)  
A simple CLI program for increasing productivity keep a list of everything you want and marked them as done when you finished that thing.  
It's too hard to keep separate note files for things to read things to watch things to listen .... let TTIS help you with its easy to use.  


## Installing  
1)Clone the repo  
2)copy the exec file under /dist folder to /usr/bin by   ``` sudo cp dist/TTIS /usr/bin/ ```  
3)from terminal run the command ``` TTIS init ```  


## Usage  
The TTIS works with 3 simple commands:  
1)add -> adds a task to given category syntax : TTIS category_name add task_name  NOTE: for spaced task_name or category_name use "(double quotes)  
Example : TTIS "Things to do" add "Go to the bank"  
2)list -> lists all the task in the given category syntax : TTIS category_name list  
3)done -> marks a task as done and deletes it from category sytnax : TTIS category_name done task_name   
4)listcat -----lists all categories syntax:TTIS listcat  
5)delcat -----deletes the category with the given name syntax : TTIS delcat category_name  


*(Created by ZE0TRON)*
