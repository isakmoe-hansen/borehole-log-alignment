import lasio

class LASLoader:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def raw_data(self):
        las = lasio.read(self.filepath)
        df = las.df()
        df.reset_index(inplace=True)

        return df


