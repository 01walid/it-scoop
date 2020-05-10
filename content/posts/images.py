
import os

from pathlib import Path
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
import urllib.request
import requests

# First create the treeprocessor

class ImgExtractor(Treeprocessor):
    def run(self, doc):
        "Find all images and append to markdown.images. "
        self.md.images = []
        for image in doc.findall('.//img'):
            self.md.images.append(image.get('src'))

# Then tell markdown about it

class ImgExtExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        img_ext = ImgExtractor(md)
        md.treeprocessors.add('imgext', img_ext, '>inline')

# Finally create an instance of the Markdown class with the new extension

md = markdown.Markdown(extensions=[ImgExtExtension()])

# Now let's test it out:
dir_path = os.path.dirname(os.path.realpath(__file__))
for path, subdirs, files in os.walk(dir_path):
    if '2020-' in path:
        continue

    for name in files:
        if not name.endswith('.md') or name.startswith("_"):
            continue
        
        file_path = os.path.join(path, name)

        print(os.path.dirname(file_path))

        contents = Path(file_path).read_text()
        html = md.convert(contents)
        # print(md.images)

        for image in md.images:
            if "socialmedia4arab.com" in image:
                continue

            retries = 0
            while retries < 3:
                try:
                    print(f"Getting image: {image}")
                    response = requests.get(image, timeout=30)
                    break
                except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL):
                    print(f"{image} is not a valid URL")
                    retries += 3
                except requests.exceptions.ConnectionError:
                    print("Network Error")
                    retries += 3
                except requests.exceptions.Timeout:
                    print("Timed out, retrying...")
                    retries += 1
            
            if retries >= 3:
                print(f"Could not get image: {image}")
                continue 

            if response.status_code == 200:
                dirname = os.path.dirname(file_path)
                img_basename = Path(image).name
                img_filename = Path(f'{dirname}/{img_basename}')
                img_filename.write_bytes(response.content)
                contents = contents.replace(image, img_basename)
                with open(file_path, "wt") as ff:
                    ff.write(contents)
                    # print(contents)
            print(response.status_code)

data = '''
**this is some markdown**
blah blah blah
![image here](http://somewebsite.com/image1.jpg)
![another image here](http://anotherwebsite.com/image2.jpg)
'''
# html = md.convert(data)
# print(md.images)
