

module aws_wordpress {
    source              = "./modules/latest"
    database_name           = "wordpress_db"   // database name
    database_user           = "wordpress_user" // database username
    // Password here will be used to create master db user.It should be changed later
    database_password = "PassWord4-user" // password for user database
    wp_version = "latest" // WordPress version to be installed
    shared_credentials_file = "~/.aws/credentials"         // Access key and Secret key file location
    region                  = "eu-central-1" // Europe-Frankfurt region
    IsUbuntu                = true             // true for ubuntu, false for linux 2  //boolean type
    // avaibility zone and their CIDR
    AZ1          = "eu-central-1a" // for EC2
    AZ2          = "eu-central-1b" // for RDS 
    AZ3          = "eu-central-1c" // for RDS
    VPC_cidr     = "10.0.0.0/16"     // VPC CIDR
    subnet1_cidr = "10.0.1.0/24"     // Public Subnet for EC2
    subnet2_cidr = "10.0.2.0/24"     // Private Subnet for RDS
    subnet3_cidr = "10.0.3.0/24"     // Private subnet for RDS
    PUBLIC_KEY_PATH  = "./mykey-pair.pub" // Key name for ec2, make sure it is created before terrafomr apply
    PRIV_KEY_PATH    = "./mykey-pair"
    instance_type    = "t2.micro"    // Type of instance
    instance_class   = "db.t2.micro" // Type of RDS Instance
    root_volume_size = 22
}
