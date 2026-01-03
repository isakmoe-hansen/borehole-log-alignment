import matplotlib.pyplot as plt


class LogPlotter:
    def __init__(self, zA, grA, zB, grB, zB_aligned, dz):
        self.zA = zA
        self.grA = grA
        self.zB = zB
        self.grB = grB
        self.zB_aligned = zB_aligned
        self.dz = dz

    def plot(self):
        fig, axes = plt.subplots(1, 2, figsize=(12, 8), sharey=True)

        axes[0].plot(self.grA, self.zA, label="A (Reference)")
        axes[0].plot(self.grB, self.zB, label="B (Before)")
        axes[0].set_title("Before alignment")
        axes[0].set_xlabel("GR [API]")
        axes[0].set_ylabel("Depth [m]")
        axes[0].invert_yaxis()
        axes[0].legend()

        axes[1].plot(self.grA, self.zA, label="A (Reference)")
        axes[1].plot(self.grB, self.zB_aligned, label="B (Aligned)")
        axes[1].set_title("After alignment")
        axes[1].set_xlabel("GR [API]")
        axes[1].invert_yaxis()
        axes[1].legend()

        fig.suptitle(f"GR Alignment (Δz = {self.dz:.2f} m)", fontsize=14)

        plt.tight_layout()
        plt.show()
