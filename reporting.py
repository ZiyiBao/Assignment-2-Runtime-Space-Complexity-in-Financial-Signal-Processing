
import matplotlib.pyplot as plt


def plot(results, filename):
    for name, runs in results.items():
        x = [r.n for r in runs]
        y = [r.runtime for r in runs]
        plt.plot(x, y, marker="o", label=name)

    plt.xlabel("Number of ticks")
    plt.ylabel("Runtime (seconds)")
    plt.legend()
    plt.title("Runtime Scaling")
    plt.savefig(filename)
    plt.close()



