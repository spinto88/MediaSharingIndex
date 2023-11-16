# MediaEchoChambers

Code of the paper "The hidden dimension of information diffusion: A latent space representation of Social Media News Sharing behavior"

- *Data_description.ipynb* provides a brief description of the data and reproduces Figure 1 of the paper.

- *Media_outlets_projection_figure.ipynb* creates the layout of the projection over the media-outlets layer by the BiCM, reproducing Figure 2 of the paper.

- *MediaSharingIndex.ipynb* calculates the MSI of the users and media outlets and show the distribution of these values as Figure 3 of the paper shows. It also reproduces the images of the supplementary material.

- *MediaSharingIndex_and_IdeologicalValence.ipynb* compares the MSI with the ideological valence, reproducing Figure 4 of the paper.

- *MediaSharingIndex_and_SentimentBias.ipynb* compares the MSI and the SentimentBias of the media outlets, reproducing Figure 5 of the paper.

- *MSI_and_IV_per_community.ipynb* shows the distribution of MSI and IV per community of the retweet graph, information shown in Figure 6 of the paper. Community detection was made with *scripts/retweet_network_communities.py*.

- *EchoChambersVisualization.ipynb* reproduces Figure 7 of the paper, taking precomputed averages data by *scripts/echo_chambers_matrix.py* 
