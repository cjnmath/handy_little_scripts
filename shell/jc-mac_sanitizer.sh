#! /bin/bash

target_folder=$1

if [[ -z $target_folder ]]; then
	target_folder=.
fi

find $target_folder \( -type f -name "._*" -o -type d -name "__MACOS*" \) -exec rm -rv "{}" +
