# Sentiment-Geometry-with-Embedding-Vectors

### *Exploring Vector Arithmetic for Emotion Transformation using LLM Embeddings*

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/your-repo/blob/main/sentiment_shift_experiment.ipynb)

---

## Overview

This project investigates whether **sentiment can be manipulated through vector arithmetic** in the latent embedding space of GPT-based language models.

We ask:  
> **Can emotion be treated as a direction in embedding space?**  
> **Can a sentence be shifted from negativity to positivity like a coordinate shift?**

Using PCA, nearest neighbor search, and embedding arithmetic, this notebook explores if emotional tone can be predictably adjusted from negativeness to positiveness through math on high-dimensional sentence embeddings.

---

## 🧠 Core Ideas

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

## 📊 Visual Results

- ✅ Clear PCA clustering between negative, neutral, and positive sentence embeddings
- ✅ Nearest-neighbor similarity confirms sentiment shift post vector transformation
- ✅ Vector shifts result in **semantically similar but emotionally re-tuned** sentence!

*Example:*  
**Input:** `"Everything is falling apart."`  
**Shifted:** `"Everything feels like it's falling into place."`  
🧠 Similar meaning, **dramatically different emotional tone**

---

## 🛠 Tech Stack

- **OpenAI Embeddings API**
- **Scikit-learn** for PCA and nearest-neighbor search
- **Matplotlib / Plotly** for interactive visualizations
- **Google Colab** for reproducible, cloud-executed experimentation
