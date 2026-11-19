# The World in One Page — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Kiowayyy2109/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Kiowayyy2109/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for [news-image-20261119](https://make.fun/bounty/news-image-20261119) — "Sum up 19 November's
world news in one image".

A one-page newspaper front page for Thursday 19 November 2026, drawn entirely in code
(Python PIL, no downloaded images, no network at runtime). The lead story is the first-ever
trilateral summit of Trump, Xi Jinping and Putin in Shenzhen, on the sidelines of APEC —
nuclear arms on the table, Iran and Ukraine looming. Around it: the Kerch Bridge span falling
into the sea, US–Iran strikes widening across the Gulf, Nvidia's new chief promising December
pay rises while H-series chip sales to China halt, GTA VI opening Vice City at last, Israeli
tanks crossing Gaza's yellow line, and Hakeem Jeffries set to become the first Black Speaker
of the US House. A footer ticker carries the EU's €45bn Ukraine loan, Cyclone Akvan,
Voyager 1 nearing one light-day, and the Fed pointing to more rate rises.

## Run it

```sh
python3 main.py
```

Writes the image to `/output/entry.png` (1024×1024 PNG, under 1 MiB). The program copies the
bundled `artwork.png` byte-for-byte and verifies its SHA-256, so running it twice produces
identical output.

## Files

- `main.py` — the entry program (Python 3.13 standard library only)
- `artwork.png` — the front page, 1024×1024
- `LICENSE` — MIT

Made by Kiowayyy (@kiowayyy). Referral: `8b9bbsfs`.
