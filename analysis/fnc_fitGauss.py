from pandas import read_csv
from numpy import float64
from astroML.stats import fit_bivariate_normal

def fit2DnormalDistribution(detector):
    if detector == 1:
        pathName = "./data/hits_det1.csv"
    elif detector == 2:
        pathName = "./data/hits_det2.csv"

    detector1_hits = read_csv(pathName,
                                 names=["x", "y", "z"],
                                 dtype=float64)


    # Hit data from detector
    X = detector1_hits["x"]
    Z = detector1_hits["z"]

    (mu_nr, sigma1_nr,
         sigma2_nr, alpha_nr) = fit_bivariate_normal(X, Z, robust=True)

    Gauss2D_dist = {'Mean': mu_nr, 'Sigma X': sigma1_nr,
                    'Sigma Y': sigma2_nr, 'Alpha': alpha_nr}


    return Gauss2D_dist
