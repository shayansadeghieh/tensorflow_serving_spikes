import os
import matplotlib.pyplot as plt
import seaborn as sns
import json
import requests
import statistics
import time
import numpy as np

# Define dummy data
data = {
    "instances": [
        {
            "bill_length_mm": 20.0,
            "body_mass_g": 100.0,
            "bill_depth_mm": 100.0,
            "flipper_length_mm": 100.0,
            "island": "Mallorca",
            "sex": "male",
            "year": 2021,
        }
    ]
}


def make_request(data):
    # Define start time of prediction
    start_time = time.time()

    # Define request to fake_model_id
    requests.post(
        "http://localhost:8501/v1/models/fake_model_id_gbt:predict",
        headers={"Content-Type": "application/octet-stream"},
        data=json.dumps(data),
    )

    # Track end time
    end_time = time.time()
    pred_time = (end_time - start_time) * 1000
    # print("prediction time was {} ms".format(pred_time))
    return pred_time


time_tracker = []
count = 0
NUM_REQUESTS = 10000
for i in range(NUM_REQUESTS):
    req_time = make_request(data)

    # Skip the first couple to avoid warm up time
    if i > 20:
        time_tracker.append(req_time)
        if req_time >= 20:
            count += 1

print("The mean pred time was {} ms".format(np.mean(time_tracker)))
print("The max pred time was {} ms".format(np.max(time_tracker)))
print(f"Out of {NUM_REQUESTS} requests there were {count} spikes")


# Plot the distribution
sns.displot(time_tracker)
plt.xlabel("prediction time (ms)")
plt.show()
