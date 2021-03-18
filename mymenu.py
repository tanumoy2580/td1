import os
import subprocess as sr
import getpass
import socket
while True:
    psswd=getpass.getpass("Enter password to proceed :  ")
    if psswd == "tt":
        break
    else:
        print('\t > Please Enter Correct Password\n')

os.system('clear')
print('\n\n\t\t\t\t\t',end='')
os.system('tput setaf 3')
print('''Automated Program for RHEL8
*************************************************************************************************''')
    
os.system('tput setaf 2')
print('''\n\nWhich system you want to operate :-
\t\t1. Remote System
\t\t2. Local System
\n\t [[  Type '3' To Exit  ]]''')
sys=input('\n\tEnter your option :  ')


#Exit
if sys=='3':
    os.system('clear')
    exit()


#Local System
elif sys=='2':
    while True:
        os.system('clear')
        os.system('tput setaf 7')
        print('''
    \t\t 1. Show Current Date
    \t\t 2. Show Current Time
    \t\t 3. Show My Private IP
    \t\t 4. Configure Web Server
    \t\t 5. Configure HDFS Cluster
    \t\t 6. Configure AWS
    \t\t 7. Configure Docker
    \t\t 8. Configure LVM
    \t\t 9. Ping a Server
    \t\t10. Exit''')
        a=input('Enter your choice : ')
        if a=='1':
            op=sr.getstatusoutput("date +%d/%m/%Y")
            print("\n\t\tToday's date is  >>  {}\n".format(op[1]))
            input('\nPress enter key to continue...')
        elif a=='2':
            op=sr.getstatusoutput('date +%I:%M:%S')
            print("\n\t\tCurrent Time Is  >>  {}\n".format(op[1]))
            input('\nPress enter key to continue...')
        elif a=='3':
            print('\t\t>> Please Wait...\n')
            hn=socket.gethostname()
            ip=socket.gethostbyname(hn)
            print("Your Private IP Is  >>  {}".format(ip))
            input('\nPress enter key to continue...')
        elif a=='4':
            print('\n\t\t >>Please wait...')
            op=sr.getstatusoutput('dnf install -y httpd')
            if op[0]==0:
                print('\t\t>>  HTTPD Installed  <<')
            op=sr.getstatusoutput('systemctl start httpd')
            if op[0]==0:
                print('\t\t>>  Service Started  <<')
            obj=open('/var/www/html/default.html','w+')
            txt='Hi, this is a pre-created webpage'
            obj.writelines(txt)
            obj.close()
            print("\t\t>>  An html Page In The Name of 'default.html' Is Created \n\t\tIn The Root Directory of The Web Server <<")
            print('\t\t>>  Web Server Configured  <<')
            input('\nPress enter key to continue...')
        elif a=='5':
            print('''\t\tWhat Do You Want To Configure?
            \t\t  1. NameNode
            \t\t  2. DataNode
            \t\t  3. Client''')
            ch=input('\t\tEnter Your Selection :  ')
            if ch=='1':
                loc=input('Enter The Directory :  ')
                port=input('Enter The Port No. :  ')
                print('\n\t\t>> Please Wait...')
                op=sr.getstatusoutput('rpm -i jdk-8u171-linux-x64.rpm --force')
                if op[0]==0:
                    print('\n\t\t>>  JDK Installed  <<')
                op=sr.getstatusoutput('rpm -i hadoop-1.2.1-1.x86_64.rpm --force')
                if op[0]==0:
                    print('\n\t\t>>  Hadoop Installed  <<')
                obj=open('/etc/hadoop/hdfs-site.xml','w+')
                hn=socket.gethostname()
                ip=socket.gethostbyname(hn)
                txt='<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>{}</value>\n</property>\n</configuration>'.format(loc)
                obj.writelines(txt)
                obj.close()
                obj=open('/etc/hadoop/core-site.xml','w+')
                txt='<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:{1}</value>\n</property>\n</configuration>'.format(ip,port)
                obj.writelines(txt)
                obj.close()
                os.system('rm -rf {}'.format(loc))
                os.system('mkdir {}'.format(loc))
                print('\n\t\t>>  Formatting NameNode Directory  <<')
                op=sr.getstatusoutput('hadoop namenode -format <<< Y')
                os.system('systemctl stop firewalld')
                os.system('setenforce 0')
                op=sr.getstatusoutput('hadoop-daemon.sh start namenode')
                print('\n\t\t>>  NameNode Configured AND Started  <<')
                input('\nPress enter key to continue...')
            elif ch=='2':
                ip=input('Enter IP of NameNode :  ')
                loc=input('Enter The Directory :  ')
                port=input('Enter The Port No. :  ')
                print('\n\t\t>> Please Wait...')
                op=sr.getstatusoutput('rpm -i jdk-8u171-linux-x64.rpm --force')
                if op[0]==0:
                    print('\n\t\t>>  JDK Installed  <<')
                op=sr.getstatusoutput('rpm -i hadoop-1.2.1-1.x86_64.rpm --force')
                if op[0]==0:
                    print('\n\t\t>>  Hadoop Installed  <<')
                obj=open('/etc/hadoop/hdfs-site.xml','w+')
                txt='<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>{}</value>\n</property>\n</configuration>'.format(loc)
                obj.writelines(txt)
                obj.close()
                obj=open('/etc/hadoop/core-site.xml','w+')
                txt='<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:{1}</value>\n</property>\n</configuration>'.format(ip,port)
                obj.writelines(txt)
                obj.close()
                os.system('rm -rf {}'.format(loc))
                os.system('mkdir {}'.format(loc))
                os.system('systemctl stop firewalld')
                os.system('setenforce 0')
                op=sr.getstatusoutput('hadoop-daemon.sh start datanode')
                print('\n\t\t>>  DataNode Configured AND Started  <<')
                input('\nPress enter key to continue...')
            elif ch=='3':
                ip=input('Enter IP of NameNode :  ')
                port=input('Enter The Port No. :  ')
                print('\n\t\t>> Please Wait...')
                op=sr.getstatusoutput('rpm -i jdk-8u171-linux-x64.rpm --force')
                if op[0]==0:
                    print('\n\t\t>>  JDK Installed  <<')
                op=sr.getstatusoutput('rpm -i hadoop-1.2.1-1.x86_64.rpm --force')
                if op[0]==0:
                    print('\n\t\t>>  Hadoop Installed  <<')
                obj=open('/etc/hadoop/core-site.xml','w+')
                txt='<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:{1}</value>\n</property>\n</configuration>'.format(ip,port)
                obj.writelines(txt)
                obj.close()
                obj=open('/etc/hadoop/hdfs-site.xml','w+')
                txt='<configuration>\n</configuration>'
                obj.writelines(txt)
                obj.close()
                os.system('systemctl stop firewalld')
                os.system('setenforce 0')
                print('\n\t\t>>  Client Configured  <<')
                input('\nPress enter key to continue...')
        elif a=='6':
            def aws():
                import os
                os.system("clear")
                os.system("tput setaf 1")
                os.system("tput bold")
                os.system("tput smul")
                print("\t\t\t\tCONTROL AWS AT YOUR FINGER TIPS")
                os.system("tput rmul")
                os.system("sleep 1")
                os.system("tput setaf 7")
                print("please enter your AWS credentials below")
                print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
                os.system("sleep 1")
                os.system("tput rmul")
                os.system("aws configure")
                print("select the service of aws on which you would like to perform operations")
                os.system("sleep 1")
                print("""
                        1.EC2(elastic compute cloud)
                        2.S3(simple storage service)
                        """)
                service=int(input("enter your choice: "))
                if service==1:
                    while True:
                        os.system("clear")
                        print("select the sub-service of EC2")
                        print("""
                        1.create key-pair
                        2.create security group
                        3.add ingress rules to security group
                        4.create EBS volume
                        5.attach volume to instance
                        6.launch instance
                        7.exit
                            """)
                        ec2=int(input("enter your choice: "))
                        if ec2==1:
                            key_name=input("enter the name you want to give to your key: ")
                            os.system("aws ec2 create-key-pair --key-name {0} > {0}.pem".format(key_name))
                            print("the key is saved as {}.pem".format(key_name))
                        elif ec2==2:
                            sg_name=input("enter the name you want to give to your security group: ")
                            os.system(""" aws ec2 create-security-group --group-name {} --description "security group" """.format(sg_name))
                        elif ec2==3:
                            print("Rules created can be accessed from all the IP's")
                            sg_port=int(input("enter ingress port number: "))
                            sg_protocol=input("enter protocol: ")
                            sg_groupid=input("enter group-id: ")
                            os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr 0.0.0.0/0".format(sg_groupid,sg_protocol,sg_port))
                        elif ec2==4:
                            ebs_region=input("enter the region to create EBS: ")
                            ebs_size=int(input("enter the size for EBS volume in GB: "))
                            os.system("aws ec2 create-volume --volume-type gp2 --size {} --availability-zone {}".format(ebs_size,ebs_region))
                        elif ec2==5:
                            vol_id=input("enter volume id: ")
                            inst_id=input("enter instance id: ")
                            dev=input("enter device name: ")
                            os.system ("aws ec2  attach-volume   --volume-id {}  --instance-id {} --device {}".format(vol_id,inst_id,dev))
                        elif ec2==6:
                            inst_sg_id=input("enter security group id: ")
                            inst_type=input("enter instance type: ")
                            inst_ami_id=input("enter AMI id: ")
                            inst_key=input("enter key name: ")
                            os.system("aws ec2 run-instances   --security-group-ids {}  --instance-type {}  --image-id {}   --key-name {} ".format(inst_sg_id,inst_type,inst_ami_id,inst_key))
                        elif ec2==7:
                            exit()
                        else:
                            print("option not supported")
                        input("enter any key to continue....")
                if service==2:
                    while True:
                        os.system("clear")
                        print("select sub-service of S3")
                        print("""
                                1.create a bucket
                                2.add object to bucket
                                3.exit
                                """)
                        s3=int(input("enter your choice: "))
                        if s3==1:
                            s3_name=input("enter the name you want to give to the S3 bucket: ")
                            s3_region=input("enter the region to create S3 bucket: ")
                            os.system("aws s3api create-bucket --bucket {0} --region {1} --acl public-read --create-bucket-configuration LocationConstraint={1}".format(s3_name,s3_region))
                        elif s3==2:
                            s3_local_path=input("enter your local path for file: ")
                            s3_bucket_name=input("enter the name of bucket to upload: ")
                            os.system("""aws s3 cp {} s3://{} --acl public-read""".format(s3_local_path,s3_bucket_name))
                        elif s3==3:
                            exit()
                        else:
                            print("option not supported")
                        input("enter any key to continue....")
            aws()
        elif a=='7':
            import os
            import subprocess as sr
            import socket
            while True: 
                os.system('clear')
                print("\n\n\t 1. To install docker\n\t 2. To start docker services\n\t 3. O.S to install\n\t 4. Exit")
                a= input("Enter your choice ")
                if a=='1':
                    op=sr.getstatusoutput('dnf install docker-ce --nobest')
                    if op[0]==0:
                        print("Docker installed successfully")
                    input("Press enter button to continue...")
                elif a=='2':
                    print("Start docker permanently")
                    x=input("yes/no\n")
                    if x=='yes':
                        op=sr.getstatusoutput('systemctl start docker')
                        op=sr.getstatusoutput('systemctl enable docker')
                    else:
                        op=sr.getstatusoutput('systemctl start docker')
                elif a=='3':
                    print('''\nSelect O.S to install and run
                    \n\t\t1. Ubuntu
                    \n\t\t2. Centos
                    \n\t\t3. Amazonlinux''')
                    ch=input("Enter your choice\n")
                    if ch=='1':
                        ver=input("Enter version of O.S : ")
                        print('\n\t\tPlease wait...')
                        op=sr.getstatusoutput('docker pull ubuntu:{}'.format(ver))
                        os.system ('clear')
                        os.system('docker run -it ubuntu:{}'.format(ver))
                    elif ch=='2':
                        ver=input("Enter version of O.S : ")
                        print('\n\t\tPlease wait...')
                        op=sr.getstatusoutput('docker pull centos:{}'.format(ver))
                        os.system('clear')
                        os.system('docker run -it centos:{}'.format(ver))
                    elif ch=='3':
                        ver=input("Enter version of O.S : ")
                        print('\n\t\tPlease wait...')
                        op=sr.getstatusoutput('docker pull amazonlinux:{}'.format(ver))
                        os.system('clear')
                        os.system('docker run -it amazonlinux:{}'.format(ver))
                elif a=='4':
                    os.system('clear')
                    exit()
        elif a=='8':
            import os 
            print("\t\t\tWelcome To Menu !!")
            print("\t\t--------------------------------")

        #local system 

            while True:
                print("""
             \n
             press 1 : to display the hardisk 
             press 2 : to creating physical volume
             press 3 : to create volume group
             press 4 : to create a logical volume 
             press 5 : to format the partion 
             press 6 : to mount the partion 
             press 7 : to display all mounted partition
             press 8 : to extend the size of partition and resize the partition
             press 9 : to exit
             """)
                a=input("enter your choice :")
                if a=="1":
                    os.system("fdisk -l")
                elif a=="2":
                    ch = input("enter the name of hard disk :")
                    print()
                    os.system("pvcreate /dev/{}".format(ch))
                    os.system("pvdisplay /dev/{}".format(ch))
                elif a=="3":
                    ch = input("enter the name of hard disk :")
                    ch1=input("enter the name of volume group :")
                    print()
                    os.system("vgcreate {} /dev/{}".format(ch1,ch))
                    os.system("vgdisplay {}".format(ch1))
                elif a=="4":
                    ch1=input("enter the name of volume group :")
                    ch2 = input("enter the size of logical volume informat of G and M :")
                    ch3 = input("enter the name of logical volume :")
                    print()
                    os.system("lvcreate --size {} --name {} {}".format(ch2,ch3,ch1))
                    os.system("lvdisplay {}/{}".format(ch1,ch3))
                    print("\tnow the partition is created")

                elif a=="5":
                    ch1=input("enter the name of volume group :")
                    ch3 = input("enter the name of logical volume :")
                    ch4 = input("enter the type of format :")
                    os.system("mkfs.{} /dev/{}/{}".format(ch4,ch1,ch3))
                    print()
                    print("\tnow the partition is formatted") 
                elif a=="6":
                    ch1=input("enter the name of volume group :")
                    ch3 = input("enter the name of logical volume :")
                    ch5 = input("enter the name of directory/folder which you want to mount :")
                    os.system("mkdir /{}".format(ch5))
                    os.system("mount /dev/{}/{}  /{}".format(ch1,ch3,ch5))
                    print()
                    print("\tnow the partition is mounted")
                elif a=="7":
                    os.system("df -h")
                elif a=="8":
                    ch1=input("enter the name of volume group :")
                    ch3 = input("enter the name of logical volume :")
                    ch6=input("emter the size which you want to extend :")
                    os.system("lvextend --size +{} /dev/{}/{}".format(ch6,ch1,ch3))
                    os.system("resize2fs /dev/{}/{}".format(ch1,ch3))
                elif a=="9":
                    exit()
        elif a=='9':
            dns=input('\n\t\t >>  IP OR Domain Name Of The Server :  ')
            os.system('ping -c 4 {}'.format(dns))
            input('\nPress enter key to continue...')
        elif a=='10':
            os.system('clear')
            exit()


#Remote System
elif sys=='1':
    os.system('clear')
    rip=input('\n\t\t >>  Enter IP Of The  Remote System :  ')
    print('\n\t\t >>  Creating and Copying Public/Private Key-Pair')
    print('\n\t\tType Password Of The Remote System Below(If Prompted) :-\n\n')
    os.system('ssh-copy-id root@{}'.format(rip))
    while True:
        os.system('clear')
        os.system('tput setaf 7')
        print('''
    \t\t 1. Show Current Date
    \t\t 2. Show Current Time
    \t\t 3. Show My Private IP
    \t\t 4. Configure Web Server
    \t\t 5. Configure HDFS Cluster
    \t\t 6. Configure LVM
    \t\t 7. Ping a Server
    \t\t 8. Exit''')
        a=input('Enter your choice : ')
        if a=='1':
            op=sr.getstatusoutput("ssh {} date +%d/%m/%Y".format(rip))
            os.system('tput setaf 7')
            print("\n\t\tToday's date is  >>  {}\n".format(op[1]))
            input('\nPress enter key to continue...')
        elif a=='2':
            op=sr.getstatusoutput('ssh {} date +%I:%M:%S'.format(rip))
            os.system('tput setaf 7')
            print("\n\t\tCurrent Time Is  >>  {}\n".format(op[1]))
            input('\nPress enter key to continue...')
        elif a=='3':
            print('\t\t>> Please Wait...\n')
            print("Your Private IP Is  >>  {}".format(rip))
            input('\nPress enter key to continue...')
        elif a=='4':
            print('\n\t\t >>Please wait...')
            op=sr.getstatusoutput('ssh root@{} dnf install httpd'.format(rip))
            if op[0]==0:
                print('\n\t\t>>  HTTPD Installed  <<')
            op=sr.getstatusoutput('ssh root@{} systemctl start httpd'.format(rip))
            if op[0]==0:
                print('\n\t\t>>  Service Started  <<')
            obj=open('/root/test@2580.html','w+')
            txt='Hi, this is a pre-created webpage'
            obj.writelines(txt)
            obj.close()
            op=sr.getstatusoutput('scp /root/test@2580.html root@{}:/var/www/html/default.html'.format(rip))
            os.system('rm -f /root/test@2580.html')
            print("\n\t\t>>  An html Page In The Name of 'default.html' Is Created \n\t\tIn The Root Directory of The Web Server <<")
            print('\n\t\t>>  Web Server Configured  <<')
            input('\nPress enter key to continue...')
        elif a=='5':
            print('''\t\tWhat Do You Want To Configure?
            \t\t  1. NameNode
            \t\t  2. DataNode
            \t\t  3. Client''')
            ch=input('\t\tEnter Your Selection :  ')
            if ch=='1':
                loc=input('Enter The Directory :  ')
                port=input('Enter The Port No. :  ')
                print('\n\t\t>> Please Wait...')
                op=sr.getstatusoutput('ssh root@{} rpm -i jdk-8u171-linux-x64.rpm --force'.format(rip))
                if op[0]==0:
                    print('\n\t\t>>  JDK Installed  <<')
                op=sr.getstatusoutput('ssh root@{} rpm -i hadoop-1.2.1-1.x86_64.rpm --force'.format(rip))
                if op[0]==0:
                    print('\n\t\t>>  Hadoop Installed  <<')
                obj=open('/root/test@2580.xml','w+')
                txt='<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>{}</value>\n</property>\n</configuration>'.format(loc)
                obj.writelines(txt)
                obj.close()
                op=sr.getstatusoutput('scp /root/test@2580.xml root@{}:/etc/hadoop/hdfs-site.xml'.format(rip))
                op=sr.getstatusoutput('rm -f test@2580.xml')
                obj=open('/root/test@2580.xml','w+')
                txt='<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:{1}</value>\n</property>\n</configuration>'.format(rip,port)
                obj.writelines(txt)
                obj.close()
                op=sr.getstatusoutput('scp /root/test@2580.xml root@{}:/etc/hadoop/core-site.xml'.format(rip))
                os.system('rm -f test@2580.xml')
                os.system('ssh root@{} rm -rf {}'.format(rip,loc))
                os.system('ssh root@{} mkdir {}'.format(rip,loc))
                print('\n\t\t>>  Formatting NameNode Directory  <<')
                op=sr.getstatusoutput('ssh root@{} hadoop namenode -format <<< Y'.format(rip))
                os.system('ssh root@{} systemctl stop firewalld'.format(rip))
                os.system('ssh root@{} setenforce 0'.format(rip))
                op=sr.getstatusoutput('ssh root@{} hadoop-daemon.sh start namenode'.format(rip))
                print('\n\t\t>>  NameNode Configured AND Started  <<')
                input('\nPress enter key to continue...')

            elif ch=='2':
                ip=input('Enter IP of NameNode :  ')
                loc=input('Enter The Directory :  ')
                port=input('Enter The Port No. :  ')
                print('\n\t\t>> Please Wait...')
                op=sr.getstatusoutput('ssh root@{} rpm -i jdk-8u171-linux-x64.rpm --force'.format(rip))
                if op[0]==0:
                    print('\n\t\t>>  JDK Installed  <<')
                op=sr.getstatusoutput('ssh root@{} rpm -i hadoop-1.2.1-1.x86_64.rpm --force'.format(rip))
                if op[0]==0:
                    print('\n\t\t>>  Hadoop Installed  <<')
                obj=open('/root/test@2580.xml','w+')
                txt='<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>{}</value>\n</property>\n</configuration>'.format(loc)
                obj.writelines(txt)
                obj.close()
                op=sr.getstatusoutput('scp /root/test@2580.xml root@{}:/etc/hadoop/hdfs-site.xml'.format(rip))
                op=sr.getstatusoutput('rm -f test@2580.xml')
                obj=open('/root/test@2580.xml','w+')
                txt='<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:{1}</value>\n</property>\n</configuration>'.format(ip,port)
                obj.writelines(txt)
                obj.close()
                op=sr.getstatusoutput('scp /root/test@2580.xml root@{}:/etc/hadoop/core-site.xml'.format(rip))
                os.system('rm -f test@2580.xml')
                os.system('ssh root@{} rm -rf {}'.format(rip,loc))
                os.system('ssh root@{} mkdir {}'.format(rip,loc))
                os.system('ssh root@{} systemctl stop firewalld'.format(rip))
                os.system('ssh root@{} setenforce 0'.format(rip))
                op=sr.getstatusoutput('ssh root@{} hadoop-daemon.sh start datanode'.format(rip))
                print('\n\t\t>>  DataNode Configured AND Started  <<')
                input('\nPress enter key to continue...')

            elif ch=='3':
                ip=input('Enter IP of NameNode :  ')
                port=input('Enter The Port No. :  ')
                print('\n\t\t>> Please Wait...')
                op=sr.getstatusoutput('ssh root@{} rpm -i jdk-8u171-linux-x64.rpm --force'.format(rip))
                if op[0]==0:
                    print('\n\t\t>>  JDK Installed  <<')
                op=sr.getstatusoutput('ssh root@{} rpm -i hadoop-1.2.1-1.x86_64.rpm --force'.format(rip))
                if op[0]==0:
                    print('\n\t\t>>  Hadoop Installed  <<')
                obj=open('/root/test@2580.xml','w+')
                txt='<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:{1}</value>\n</property>\n</configuration>'.format(ip,port)
                obj.writelines(txt)
                obj.close()
                op=sr.getstatusoutput('scp /root/test@2580.xml root@{}:/etc/hadoop/core-site.xml'.format(rip))
                obj=open('/root/test@2580.xml','w+')
                txt='<configuration>\n</configuration>'
                obj.writelines(txt)
                obj.close()
                op=sr.getstatusoutput('scp /root/test@2580.xml root@{}:/etc/hadoop/hdfs-site.xml'.format(rip))
                os.system('rm -f test@2580.xml')
                os.system('ssh root@{} systemctl stop firewalld'.format(rip))
                os.system('ssh root@{} setenforce 0'.format(rip))
                print('\n\t\t>>  Client Configured  <<')
                input('\nPress enter key to continue...')
        elif a=='6':

            #remote system
            while True:
                print("""
                \n
                press 1 : to display the hardisk 
                press 2 : to creating physical volume
                press 3 : to create volume group
                press 4 : to create a logical volume 
                press 5 : to format the partion 
                press 6 : to mount the partion 
                press 7 : to display all mounted partition
                press 8 : to extend the size of partition and resize the partition
                press 9 : to exit
                """)
                a=input("enter your choice :")
                if a=="1":
                    os.system("ssh {} fdisk -l".format(ip))
                elif a=="2":
                    ch = input("enter the name of hard disk :")
                    print()
                    os.system("ssh {} pvcreate /dev/{}".format(ip,ch))
                    os.system("ssh {} pvdisplay /dev/{}".format(ip,ch))
                elif a=="3":
                    ch = input("enter the name of hard disk :")
                    ch1=input("enter the name of volume group :")
                    print()
                    os.system("ssh {} vgcreate {} /dev/{}".format(ip,ch1,ch))
                    os.system("ssh {} vgdisplay {}".format(ip,ch1))
                elif a=="4":
                    ch1=input("enter the name of volume group :")
                    ch2 = input("enter the size of logical volume informat of G and M :")
                    ch3 = input("enter the name of logical volume :")
                    print()
                    os.system("ssh {} lvcreate --size {} --name {} {}".format(ip,ch2,ch3,ch1))
                    os.system("ssh {} lvdisplay {}/{}".format(ip,ch1,ch3))
                    print("\tnow the partition is created")
                elif a=="5":
                    ch1=input("enter the name of volume group :")
                    ch3 = input("enter the name of logical volume :")
                    ch4 = input("enter the type of format :")
                    os.system("ssh {} mkfs.{} /dev/{}/{}".format(ip,ch4,ch1,ch3))
                    print()
                    print("\tnow the partition is formatted")
                elif a=="6":
                    ch1=input("enter the name of volume group :")
                    ch3 = input("enter the name of logical volume :")
                    ch5 = input("enter the name of directory/folder which you want to mount :")
                    os.system("ssh {} mkdir /{}".format(ip,ch5))
                    os.system("ssh {} mount /dev/{}/{}  /{}".format(ip,ch1,ch3,ch5))
                    print()
                    print("\tnow the partition is mounted")
                elif a=="7":
                    os.system("ssh {} df -h".fomat(ip))
                elif a=="8":
                    ch1=input("enter the name of volume group :")
                    ch3 = input("enter the name of logical volume :")
                    ch6=input("emter the size which you want to extend :")
                    os.system("ssh {} lvextend --size +{} /dev/{}/{}".format(ip,ch6,ch1,ch3))
                    os.system("ssh {} resize2fs /dev/{}/{}".format(ip,ch1,ch3))
                elif a=="9":
                    exit()

        elif a=='7':
            dns=input('\n\t\t >>  IP OR Domain Name Of The Server :  ')
            os.system('ssh root@{} ping -c 4 {}'.format(rip,dns))
            input('\nPress enter key to continue...')
        elif a=='8':
            os.system('clear')
            exit()
