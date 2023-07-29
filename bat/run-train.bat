@echo off
cls
cd ..
rasa train --debug --fixed-model-name model-rnn
rmdir .rasa