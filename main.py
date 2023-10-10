
# import onadata package
import onadata as ona
import pandas as pd

# see a list of data sets
ona.list_sets()

# load data into a dataframe
df = ona.karate()

# find out more about a specific data set ('karate' example)
ona.karate().info()
