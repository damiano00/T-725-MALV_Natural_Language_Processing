#!/bin/bash

# 2.1
# eng.sent is pre-tokenised even though the <token,tag> pairs do not appear on a separate line. However,
# in order to construct the language model you need a file with one token (word) per line without any empty
# lines. Use awk for this purpose. Show the awk command that you use for constructing this file, eng.tok.

#TODO: awk command
awk '{
    for (i=1; i<=NF; i+=2) {
        if (i+1 <= NF ) {
            printf "%s\n",$i
        }
    }
}' eng.sent > eng.tok