@echo off
cls
cd ..
rasa train --fixed-model-name rnn
rmdir .rasa