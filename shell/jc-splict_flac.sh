#! /bin/bash
# sudo apt install flac wavpack
# sudo apt install cuetools shntool

for flacfile in "$PWD"/*.flac;
do
    if [[ -e "$flacfile" ]]; then
        echo -e "\e[1;33m start splitting flac file \n Checking cue file ....\e[0m";
        flac_name=${flacfile%.*}
        if [[ -e "${flac_name}.cue" ]]; then
            echo -e "\e[1;33m '$flac_name'.cue did exist! Statrt splitting \n ................ \e[0m";
            shnsplit -O always -o flac -f "${flac_name}".cue -t '%n-%t' "${flac_name}".flac;
            if [[ $? == 0 ]]; then
                echo -e "\e[1;32m shnsplit flac successfully!!! \n Deleting original flac file \n ............\e[0m"
                rm "${flac_name}".flac;
                if [[ -e "${00*.flac}" ]]; then
                    rm 00*.flac
                fi
                echo -e "\e[1;33m original flac file deleted.";
            fi
            echo -e "\e[1;33m start tag the remain flac ";
            cuetag *.cue *.flac;
            if [[ $? == 0 ]]; then
                echo -e "\e[1;32m ********************************************** \e[0m"
                echo -e "\e[1;32m "$flac_name"\e[0m"
                echo -e "\e[1;32m Finished processing !!!!  \e[0m"
                echo -e "\e[1;32m ********************************************** \e[0m"
            else
                echo -e "\e[1;31m Something wrong while tagging the flac files, have a check \e[0m";
            fi
        fi
    fi
done
