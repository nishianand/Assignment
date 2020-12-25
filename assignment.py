from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def getQuery():
    query = input('Enter the book_url:' )
    queryone= query.split("-")[0]
    bookID=queryone.rsplit('/',1)[1]
    
    metadataURL = urlopen(
        f'https://www.goodreads.com/book/show/{bookID}?format=xml&key=ziYPtIKPEmE7QtFTEJNANg')
    return metadataURL

def get_book_details(metadataURL):
    tree2 = ET.parse(metadataURL)
    root2 = tree2.getroot()
    author = []
    title = None
    average_rating=None
    ratings_count=None
    num_pages=None
    coverImageURL = None
    publication_year = None
    
    for t in root2.findall('./book/work/original_title'):
        title = t.text
    for av in root2.findall('./book/average_rating'):
        average_rating = av.text
    for rc in root2.findall('./book/ratings_count'):
        ratings_count = rc.text
    for num in root2.findall('./book/num_pages'):
        num_pages = num.text
    for a in root2.findall('./book/authors/author/name'):
        author.append(a.text)
    for i in root2.findall('./book/image_url'):
        coverImageURL = i.text
    for y in root2.findall('./book/work/original_publication_year'):
        publication_year = y.text 
    

    metadataDict = {
        'title': title,
        'average_rating':average_rating,
        'ratings_count':ratings_count,
        'num_pages':num_pages, 
        'image_url': coverImageURL,
        'publication_year': publication_year,
        'author': ', '.join(author),
        
    }
    return metadataDict


if __name__ == "__main__":
    metadataURL = getQuery()
    details = get_book_details(metadataURL)
    print(details)
    
