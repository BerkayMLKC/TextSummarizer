# Project Description
This project aims to develop a desktop application using Python that allows users to input an English text, which the program then processes to generate a summary. The project utilizes natural language processing techniques and graphical representation to analyze the text, calculate sentence scores based on TF-IDF values, and display the similarities between sentences in a graph format. Additionally, the application presents the summarized text alongside the individual sentence scores.

# Features

## 1-Text Input and Preprocessing
-Accepts English text input from the user.

-Tokenizes the text into sentences and words.

-Removes stopwords and lemmatizes the words.

## 2-Sentence Similarity Calculation
-Calculates the TF-IDF values for words in each sentence.

-Computes the similarity scores between sentences.

## 3-Graph Construction and Visualization
-Constructs a graph where nodes represent sentences and edges represent similarity scores.

-Visualizes the graph with nodes and edges using NetworkX and Matplotlib.

## 4-Text Summarization
-Ranks sentences using the PageRank algorithm.

-Generates a summary by selecting top-ranked sentences.

## 5-Graphical User Interface (GUI)
-Provides a user-friendly interface using Tkinter.

-Displays the input text, graph visualization, and the summarized text with sentence scores.

# Installation
To run the project, ensure you have the following Python packages installed:

pip install nltk networkx matplotlib scipy tkinter

# Usage

## 1-Launch the Application:
Run the Python script to start the application.
python TextSummarizer.py

## 2-Input Text:
Enter or paste the English text into the text box provided in the application.

## 3-Generate Summary:
Click on the "Özetle" (Summarize) button to process the text.

## 4-View Results:
The application will display a graph of sentence similarities and the summarized text with sentence scores in separate windows.

# Code Explanation

## 1-Text Preprocessing:
-The onislememetni function tokenizes the input text into sentences and words, removes stopwords, and lemmatizes the words.

## 2-Sentence Similarity Calculation:
-The cumleBenzerlikHesaplama function computes the TF-IDF similarity between sentences.

## 3-Graph Construction:
-The graphOlustur function builds a graph based on sentence similarities.

-The graphGorselleme function visualizes this graph.

## 4-Text Summarization:
-The ozetMetni function ranks sentences and selects the top sentences for the summary.

## 5-GUI Components:
-Tkinter is used to create the GUI with text input, a button to trigger summarization, and text boxes to display results.

# Functions

## onislememetni(text)
Preprocesses the input text.

## cumleBenzerlikHesaplama(cümle1, cümle2, dökümanlar)
Calculates the similarity score between two sentences.

## graphOlustur(cümleler)
Constructs a graph from sentences.

## graphGorselleme(graph)
Visualizes the constructed graph.

## ozetMetni(graph, cümleler, num_sentences=3)
Generates a summary from the graph.

## ozet()
Main function to handle text input, processing, and displaying results in the GUI.

# Example

Here is a simple example of how to use the script:

1-Run the script to open the GUI.

2-Enter the text you want to summarize in the provided text box.

3-Click the "Özetle" button.

4-View the summarized text and the graph of sentence similarities.

