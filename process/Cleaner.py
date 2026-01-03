import numpy as np

class dfCleaner:
    def __init__(self, df):
        self.df = df

    def cleaning(self):
        df_zgr = self.df[["DEPT", "GAMMA"]]

        df_zgr = df_zgr.sort_values("DEPT")
        df_zgr = df_zgr.set_index("DEPT")
        df_zgr = df_zgr.interpolate(method="index")
        df_zgr = df_zgr.dropna() 
        df_zgr = df_zgr.reset_index()

        gr_arr = np.array(df_zgr["GAMMA"])
        z_arr = np.array(df_zgr["DEPT"])

        return gr_arr, z_arr
    
