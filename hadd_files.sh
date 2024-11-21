#!/bin/bash

cd /eos/user/t/toakhter/HH_bbtautau_Run3/anaTuples/puCorr/Run3_2022/
rm -p test_hadd_files

# for d in /eos/user/t/toakhter/HH_bbtautau_Run3/anaTuples/puCorr/Run3_2022/
# do
#     ( pwd && cd "$d" && pwd && echo $d ) #hadd ../test_hadd_files/{$d}.root ./*.root && cd ..)
# done

#find . -type d -exec bash -c "cd '{}' && pwd && hadd nano_hadd.root *.root" \;
find . -type d -exec bash -c "cd '{}' && pwd && rm nano_hadd.root" \;