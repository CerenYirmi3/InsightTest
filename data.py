import sqlite3

# Veritabanı bağlantısı
conn = sqlite3.connect("feedbacks.db")
cursor = conn.cursor()

# Tablo oluşturma
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedbacks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feedback_text TEXT NOT NULL,
    category TEXT NOT NULL
)
""")
conn.commit()

# Geri bildirim ekleme
def add_feedback(feedback_text, category):
    cursor.execute("""
    INSERT INTO feedbacks (feedback_text, category)
    VALUES (?, ?)
    """, (feedback_text, category))
    conn.commit()

# Örnek geri bildirim ekleme
add_feedback("Sayfa yüklenmiyor.", "Hata")
add_feedback("Buton daha belirgin olmalı.", "Öneri")

# Veritabanını kapatma
conn.close()
