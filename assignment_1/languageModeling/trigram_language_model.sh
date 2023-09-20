#!/bin/bash

# 2.1
awk '{
    for(i=1; i<=NF; i+=2) {
        printf "%s\n",$i
    }
}' eng.sent > eng.tok

# 2.2
awk '{
    prev1 = prev2; prev2 = prev3; prev3 = $0;
    if (NR >= 3) print prev1, prev2, prev3
}' eng.tok > eng.trigrams
sort eng.trigrams | uniq -c | sort -nr > engTri.freq

# 2.3
echo "2.3) Amount of trigrams and distinct trigrams in eng.sent relatively:"
# amount of trigrams
awk '{sum += $1} END {print sum}' engTri.freq
# amount of distinct trigrams
awk '{print $2, $3, $4}' engTri.freq | wc -l

# 2.4
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