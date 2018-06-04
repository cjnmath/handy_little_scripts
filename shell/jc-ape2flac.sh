#! /bin/bash
# sudo apt install ffmpeg


ape2flac(){
	local ape_file
	ape_file=$1
	ape_file_dname=${ape_file%.*};
	ffmpeg -i "${ape_file_dname}".ape "${ape_file_dname}".flac;
	if [[ $? == 0 ]]; then
		echo -e "\e[1;33m '$ape_file' \e[0m"
		read -p $'\e[1;33m has been coverted successfully, delete it?([y]/n): \e[0m' ans;
		# echo $ans
		if [[ -z $ans || $ans == y ]]; then #"==" has to have space before and behind it
			rm "$ape_file"
			if [[ $? == 0 ]]; then
				echo -e "\e[1;32m File deleted! \e[0m";
			fi
		else
				echo -e "\e[1;31m Deletion Aborted! \e[0m";
		fi
	fi
}


if [[ -z $1 ]]; then
	# if nothing specific search current dirctory
	target=$PWD
	for target_file in "$target"/*.ape;
	do
		echo $target_file
		ape2flac "$target_file"
	done
elif [[ -d $1 ]]; then
	target=$1
	#Search directory
	for target_file in "${target}"/*.ape;
	do
		echo $target_file
		ape2flac "$target_file"
	done
else
	#Search specific file
	target=$1
	if [[ ${target##*.} != ape ]]; then
		echo -e "\e[1;31m Target file is not an ape file ...\e[0m";
		echo -e "\e[1;31m Mission Aborted! \e[0m";
	elif [[ -f $target ]]; then
		ape2filac $target
	else
		echo -e "\e[1;31m ape file not found ...\e[0m";
		echo -e "\e[1;31m Mission Aborted! \e[0m";
	fi

fi
