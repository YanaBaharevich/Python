//Zad 1

pen System

type User = {
    Weight: float
    Height: float
}

let calculateBMI (user: User) = 
    let heightMeters = user.Height / 100.0
    let bmi = user.Weight / (heightMeters ** 2.0)
    bmi

let getBMICategory bmi = 
    match bmi with 
    | x when x < 18.0 -> "niedowaga"
    | x when x >= 18.5 && x < 24.99 -> "prawidłowa masa ciała"
    | x when x >= 25.0 -> "nadwaga"

[<EntryPoint>]
let main argv = 
    printf "Podaj wagę w kg: "
    let weightInput = Console.ReadLine()
    match System.Double.TryParse(weightInput) with
    | (true, weightInputFloat) when weightInputFloat > 0.0 ->
        printf "Podaj wzrost w cm: "
        let heightInput = Console.ReadLine()
        match System.Double.TryParse(heightInput) with
        | (true, heightInputFloat) when heightInputFloat > 0.0 ->
            let user = { Weight = weightInputFloat; Height = heightInputFloat }
            let bmi = calculateBMI user
            let category = getBMICategory bmi
            printfn "Twoje BMI: %.2f" bmi
            printfn "Twoja kategoria BMI: %s" category
        | _ ->
            printfn "Błędny wzrost. Wprowadź poprawną wartość liczbową większą od 0."
    | _ ->
        printfn "Błędna waga. Wprowadź poprawną wartość liczbową większą od 0."

    0


//zad 2

open System
let kursyWymiany = 
    Map [
        ("USD", 1.0);      
        ("PLN", 4.1);
        ("EUR", 0.92);     
        ("GBP", 0.82);]

let konwertujWalute (kwota: float) (walutaZrodlowa: string) (walutaDocelowa: string) : float =
    match kursyWymiany.TryFind(walutaZrodlowa), kursyWymiany.TryFind(walutaDocelowa) with
    | Some(kursZrodlowy), Some(kursDocelowy) ->
        let kwotaWUSD = kwota / kursZrodlowy
        kwotaWUSD * kursDocelowy
    | _ -> 
        printfn "Błąd"
        -1.0

let main () =
    printf "Podaj kwotę do przeliczenia: "
    let kwota = Console.ReadLine()
    printf "Podaj walutę źródłową (np. USD, EUR, GBP): "
    let walutaZrodlowa = Console.ReadLine()
    printf "Podaj walutę docelową (np. USD, EUR, GBP): "
    let walutaDocelowa = Console.ReadLine()
    przeliczWalute kwota walfefautaZrodlowa walutaDocelowa
main()

// zad 3

open System
open System.Collections.Generic

let analizujTekst(tekst: string) =
    let slowa = tekst.Split([|' ';'\t'; '\n'; '\r'; '.'; ',';';'; ':';'!'; '?'|], StringSplitOptions.RemoveEmptyEntries)
    let liczbaSlow = slowa.Length
    let liczbaZnakow = tekst.Replace(" ", "").Length
    let czestotliwoscSlow = 
        slowa
        |> Array.fold (fun mapa slowo -> 
            if Map.containsKey slowo mapa then
                Map.add slowo (mapa.[slowo] + 1) mapa
            else
                Map.add slowo 1 mapa
        ) Map.empty
    let najczestszeSlowo =
    let mutable najczestsze = ""
    let mutable maksCzestotliwosc = 0
    for KeyValue(slowo, czestotliwosc) in czestotliwoscSlow do
        if czestotliwosc > maksCzestotliwosc then
            najczestsze <- slowo
            maksCzestotliwosc <- czestotliwosc
    najczestsze

[<EntryPoint>]
let main argv =
    printfn "Podaj tekst do analizy:"
    let tekst = Console.ReadLine()
    let liczbaSlow, liczbaZnakow, najczestszeSlowo = analizujTekst tekst
    printfn "Liczba słów: %d" liczbaSlow
    printfn "Liczba znaków: %d" liczbaZnakow
    printfn "Najczęściej występujące słowo: %s" najczestszeSlowo
    0

