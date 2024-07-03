#!/bin/bash
set -e
sudo service ssh start

sudo chmod +x Part_1/*
sudo chmod +x Part_2/*
sudo chmod +x Part_3/*

if [ ! -d "/tmp/hadoop-hduser/dfs/name" ]; then
        $HADOOP_HOME/bin/hdfs namenode -format && echo "OK : HDFS namenode format operation finished successfully !"
fi

$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hduser

$HADOOP_HOME/bin/hdfs dfs -chmod 777 /user
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /user/hduser

$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hduser/Part_1
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /user/hduser/Part_1

cd Part_1
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hduser/Part_1/input

if ! hdfs dfs -test -e /user/hduser/Part_1/input/1.txt; then
    $HADOOP_HOME/bin/hdfs dfs -put *.txt /user/hduser/Part_1/input
fi

cd ..

$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hduser/Part_2
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /user/hduser/Part_2

cd Part_2
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hduser/Part_2/input

if ! hdfs dfs -test -e /user/hduser/Part_2/input/input.txt; then
    $HADOOP_HOME/bin/hdfs dfs -put input.txt /user/hduser/Part_2/input
fi

cd ..

$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hduser/Part_3
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /user/hduser/Part_3

cd Part_3

$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hduser/Part_3/input

if ! hdfs dfs -test -e /user/hduser/Part_3/input/access_log; then
    $HADOOP_HOME/bin/hdfs dfs -put access_log Part_3/input
fi

cd ..

# Keep the container running
tail -f /dev/null