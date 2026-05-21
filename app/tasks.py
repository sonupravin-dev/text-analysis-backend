import random
import time

def analyze_text(text):
    time.sleep(1)

    if random.randint(1, 10) < 3:
        raise Exception("Random API Failure")

    return {
        "text": text,
        "analysis": "success"
    }