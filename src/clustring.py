from sklearn import metrics
from sklearn.cluster import  MiniBatchKMeans,KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from time import time

def bench_k_means(estimator, name, data, sample_size, labels,cluster_size, applySVD):
    t0 = time()
    if applySVD==1:
        lsa = TruncatedSVD(500)
        data = lsa.fit_transform(data)
        data = Normalizer(copy=False).fit_transform(data)        
    
    val=estimator.fit(data)
    print('% 9s   %.2fs    %i   %.3f   %.3f   %.3f   %.3f   %.3f    %.3f'
          % (name, (time() - t0), estimator.inertia_,
             metrics.homogeneity_score(labels, estimator.labels_),
             metrics.completeness_score(labels, estimator.labels_),
             metrics.v_measure_score(labels, estimator.labels_),
             metrics.adjusted_rand_score(labels, estimator.labels_),
             metrics.adjusted_mutual_info_score(labels,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean',
                                      sample_size=sample_size)))

def kMeanClustring(sampleData,clustersize,samplesize,labels,applyPCA):
    data = sampleData
    n_samples, n_features = data.shape
    n_digits = clustersize 
    print("n_digits: %d, \t n_samples %d, \t n_features %d"  % (n_digits, n_samples, n_features))
    
    
    print(79 * '_')
    print('% 9s' % 'init'
          '    time  inertia    homo   compl  v-meas     ARI AMI  silhouette')
    
    bench_k_means(KMeans(init='k-means++', n_clusters=n_digits, n_init=10),
               name="k-means++", data=data, sample_size=samplesize, labels=labels,cluster_size=clustersize, applySVD=applyPCA)
   
    bench_k_means(KMeans(init='random', n_clusters=n_digits, n_init=10),
               name="random", data=data, sample_size=samplesize, labels=labels,cluster_size=clustersize, applySVD=applyPCA)
    
    if applyPCA==1:
        bench_k_means(KMeans(init='k-means++', n_clusters=n_digits, n_init=10),
               name="k-means++ SVD", data=data, sample_size=samplesize, labels=labels,cluster_size=clustersize, applySVD=applyPCA)
   
        bench_k_means(KMeans(init='random', n_clusters=n_digits, n_init=10),
               name="randomSVD", data=data, sample_size=samplesize, labels=labels,cluster_size=clustersize, applySVD=applyPCA)
   
        
print(79 * '_')



def kMeanMiniBatchClustring(sampleData,clustersize,samplesize,labels,applyPCA):
    data = sampleData
    n_samples, n_features = data.shape
    n_digits = clustersize 
    print("n_digits: %d, \t n_samples %d, \t n_features %d"  % (n_digits, n_samples, n_features))
    
    
    print(79 * '_')
    print('% 9s' % 'init'
          '    time  inertia    homo   compl  v-meas     ARI AMI  silhouette')
    
    bench_k_means(MiniBatchKMeans(init='k-means++', n_clusters=n_digits, n_init=10),
               name="k-means++", data=data, sample_size=samplesize, labels=labels,cluster_size=clustersize, applySVD=applyPCA)
   
    bench_k_means(MiniBatchKMeans(init='random', n_clusters=n_digits, n_init=10),
               name="random", data=data, sample_size=samplesize, labels=labels,cluster_size=clustersize, applySVD=applyPCA)
    
    if applyPCA==1:
        bench_k_means(MiniBatchKMeans(init='k-means++', n_clusters=n_digits, n_init=10),
               name="k-means++ SVD", data=data, sample_size=samplesize, labels=labels,cluster_size=clustersize, applySVD=applyPCA)
   
        bench_k_means(MiniBatchKMeans(init='random', n_clusters=n_digits, n_init=10),
               name="randomSVD", data=data, sample_size=samplesize, labels=labels,cluster_size=clustersize, applySVD=applyPCA)
   
        
print(79 * '_')

