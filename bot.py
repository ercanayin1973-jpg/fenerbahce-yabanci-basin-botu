import feedparser
import re

# Google News araması
url = (
    "https://news.google.com/rss/search?"
    "q=Fenerbahce%20OR%20Fenerbah%C3%A7e"
    "%20football%20OR%20soccer%20OR%20transfer%20OR%20manager%20OR%20player"
    "&hl=en-US&gl=US&ceid=US:en"
)

feed = feedparser.parse(url)

# İlgili kelimeler
ilgili_kelimeler = [
    "fenerbahce",
    "fenerbahçe",
    "fenerbahce sk",
    "fenerbahçe sk",
    "fenerbahce football",
    "fenerbahce soccer",
]

# Futbol bağlamı
futbol_kelimeleri = [
    "football",
    "soccer",
    "transfer",
    "player",
    "manager",
    "coach",
    "match",
    "league",
    "champions",
    "europa league",
    "super lig",
    "super lig",
    "goal",
    "signing",
    "contract",
]

print("===== FENERBAHÇE YABANCI BASIN =====")
print()

sayac = 0

for entry in feed.entries:
    baslik = entry.title
    link = entry.link

    # Kaynak
    if "source" in entry:
        kaynak = entry.source.title
    else:
        kaynak = "Bilinmeyen Kaynak"

    # Başlığı küçük harfe çevir
    metin = baslik.lower()

    # Fenerbahçe geçmiyorsa atla
    fenerbahce_var = any(
        kelime in metin for kelime in ilgili_kelimeler
    )

    if not fenerbahce_var:
        continue

    # Futbol ile ilgili kelime var mı?
    futbol_var = any(
        kelime in metin for kelime in futbol_kelimeleri
    )

    # Başlıkta Fenerbahçe + futbol bağlamı yoksa atla
    if not futbol_var:
        continue

    print(f"Kaynak: {kaynak}")
    print(f"Başlık: {baslik}")
    print(f"Link: {link}")
    print("-" * 60)

    sayac += 1

    if sayac >= 15:
        break

print()
print(f"Toplam ilgili haber: {sayac}")
