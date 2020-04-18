# bible.com scraper

### Configuring environment and running the project

```console
conda create --name bible-dot-com-downloader python=3
source activate bible-scraper
pip install -r requirements.txt

Go into the folder:
cd bible

Change language version in \bible\spiders\spider.py
Run using:
scrapy crawl bible

The downloaded json file will be in \bible\data

JSON file structure (this is just an example, your .json file will not be in this order):
JList
[
"BookName":
{"ChapterNumber":
{"VerseNumber":"Verse String"}

}
]

```
