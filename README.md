# Introduction

Originally found in a coursera course. The 100k dataset can be downloaded via [http://files.grouplens.org/datasets/movielens/ml-100k.zip ](http://files.grouplens.org/datasets/movielens/ml-100k.zip) And it is very suitable to play around using Python with numpy, Pandas, etc.

# Rating standard deviation with different gender

The assignment from that same course. To calculate the standard deviation of the different gender. The way to do that is to read from file and generate DataFrame first. Then calculate the mean rating value of each person. Last of all, calculate the standard deviation value of male and female with the mean value mentioned above. 

The rating value is retrieved from u.data, with each column represents `user id | item id | rating | timestamp `. The gender data is retrieved from u.user, with each column represents `user id | age | gender | occupation | zip code `. In this case, only `user id | rating | gender` is needed for calculation.