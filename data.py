import sqlite3
from datetime import datetime

# Veritabanı bağlantısı
conn = sqlite3.connect("feedbacks.db")
cursor = conn.cursor()

# Tablo oluşturma
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedbacks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feedback_text TEXT NOT NULL,
    category TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# Geri bildirim ekleme
def add_feedback(feedback_text, category):
    timestamp = datetime.now()
    cursor.execute("""
    INSERT INTO feedbacks (feedback_text, category, timestamp)
    VALUES (?, ?, ?)
    """, (feedback_text, category, timestamp))
    conn.commit()

# Örnek geri bildirim ekleme
add_feedback("Sayfa yüklenmiyor.", "Hata")
add_feedback("Buton daha belirgin olmalı.", "Öneri")

# Veritabanını kapatma
conn.close()
