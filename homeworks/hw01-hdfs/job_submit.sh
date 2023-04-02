hdfs dfsadmin -reportdocker cp mapred/. hadoop-namenode:/jobs/
docker cp AB_NYC_2019.csv hadoop-namenode:/

docker exec -t hadoop-namenode hadoop fs -put -f AB_NYC_2019.csv /
docker exec -t hadoop-namenode hadoop fs -rm -r /output-mean
docker exec -t hadoop-namenode hadoop fs -rm -r /output-var

# Map Reduce jobs
docker exec -t hadoop-namenode mapred streaming \
  -input /AB_NYC_2019.csv \
  -output /output-mean \
  -mapper ./mapper-mean.py \
  -file jobs/mapper-mean.py \
  -reducer ./reducer-mean.py \
  -file jobs/reducer-mean.py

docker exec -t hadoop-namenode mapred streaming \
  -input /AB_NYC_2019.csv \
  -output /output-var \
  -mapper ./mapper-var.py \
  -file jobs/mapper-var.py \
  -reducer ./reducer-var.py \
  -file jobs/reducer-var.py

# Results
echo "Mean"
docker exec -t hadoop-namenode hadoop fs -cat /output-mean/part-00000

echo "Var"
docker exec -t hadoop-namenode hadoop fs -cat /output-var/part-00000