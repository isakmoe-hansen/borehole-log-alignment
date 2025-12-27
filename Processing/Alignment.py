
class Zshift:
    def __init__(self, zA, zB, labelsA, labelsB, centroidsA, centroidsB):
        self.zA = zA
        self.zB = zB
        self.labelsA = labelsA
        self.labelsB = labelsB
        self.centroidsA = centroidsA
        self.centroidsB = centroidsB

        self.qA = None
        self.qB = None

    def quantize_gr(self):
        self.qA = self.centroidsA[self.labelsA]
        self.qB = self.centroidsB[self.labelsB]

        print(self.qA)
        print(self.qB)
        return self.qA, self.qB

