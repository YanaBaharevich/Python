open System

//ZAD1 + 2 + 3

let liczbaSlow (tekst: string) =
    tekst.Split([|' '|], StringSplitOptions.RemoveEmptyEntries)
    |> Array.length

let liczbaZnakow (tekst: string) =
    tekst.Replace(" ", "")
    |> fun t -> t.Length

let czyPalindrom (tekst: string) =
    let oczyszczonyTekst = 
        tekst.Replace(" ", "").ToLower()
    
    oczyszczonyTekst = String(oczyszczonyTekst.ToCharArray() |> Array.rev)

let removeDuplicates (words: string list) =
    words |> List.distinct

[<EntryPoint>]

let main argv =
    printfn "Podaj tekst: "
    let tekst = Console.ReadLine()

    let liczbaSlow = liczbaSlow tekst
    let liczbaZnakow = liczbaZnakow tekst

    printfn "Liczba słów: %d" liczbaSlow
    printfn "Liczba znaków (bez spacji): %d" liczbaZnakow

    printfn "Podaj tekst: "
    let tekst = Console.ReadLine()

    if czyPalindrom tekst then
        printfn "Tekst jest palindromem."
    else
        printfn "Tekst nie jest palindromem."

    printfn "Wprowadź słowa oddzielone spacjami:"
    let input = Console.ReadLine()
    let words = input.Split([|' '|], StringSplitOptions.RemoveEmptyEntries) |> Array.toList

    let uniqueWords = removeDuplicates words

    printfn "Unikalne słowa: %A" uniqueWords

    0

// zad 5

let znajdzNajdluzszeSlowo tekst =
    let slowa = tekst.Split([|' '; '\n'; '\t'; '.'; ','; ';'; '!'|], System.StringSplitOptions.RemoveEmptyEntries)
    let najdluzszeSlowo = slowa |> List.ofArray |> List.maxBy String.length
    let dlugosc = String.length najdluzszeSlowo
    najdluzszeSlowo, dlugosc
let tekst = "Jakiś tekst. La la aaa"
let najdluzszeSlowo, dlugosc = znajdzNajdluzszeSlowo tekst
printfn "Najdłuższe słowo: %s" najdluzszeSlowo
printfn "Długość najdłuższego słowa: %d" dlugosc

// zad 6

let zamienSlowo tekst stareSlowo noweSlowo =
    let zmodyfikowanyTekst = tekst.Replace(stareSlowo, noweSlowo)
    zmodyfikowanyTekst
printfn "Wprowadz tekst"
let tekst = Console.ReadLine()
printfn "Stare slowo:"
let stareSlowo = Console.ReadLine()
printfn "Nowe słowo:"
let noweSlowo = Console.ReadLine()
let zmodyfikowanyTekst = zamienSlowo tekst stareSlowo noweSlowo
printfn "Zmodyfikowany tekst: %s" zmodyfikowanyTekst


