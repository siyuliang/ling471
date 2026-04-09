from collections import Counter
import re
import matplotlib.pyplot as plt

input_file = "ling471/demos/4_09/ulysses.txt"
output_file = "ling471/demos/4_09/output.txt"

# read file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read().lower()

# extract words
words = re.findall(r"[a-z]+", text)

# count frequencies
counts = Counter(words)

# write results
with open(output_file, "w", encoding="utf-8") as f:
    for word, freq in counts.most_common():
        f.write(f"{word} {freq}\n")

# ----- Zipf plot -----

# get frequency values sorted descending
frequencies = [freq for word, freq in counts.most_common()]

# compute ranks
ranks = range(1, len(frequencies) + 1)

# plot
plt.figure(figsize=(8,6))
plt.scatter(ranks, frequencies, s=10)

plt.xscale("linear")
plt.yscale("log")

plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Distribution of Word Frequencies")

plt.show()