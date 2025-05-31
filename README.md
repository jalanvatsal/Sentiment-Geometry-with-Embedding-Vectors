### *Sentiment-Geometry-with-Embedding-Vectors*

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jalanvatsal/Sentiment-Geometry-with-Embedding-Vectors/blob/main/Sentiment_Geometry_with_Embedding_Vectors.ipynb)

---

## Overview

This project investigates whether **sentiment can be manipulated through vector arithmetic** in the latent embedding space of GPT-based language models.

> **Can emotion be treated as a direction in embedding space?**  
> **Can a sentence be shifted from negativity to positivity like a coordinate shift?**

Using PCA, nearest neighbor search, and embedding arithmetic, this notebook explores if emotional tone can be predictably adjusted from negativeness to positiveness through math on high-dimensional sentence embeddings.

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
   Add your custom set of sentences with positive, negtaive, and neutral sentiment into the positive_sentences, negative_sentences, and neutral_sentences lists in generate_embeddings.py.

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
