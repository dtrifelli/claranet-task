# Tasks

## Exercise 1

Write a python or bash script that takes three parameters, two strings and a directory name, and substitutes any occurrence of the first string with the second string for any file in the directory, recursively

This task is handled by the strrep.py script.
Usage: `strrep <string to replace> <replacement string> <target path>`

## Exercise 2

Write a python or bash script that counts the number of script files in a directory subdividing it by the shebang interpreter.

This task is handled by the countexec.py script.
Usage: `countexec <target path>`

## Exercise 3

Write a cron string that every sunday night create a backup of /home/user folder and send it to a remote server which can be reached using ssh with user@192.168.1.100 (consider private and public key already correctly installed and configured)

The cronjobbackup.sh file contains three different cronjobs that can be used, either using SCP or SFTP to transfer files. Two out of three versions will create an archive of the home directory before the transfer.

## Exercise 4

You have these instructions: 
- Automate the creation of the infrastructure and the setup of the application
- It's based on the last version of WordPress (it will be more useful if we can parameterize the version) 
- You can choose Apache, Nginx, or whatever you want. 
- Once deployed, the application should be:  secure , fast , fault-tolerant , adaptive to average load 
- To provision the infrastructure, choose one between CloudFormation and Terraform (CloudFormation, Terraform) 
- Optional: Create a CI/CD pipeline to deploy WordPress 
- Write a readme with an architecture diagram and all the required instructions to install and try your solution

The [terraform-ec2-RDS-wordpress-master](terraform-ec2-RDS-wordpress-master/) directory contains the project relative to this task, complete with further information.
