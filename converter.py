import os
import subprocess
import sys

# --- DINAMIKUS MAPPA MEGHATÁROZÁS ---
try:
    script_abs_path = os.path.abspath(__file__)
    TARGET_DIRECTORY = os.path.dirname(script_abs_path)
except NameError:
    TARGET_DIRECTORY = os.getcwd()

# --- BEÁLLÍTÁSOK ---
BITRATA = '320k'
# ÚJ BEÁLLÍTÁS: Hány processzormagot használhat az ffmpeg.
# Próbáld 1-gyel vagy 2-vel, hogy kevésbé melegedjen a gép.
CPU_KORLAT = 2 

def convert_wav_to_aac_in_current_folder():
    print(f"Működési mappa: {TARGET_DIRECTORY}")
    print(f"CPU magok korlátozása: {CPU_KORLAT}")
    print("-" * 30)

    try:
        wav_files = [f for f in os.listdir(TARGET_DIRECTORY) if f.lower().endswith('.wav')]
    except FileNotFoundError:
        print(f"HIBA: A mappa nem olvasható vagy nem létezik: '{TARGET_DIRECTORY}'")
        return

    if not wav_files:
        print("Nem található .wav kiterjesztésű fájl ebben a mappában.")
        return

    total_files = len(wav_files)
    success_count = 0
    print(f"Összesen {total_files} .wav fájl található, a konvertálás indul.\n")

    for i, filename in enumerate(wav_files, 1):
        input_path = os.path.join(TARGET_DIRECTORY, filename)
        output_filename_base = os.path.splitext(filename)[0]
        output_path = os.path.join(TARGET_DIRECTORY, output_filename_base + '.aac')

        print(f"[{i}/{total_files}] Konvertálás: '{filename}'")

        command = [
            'ffmpeg', '-i', input_path, '-y',
            # ITT VAN A VÁLTOZÁS:
            '-threads', str(CPU_KORLAT),
            '-c:a', 'aac', '-b:a', BITRATA, '-loglevel', 'error', output_path
        ]

        try:
            subprocess.run(command, check=True)
            print(f"    SIKER: '{os.path.basename(output_path)}' létrehozva.")
            success_count += 1
        except Exception as e:
            print(f"    HIBA a konvertálás során: {e}")

    print("\n--- Konvertálás befejezve! ---")
    print(f"Sikeres konverziók: {success_count} / {total_files}")
    
if __name__ == "__main__":
    convert_wav_to_aac_in_current_folder()
