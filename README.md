WAV -> AAC Audio Konverter
Egyszerű, platformfüggetlen Python script, amely egy adott mappában található összes .wav kiterjesztésű audiofájlt magas minőségű .aac formátumra konvertál az FFmpeg segítségével.

Jellemzők
Kötegelt konvertálás: A script automatikusan feldolgozza a mappában lévő összes .wav fájlt.

Hordozhatóság: A script mindig abban a mappában dolgozik, amelyikben ő maga található. Nincs szükség az elérési utak módosítására a kódban.

Magas minőség: Alapértelmezetten 320 kbps bitrátájú AAC fájlokat hoz létre, de ez könnyen konfigurálható.

Teljesítmény-szabályozás: Beállítható, hogy a konvertálás hány processzormagot használjon, így kímélhető a gép a túlmelegedéstől.

Platformfüggetlenség: Működik Windowson, macOS-en és Linuxon is, amennyiben a szükséges előfeltételek telepítve vannak.

Előfeltételek
A script futtatásához két dologra van szükség a számítógépeden:

Python 3: A legtöbb modern operációs rendszeren már előre telepítve van. A telepítését itt ellenőrizheted.

FFmpeg: Ez egy ingyenes, nyílt forráskódú program, ami a tényleges audio- és videókonverziót végzi. A script ezt a programot hívja meg a háttérben. Telepíteni kell, és a rendszer számára elérhetővé kell tenni (PATH-ban kell lennie).

FFmpeg telepítése

macOS (Homebrew használatával):

Bash
brew install ffmpeg
Linux (Debian/Ubuntu alapú rendszerek):

Bash
sudo apt update && sudo apt install ffmpeg
Windows:
A legegyszerűbb módja a Chocolatey csomagkezelő használata:

Bash
choco install ffmpeg
Alternatívaként letölthető a hivatalos oldalról, majd a bin mappáját manuálisan hozzá kell adni a Windows PATH környezeti változójához.

A telepítés sikerességét a ffmpeg -version paranccsal ellenőrizheted a terminálban.

Használat
A script használata rendkívül egyszerű:

Helyezd el a scriptet: Másold a konverter.py (vagy bármi legyen a neve) fájlt abba a mappába, ahol a konvertálandó .wav fájljaid vannak.

Nyiss egy terminált/parancssort:

macOS/Linux: Nyisd meg a Terminál alkalmazást.

Windows: Nyisd meg a Parancssort (Command Prompt) vagy a PowerShellt.

Navigálj a mappába: A terminálban lépj be abba a mappába, ahová a scriptet és a fájlokat másoltad.

Bash
# Példa:
cd /eleresi/ut/a/mappadhoz
Tipp Mac-en: Írd be, hogy cd , majd húzd be a mappát a Finderből a Terminál ablakra, és nyomj Entert.

Futtasd a scriptet: Add ki a következő parancsot:

Bash
python3 konverter.py
Megjegyzés: Néhány rendszeren a parancs python lehet python3 helyett.

A script elindul, kiírja a folyamatot, és a .wav fájlok mellé létrehozza az új, azonos nevű .aac fájlokat.

Konfiguráció
A script viselkedése egyszerűen módosítható a fájl elején található változók átírásával:

BITRATA: Meghatározza a kimeneti .aac fájl bitrátáját. Alapértelmezetten '320k'. Átírható pl. '256k' vagy '192k' értékre a kisebb fájlméret érdekében.

CPU_KORLAT: Meghatározza, hogy az FFmpeg hány processzormagot (szálat) használhat a konvertáláshoz. Ez hasznos lehet, ha a számítógép túlságosan felmelegszik a folyamat során. Alapértelmezetten 2.

Hogyan működik?
A script Python beépített os és subprocess moduljait használja.

Az os modul segítségével felderíti a saját helyét, és listázza az adott mappában található összes fájlt.

Kiszűri azokat a fájlokat, amelyek .wav kiterjesztésűek.

Egy cikluson belül végigmegy minden egyes .wav fájlon.

A subprocess modul segítségével minden fájlra meghívja az ffmpeg parancssori programot a megfelelő paraméterekkel (bemeneti fájl, kimeneti fájl, bitráta stb.).

Hibakezeléssel van ellátva: ha egy fájl konvertálása sikertelen, a script kiírja a hibát, de nem áll le, hanem folytatja a munkát a következő fájllal.

Licenc
Ez a projekt az MIT Licenc alatt van közzétéve.
