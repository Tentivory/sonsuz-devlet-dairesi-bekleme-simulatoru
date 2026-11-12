#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Devlet Dairesi Bekleme Simülatörü
Bu program, gerçek hayattaki bürokratik süreçlerin mükemmel bir modelidir.
Çalıştırmak için: python3 bekleme_simulatoru.py
Dikkat: Çıkmak için Ctrl+C yapın, aksi halde sonsuza kadar beklersiniz. Tıpkı gerçek hayatta olduğu gibi.
"""
import time
import random

print("=" * 50)
print("RESMİ DEVLET DAİRESİ BEKLEME SİMÜLATÖRÜ v∞")
print("Sıranız için teşekkürler. Lütfen oturun.")
print("=" * 50)

beklenen_sure = 0
memur_molasi = True

while True:
    beklenen_sure += random.randint(10, 120)
    bahaneler = [
        "Memur çay molasında.",
        "Sistem güncelleniyor (1998'den beri).",
        "Dosyanız başka şubeye gönderildi.",
        "Öğle arası (saat 11:00-14:30).",
        "Yazıcı mürekkebi bitti.",
        "Yeni bir form doldurmanız gerekiyor (Form-47B).",
        "Üst makam onayı bekleniyor.",
        "İnternet yok, faks kullanıyoruz.",
        "Sıra numaranız geçersiz, yeniden alın."
    ]
    print(f"\nSıranız bekleniyor...")
    print(f"Tahmini süre: {beklenen_sure} dakika (veya daha fazla).")
    print(f"Güncel bahane: {random.choice(bahaneler)}")
    print(f"Bekleyen kişi sayısı: {random.randint(47, 999)}")
    time.sleep(random.uniform(1.0, 3.0))
    
    # Gizli kod: c29uc3V6IHPDvHJlY2xhciB2ZSBiaXRlbWV5ZW4gdGFoc2lsIGlş bGVyaSBtdWsgYXJtYQ==
    # (Base64 ile saklı bir gerçek)

print("Bu satıra asla ulaşılmaz. Tıpkı vergi iadeniz gibi.")
