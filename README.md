# tensorflow_serving_spikes
There seems to be some arbitrary spikes in latency when using tensorflow serving. To replicate the issue, I created a dummy tensorflow decision forest gradient boosted tree model that predicts penguin types. I used a docker image from the ml6 team that supports tensorflow decision forests ops in tensorflow serving. I then send requests to the fake_model_id predict url and track prediction times/spikes in prediction times.

The average prediction time is around 6 ms, and I defined a spike in prediction time as any prediction time greater than 20ms. I also read the results prior to moving onto the next request as to avoid qeueing.

The docker image can be found here: https://hub.docker.com/r/ml6team/tf-serving-tfdf

# To run
1. Clone the repo `git clone https://github.com/shayansadeghieh/tensorflow_serving_spikes.git`
2. Enter the root directory `cd tensorflow_serving_spikes`
3. From the root directory in your terminal run `bash serving.sh fake_model_id` to start up the docker container
4. From the root directory in your terminal run `python tfdf_serving.py`. It will output the number of latency spikes that occur and provide a distribution plot. 

When I run for 10000 requests I get:
```
The mean pred time was 6.1302518830269275 ms
Out of 10000 requests there were 38 spikes
```
The distribution plot looks like this:
<img width="620" alt="image" src="https://user-images.githubusercontent.com/62001365/152210013-5ec04d7b-9390-4be1-a7d6-e3210985f9b9.png">

But if you zoom past the 20ms point, you'll see the spikes
<img width="612" alt="image" src="https://user-images.githubusercontent.com/62001365/152209867-1a567208-24af-453f-ad87-0a5dbfc4e61c.png">
