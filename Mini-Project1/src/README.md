# Cloud Computing Miniproject 1
## By -  Navodita Mathur, Allie Azzarello, Naveena Nagaraju 

Please run open a terminal and run the following  commands

Built image using command.
    $ docker build -t cc_mini_1 .

Run container using command.
    $ docker run -it  -p 9864:9864 -p 9870:9870 -p 8088:8088 cc_mini_1

The file bootstrap.sh contains commands to make input directories and place input files within hdfs.

Open docker desktop and run commands in docker terminal from Part_2/README.md and Part_3/README.md

The hadoop file system can be accessed by going to http://localhost:9870/

To debug -
If the command fails while executing program, delete the respective output directory, and make sure your files have execute permission 
    $ sudo chmod +x <file_path>
    
**Note:** Keep the container running, at no point close the terminal, which can cause the container to terminate. If this happens, rebuild the image and give the command to run the container (This might cause you to delete the container)
