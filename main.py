from Processing.Loader import LASLoader
from Processing.Cleaner import dfCleaner
from Processing.Clustering import KMeans
from Processing.Alignment import Zshift

#DataLoader
lasA = LASLoader("/Users/isakmh/Documents/PythonProjects/AlignBorehole/Data/CL1_DEN.LAS")
lasB = LASLoader("/Users/isakmh/Documents/PythonProjects/AlignBorehole/Data/CL1_GR.LAS")
dfA = lasA.raw_data()
dfB = lasB.raw_data()

#DataCleaner
dfA_clean = dfCleaner(dfA)
dfB_clean = dfCleaner(dfB)
grA, zA = dfA_clean.cleaning()
grB, zB = dfB_clean.cleaning()

#CLustering
clusterA = KMeans(grA, k = 5, max_iter = 100, tol = 10e-6)
clusterB = KMeans(grB, k = 5, max_iter = 100, tol = 10e-6)
labelsA, centroidsA = clusterA.clustering()
labelsB, centroidsB = clusterB.clustering()

#Alignment
align = Zshift(zA, zB, labelsA, labelsB, centroidsA, centroidsB)
prepared_data = align.quantize_gr()




