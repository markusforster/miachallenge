# COMPOUND NOUNS CHALLENGE
The basic idea for my solution is to split the compound nouns into syllables, create a training set containing all permutations from the syllables together with their labels.
This training set is used to fine-tune a dilibert word model for German language that is used in the encoder and also in the decoder.
The last layer in the decoder is replaced by a linear layer that ouptuts logits in the shape of the labels (7 in our case).
