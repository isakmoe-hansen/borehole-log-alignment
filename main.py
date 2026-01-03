from pathlib import Path

from process.Loader import LASLoader
from process.Cleaner import dfCleaner
from process.Clustering import KMeans
from process.Alignment import Zshift
from process.Plotter import LogPlotter


def main():
    base_dir = Path(__file__).resolve().parent

    file_A = base_dir / "data" / "CL1_DEN.LAS"
    file_B = base_dir / "data" / "CL1_GR.LAS"

    loaderA = LASLoader(file_A)
    loaderB = LASLoader(file_B)

    dfA = loaderA.raw_data()
    dfB = loaderB.raw_data()

    cleanerA = dfCleaner(dfA)
    cleanerB = dfCleaner(dfB)

    zA, grA = cleanerA.cleaning()
    zB, grB = cleanerB.cleaning()

    clusterA = KMeans(grA, k=5, max_iter=100, tol=0.01)#
    clusterB = KMeans(grB, k=5,max_iter=100, tol=0.01)#

    labelsA, centroidsA = clusterA.clustering()
    labelsB, centroidsB = clusterB.clustering()

    aligner = Zshift(zA, zB, labelsA, labelsB, centroidsA, centroidsB)
    
    dz = aligner.calculate_shift()
    zB_aligned = zB + dz


    plotter = LogPlotter(zA, grA, zB, grB, zB_aligned, dz)
    plotter.plot()


if __name__ == "__main__":
    main()
