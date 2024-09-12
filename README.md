# Scraper volebních výsledků

Tento projekt je scraper pro stahování výsledků voleb z roku 2017 z webu [volby.cz](https://volby.cz). 
Skript stahuje výsledky hlasování pro všechny obce v zadaném územním celku a ukládá je do CSV souboru.

## Požadavky

Projekt vyžaduje Python 3 a následující knihovny:
- `requests`
- `beautifulsoup4`

Tyto knihovny lze nainstalovat pomocí příkazu:
```bash
pip install -r requirements.txt
```

## Jak projekt používat

Skript se spouští pomocí příkazového řádku s dvěma argumenty:
1. **URL**: Odkaz na územní celek, který chcete scrapovat (např. odkaz na Bruntál).
2. **Název výstupního souboru**: Název CSV souboru, kam se uloží výsledky (např. `vysledky_bruntal.csv`).

### Instalace potřebných knihoven

Pokud nemáte nainstalované potřebné knihovny, postupujte podle těchto kroků:

1. Vytvořte virtuální prostředí (doporučeno):
   ```bash
   python -m venv venv
   ```

2. Aktivujte virtuální prostředí:
   - **Windows:**
     ```bash
     venv\Scripts\Activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. Nainstalujte požadované knihovny:
   ```bash
   pip install -r requirements.txt
   ```

### Příklad spuštění

Chcete scrapovat výsledky pro územní celek Bruntál a uložit je do souboru `vysledky_bruntal.csv`. Příkaz pro spuštění skriptu by vypadal následovně:

```bash
python volby.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8101" "vysledky_bruntal.csv"
```

## Struktura výstupního souboru

Výstupní CSV soubor obsahuje následující sloupce:
- **Kód obce**: Kód obce z volební stránky.
- **Název obce**: Název obce.
- **Počet voličů**: Počet registrovaných voličů.
- **Počet obálek**: Počet vydaných obálek.
- **Platné hlasy**: Počet platných hlasů.
- **Hlasy pro jednotlivé strany**: Počet hlasů pro každou politickou stranu.

## Chyby a problémy

Pokud se při spuštění skriptu objeví chybová hlášení týkající se špatně zadané URL nebo chybějících argumentů, zkontrolujte:
- Správnost zadaného odkazu.
- Zda jsou oba argumenty zadány a ve správném pořadí.
