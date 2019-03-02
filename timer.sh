export export PYTHONPATH=$PYTHONPATH:~/bandit

PROJECT=~/zulip/zerver

rm -rf ~/bandit/bandit/__pycache__/

time python3 ~/bandit/bandit -q -r $PROJECT
