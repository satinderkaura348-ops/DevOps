#!/bin/bash
#
#
usage() {
	echo "==============================================="
	echo "        Logical Volume Creation Script         "
	echo "==============================================="
	echo
	echo "This script simplifies the process of creating a Logical Volume (LV) from a Physical Disk."
	echo
	echo "Follow the prompts carefully and provide the appropriate disk names and sizes as requested."
	echo
	echo "To identify available disks, you can use the command: df -h"
	echo
	echo "The script will guide you through:"
	echo "  1. Creating a Physical Volume (PV)"
	echo "  2. Creating a Volume Group (VG)"
	echo "  3. Creating a Logical Volume (LV)"
	echo "  4. Formatting the LV with your chosen filesystem"
	echo "  5. Mounting the LV for immediate use"
	echo
	echo "Please ensure you have appropriate permissions and that the disks are not in use."
	echo "==============================================="
	echo

}

if [[ "$1" == "-help" ]];
then
	usage
	exit 1
fi


read -p "Provide the physical disk name that you want to convert into physical volume: " Physical_Disk
pvcreate /dev/"$Physical_Disk"
if [[ $? -ne 0 ]];
then
	exit 1
else
	echo "****Successfully created physical volume $Physical_Disk****"
fi

read -p "Provide a name for new Volume Group: " VG_name
vgcreate "$VG_name" /dev/"$Physical_Disk"
if [[ $? -ne 0 ]]; 
then
	exit 1
else
	echo "****Successfully created volume Group $VG_name****"
fi



read -p "What name you would like to choose for new Logical volume: " LV_name
read -p "What size of Logical volume you want to create: " LV_size
lvcreate -n "$LV_name" -L "$LV_size" "$VG_name"
if [[ $? -ne 0 ]];
then
	exit 1
else
echo "Successfully created $LV_name logical volume"
fi


read -p "provide the formate in which you wish to format $LV_name logical volume: " format
mkfs."$format" /dev/"$VG_name"/"$LV_name"
if [[ $? -ne 0 ]];
then
	exit 1
else
	echo "Successfully formated $LV_name logical volume to $format"
fi


read -p "Provide the path where you want to mount logical volume $LV_name: " mount_path
mount /dev/"$VG_name"/"$LV_name" "$mount_path"
if [[ $? -ne 0 ]]; 
then
	exit 1
else
	echo "*****$LV_name successfully mounted to $mount_path"
fi
