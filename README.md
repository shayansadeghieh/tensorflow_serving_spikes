# tensorflow_serving_spikes
There seems to be some arbitrary spikes in latency when using tensorflow serving. To replicate the issue, I created a dummy tensorflow decision forest gradient boosted tree model that predicts penguin types. I used a docker image from the ml6 team that supports tensorflow decision forests ops in tensorflow serving. I then send requests to the fake_model_id and track prediction times. 

The docker image can be found here: https://hub.docker.com/r/ml6team/tf-serving-tfdf

# To run
1. Clone the repo `git clone https://github.com/shayansadeghieh/tensorflow_serving_spikes.git`
2. Enter the root directory `cd tensorflow_serving_spikes`
3. from the root directory in the repo run `bash serving.sh fake_model_id` to start up the docker container
4. from the root directory run `python tfdf_serving.py`. It will output the number of latency spikes that occur and provide a distribution plot. 
