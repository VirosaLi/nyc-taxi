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

create_hashes.py creates one lookup table for all valid licenses and one for all valid medallion.

## Decrypt Medallion and License

python decrypt_pandas.py

## Todo

### Missing Hashes in the Lookup Table

Some hashes are not in the lookup table. According sources online, there are only three formats of medallion, 5X55,
XX555, and XXX555. And all letters should be in upper case. But in the dataset, some of the medallion are not in standard format.

For example:

D39704A62CF63852EE31C1B66275E75D : NYTX

A00EDFCF1DD459755344024DD6AA1103 : 2c31

9DAAD7BFA53C91605104DD1874EF97E4 : METRO3

F8A0B52B22BB58B3C45E66CEE135C29D : NYT36N

A34DA2BE0F5F3F0A20DA7615B40DEB3D : NYM10X


Also, there are licences that are not 6 or 7 digits long.

For example:

1F33D7CF6693DC6DCC7029B97CC29487 : 7022

816B112C6105B3EBD537828A39AF4818 : 401

4968A8407E09C1B756BD6D43CD2A2E88 : 50893

37BDAD8C38C1AA3DD703C1E8B84EF5FB : 47830



### Clarify Potential Collision in the Hashes

Investigate potential collisions in the dataset and lookup table. It's very unlikely to occur.


## Reference

This repo is forked from Vijay's nyc taxi repo. But everything has been writen. His blog post is very helpful as well.

https://github.com/vijayp/nyc-taxi

https://tech.vijayp.ca/of-taxis-and-rainbows-f6bc289679a1