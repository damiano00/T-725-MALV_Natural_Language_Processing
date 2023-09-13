#!/bin/bash

# In this part, you develop an English trigram language model based on eng.sent 1 by only using the following UNIX
# tools: awk, head, tail, paste, sort, uniq, wc. Note that here we are only interested in word (token) trigrams
# (including punctuations), not part-of-speech trigrams.

# 2.1
# eng.sent is pre-tokenised even though the <token,tag> pairs do not appear on a separate line. However,
# in order to construct the language model you need a file with one token (word) per line without any empty
# lines. Use awk for this purpose. Show the awk command that you use for constructing this file, eng.tok.

awk '{
    for(i=1; i<=NF; i+=2) {
        printf "%s\n",$i
    }
}' eng.sent > eng.tok

# 2.2
# Show the sequence of commands you use to construct a trigram frequency file engTri.freq (from eng.tok)(Containing four columns: frequency, word1, word2, word3),
# sorted in descended order of frequency. Note that you can specify the flag −k1, 1 to sort, for specifying sorting
# only on the first column.

awk '{ prev1 = prev2; prev2 = prev3; prev3 = $0; if (NR >= 3) print prev1, prev2, prev3 }' eng.tok > eng.trigrams
sort eng.trigrams | uniq -c | sort -nr > engTri.freq

# 2.3
