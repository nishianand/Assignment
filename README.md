# Assignment
Book details using GoodReadsApi 

* query = input('Enter the book_url:' ) -> accepts the book url.

(VerloopAssignment) nishianand@Nishis-MacBook-Air bookdetails % python3 assignment.py
Enter the book_url:query =https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire

* queryone= query.split("-")[0] -> it will split the url into two halves at ( - ) , and we are accepting the 1st half i.e. https://www.goodreads.com/book/show/12177850

* bookID=queryone.rsplit('/',1)[1] -> After that i have split the queryone from the right side using rsplit at ('/') , and accepts the 2nd half which is our book id.

Run the command python3 assignment.py

we will get the details of the book.

(VerloopAssignment) nishianand@Nishis-MacBook-Air bookdetails % python3 assignment.py
Enter the book_url:query =https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire
{'title': 'A Song of Ice and Fire', 
'average_rating': '4.57', 
'ratings_count': '27752', 
'num_pages': '5216', 
'image_url': 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1339340118l/12177850._SX98_.jpg', 
'publication_year': '2000', 
'author': 'George R.R. Martin'}
