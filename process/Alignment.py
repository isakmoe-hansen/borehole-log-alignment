import numpy as np

class Zshift:
    def __init__(self, zA, zB, labelsA, labelsB, centroidsA, centroidsB):
        self.zA = zA
        self.zB = zB
        self.labelsA = labelsA
        self.labelsB = labelsB
        self.centroidsA = centroidsA
        self.centroidsB = centroidsB

        self.qA = None  # Quantized gamma ray for log A
        self.qB = None  # Quantized gamma ray for log B
        self.dz = None  # The depth shift
        self.zB_shifted = None  # Log B depths after shifting
        
    def quantize_gr(self):
        # For each point, replace its GR value with its cluster center
        self.qA = self.centroidsA[self.labelsA]
        self.qB = self.centroidsB[self.labelsB]
        
        return self.qA, self.qB
    
    def calculate_shift(self):
        if self.qA is None or self.qB is None:
            self.quantize_gr()
        
        shifts = []
        
        for cluster_id in range(len(self.centroidsA)):
            points_in_A = self.labelsA == cluster_id
            if points_in_A.sum() > 0:
                avg_depth_A = np.mean(self.zA[points_in_A])
            else:
                continue
            
            points_in_B = self.labelsB == cluster_id
            if points_in_B.sum() > 0:
                avg_depth_B = np.mean(self.zB[points_in_B])
            else:
                continue
            
            shift = avg_depth_A - avg_depth_B
            shifts.append(shift)
        
        self.dz = np.mean(shifts)
        
        self.zB_shifted = self.zB + self.dz
        
        return self.dz