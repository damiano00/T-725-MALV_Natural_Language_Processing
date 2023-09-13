#!/bin/bash

# In this part, you develop an English trigram language model based on eng.sent 1 by only using the following UNIX
# tools: awk, head, tail, paste, sort, uniq, wc. Note that here we are only interested in word (token) trigrams
# (including punctuations), not part-of-speech trigrams.

# 2.1
# eng.sent is pre-tokenized even though the <token,tag> pairs do not appear on a separate line. However,
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

awk '{
    prev1 = prev2; prev2 = prev3; prev3 = $0;
    if (NR >= 3) print prev1, prev2, prev3
}' eng.tok > eng.trigrams
sort eng.trigrams | uniq -c | sort -nr > engTri.freq

# 2.3
# How many trigrams and distinct trigrams exists in eng.sent? Use awk and wc and engTri.freq to figure
# this out (show your commands and the output).

echo "2.3) Amount of trigrams and distinct trigrams in eng.sent relatively:"
# amount of trigrams
awk '{sum += $1} END {print sum}' engTri.freq
# amount of distinct trigrams
awk '{print $2, $3, $4}' engTri.freq | wc -l

# 2.4
# Calculate the  Maximum Likelihood Estimation P(Monday | said on) using the data in engTri.freq.

echo "2.4)  Maximum Likelihood Estimation P(Monday | said on):"
awk '
    BEGIN {
    word1 = "said"; word2 = "on"; word3 = "Monday";
    count_trigram = 0;
    count_said_on = 0;
    result = 0;
    }
    {
        if ($2 == word1 && $3 == word2 && $4 == word3) {
            count_trigram += $1;
        }
        if ($2 == word1 && $3 == word2) {
            count_said_on += $1;
        }
    }
    END {
        result = count_trigram / count_said_on;
        print result;
    } ' engTri.freq