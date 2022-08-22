import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

    sc = SparkContext(appName="StreamingErrorCount")
    ssc = StreamingContext(sc, 1)
    ssc.checkpoint("file:///tmp/streaming")    
    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    counts = lines.flatMap(lambda line: line.split(" "))\
                  .filter(lambda line:"ERROR" in line)\
                  .map(lambda word: (word, 1))\
                  .reduceByKeyAndWindow(lambda x, y: x + y, lambda x, y: x - y, 30, 10)
                  
    counts.pprint()
    ssc.start()
    ssc.awaitTermination()
