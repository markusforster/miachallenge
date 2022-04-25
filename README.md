# COMPOUND NOUNS CHALLENGE
The basic idea for my solution is to split the compound nouns into syllables, create a training set containing all permutations from the syllables together with their labels.
This training set is used to fine-tune a dilibert word model for German language that is used in the encoder and also in the decoder.
The last layer in the decoder is replaced by a linear layer that ouptuts logits with the shape of the labels (7 in our case).

## Inspect the development
It is recommended to use a virtual environment that comprises jupyter-lab or jupyter-notebook.
In the virtual environment you can install all necessary libraries by:
```bash
pip install -r requirements
```
