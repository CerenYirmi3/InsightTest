from transformers import pipeline
import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"


# Hugging Face modeli ile bir metin oluşturucu başlatma
generator = pipeline("text2text-generation", model="t5-small")

# Geri bildirimden test senaryosu oluşturma
def generate_test_scenario(feedback):
    prompt = f"Feedback: {feedback}\nGenerate a test scenario for this feedback:"
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return result[0]["generated_text"]

# Örnek geri bildirimler
feedbacks = [
    "Sepetteki ürünlerin toplam fiyatı yanlış hesaplanıyor.",
    "Mobil uyumluluk hatalı çalışıyor.",
    "Butonlar görünmüyor.",
    "Ürün açıklamaları eksik."
]

# Geri bildirimlerden test senaryosu oluşturma
for feedback in feedbacks:
    test_scenario = generate_test_scenario(feedback)
    print(f"Geri Bildirim: {feedback}")
    print(f"Oluşturulan Test Senaryosu: {test_scenario}\n")
