// zad 1

type 'T lista =
    | Pusta
    | Węzeł of 'T * 'T lista
let utworzListeLaczona (lista: 'T list) : 'T lista =
    let rec pomoc lista =
        match lista with
        | [] -> Pusta
        | głowa :: reszta -> Węzeł (głowa, pomoc reszta)
    pomoc lista

// zad 2

let sumaListy (lista: int list) : int =
    List.fold (+) 0 lista

// zad 3

let minMaxListy (lista: int list) : (int * int) =
    let minWartość = List.min lista
    let maxWartość = List.max lista
    (minWartość, maxWartość)

// zad 4

let odwrocListe (lista: 'T list) : 'T list =
    List.rev lista

// zad 5

let zawieraElement (element: 'T) (lista: 'T list) : bool =
    List.contains element lista

// za 6

type 'T Wynik =
    | Znaleziono of int
    | NieZnaleziono
let znajdzIndeks (element: 'T) (lista: 'T list) : 'T Wynik =
    let rec pomoc indeks lista =
        match lista with
        | [] -> NieZnaleziono
        | głowa :: reszta when głowa = element -> Znaleziono indeks
        | _ :: reszta -> pomoc (indeks + 1) reszta
    pomoc 0 lista

// zad 7

let zliczWystapienia (element: 'T) (lista: 'T list) : int =
    List.filter (fun x -> x = element) lista |> List.length

// zad 8

let polaczListeLaczone (lista1: 'T ListaLaczona) (lista2: 'T ListaLaczona) : 'T ListaLaczona =
    match lista1 with
    | Pusta -> lista2
    | Węzeł (głowa, reszta) -> Węzeł (głowa, polaczListeLaczone reszta lista2)

// zad 9

let porownajListy (lista1: int list) (lista2: int list) : bool list =
    if List.length lista1 <> List.length lista2 then
        raise (ArgumentException "Listy muszą mieć tę samą długość.")
    else
        List.map2 (fun a b -> a > b) lista1 lista2

[<EntryPoint>]
let main argv =
    let lista = [1; 2; 3; 4; 5]
    let listaLaczona = utworzListeLaczona lista
    printfn "Lista łączona: %A" listaLaczona
    let suma = sumaListy lista
    printfn "Suma elementów: %d" suma
    let (minWartość, maxWartość) = minMaxListy lista
    printfn "Min: %d, Max: %d" minWartość maxWartość
    let odwróconaLista = odwrocListe lista
    printfn "Odwrócona lista: %A" odwróconaLista
    let zawiera = zawieraElement 3 lista
    printfn "Czy lista zawiera 3? %b" zawiera
    match znajdzIndeks 3 lista with
    | Znaleziono indeks -> printfn "Indeks elementu 3: %d" indeks
    | NieZnaleziono -> printfn "Element 3 nie znaleziono"
    let wystapienia = zliczWystapienia 3 lista
    printfn "Liczba wystąpień 3 w liście: %d" wystapienia
    let lista1 = utworzListeLaczona [1; 2; 3]
    let lista2 = utworzListeLaczona [4; 5; 6]
    let połączonaLista = polaczListeLaczone lista1 lista2
    printfn "Połączona lista łączona: %A" połączonaLista
    let listaA = [1; 5; 3; 9]
    let listaB = [0; 6; 3; 8]
    try
        let wynik = porownajListy listaA listaB
        printfn "Porównanie list: %A" wynik
    with
    | ex -> printfn "Błąd: %s" ex.Message
    0
