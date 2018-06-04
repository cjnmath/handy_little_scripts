#! /bin/bash
rarfile=$1
extend=${rarfile##*.}
folder=${rarfile%.*}
if [[ "$extend" == "rar" ]]; then
	mkdir $PWD/"$folder"
	mv "$PWD/$rarfile" "$PWD/$folder"
	(cd "$folder"
	unrar x *.rar
	if [[ $? == 0 ]]; then
		rm *.rar
		echo "ok."
		nautilus .
	else
		echo "something wrong, please have a check..."
	fi)
fi