@echo off
cls
cd ..
rasa train --fixed-model-name model-rnn
rmdir .rasa