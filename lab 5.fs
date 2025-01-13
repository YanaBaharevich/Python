// zad 1

let rec  fib n = 
    if n <= 1 then n 
    else fib(n-1) + fib(n-2)

let wynik = fib 4
printfn "%d" wynik

let fibtail n =
    let rec fib n acc = 
        if n <= 1 then acc
        else fib(acc-1) (acc-2)
    fib n n

let wynik2 = fibtail 4
printfn "%d" wynik2

// zad 2

type Drzewo<'T> =
    | Puste
    | Wezel of 'T * Drzewo<'T> * Drzewo<'T>
let rec znajdzRekurencyjnie wartosc drzewo =
    match drzewo with
    | Puste -> false
    | Wezel(wart, lewe, prawe) ->
        if wart = wartosc then true
        else znajdzRekurencyjnie wartosc lewe || znajdzRekurencyjnie wartosc prawe

// zad 3
let rec usunElement x lista =
    match lista with
    | [] -> []
    | y :: ys when y = x -> ys
    | y :: ys -> y :: usunElement x ys
let rec permutacje lista =
    match lista with
    | [] -> [[]]
    | _ ->
        lista
        |> List.collect (fun x ->
            let pozostale = usunElement x lista
            let permutacjePozostalych = permutacje pozostale
            List.map (fun perm ->x :: perm) permutacjePozostalych
        )

// zad 5

let rec quicksort lista =
    let podziel pivot reszta =
        List.fold (fun (mniejsze, wieksze) x ->
            if x <= pivot then (x :: mniejsze, wieksze)
            else (mniejsze, x :: wieksze)
        ) ([], []) reszta
    match lista with
    | [] -> []
    | pivot :: reszta ->
        let mniejsze, wieksze = podziel pivot reszta
        quicksort mniejsze @ [pivot] @ quicksort wieksze
