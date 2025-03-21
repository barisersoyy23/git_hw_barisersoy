Git & GitHub Assignment

 Proje Açıklaması

Bu proje, Git ve GitHub kullanımını pratik etmek amacıyla oluşturulmuştur. Proje kapsamında aşağıdaki adımlar uygulanmıştır:

Bir Git deposu oluşturuldu ve yerel makinada çalıştırıldı.

Git komutları kullanılarak dosya versiyonlama işlemleri gerçekleştirildi.

GitHub'a proje yüklendi ve uzak repo ile bağlantı sağlandı.

README dosyası oluşturularak proje detayları ve kullanılan komutlar açıklandı.

├── img/               # README'de kullanılan görseller
├── tests/             # Boş test klasörü
├── coordinates.csv    # Koordinat bilgilerini içeren CSV dosyası
├── point.py           # Nokta işlemlerini yapan Python kodu
└── README.md          # Proje dokümantasyonu

Kullanılan Git Komutları

| Git Komutu  | Açıklaması  |
|-------------|------------|
| `git init`  | Yerel bir Git deposu oluşturur. |
| `git add .` | Tüm değişiklikleri sahneye alır. |
| `git commit -m "Mesaj"` | Sahneye alınan değişiklikleri kaydeder. |
| `git status` | Deponun mevcut durumunu gösterir. |
| `git log` | Yapılan commitleri listeler. |
| `git branch -M main` | Ana branch'in adını değiştirir. |
| `git remote add origin <repo-url>` | Uzak GitHub deposuyla bağlantı kurar. |
| `git push -u origin main` | Değişiklikleri uzak depoya gönderir. |
| `git pull origin main` | Uzak depodaki en güncel değişiklikleri çeker. |
| `git clone <repo-url>` | Mevcut bir GitHub deposunu yerel bilgisayara kopyalar. |

Git ve GitHub İş Akışı Karşılaştırması

| Yerel Git İş Akışı | GitHub İş Akışı |
|--------------------|---------------|
| `git init` ile başlar. | GitHub'da bir repo oluşturulur. |
| Değişiklikler `git add .` ve `git commit -m "mesaj"` ile kaydedilir. | `git push` ile değişiklikler uzak depoya gönderilir. |
| `git status` ile yerel depo durumu kontrol edilir. | `git pull` ile güncellemeler alınır. |
| İnternet bağlantısı olmadan çalışabilir. | Paylaşım ve işbirliği için internet gereklidir. |

Karşılaşılan Zorluklar

Bu süreçte karşılaşılan bazı zorluklar şunlardı:

git push sırasında kimlik doğrulama hatası alındı. Çözüm olarak, SSH anahtarı oluşturulup GitHub hesabına eklendi.


Yanlışlıkla sahneye alınan dosyalar için git reset ve git restore komutları kullanıldı.

Merge işlemlerinde çakışmalar yaşandı ve git merge ile çözüldü.

 Commit Stratejisi

Commit yaparken şu prensiplere dikkat edildi:

Küçük ve anlamlı değişiklikler yapmak.

Her değişiklik sonrası commit atmak ve açıklayıcı mesajlar kullanmak.

Kritik değişiklikler öncesi ayrı bir branch açarak test etmek.

 AI Kullanımı Hakkında

Bu ödev sırasında ChatGPT'den aşağıdaki konular hakkında yardım alındı:

README dosyası nasıl yazılır?

Git ve GitHub iş akışları arasındaki farklar nelerdir?

Git komutlarının açıklamaları ve kullanım senaryoları.

Sorulan soru: "GitHub README.md dosyası nasıl hazırlanır?"

Öğrenilenler: Markdown formatında tablolar oluşturma, Git komutlarının açıklamalarını detaylandırma, commit mesajlarını daha açıklayıcı yazma.


![](https://github.com/barisersoyy23/git_hw_barisersoy/blob/master/img/image_barisersoy.png)