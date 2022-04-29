import matplotlib.pyplot as plt

true_k = 10
model = KMeans(n_clusters=true_k)

model.fit(vectors)

order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()

clusters = model.labels_.tolist()
print("Clusters: {}".format(clusters))


with open ("clustering_post_klasla.txt", "w", encoding = "utf-8") as f:
    for i in range (true_k):
        f.write(f"Cluster {i}")
        f.write("\n")
        for ind in order_centroids[i, :20]:
            f.write(" %s" % terms[ind],)
            f.write("\n")
        f.write("\n")
        f.write("\n")