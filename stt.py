import requests
import time

def time_request():
    api_key = "6a078665d65eec1d7ae22268e3627db281c04633"
    url = "https://api.deepgram.com/v1/listen?model=nova-2&smart_format=true"
    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "application/json"
    }
    data = {"url": "https://static.deepgram.com/examples/interview_speech-analytics.wav"}

    start_time = time.time()
    response = requests.post(url, headers=headers, json=data)
    end_time = time.time()
    return end_time - start_time

# Run the timing function 10 times
times = [time_request() for _ in range(10)]

# Save timings to a text file
with open('Deepgram_Timings.txt', 'w') as file:
    file.write("All request timings:\n")
    for i, timing in enumerate(times):
        file.write(f"Iteration {i+1}: {timing:.3f} seconds\n")

print("Timings recorded successfully in 'Deepgram_Timings.txt'.")





# import os
# from deepgram import DeepgramClient, PrerecordedOptions
# import time
# import statistics

# # Target URL domain for the traceroute
# TARGET_DOMAIN = 'dpgr.am'
# API_KEY = '6a078665d65eec1d7ae22268e3627db281c04633'  # Replace with your actual API key
# AUDIO_URL = {"url": "https://dpgr.am/spacewalk.wav"}


# def run_latency_tests():
#     latencies = []

#     # Create a Deepgram client using the API key
#     deepgram = DeepgramClient(API_KEY)
#     options = PrerecordedOptions(model="nova-2", smart_format=True)

#     for _ in range(NUM_REQUESTS):
#         start_time = time.time()  # Capture the exact moment the request is sent
#         response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options)
#         end_time = time.time()  # Capture the moment the response is fully received
#         latency = end_time - start_time  # Calculate the round-trip time in seconds
#         latencies.append(latency)
    
#     return latencies

# def main():
#     all_run_stats = []

#     for run_index in range(NUM_RUNS):
#         latencies = run_latency_tests()

#         # Calculate statistics for latencies measured in seconds
#         avg_latency = statistics.mean(latencies)
#         min_latency = min(latencies)
#         max_latency = max(latencies)
#         std_dev_latency = statistics.stdev(latencies) if len(latencies) > 1 else 0  # Handle standard deviation for single value

#         all_run_stats.append((avg_latency, min_latency, max_latency, std_dev_latency))
#         print(f"Run {run_index+1}: Avg: {avg_latency:.3f}s, Min: {min_latency:.3f}s, Max: {max_latency:.3f}s, SD: {std_dev_latency:.3f}s")

#     # Save results to a text file
#     with open('stt_latency_results_local.txt', 'w') as file:
#         for idx, stats in enumerate(all_run_stats):
#             file.write(f"Run {idx+1}: Avg Latency: {stats[0]:.3f}s, Min Latency: {stats[1]:.3f}s, Max Latency: {stats[2]:.3f}s, SD: {stats[3]:.3f}s\n")

# if __name__ == "__main__":
#     main()