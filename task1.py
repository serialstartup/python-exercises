# 1) list — Değiştirilebilir, sıralı koleksiyon
    # Ne zaman kullanılır? Sıra önemliyse, tekrar eden elemanlar olabilirse, sık sık ekleme/çıkarma yapacaksan.
alisveris = ["elma", "süt", "ekmek"]
alisveris.append("yumurta")      # sona ekler
alisveris.insert(0, "peynir")    # belirli indekse ekler
alisveris.remove("süt")          # değere göre siler
alisveris.pop()                  # sondan siler ve döner
alisveris[1] = "tereyağı"        # index ile güncelleme
print(alisveris)


# 2) tuple — Değiştirilemez (immutable), sıralı
    # Ne zaman kullanılır? Veri değişmeyecekse (sabit bir kayıt gibi), dict key olarak kullanılacaksa (list olamaz çünkü değiştirilebilir), fonksiyondan birden fazla değer dönerken.
koordinat = (41.0, 28.9)  # değiştirilemez
# koordinat[0] = 5  → HATA verir

# dict — Anahtar-değer eşleşmesi
    # Ne zaman kullanılır? Hızlı arama/eşleştirme gerektiğinde (LeetCode'da hash map olarak resmen can simidi olacak).
urun_fiyat = {"elma": 15, "süt": 30}
urun_fiyat["ekmek"] = 10          # ekleme/güncelleme
del urun_fiyat["süt"]             # silme
urun_fiyat.get("armut", 0)        # yoksa hata vermez, default döner
"elma" in urun_fiyat              # True/False, O(1) hızlı arama    

# set — Sırasız, benzersiz elemanlar
    # Ne zaman kullanılır? Tekrar eden veriyi elemek, iki grup arasında kesişim/fark bulmak istediğinde.
alinanlar = {"elma", "süt"}
alinanlar.add("ekmek")
alinanlar.add("elma")   # zaten var, tekrar eklenmez
"süt" in alinanlar       # O(1) hızlı kontrol

# Görev: Todo Listesi

# Aşağıdaki özelliklere sahip basit bir konsol uygulaması yaz:

# Kullanıcı görev ekleyebilsin
# Kullanıcı görev silebilsin (numaraya göre)
# Kullanıcı bir görevi "tamamlandı" olarak işaretleyebilsin
# Tüm görevleri listelerken tamamlananları [x], bekleyenleri [ ] şeklinde göstersin

# İpucu: Her görevi bir dict olarak tutabilirsin, örneğin {"gorev": "Süt al", "tamamlandi": False}, ve hepsini bir list içinde saklayabilirsin.

tasks = [ {"gorev": "Clean home", "tamamlandi": False}, 
          {"gorev": "Do homework", "tamamlandi": True},
          {"gorev": "Read book", "tamamlandi": True} ]


print(tasks[1]["gorev"])  # Clean home
print(f"En son görev: {tasks[-1]['gorev']}")  # Read book
print(f"Tamamlanan görev sayısı: {sum(1 for task in tasks if task['tamamlandi'])}")  # 1

def list_tasks():
   for i, task in enumerate(tasks):
      print(f"index: {i}, Gorev: {task['gorev']}, Durum: {'[x]' if task['tamamlandi'] else '[ ]'}")


def add_task(gorev):
   tasks.append({"gorev": gorev, "tamamlandi": False})
   print(f"Görev eklendi: {gorev}")


def remove_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Görev silindi: {removed_task['gorev']}")
    else:
        print("Geçersiz indeks!")


def mark_task_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["tamamlandi"] = True
        print(f"Görev tamamlandı: {tasks[index]['gorev']}")
    else:
        print("Geçersiz indeks!")