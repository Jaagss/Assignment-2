# Library Management System


- This project is a simple Java-based library management system that allows librarians and library members to manage books, members, and book borrowing and returning operations. It consists of three main classes: Book, Member, and Library, as well as a Main class for user interaction.
- This library management system allows for efficient management of books and members, tracks borrow times, enforces borrowing limits, and calculates fines for overdue books, ensuring smooth library operations.
## How to run the code
- variable phone number is in long type which accepts only 10 digits numbers which are standard in india.
- age as an integer value
- each choice prints according to what was written in the Assigment 1 Document and things which were not specifically written are being done according to the sample or how i thought it would be appropriate. 

## Implementation
- The library management system is implemented using Java and follows an object-oriented approach. Here's a brief explanation of each class:

## Book Class
- Represents a book in the library.
- Contains attributes for book ID, title, author, number of copies, and availability status.
- Provides methods to get and set book details, check out a book, return a book, decrement the number of copies, and increment the number of copies.
- The toString method is overridden to display book information.
## Member Class
- Represents a library member.
- Contains attributes for member ID, name, age, phone number, fines, and a list of borrowed books.
- Provides methods to register a member, borrow a book, return a book, calculate the time a book was borrowed, get and set member details, add fines, remove fines, reset fines, and display member information.
- Uses a map to track borrowed books and their borrow times.
## Library Class
- Represents the library itself and manages its operations.
- Contains lists of books and members.
- Provides methods to add books, register members, list available books, list members with fines, find a member by name and phone number, find a book by ID, remove a member, and remove a book.
- Ensures constraints like not allowing a member to borrow more than two books or checking fines for overdue books.
## Main Class
- Handles user interaction through the command line.
- Offers options for librarians and members to perform various operations, such as registering members, adding/removing books, listing books/members, borrowing/returning books, and paying fines.
# Features/Functions
## Librarian Functions:

- Register a new member.
- Remove a member (if no books are borrowed and no fines are pending).
- Add a book to the library.
- Remove a book (if it's available).
- List all members along with their borrowed books and fines.
- List all available books in the library.
## Member Functions:

- List available books.
- List books borrowed by the member.
- Borrow a book (if eligible and available).
- Return a book (calculating fines for overdue books).
- Pay fines (if any).
# How Functions Are Related
- The Library class serves as the central component that manages books and members.
- Librarians can interact with the library to add/register members and add/remove books.
- Members can borrow and return books, check their fines, and see available books.
- The Book and Member classes contain methods specific to book and member operations, while the Library class orchestrates these operations.
- The Main class provides a user-friendly interface for both librarians and members to interact with the library system.


