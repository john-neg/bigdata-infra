docker cp -a ./upload hadoop-namenode:/hadoop/dfs/name
docker exec -t hadoop-namenode hdfs dfs -put -f /hadoop/dfs/name/upload/. /
docker exec -t hadoop-namenode rm -rf /hadoop/dfs/name/upload
