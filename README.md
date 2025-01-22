# bible.com scraper

THIS ONLY WORKS WITH Python 3.9

Please refer to the original READ.md file here: https://github.com/mightmay/youversion-bible.com-downloader/blob/master/README.md

NOTE:
- I am using MacOS and Python 3.11.2. If you are using a different OS or Python version, please modify the code to fit your requirements.
- I am new to Python and Git, and I am still learning. If you have any suggestions or corrections, please let me know.
- An idea I could not implement was to create a script to automate the whole proced: receive variables (bible version ID, bible version abbreviation, output filename). Maybe in future updates.

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

5. **CD to bible folder and run "scrapy crawl bible"**:

   - Run the following command in your terminal:
     ```bash
     cd bible
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
