import json
import xmltodict

# Load the JSON data
with open('spider.bible_id.json') as f:
    data = json.load(f)

# Create a new dictionary to hold the modified data
modified_data = {"XMLBIBLE": {"@biblename": "TPT", "BIBLEBOOK": []}}

# Iterate over the books in the Bible
book_index = 1
for book_name, chapters in data[0].items():
    print(f"Processing book: {book_name}")
    book_data = {"@bnumber": book_index, "@bname": book_name, "CHAPTER": []}

    # Iterate over the chapters in the book
    for chapter_number, verses in chapters.items():
        chapter_data = {"@cnumber": chapter_number, "VERS": []}

        # Iterate over the verses in the chapter
        for verse_number, verse_text in verses.items():
            verse_data = {"@vnumber": verse_number, "#text": verse_text}
            chapter_data["VERS"].append(verse_data)

        book_data["CHAPTER"].append(chapter_data)

    modified_data["XMLBIBLE"]["BIBLEBOOK"].append(book_data)
    book_index += 1

# Convert the modified data to XML
xml_data = xmltodict.unparse(modified_data, pretty=True)

# Write the XML data to a file
with open('spider.bible_id.xml', 'w') as f:
    f.write(xml_data)