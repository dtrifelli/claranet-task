# WordPress Deployement

## Architecture Diagram

![Diagram](https://i.imgur.com/WfubYay.png)
## Installation

To deploy the AWS resources and install WordPress, the steps are as follows.

### Prerequisites

- AWS CLI.
- Terraform.
- Configure AWS CLI with `aws configure`.

### Procedure

- Download this repo.
- Open a terminal and move to the root folder of this project.
- Initialize Terraform: `terraform init`.
- Edit the variables in the main.tf file as necessary.
- Generate keypair: `ssh-keygen -f mykey-pair`.
- View and check Terraform plan: `terraform plan`.
- Apply the plan: `terraform apply`.
- Once the entire process is over it is safe to destroy the Terraform resources: `terraform destroy`.

The WordPress installation process is completely automated, once it is done you will receive the application endpoint.