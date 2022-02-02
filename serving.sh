
docker kill tf_serving || true
docker rm tf_serving || true

docker build -f serving.Dockerfile ./$1 -t tf_serving --build-arg MODELID=$1

docker run -d --name tf_serving -p 8501:8501 -e MODEL_NAME=$1 tf_serving

echo "Container running..."