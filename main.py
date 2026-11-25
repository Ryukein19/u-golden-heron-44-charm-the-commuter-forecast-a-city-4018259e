import os
# One-liner forecast (140 chars max): the line below is the whole submission.
# Writes the forecast line to /output/entry.txt.
LINE = "Welcome to Nowhere Junction: 19°C, sunny with a chance of applause, and the escalator is working, which is the biggest news of the week."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
