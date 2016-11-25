#!/usr/bin/python

import sys
import re
from collections import defaultdict


def read_counts(lines):
  counts = {}
  sum = 0.0
  for line in lines:
    splitted = re.split('\s+', line)
    count = int(splitted[1])
    char = splitted[2]
    if len(splitted) < 4 or char.isalpha() or char.isdigit():
      continue
    counts[char] = count
    sum += count
  return counts, sum

def make_freqs(counts_sum):
  freqs = defaultdict(lambda: 0.0)
  counts, sum = counts_sum
  for char, count in counts.iteritems():
    freqs[char] = count / sum
  return freqs

def sort_by_freqs(freqs):
  l = []
  for char, freq in freqs.iteritems():
    l.append((char, freq))
  l.sort(key=lambda x: x[1], reverse=True)
  return l

def merge_freqs(all_freqs):
  nb_freqs = len(all_freqs)
  merged = defaultdict(lambda: 0.0)
  for freqs in all_freqs:
    for char, freq in freqs.iteritems():
      merged[char] += freq
  for char, freq in merged.iteritems():
    merged[char] = merged[char] / nb_freqs
  return merged

def print_sorted_freqs(sorted_freqs):
  for f in sorted_freqs:
    print f[0], ' ', f[1]

if __name__ == '__main__':
  all_freqs = []
  for file in sys.argv[1:]:
    freqs = make_freqs(read_counts(open(file).readlines()))
    all_freqs.append(freqs)
  merged = merge_freqs(all_freqs)
  print_sorted_freqs(sort_by_freqs(merged))
