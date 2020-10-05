import requests
import unittest

class BookDetailTestView(unittest.TestCase):
    def setUp(self):
       
        self.valid_payload = {
            'title':'A Song of Ice and Fire',
            'average_rating':'4.57',
            'ratings_count':'27741',
            'num_pages':'5216',
            'author':'George R.R. Martin',
            'pages':'5216',
            'image_url':'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1339340118l/12177850._SX98_.jpg',
            'year':'2000'

        }
       
    def test_url_get(self):
        response = requests.get('https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
        
        

