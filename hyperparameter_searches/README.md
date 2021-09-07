## hyperparameter_searches

This folder contains two subdirectories that together contain the full results from most of my scikit-learn hyperparameter grid and randomized searches. In total, I ran 14 hyperparameter searches to find the optimal hyperparameters for my models; these 14 are summarized (with information on the accuracy of the optimal hyperparameter combination for each) in the slide [here](https://docs.google.com/presentation/d/1-4lD1JnZ_y5GpXJUkj3m67tK97MZ3NX92SAqbPB1eN4/edit?usp=sharing). The three runs in the "1st W&B (no CV)" row were done using the Weights & Biases (W&B) _sweep_ functionality for searching over hyperparameters, which does not involve cross-validation. Information on the different models trained with different sets of hyperparameters is recorded in W&B [here](https://wandb.ai/parsellsx/tess/sweeps) under the names test-sweep-3 (this is the original support vector classifier sweep), forest-sweep-1 (first random forest sweep), and kneigh-sweep-1 (first k-nearest-neighbors sweep). The other sweeps were tests I ran earlier that aren't relevant.