# Technology-Usage-Mining
Antler, Maven and Gradle usage mining from GitHub public repositories

## Running the project
There is only one main.py file needed to be executed. All the ropositories are cloned to local file system. The parent folder's path which containes all the repos should be specified in the python file. Three libraries used to help the analysis. OS used to iterate over the directories, XML Element Tree helped to parse XML file and Pandas for output data representation.

The steps are as follows:
1. Download/save all the repositores to be mined under a parent folder
2. Open the main.py file in any python IDE
3. Change the 'directory' variable and assign full path of the parent directory
4. Run and view output in 'df' dataframe


## Output interpretetaion 
There are four columns in the dataframe. 
1. Repo Name: Contains the name of individual repositories
2. Maven Version: Version of Maven 
3. Antlr Dependency: It contains boolean value. 0 means antler is not used and 1 means antler is used as dependency
4. Antlr Version: Version of Antlr
