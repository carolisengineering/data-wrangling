# scrape-data

using scrapy spiders

## dependencies

- Scrapy: to download dataset from the web
- pandas: to read excel files
- xlrd: to open .xls files
- openpyxl: to open .xlsx files

```
$ poetry install
```

## to run

this script downloads one html file and many .xls files containing demographic data from cps

```
$ cd scrape_data/cpsdemographics/cpsdemographics
$ scrapy crawl cpsdemographics
```

this script prints the rows of interesting data in a subset of the demographic data downloaded in the previous step. there is a conversion step that must be done between these two commands (it is currently commented out in scrape_data.py)

```
              $ poetry shell
(scrape-data) $ cd scrape_data
(scrape-data) $ python scrape_data.py
``` 
