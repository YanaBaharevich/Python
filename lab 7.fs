// zad 1

open System
open System.Collections.Generic

type Book(title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages

    member this.GetInfo() = 
        printfn "Tytuł : %s \nAutor: %s \nIlość stron: %d" this.Title this.Author this.Pages

type User(name: string) = 
    member this.Name = name
    member this.BorrowedBooks = new List<Book>()

    member this.BorrowBooks(book: Book) = 
        this.BorrowedBooks.Add(book)
        printfn "%s wypożyczył książkę: %s" this.Name book.Title

    member this.ReturnBooks(book: Book) = 
        if this.BorrowedBooks.Remove(book) then
            printfn "%s zwrócił książkę: %s" this.Name book.Title
        else 
            printfn "%s nie ma książki: %s" this.Name book.Title

type Library() =
    let books = new List<Book>()

    member this.AddBook(book: Book) =
        books.Add(book)
        printfn "Dodano książkę: %s" book.Title

    member this.RemoveBook(book: Book) =
        if books.Remove(book) then
            printfn "Usunięto książkę: %s" book.Title
        else
            printfn "Nie ma takiej książki"

    member this.ListBooks() =
        printfn "Książki w bibliotece:"
        books |> List.iter (fun book -> printfn "%s" book.Title)

[<EntryPoint>]
let main argv =
    let library = Library()

    let book1 = Book("1", "A", 1234)
    let book2 = Book("2", "B", 5678)
    let book3 = Book("3", "C", 9000)

    library.AddBook(book1)
    library.AddBook(book2)
    library.AddBook(book3)

    library.ListBooks()

    let user = User("Jan Kowalski")

    user.BorrowBooks(book1)
    user.BorrowBooks(book2)

    user.ReturnBooks(book2)

    library.ListBooks()

    0

// zad 2
