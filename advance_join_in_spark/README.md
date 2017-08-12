Used the data under https://github.com/rmalik123/sparkHadoop/tree/master/Joining_data ( genchan* and gennum" for this project assignment as well)
input/join2_genchanA.txt
input/join2_genchanB.txt
input/join2_genchanC.txt
input/join2_gennumA.txt
input/join2_gennumB.txt
input/join2_gennumC.txt
Goal of the programming assignment 
find out the total number of viewers across all shows for the channel BAT.

First load and parse the files of shows and viewers

show_views_file = sc.textFile("input/join2_gennum?.txt")
show_views = show_views_file.map(split_show_views)
Check the output of RDD (by copying some elements of an RDD back to the driver:)
show_views_file.take(2)

Similarly
show_channel_file = sc.textFile("input3/join2_genchan?.txt")
show_channel = show_channel_file.map(split_show_channel)


At this point use the join transformation to join the 2 datasets using the show name as the key.

join the datasets in any order.

joined_dataset = show_channel.join(show_views)

find the total viewers by channel, create an RDD with the channel as key and all the viewer counts, whichever is the show.


Apply the function extract_channel_views to to create an RDD with the channel as key and all the viewer counts, whichever is the show.

channel_views = joined_dataset.join(extract_channel_views)

Finally, we need to sum all of the viewers for each channel and copy the results back to the Driver with collect:

channel_views.reduceByKey(sum_channel_views).collect()

