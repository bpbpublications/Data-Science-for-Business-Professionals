import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 
from string import punctuation
import collections

# To obtain the full width of a cell in a dataframe
pd.set_option('display.max_colwidth', -1)
desc = data_train1.loc[1,'FullDescription']

# Creating a list of words from all the job descriptions in train_df1 data
all_desc = []
for i in range(0,data_train1.shape[0]):
    desc = data_train1.loc[i,'FullDescription']
    desc1 = desc.lower()
    # Removing numbers, *** and www links from the data
    desc2 = re.sub('[0-9]+\S+|\s\d+\s|\w+[0-9]+|\w+[\*]+.*|\s[\*]+\s|www\.[^\s]+','',desc1)
    # Removing punctuation
    for p in punctuation:
        desc2 = desc2.replace(p,'')
    all_desc.append(desc2)


# Creating word tokens for all the descriptions
final_list = []
for desc in all_desc:
    word_list = word_tokenize(desc)
    final_list.extend(word_list)

# 3. Tagging parts of speech
pos_tagged = nltk.pos_tag(final_list)

# 4. Identifying the most common parts of speech
tag_fd = nltk.FreqDist(tag for (word, tag) in pos_tagged)
tag_fd.most_common()[:5]


# Excluding stopwords from the analysis
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english')) 

list_wo_stopwords = []
for w in final_list:
    if w not in stop_words:
        list_wo_stopwords.append(w)
        
# 3. Tagging parts of speech
pos_tagged_wo_sw = nltk.pos_tag(list_wo_stopwords)

# 4. Identifying the most common parts of speech
tag_fd_wo_sw = nltk.FreqDist(tag for (word, tag) in pos_tagged_wo_sw)
tag_fd_wo_sw.most_common()[:5]


p_75 = np.percentile(data_train1['SalaryNormalized'], 75)
data_train1['target'] = data_train1['SalaryNormalized'].apply(lambda x: 1 if x>=p_75 else 0)

costly_cities = ['London','Brighton','Edinburgh','Bristol','Southampton','Portsmouth','Exeter','Cardiff','Manchester',
                 'Birmingham','Leeds','Aberdeen','Glasgow','Newcastle','Sheffield','Liverpool']
costly_cities_lower = [x.lower() for x in costly_cities]

# More robust if lower() is applied
data_train1['location_flag'] = data_train1['LocationNormalized'].apply(lambda x: 1 if x in costly_cities else 0)

# Dropping job description column from the dataset
data_train2 = data_train1.drop(['FullDescription','index','Id','LocationRaw','Title','Company','LocationNormalized','SalaryRaw','SalaryNormalized',
                    'target'],axis=1)
