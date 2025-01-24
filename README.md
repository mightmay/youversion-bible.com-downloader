# bible.com scraper

THIS ONLY WORKS WITH Python 3.9

NOTE:

- Thanks to @mightmay for this cool project!
- I am new to Python and Git, and I am still learning (My first commit & pull 🤗). If you have any suggestions or corrections, please let me know.
- I am using MacOS and Python 3.11.2. If you are using a different OS or Python version, please modify the code to fit your requirements.
- An idea I could not implement was to create a script to automate the whole process from steps 5 to 7: receive variables (bible version ID, bible version abbreviation, output filename), run scrapy, run pip install xmltodict, and convert JSON file to XML. Maybe in future updates.

## Configuring environment and running the project

To run the project, follow these steps:

1. **Fork/Clone the repository**:

   - Run the following command in your terminal: `git clone https://github.com/jerryagenyi/youversion-bible.com-downloader-json2xml.git`

2. **Create new virtual environment**:

   - Run the following command in your terminal:
     ```bash
     python -m venv venv
     ```
     OR, using Conda:
     ```bash
     conda create --name bible-dot-com-downloader python=3
     ```

3. **Activate virtual environment**:

   - Run the following command in your terminal:
     ```bash
     source venv/bin/activate
     ```
     OR, using Conda:
     ```bash
     source activate bible-scraper
     ```

4. **CD to bible folder and Install requirements**:

   - Run the following command in your terminal:
     ```bash
     cd bible
     pip install -r requirements.txt
     ```

5. **Next run "scrapy crawl bible"**:

   - Run the following command in your terminal:
     ```bash
     scrapy crawl bible
     ```

6. **Install xmltodict**:

   - Run the following command in your terminal:
     ```bash
     pip install xmltodict
     ```

7. **CD to bible/data folder and run the 'generate_xml.py' file**:
   - Run the following command in your terminal:
     ```bash
     cd bible/data
     python generate_xml.py
     ```

## Notes

- The downloaded json file will be in `\bible\data`
- JSON file structure (this is just an example, your .json file will not be in this order):

  ```json
  JList
  [
    {"BookName":
      {"ChapterNumber":
        {"VerseNumber":"Verse String"}

        ...
      }
    }
  ]
  ```

- **REMEMBER:**
  - Get Bible version IDs from www.bible.com (i.e. NIV version ID is 59: https://www.bible.com/bible/59/GEN.1.ESV)
  - Don't forget to change the Bible Version abbreviation in line 9 of generate_xml.py when declaring the dictionary (i.e. @biblename": "TPT", to @biblename": "IUMN" or @biblename": "ARA" etc).
  - The JSON and XML files generated (spider.bible_id.json and spider.bible_id.xml) are in `\bible\data`.
