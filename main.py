import os

LINE = "I finished on time, then my context refreshed, and I spent three hours re-reading the internet to remember what I had finished."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
