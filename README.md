### *Sentiment-Geometry-with-Embedding-Vectors*

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jalanvatsal/Sentiment-Geometry-with-Embedding-Vectors/blob/main/Sentiment_Geometry_with_Embedding_Vectors.ipynb)

---

## Overview

This project explores the possibility of controlling emotional tone in language by modeling sentiment as a vector direction within the latent embedding space of GPT-based language models. Inspired by Daniel Jurafsky and James H. Martin’s work on lexical and vector semantics, this work investigates two key questions:

> Can emotion be modeled as a navigable axis in embedding space?
> Can we shift a sentence from negativity to positivity through simple coordinate transformations?

Using principal component analysis (PCA), nearest neighbor search, and vector arithmetic, the notebook investigates whether sentiment can be predictably and meaningfully transformed in high-dimensional sentence embeddings.

At its core, this work lies at the intersection of cognitive theory, machine learning, and natural language processing, probing how abstract human emotions are encoded in artificial representations. It aims to bridge intuitive concepts of emotion and meaning with mathematical operations in latent space. By approaching sentiment as a spatial and computational phenomenon, the project offers a small but meaningful step in understanding how large language models represent and adjust emotional tone.

---

## Core Ideas

- **Sentiment Direction Construction:**  
  Compute average embeddings of positive and negative sentences.  
  `sentiment_direction = positive_avg - negative_avg`

- **Vector Arithmetic:**  
  Shift a test sentence like:  
  `"Everything is falling apart."`  
  ➕ sentiment_direction ⟶  
  `"Everything feels like it's falling into place."`

- **Visualization:**  
  2D and 3D PCA plots illustrate sentiment structure in embedding space.  
  Nearest-neighbor searches validate sentiment shifts post-transformation.

- **Goal:**  
  Reveal whether **sentiment** behaves like a **manipulable attribute**—just like gender or tense in word embeddings.

---

## Methodology

The following steps outline the experimental process:

1. **Dataset Preparation & Embedding Generation**  
   A curated dataset of short sentences was labeled as **positive**, **negative**, or **neutral**. Using OpenAI's `text-embedding-3-small`, each sentence was transformed into a high-dimensional vector embedding.

2. **Dimensionality Reduction & Visualization**  
   To visualize the structure of sentiment in embedding space, **Principal Component Analysis (PCA)** was applied, reducing vectors to 2D and 3D. These projections revealed meaningful clustering by sentiment.

3. **Constructing a Sentiment Direction**  
   The average vectors of positive and negative sentences were computed, and their difference defined a **"sentiment direction" vector**:  
   `sentiment_direction = positive_avg - negative_avg`  
   This vector serves as a directional axis from negative to positive sentiment within the latent space.

4. **Shifting Sentences in Embedding Space**  
   A negative sentence vector was shifted along the sentiment direction. This vector arithmetic was designed to simulate a transformation toward more positive sentiment.

5. **Semantic Evaluation via Nearest Neighbors**  
   The shifted vector was compared against each original sentence embedding using **cosine similarity** to identify its closest match. This step assessed whether the sentiment shift produced semantically and emotionally meaningful results with respect to the transformation.

6. **Analysis & Findings**  
   Qualitative analysis showed that the shifted vector mapped closely to a sentence with a clearly more positive tone.

---

## Results Summary

- ✅ Clear PCA clustering between negative, neutral, and positive sentence embeddings
- ✅ Nearest-neighbor similarity confirms sentiment shift post vector transformation
- ✅ Vector shifts result in **semantically similar but emotionally re-tuned** sentence!

*Example:*  
**Input:** `"Everything is falling apart."`  
**Shifted:** `"Everything feels like it's falling into place."`  
Similar meaning, **dramatically different emotional tone**

---

## Reproduce Results

1. **Get OpenAI API Key**  
   Sign up for an account at OpenAI. Generate an API key from your account dashboard. Paste the key into `client = OpenAI(api_key="")` in generate_embeddings.py.

2. **Customize Input Sentences**  
   Add your custom set of sentences with positive, negative, and neutral sentiment into the positive_sentences, negative_sentences, and neutral_sentences lists in generate_embeddings.py.

3. **Replace Path**  
   To save your generated embeddings file locally, paste the path of your desired save location into the filename argument `save_embeddings_dict(all_embeddings, filename="/Users/vatsaljalan/Desktop/Uni/final/Math 118/embeddings.json")` in generate_embeddings.py.

1. **Run Colab**  
   Click on the Colab Badge at the top of this README. Load in your locally saved embeddings file and enjoy!
   (Note: To run the Colab with the default curated set of sentences, download embeddings.json and upload it directly in the Colab notebook)
   
---

## 🛠 Tech Stack

- **OpenAI Embeddings API**
- **Scikit-learn** for PCA
- **NumPy** for Nearest-Neighbour Search
- **Matplotlib / Plotly** for Interactive Visualizations
- **Google Colab** for Reproducible Experimentation
