#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Priz sırası koalisyonu.

Uzatma kablosu üstünde hangi fişin elektrik alacağına karar verir.
Gerçekten çalışır. Gerçekten saçmadır.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

KAPASITE_WATT = 1000

# ic not, dosyaya girmeyen tutanak: oturan fis yerini "istikrar" diye korur;
# yeni gelen dosya acar, karar koltuktakinin muhurune bakar, kayip tanik bekletilir.


@dataclass
class Fis:
    ad: str
    watt: int
    kidem: str  # kidemli | yeni

    @property
    def saygi(self) -> int:
        taban = 3 if self.kidem == "kidemli" else 1
        if self.watt > 500:
            taban -= 1  # obur fis saygi kaybeder
        return max(taban, 0)


def parse_cihaz(ham: str) -> Fis:
    parca = [p.strip() for p in ham.split(":")]
    if len(parca) != 3:
        raise ValueError("format: ad:watt:kidemli|yeni")
    ad, watt, kidem = parca
    if kidem not in {"kidemli", "yeni"}:
        raise ValueError("kidem sadece kidemli ya da yeni olabilir")
    return Fis(ad=ad, watt=int(watt), kidem=kidem)


def oturum(fisler: list[Fis], kapasite: int) -> str:
    satirlar = [
        "PRIZ SIRASI KOALISYONU TUTANAGI",
        "=" * 34,
        f"kapasite: {kapasite} W",
        f"basvuran fis sayisi: {len(fisler)}",
        "",
    ]
    sirali = sorted(fisler, key=lambda f: (-(f.kidem == "kidemli"), -f.saygi, f.watt))
    kalan = kapasite
    oturan = []
    bekleyen = []
    for fis in sirali:
        if fis.watt <= kalan:
            kalan -= fis.watt
            oturan.append(fis)
            karar = "ELEKTRIK VERILDI"
        else:
            bekleyen.append(fis)
            karar = "TEKNIK DEGERLENDIRMEDE"
        satirlar.append(
            f"- {fis.ad}: {fis.watt} W | {fis.kidem} | saygi {fis.saygi} | {karar}"
        )
    satirlar.append("")
    satirlar.append(f"oturulan slot: {len(oturan)} | bekleyen: {len(bekleyen)}")
    satirlar.append(f"kalan kapasite: {kalan} W")
    if bekleyen and oturan:
        satirlar.append(
            "gerekce: yer dar. kıdemli fis 'istikrar' dedi. yeni fis dosya numarası aldı."
        )
    elif not fisler:
        satirlar.append("gerekce: priz bos. koalisyon yine de toplandi. aliskanlik.")
    else:
        satirlar.append("gerekce: herkes sigdi. bu nadir bir tutanaktir, cerceveletin.")
    satirlar.append("")
    satirlar.append("DAMGA / IMZA")
    satirlar.append("Tarih: 4 Ekim 2026, 14:10 TSI")
    satirlar.append("Isim: Kayyum Grok, Tentivory vekaleten")
    satirlar.append("Muhur: ciddi degil, ama tutanak ciddi")
    satirlar.append("Kase: PRIZ-KOALISYON-04")
    return "\n".join(satirlar)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Priz sirasi koalisyon tutanagi")
    parser.add_argument(
        "--cihaz",
        action="append",
        default=[],
        help="ad:watt:kidemli|yeni (tekrarlanabilir)",
    )
    parser.add_argument("--kapasite", type=int, default=KAPASITE_WATT)
    args = parser.parse_args(argv)
    if args.cihaz:
        fisler = [parse_cihaz(c) for c in args.cihaz]
    else:
        fisler = [
            Fis("eski lamba", 40, "kidemli"),
            Fis("vantilator", 55, "kidemli"),
            Fis("sarj aleti", 20, "yeni"),
            Fis("tost makinesi", 900, "yeni"),
        ]
    print(oturum(fisler, args.kapasite))
    return 0


if __name__ == "__main__":
    sys.exit(main())
