import plistlib

# Load the XML file
with open("/Users/aryansharma/Desktop/Bookmarks.xml", "rb") as plist_file:
    bookmarks_data = plistlib.load(plist_file)

def extract_bookmarks(data):
    html_output = "<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<TITLE>Bookmarks</TITLE>\n<H1>Bookmarks</H1>\n<DL><p>\n"

    def parse_children(children):
        html = ""
        for child in children:
            if "URIDictionary" in child and "URLString" in child:
                title = child["URIDictionary"].get("title", "Untitled")
                url = child["URLString"]
                html += f'    <DT><A HREF="{url}">{title}</A>\n'
            elif "Children" in child:
                folder_name = child.get("Title", "Untitled Folder")
                html += f'    <DT><H3>{folder_name}</H3>\n    <DL><p>\n'
                html += parse_children(child["Children"])
                html += '    </DL><p>\n'
        return html

    html_output += parse_children(bookmarks_data["Children"])
    html_output += "</DL><p>\n"

    return html_output

# Save as HTML
html_content = extract_bookmarks(bookmarks_data)
with open("/Users/aryansharma/Desktop/Safari_Bookmarks.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("✅ Conversion complete! File saved as 'Safari_Bookmarks.html'.")
