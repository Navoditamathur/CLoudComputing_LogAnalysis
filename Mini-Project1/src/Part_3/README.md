# Part03: Developing a Hadoop program to analyze real logs

## Loading files into HDFS (Hadoop Distributed FileSystem).

First of all, we have to go to the directory Part_3.

     $ cd Part_3

Now, copy the files input.txt from the local filesystem to HDFS using the following commands.

     $ hdfs dfs -put access_log Part_3/input

**Note:** if you aren't created the directory input in the hadoop distributed filesystem you have to execute the following commands:

     $ hdfs dfs -mkdir /user
     $ hdfs dfs -mkdir /user/hduser
     $ hdfs dfs -mkdir Part_3/input

We can check the files loaded on the distributed file system using.

     $ hdfs dfs -ls Part_3/input
     Found 1 items 
     -rw-r--r--   1 hduser supergroup 1754380132 2024-02-20 19:29 Part_3/input/access_log
     
Log out of the directory

      $ cd ..
     
**Note:**This part is already done via bootstrap.sh

## Checking and understanding the file system

The files are in Part_3/\*, where * is numbers from 1-10 answering the questions:

Problems:
1. How many hits were made to the website directory “/images/smilies/”(including subdirectories and files)?
2. How many hits were made from the IP: 96.32.128.5?
3. How many HTTP request methods are used in this file? What are they?
4. Which path in the website has been hit most? How many hits were made to the path?
5. Which IP accesses the website most? How many accesses were made by it?
6. How many POST request were made?
7. How many requests received a 404 status code?
8. How much data was requested on 19/Dec/2020?
9. List 3 IPs that access the most, and what is the total data flow size of each IP?
10. How much data(in bytes) was successfully(with status code 200) requested on 16/Jan/2022?

## Executing the MapReduce

The following command will execute the MapReduce process using the txt files located in **/user/hduser/Part_3/input** (HDFS), **Part_3/*/mapper.py** and **Part_3/*/reducer.py**. The result will be written in the distributed file system **/user/hduser/Part_3/output/***.

     $ sudo chmod +x Part_3/*/mapper.py
     $ sudo chmod +x Part_3/*/reducer.py

     $ hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -mapper Part_3/*/mapper.py -reducer Part_3/*/reducer.py -input /user/hduser/Part_3/input/access_log -output /user/hduser/Part_3/output/*

To check the results we can execute.

     $ hdfs dfs -cat Part_3/output/*/*
     
where * refers to 1-10 number, each referring to directories 1-10 containing programs answering the above mentioned problems.

For example: for problem 1,

     $ sudo chmod +x Part_3/1/mapper.py
     $ sudo chmod +x Part_3/1/reducer.py

     $ hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -mapper Part_3/1/mapper.py -reducer Part_3/1/reducer.py -input /user/hduser/Part_3/input/access_log -output /user/hduser/Part_3/output/1

To check the results we can execute.

     $ hdfs dfs -cat Part_3/output/1/*
     
**Note:** Please read report for other problems execution and output