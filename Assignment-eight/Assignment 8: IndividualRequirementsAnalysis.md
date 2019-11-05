# Assignment 8: Individual Requirements Analysis for Semester Project<br><br>Guangzu Li <br><br> 14247798

## Introduction

Our group is a mixed team, we should focus on Front-end, Api and ,and Back-end. However, there are enough data to use in our project. Thus, we choose to use origin Api from Augur system. We should use end point from Augur system, we will displaying, analyzing data. We should use mitipule developjment tool to build our webiste that allows people check the data from augur. Thus, our goal is to make the data from augur to be readable, clear ,and accuracy.

## System use

We should build a project which can get and display the data from augur endpoints. Also, change the view which can make user see the data clearly. It will help the augur data base to fix problem and help user to find the data which they want by a search function.

## System Requirements 

### use cases
####  Use case 1:

diagram link:https://github.com/Natsukie/glgw7/blob/master/Assignment-eight/UseCaseImage/use%20case%201.jpg

Title: Repo and Repo Group display pages

Description: It is two pages basic on data, you can choose to go to repo/repo-group. If go to repo-group pages, you can search the repo by repo group. If you go to repo pages, it will show all the repo.

Actor: User and the administrators from augur data system

Goals: Main goal is the user can see repo pages is to display repo and can use repo group pages to search the repo detail follow by repo groups.

Fail: No result if there no response from Augur end point.

Steps for execution:

 First case:
 
	- 1. go to repo pages
	- 2. loading repo data from Augur
	- 3. display repo data
Second case:
	- 1. go to repo group pages
	- 2. loading repo group pages from Augur
	- 3. display repo group data
	- 4. choose repo group to search repo data
	- 5. loading specific repo data from Augur
	- 6. display specific repo data


####  Use case 2:

diagram link:https://github.com/Natsukie/glgw7/blob/master/Assignment-eight/UseCaseImage/use%20case%202.jpg

Title: Top commit, pull request, and contributor detail display pages

Description: We can get the detail from Augur end point such as top commit, pull request, and contributor.

Actor: User and the administrators from augur data system

Goals: Main goal is the user can get the specific detail from augur end point

Fail: No result if there no response from Augur end point.

Steps for execution:
	- 1. go to repo pages
	- 2. loading repo data from Augur end point
	- 3. Search data top commit pull request, or contributor by repo info
	- 4. loading specific info from Augur data
	- 5. display the specific info in pages

### Functional specification
  - System can check data from augur endpoint
  - System can display the data from augur
  - System can check data which user want from augur database
  - System can should the data using graph
  - System can tell user "no Result" from augur basic on his sereach detail
  - System can have mutiple pages to show the data
  - System can see by user on the internet
  
### Non-functional requirements
  - We will have a clear UI design can make user understand the data which they sereach)
  - Design baicly use in website browsers.
  - Make sure the web's safety
  - Data is display by graph (follow the time， people , and order）
  - Help page to show the description of webpage features

## Design Constraints 
  
  - Web UI Desigin
    - use Augular frameworks
    - HTML, CSS, Javascript
  - Back-end
    - use Augular HTTPClient
  - Use Augur Api end ponint (relevant data)
  - Use github pages sever display the project
  - Sereach time depend on reflection from Augur end point.
  
## Purchased Components
  
  - Website free resources
		- Augur (Web frame works, httpclient, github,io)
	- Amazon AWS

## Interfaces

  -	The web application interface will be created by HTML, CSS and Javascript. It will be post to a server and accessed by any user on the internet.
