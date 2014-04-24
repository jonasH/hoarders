#! /bin/bash

SUCCESS_TESTS=0
TOTAL_TESTS=0

function success
{
    echo "Test " $* " $(tput setaf 2) Success"
    tput sgr0
    SUCCESS_TESTS=$(($SUCCESS_TESTS + 1))
    TOTAL_TESTS=$(($TOTAL_TESTS + 1))
}
function fail
{
    echo "Test " $* " $(tput setaf 1) FAILED"
    tput sgr0
    TOTAL_TESTS=$(($TOTAL_TESTS + 1))
}
function print_result
{
    echo $SUCCESS_TESTS "/" $TOTAL_TESTS " is the result"
}




DATAFILE=/home/jonas/data/scrapy/tradera.txt

if [ -e $DATAFILE ];then
    echo "removing $DATAFILE"
    rm $DATAFILE
fi

scrapy crawl tradera &>/dev/null

if [ -e $DATAFILE ];then
    WC_COUNT=$(wc -w $DATAFILE| cut -d' ' -f1)
    if [ $WC_COUNT -gt 0 ];then
	success " get data "
    else
	fail " get data "
	
    fi

fi

print_result
