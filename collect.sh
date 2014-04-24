#! /bin/bash

DATENAME=$(date "+%d%m%y")


scrapy crawl tradera -o /home/jonas/data/scrapy/tradera/${DATENAME}.json -t json
