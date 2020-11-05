import math
import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from IPython.display import display,HTML
from patsy import dmatrices
import warnings
warnings.filterwarnings("ignore")
get_ipython().run_line_magic('pylab', 'inline')


# ### Load Dataset

# **Train dataset contains 244768 rows × 12 columns**
# 
# * Id - A unique identitier for each job ad.
# * Title - A freetext field supplied to us by the job advertiser as the Title of the job ad.
# * LocationRaw - The freetext location as provided by the job advertiser.
# * LocationNormalized - Adzuna's normalised location from within our own location tree, interpreted by us based on the raw location. This normaliser is not **perfect**.
# * ContractType - full_time or part_time, interpreted by Adzuna from description or a specific additional field we received from the advertiser.
# * ContractTime - permanent or contract, interpreted by Adzuna from description or a specific additional field we received from the advertiser.
# * Company - the name of the employer as supplied to us by the job advertiser.
# * Category - which of 30 standard job categories this ad fits into, inferred in a very messy way based on the source the ad came from. There is a lot of **noise** and **error** in this field.
# * SalaryRaw - the freetext salary field we received in the job advert from the advertiser.
# * SalaryNormalised - the annualised salary interpreted by Adzuna from the raw salary.  Note that this is always a single value based on the midpoint of any range found in the raw salary.  This is the value we are trying to predict.
# * SourceName - the name of the website or advertiser from whom we received the job advert.

data_train = pd.read_csv('Train_rev1.csv')
data_train.head()


# **Validation set** : It is a sample of data used to provide an unbiased evaluation of a model fit on the training dataset.

data_val = pd.read_csv('Valid_rev1.csv')
data_val.head()


# **Test Data dataset contains 122463 rows × 10 columns**.
# It will be used to predict the **SalaryRaw** and **SalaryNormalised**

data_test = pd.read_csv('Test_rev1.csv')
data_test.head()
