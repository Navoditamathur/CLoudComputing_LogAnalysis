# Part02: Developing a Hadoop program Developing a Hadoop program

## Loading files into HDFS (Hadoop Distributed FileSystem).

First of all, we have to go to the directory examples.

     $ cd Part_2

Now, copy the files input.txt from the local filesystem to HDFS using the following commands.

     $ hdfs dfs -put input.txt Part_2/input

**Note:** if you aren't created the directory input in the hadoop distributed filesystem you have to execute the following commands:

     $ hdfs dfs -mkdir /user
     $ hdfs dfs -mkdir /user/hduser
     $ hdfs dfs -mkdir Part_2/input

We can check the files loaded on the distributed file system using.

     $ hdfs dfs -ls Part_2/input
     Found 1 items 
     -rw-r--r--   1 hduser supergroup      15929 2024-02-20 19:28 Part_2/input/input.txt
     
Log out of the directory

      $ cd ..
     
**Note:**This part is already done via bootstrap.sh

## Executing the MapReduce

The following command will execute the MapReduce process using the txt files located in **/user/hduser/Part_2/input** (HDFS), **mapper.py** and **reducer.py**. The result will be written in the distributed file system **/user/hduser/Part_2/output**.

     $ hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -mapper Part_2/mapper.py -reducer Part_2/reducer.py -input /user/hduser/Part_2/input/input.txt -output /user/hduser/Part_2/output -cmdenv N=3

To check the results we can execute.

     $ hdfs dfs -cat Part_2/output/*
