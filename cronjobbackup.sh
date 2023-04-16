# Three alternative cronjobs, using either SCP or SFTP to transfer files.

55 23 * * SUN scp -Cr /home/user user@192.168.1.100:/home/user/backup
55 23 * * SUN tar -czf /home/user/backup.tar.gz /home/user && scp -C /home/user/backup.tar.gz user@192.168.1.100:/home/user/backup && rm /home/user/backup.tar.gz
55 23 * * SUN tar -czf /home/user/backup.tar.gz /home/user && sftp user@192.168.1.100:/home/user/backup <<< $'put /home/user/backup.tar.gz' && rm /home/user/backup.tar.gz