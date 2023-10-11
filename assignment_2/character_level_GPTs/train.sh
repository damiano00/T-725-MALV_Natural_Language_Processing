#!/bin/bash

# eval_iter =  number of training iterations or steps between consecutive evaluations of the model's performance.
#   If eval_iters is set to 10, the model's performance (e.g., accuracy or loss) will be assessed every 10 training iterations.
#   This means that after every 10 updates, the model's current state is evaluated to monitor how well it's learning from the data.
# log_interval = 10 to 100.  if log_interval is set to 10, training statistics and information will be logged every 10 training iterations.
# block_size = 64 to 512, if block_size is set to 64, it means the text is divided into chunks of 64 characters or tokens. These chunks are then processed or analyzed one at a time
# n_layer = 2 to 10
# n_head = 4 to 12, A value of 4 is typical for smaller models, while larger models may use more heads, such as 12.
# n_embd = 64 to 512, A higher embedding size allows the model to learn more detailed representations.
# max_iters = sets the maximum number of training iterations or steps.
# lr_decay_iters = same value as max_iters, determines the frequency at which the learning rate is reduced during training. Learning rate decay is used to help the model converge and improve performance.
# dropout = 0.0 to 0.5, is a regularization technique used to prevent overfitting. It represents the probability of dropping out (setting to zero) a neuron during training.



# Step 1: Run data preparation script
python data/shakespeare_char/prepare.py

# Step 2: Run training script with customizable parameters
# default
python train.py config/train_shakespeare_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0
# 2 - more iterations, one more layer --> too random and unrelated outputs also with temp = 1
python train.py config/train_shakespeare_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=5 --n_head=4 --n_embd=128 --max_iters=3000 --lr_decay_iters=3000 --dropout=0.0
# 3 - more iteration, more layers, more n_embd --> too random and unrelated outputs. With temp =0.2 "Court of Appeals" is repeated in every sentence
python train.py config/train_shakespeare_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=10 --block_size=64 --batch_size=12 --n_layer=7 --n_head=4 --n_embd=256 --max_iters=5000 --lr_decay_iters=5000 --dropout=0.0
# 4 - less evaluate iterations
python train.py config/train_shakespeare_char.py --device=cpu --compile=False --eval_iters=10 --log_interval=10 --block_size=64 --batch_size=12 --n_layer=7 --n_head=4 --n_embd=256 --max_iters=5000 --lr_decay_iters=5000 --dropout=0.0



# Step 3: Run sampling script with customizable parameters
python sample.py --out_dir=out-shakespeare-char --device=cpu
