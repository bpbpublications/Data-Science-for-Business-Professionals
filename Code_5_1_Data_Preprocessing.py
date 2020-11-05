data_train.info()

data_val.info()

data_test.info()

cachedStopWords = stopwords.words("english") #cache stop words to speed-up removing them.
wordset = set()
text = ' '.join(
    data_train['Title'].replace(r'[^0-9a-zA-Z]+',' ',regex=True)
    .fillna('').str.lower()
)
data_train['Title'].replace(r'[^0-9a-zA-Z]+',' ',regex=True).fillna('').str.lower().str.split().apply(wordset.update)
print(list(wordset)[1:100])
most_common_terms = Counter([w for w in text.split(' ') if w not in cachedStopWords]).most_common(50)

labels, values = zip(*most_common_terms)

indexes = np.arange(len(labels))
width = 0.7

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels, rotation='vertical')
plt.show()


names = data_train.columns.values
uniq_vals = {}
for name in names:
    uniq_vals[name] = data_train.loc[:,name].unique()
    print("Count of %s : %d" %(name,uniq_vals[name].shape[0]))


# Distribution of salaries based on the train data
pylab.rcParams['figure.figsize'] = (20,10)
plt.hist(data_train['SalaryNormalized'], bins='auto')
plt.xlabel('Salaries')
plt.ylabel('Number of postings')
plt.title('Histogram of Salaries')

# Randomly selecting 2500 rows to train the classifier
import random
random.seed(1)
indices = list(data_train.index.values)
random_2500 = random.sample(indices,2500)

# Subsetting the train data based on the random indices
data_train1 = data_train.loc[random_2500].reset_index()

pylab.rcParams['figure.figsize'] = (20,10)
plt.hist(data_train1['SalaryNormalized'], bins='auto')
plt.xlabel('Salaries')
plt.ylabel('Number of postings')
plt.title('Histogram of Salaries')