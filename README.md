# nyc-taxi

tools to analyse nyc taxi data

## Conda Environment Setup

conda update conda

conda create -n nyctaxi python=3.7

conda install pyspark

conda activate nyctaxi

## Generate MD5 Lookup Table

python create_hashes.py

## Run Spark Job to Decrypt the Data

python decrypt.py

## Todo

### Missing Hashes in the Lookup Table

Some hashes are not in the lookup table.

### Clarify Potential Collision in the Hashes
