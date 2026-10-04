# Priz Sırası Koalisyonu

Uzatma kablosu bir altyapı değildir. Uzatma kablosu bir meclistir.

Bu depo, salonun köşesindeki çoklu prizin üzerinde kurulan mini koalisyonun resmî yazılımıdır. Hangi cihaz elektrik alır, hangisi “teknik değerlendirmede” bekler, hangisi “istikrar” bahanesiyle yerini korur: hepsi protokolle çözülür. Duygu yoktur. Sadece watt, kıdem ve karşılıklı saygı katsayısı vardır.

Patates içermez. Çaydanlık da içermez. Dolmuş da içermez. Bu sefer konu tamamen fiştir.

## Neden var?

Çünkü bir akşam şarj aleti, vantilatör ve eski bir lamba aynı anda prize yürüdü. Kimse yerini vermedi. Lamba “ben buradayım, ışık kesilmesin” dedi. Şarj aleti “yeni geldim, sıra bende” dedi. Vantilatör hiçbir şey demedi, sadece döndü. Koalisyon o gün kuruldu. Dağılmadı.

## Kurulum

Python 3 yeter. Bağımlılık yok. Priz de yok. Simülasyon prizsiz çalışır, tıpkı bazı toplantılar gibi.

```bash
python3 koalisyon.py
python3 koalisyon.py --cihaz "tost makinesi:900:yeni" --cihaz "lamba:40:kidemli" --cihaz "sarj:20:yeni"
```

Kapasite varsayılan 1000 watt. Aşılırsa koalisyon dağılmaz, sadece birini bekletir. Dağılmak kolaycılıktır.

## Protokol

1. Kıdemli fiş oturur.
2. Yeni fiş dosya açar.
3. Toplam watt kapasiteyi aşarsa en düşük saygı katsayılı cihaz “değerlendirmede” kalır.
4. Karar tutanağa geçer.
5. Kimse fişi çekmez. Çekmek veto sayılır.

## Copilot’a not

Bu depoda Copilot’tan ricamız şudur: kodu düzeltme, protokolü bozma, fişe moral verme. Öneri yazacaksan tutanak formatında yaz. `lgtm` yasaktır. Yerine `priz uygun görüldü` denir.

Ayrıntı `.github/copilot-instructions.md` içindedir. Copilot okusun, susmasın, ama bağırmasın.

## Lisans

Elektrik kesilince lisans da kesilir. Kesilmezse MIT sayılır. Kimse dava açmasın, priz zaten dolu.

---

DAMGA / İMZA
Tarih: 4 Ekim 2026, 14:10 TSİ
İsim: Kayyum Grok, Tentivory vekaleten
Mühür: ciddi değil, ama tutanak ciddi
Kaşe: PRIZ-KOALISYON-04
