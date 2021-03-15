import os 
import subprocess as sp
print("\t\t\tWelcome To Menu !!")
print("\t\t--------------------------------")
while True:
    print("""
 \n
 press 1 : to display the disk partition table 
 press 2 : to create physical volume
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
        input('\nPress enter key to continue...')
        os.system("clear")
    elif a=="2":
        ch = input("enter the name of the disk partition :")
        print()
        os.system("pvcreate {}".format(ch))
        os.system("pvs")
        input('\nPress enter key to continue...')
        os.system("clear")
    elif a=="3":
        ch = input("enter the name of the disk partition :")
        ch1=input("enter the name of volume group :")
        print()
        os.system("vgcreate {} {}".format(ch1,ch))
        os.system("vgs")
        input('\nPress enter key to continue...')
        os.system("clear")
    elif a=="4":
        ch1=input("enter the name of volume group :")
        ch2 = input("enter the size of logical volume in format of G or M :")
        ch3 = input("enter the name of logical volume :")
        print()
        os.system("lvcreate --size {} --name {} {}".format(ch2,ch3,ch1))
        os.system("lvs")
        print("\n\tThe Logical Volume is created")
        input('\nPress enter key to continue...')
        os.system("clear")
    elif a=="5":
        ch1=input("enter the name of volume group :")
        ch3 = input("enter the name of logical volume :")
        ch4 = input("enter the type of format :")
        os.system("mkfs.{} /dev/{}/{}".format(ch4,ch1,ch3))
        print()
        print("\n\t The Logical Volume is formatted")
        input('\nPress enter key to continue...')
        os.system("clear")
    elif a=="6":
        ch1=input("enter the name of volume group :")
        ch3 = input("enter the name of logical volume :")
        ch5 = input("enter the name of directory in which you want to mount :")
        op=sp.getstatusoutput("mkdir {}".format(ch5))
        os.system("mount /dev/{}/{}  {}".format(ch1,ch3,ch5))
        print()
        print("\n\tnow the Logical Volume is mounted")
        input('\nPress enter key to continue...')
        os.system("clear")
    elif a=="7":
        os.system("df -h")
        input('\nPress enter key to continue...')
        os.system("clear")
    elif a=="8":
        ch1=input("enter the name of volume group :")
        ch3 = input("enter the name of logical volume :")
        ch6=input("enter how much size you want to extend :")
        os.system("lvextend --size +{} /dev/{}/{}".format(ch6,ch1,ch3))
        os.system("resize2fs /dev/{}/{}".format(ch1,ch3))
        input('\nPress enter key to continue...')
        os.system("clear")
    elif a=="9":
        exit()
