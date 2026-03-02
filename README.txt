╔══════════════════════════════════════════════════════╗
║      KASMIR ÁRAJÁNLAT GENERÁTOR – ÚTMUTATÓ           ║
╚══════════════════════════════════════════════════════╝

FÁJLOK:
  arajanlat.html   – a program
  szerver.py       – helyi szerver (Python)
  inditas.bat      – Windows indító (dupla kattintás)
  api_kulcs.txt    – ide írd be az API kulcsodat
  README.txt       – ez a fájl

────────────────────────────────────────────────────────
  A. EGYSZERŰ MÓD (fotó nélkül, AI nélkül)
────────────────────────────────────────────────────────
  → Dupla kattints az arajanlat.html fájlra
  → Minden alap funkció működik (auto tételek, extras,
    Excel/PDF letöltés)
  → A fotóelemzés és AI szöveg NEM működik

────────────────────────────────────────────────────────
  B. TELJES MÓD (fotóelemzés + AI + minden funkció)
────────────────────────────────────────────────────────
  1. Szükséges: Python telepítve legyen
     → Letöltés: https://www.python.org/downloads/
     → Telepítésnél: pipáld be "Add Python to PATH"

  2. API kulcs beállítása:
     → Nyisd meg az api_kulcs.txt fájlt
     → Írd be az Anthropic API kulcsodat (sk-ant-...)
     → Mentsd el

  3. Indítás:
     → Dupla kattints az inditas.bat fájlra
     → Böngésző automatikusan megnyílik
     → http://localhost:8765

  ✓ Fotófeltöltés működik
  ✓ AI elemzés működik  
  ✓ Excel és PDF letöltés működik

────────────────────────────────────────────────────────
  C. JÖVŐBELI LEHETŐSÉGEK
────────────────────────────────────────────────────────
  • Webalkalmazás (telefon + bármilyen eszköz):
    A szerver feltölthető pl. Railway, Render, VPS-re
    → bárhonnan elérhető, bejelentkezés nélkül

  • Windows .exe (telepítés nélkül):
    PyInstaller segítségével becsomagolható
    → egy fájl, dupla kattintás, kész

────────────────────────────────────────────────────────
API KULCS MEGSZERZÉSE:
  → https://console.anthropic.com
  → Regisztráció után: API Keys → Create Key
  → Másold be az api_kulcs.txt fájlba
