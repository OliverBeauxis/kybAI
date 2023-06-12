# Rozpoznávání barev pomocí umělé inteligence

Tento program využívá umělou inteligenci k rozpoznávání barev v obrázcích. Používá knihovnu OpenCV a algoritmus K-means k identifikaci nejbližší známé barvy z dominantního shluku pixelů v obraze.

## Použití

1. Instalace závislostí
   - Tento program vyžaduje nainstalovanou knihovnu OpenCV. Můžete ji nainstalovat pomocí příkazu:
     ```
     pip install opencv-python
     ```

2. Příprava obrázku
   - Nahrajte obrázek, který chcete analyzovat, do stejného adresáře jako tento skript.

3. Spuštění programu
   - V souboru `main.py` změňte hodnotu proměnné `image_path` na název souboru se skutečným obrázkem.
   - Spusťte skript pomocí příkazu:
     ```
     python main.py
     ```

4. Výsledek
   - Program zobrazí rozpoznanou barvu z obrázku na standardní výstup.

## Omezení

- Úspěšnost rozpoznávání barev závisí na kvalitě obrázku a správném nastavení algoritmu. Můžete experimentovat s různými parametry algoritmu K-means, pokud potřebujete lepší výsledky.
- Tento program momentálně pracuje pouze s několika předdefinovanými známými barvami. Pokud chcete rozpoznávat více barev, můžete přidat další RGB hodnoty do slovníku `colors` v souboru `main.py`.