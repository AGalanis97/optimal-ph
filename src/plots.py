import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

def main():
    df = pd.read_csv("data/train_set.csv")
    df['sequence_length']  = df['sequence'].str.len()
    df.head()
    pH = df['mean_growth_PH']
    sl = df['sequence_length']
    fig, ax =plt.subplots(2,1)
    sns.displot(pH, ax=ax[0])
    sns.displot(sl, ax=ax[1], bins=30)
    fig.show()
    print("pH range:{}-{}, the median is {}".format(min(pH),max(pH),statistics.median(pH)))
    print("Seq length range:{}-{}, the median is {}".format(min(sl),max(sl),statistics.median(sl)))



if __name__ == '__main__':
    main()
