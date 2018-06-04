#! /bin/bash
zipfile=$1
extend=${zipfile##*.}
folder=${zipfile%.*}
if [[ $extend == "zip" ]]; then
	mkdir "$PWD/$folder"
	mv "$PWD/$zipfile" "$PWD/$folder"
	(cd "$folder"
	unzip *.zip
	if [[ $? == 0 ]]; then
		rm *.zip
		echo "ok."
		nautilus .
	else
		echo "something wrong, please have a check..."
	fi)
fi