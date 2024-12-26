from transformers import pipeline

# Hugging Face modelini yükle
generator = pipeline("text2text-generation", model="t5-small")

# Kategorilere uygun anahtar kelimeler
category_keywords = {
    "Sepet": ["fiyat hatası", "sepet kontrolü", "toplam fiyat", "sepet tutarı"],
    "Ödeme": ["ödeme hatası", "ödeme yöntemi", "ödeme ekranı", "ödeme başarısız"],
    "Ürün": ["ürün açıklaması", "ürün bilgisi", "ürün stoku", "ürün görseli"],
    "Üyelik": ["hesap açma", "üyelik girişi", "şifre sıfırlama", "kullanıcı hesabı"],
    "Performans": ["hız", "gecikme", "sayfa yüklenme süresi", "site hızı"],
    "Tasarım": ["buton görünürlük", "mobil uyumluluk", "site düzeni", "görsel hatalar"],
    "İletişim": ["müşteri desteği", "iletişim formu", "e-posta yanıtı", "geri dönüş"],
    "Kampanya": ["indirim", "kampanya hatası", "kampanya süresi", "promosyon kodu"],
    "Diğer": ["genel hata", "uyumsuzluk", "beklenmeyen durum", "yazılım hatası"]
}

# Test senaryosu oluşturma fonksiyonu
def generate_test_scenario(feedback, category):
    # Kategoriye uygun anahtar kelimeleri geri bildirimle birlikte ekle
    keywords = " ".join(category_keywords.get(category, []))
    prompt = f"Given the feedback: '{feedback}' from the category '{category}' with keywords: {keywords}, generate a relevant test scenario for an e-commerce site."
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return result[0]["generated_text"]

# Örnek geri bildirimler ve kategoriler
feedbacks = [
    ("Sepetteki ürünlerin toplam fiyatı yanlış hesaplanıyor.", "Sepet"),
    ("Mobil uyumluluk hatalı çalışıyor.", "Tasarım"),
    ("Butonlar görünmüyor.", "Tasarım"),
    ("Ürün açıklamaları eksik.", "Ürün")
]

# Geri bildirimlerden test senaryosu oluşturma
for feedback, category in feedbacks:
    test_scenario = generate_test_scenario(feedback, category)
    print(f"Geri Bildirim: {feedback}")
    print(f"Kategori: {category}")
    print(f"Oluşturulan Test Senaryosu: {test_scenario}\n")
