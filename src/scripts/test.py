'''
Created on 12 Nov 2018

@author: mate


UMAP tutorial copied from https://umap-learn.readthedocs.io/en/latest/basic_usage.html
'''


import numpy as np
from sklearn.datasets import load_iris, load_digits
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


print("hello umap")

sns.set(style='white', context='notebook', rc={'figure.figsize':(14,10)})

# iris = load_iris()
# print(iris.DESCR)

# iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
# iris_df['species'] = pd.Series(iris.target).map(dict(zip(range(3),iris.target_names)))
# sns.pairplot(iris_df, hue='species');

# plt.show(block = False)  




import umap

# reducer = umap.UMAP()


# embedding = reducer.fit_transform(iris.data)
# print(embedding.shape)
# 
# plt.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target])
# plt.gca().set_aspect('equal', 'datalim')
# plt.title('UMAP projection of the Iris dataset', fontsize=24);
# 
# plt.show()


digits = load_digits()

# fig, ax_array = plt.subplots(20, 20)
# axes = ax_array.flatten()
# for i, ax in enumerate(axes):
#     ax.imshow(digits.images[i], cmap='gray_r')
# plt.setp(axes, xticks=[], yticks=[], frame_on=False)
# plt.tight_layout(h_pad=0.5, w_pad=0.01)


digits_df = pd.DataFrame(digits.data[:,:10])
digits_df['digit'] = pd.Series(digits.target).map(lambda x: 'Digit {}'.format(x))
# sns.pairplot(digits_df, hue='digit', palette='Spectral')
# 
# plt.show()


reducer = umap.UMAP(random_state=42)
reducer.fit(digits.data)

embedding = reducer.transform(digits.data)

# Verify that the result of calling transform is
# idenitical to accessing the embedding_ attribute

assert(np.all(embedding == reducer.embedding_))
embedding.shape

plt.scatter(embedding[:, 0], embedding[:, 1], c=digits.target, cmap='Spectral', s=5)
plt.gca().set_aspect('equal', 'datalim')
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.title('UMAP projection of the Digits dataset', fontsize=24);

plt.show()
