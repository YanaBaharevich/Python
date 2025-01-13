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
    przeliczWalute kwota walutaZrodlowa walutaDocelowa
main()
