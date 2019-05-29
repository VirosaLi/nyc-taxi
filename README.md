# nyc-taxi

tools to analyse nyc taxi data

## Conda Environment Setup

Download and install miniconda from https://docs.conda.io/en/latest/miniconda.html

Enter following commands in terminal to setup conda python environment

--------------------------
conda update conda

conda create -n nyctaxi python=3.7

conda install pyspark pandas

conda activate nyctaxi

---------------------------

## Generate MD5 Lookup Table

python create_hashes.py

create_hashes.py creates a table that contains the MD5 hashes of all valid medallion and hack_license, It writes 
the table to a file in the working directory.

## Run Spark Job to Decrypt the Data

python decrypt.py

decrypt.py loads the lookup table into memory. Then it set up a Spark client and loads the taxi trip data into Spark.
The result is written to a folder.

I didn't implement a command line tool. Spark settings and other parameters need to be edited in the code.

## Todo

### Missing Hashes in the Lookup Table

Some hashes are not in the lookup table.

### Clarify Potential Collision in the Hashes

Investigate potential collisions in the dataset and lookup table. It's very unlikely to occur.

### Try Pandas instead of Spark

Pandas might work.

### Investigate Cloud Option

Estimate cost of running the Spark job on Cloud.
