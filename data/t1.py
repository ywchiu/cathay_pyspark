import pandas
df = pandas.read_csv('cyber_breaches.csv', index_col = 0 )
df.to_csv('cyber_breaches.tsv', sep = '\t')
