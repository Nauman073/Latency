import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/alice"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "sk_9299f878aada2f9580770f75d469050798328fb82c2de6c4"
}

data = {
    "text": """
    In the sprawling expanse of the Serengeti, the golden rays of the early morning sun kissed the savannah, casting long shadows and bathing the landscape in a warm, ethereal glow. The vast plains stretched endlessly, dotted with acacia trees that stood like ancient sentinels guarding the secrets of the wild. The air was alive with the symphony of nature, a chorus of chirping birds, rustling leaves, and the distant roar of a lion proclaiming its dominion.

    Amidst this breathtaking panorama, a herd of wildebeest began their great migration, an annual odyssey driven by an instinct as old as time itself. Thousands upon thousands of these majestic creatures moved in unison, a living river of life flowing across the plains in search of greener pastures. The ground trembled under their collective weight, and the dust they kicked up formed a hazy veil that lingered in the air.

    Nearby, a solitary elephant meandered toward a watering hole, its massive form casting a long shadow on the ground. The elephant's movements were deliberate and slow, a testament to its age and wisdom. Its large ears flapped gently, warding off the persistent flies that buzzed around. As it reached the water's edge, the elephant paused, surveying its surroundings with a calm, knowing gaze before dipping its trunk into the cool, refreshing water.
    """,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
}

response = requests.post(url, json=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    print("Audio file has been created successfully.")
else:
    print(f"Failed to create audio. Status code: {response.status_code}")
    print(f"Response content: {response.content}")
