import json
import re
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# CONFIGURATION
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent / "results" / "raw"
OUTPUT_DIR = BASE_DIR.parent / "figures"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SLICES = ["embb", "urllc", "mmtc"]

LABELS = ["eMBB", "URLLC", "mMTC"]

COLORS = ["#4472C4", "#ED7D31", "#70AD47"]

RUNS = 5

# ==========================================
# 1. READ LATENCY RESULTS
# ==========================================

def read_latency(slice_name):

    values = []

    for run in range(1, RUNS + 1):

        file_path = (
            BASE_DIR
            / "latency"
            / slice_name
            / f"{slice_name}_run_{run}.txt"
        )

        if not file_path.exists():
            raise FileNotFoundError(file_path)

        text = file_path.read_text()

        # Example:
        # rtt min/avg/max/mdev = 8.0/20.5/40.0/5.2 ms

        match = re.search(
            r"(?:rtt|round-trip)\s+min/avg/max/(?:mdev|stddev)"
            r"\s*=\s*"
            r"[\d.]+/([\d.]+)/[\d.]+/[\d.]+",
            text
        )

        if not match:
            raise ValueError(
                f"Could not extract RTT from {file_path}"
            )

        values.append(float(match.group(1)))

    return np.array(values)


# ==========================================
# 2. READ TCP THROUGHPUT RESULTS
# ==========================================

def read_throughput(slice_name):

    values = []

    for run in range(1, RUNS + 1):

        file_path = (
            BASE_DIR
            / "throughput"
            / slice_name
            / f"{slice_name}_run_{run}.json"
        )

        if not file_path.exists():
            raise FileNotFoundError(file_path)

        with open(file_path) as file:
            data = json.load(file)

        # TCP sender throughput
        bps = data["end"]["sum_sent"]["bits_per_second"]

        mbps = bps / 1_000_000

        values.append(mbps)

    return np.array(values)


# ==========================================
# 3. READ UDP JITTER RESULTS
# ==========================================

def read_jitter(slice_name):

    values = []

    for run in range(1, RUNS + 1):

        file_path = (
            BASE_DIR
            / "jitter"
            / slice_name
            / f"{slice_name}_run_{run}.json"
        )

        if not file_path.exists():
            raise FileNotFoundError(file_path)

        with open(file_path) as file:
            data = json.load(file)

        # UDP receiver jitter
        jitter = data["end"]["sum"]["jitter_ms"]

        values.append(jitter)

    return np.array(values)


# ==========================================
# 4. GENERATE COMPARISON GRAPH
# ==========================================

def generate_graph(data, ylabel, title, filename):

    means = [
        np.mean(values)
        for values in data
    ]

    stds = [
        np.std(values, ddof=1)
        for values in data
    ]

    fig, ax = plt.subplots(figsize=(7, 4.5))

    x = np.arange(len(SLICES))

    bars = ax.bar(
        x,
        means,
        yerr=stds,
        capsize=6,
        color=COLORS,
        edgecolor="black",
        linewidth=0.7,
        width=0.6,
        error_kw={"elinewidth": 1.2}
    )

    ax.set_xticks(x)
    ax.set_xticklabels(LABELS, fontsize=11)

    ax.set_ylabel(ylabel, fontsize=11)

    ax.set_title(title, fontsize=12)

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.3
    )

    ax.set_axisbelow(True)

    ax.set_ylim(
        0,
        max(
            mean + std
            for mean, std in zip(means, stds)
        ) * 1.25
    )

    for bar, mean in zip(bars, means):

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(means) * 0.02,
            f"{mean:.2f}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    png_path = OUTPUT_DIR / f"{filename}.png"
    pdf_path = OUTPUT_DIR / f"{filename}.pdf"

    plt.savefig(png_path, dpi=300, bbox_inches="tight")
    plt.savefig(pdf_path, bbox_inches="tight")

    plt.close()

    print(f"Saved: {png_path}")
    print(f"Saved: {pdf_path}")

    return means, stds


# ==========================================
# 5. PROCESS ALL RESULTS
# ==========================================

def process_metric(
    reader,
    ylabel,
    title,
    filename
):

    data = [
        reader(slice_name)
        for slice_name in SLICES
    ]

    means, stds = generate_graph(
        data,
        ylabel,
        title,
        filename
    )

    print(f"\n{title}")
    print("-" * 55)

    for label, mean, std in zip(
        LABELS,
        means,
        stds
    ):

        print(
            f"{label:8s}: "
            f"Mean = {mean:.3f}, "
            f"SD = {std:.3f}"
        )


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    print("\nGenerating experimental figures...\n")

    process_metric(
        read_latency,
        "Mean RTT (ms)",
        "Latency Comparison Across S-NSSAI Configurations",
        "latency_comparison"
    )

    process_metric(
        read_throughput,
        "Mean TCP Sender Throughput (Mbps)",
        "TCP Throughput Comparison Across S-NSSAI Configurations",
        "throughput_comparison"
    )

    process_metric(
        read_jitter,
        "Mean UDP Receiver Jitter (ms)",
        "UDP Jitter Comparison Across S-NSSAI Configurations",
        "jitter_comparison"
    )

    print("\nAll figures generated successfully!")
    print(f"Output directory: {OUTPUT_DIR}")
