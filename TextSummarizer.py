import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import networkx as nx
import matplotlib.pyplot as plt
import ssl
import scipy as sp
import tkinter as tk
from tkinter import scrolledtext, Button

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def onislememetni(text):
    cümleler = sent_tokenize(text)
    cümleler = [cümle.lower() for cümle in cümleler]
    
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    onIslenmisCumleler = []
    for cümle in cümleler:
        kelimeler = word_tokenize(cümle)
        kelimeler = [lemmatizer.lemmatize(kelime) for kelime in kelimeler if kelime.casefold() not in stop_words]
        onIslenmisCumleler.append(kelimeler)
    
    return onIslenmisCumleler

def cumleBenzerlikHesaplama(cümle1, cümle2, dökümanlar):
    def tfHesaplama(kelime, document):
        kelimetekrari = document.count(kelime)
        butunKelimeler = len(document)
        return kelimetekrari / butunKelimeler

    def dfHesaplama(kelime, dökümanlar):
        dokumanSayisi = 0
        for doc in dökümanlar:
            if kelime in doc:
                dokumanSayisi += 1
        return len(dökümanlar) / dokumanSayisi

    def idfHesaplama(df):
        from math import log10
        return log10(df)

    def tfIdfBenzerlikHesaplama(cümle1, cümle2, dökümanlar):
        words_sentence1 = set(cümle1)
        words_sentence2 = set(cümle2)
        words_union = words_sentence1.union(words_sentence2)
        tfIdfBenzerligi = 0

        for kelime in words_union:
            tf_cumle1 = tfHesaplama(kelime, cümle1)
            df = dfHesaplama(kelime, dökümanlar)
            idf = idfHesaplama(df)
            tfIdfBenzerligi += tf_cumle1 * idf

        return tfIdfBenzerligi

    benzerlikPuani = tfIdfBenzerlikHesaplama(cümle1, cümle2, dökümanlar)
    return benzerlikPuani

def graphOlustur(cümleler):
    graph = nx.Graph()
    
    for gm in range(len(cümleler)):
        graph.add_node(gm, cümle=" ".join(cümleler[gm]))
        
    for bm in range(len(cümleler)):
        for fen in range(bm+1, len(cümleler)):
            benzerlik = cumleBenzerlikHesaplama(cümleler[bm], cümleler[fen], cümleler)
            graph.add_edge(bm, fen, weight=benzerlik)
    
    return graph

def graphGorselleme(graph):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(12, 8))
    nx.draw(graph, pos, with_labels=True, font_weight='bold')
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.show()

def ozetMetni(graph, cümleler, num_sentences=3):
    cumleDerece = sorted(graph.nodes(data=True), key=lambda x: x[1]['score'], reverse=True)
    
    ozetCumleler = [cümleler[node_id] for node_id, _ in cumleDerece[:num_sentences]]
    
    ozett = " ".join([" ".join(cümle) for cümle in ozetCumleler])
    
    return ozett

def ozet():
    text = text_box.get("1.0", "end-1c")
    cümleler = onislememetni(text)
    graph = graphOlustur(cümleler)
    graphGorselleme(graph)
    scores = nx.pagerank(graph, weight='weight')
    for i, score in scores.items():
        graph.nodes[i]['score'] = score
    ozett = ozetMetni(graph, cümleler)
    ozet_box.delete("1.0", "end")
    ozet_box.insert("1.0", "Metin Özeti:\n\n")
    for i, cümle in enumerate(cümleler):
        benzerlikPuani = cumleBenzerlikHesaplama(cümle, ozett.split(), cümleler)
        ozet_box.insert(tk.END, f"Cümle {i+1} - Benzerlik Puani: {benzerlikPuani}\n")
    ozet_box.insert(tk.END, f"\nMetin Özeti: {ozett}")

window = tk.Tk()
window.title("Yazlab_2.3")

text_label = tk.Label(window, text="Metni girin:")
text_label.pack()
text_box = scrolledtext.ScrolledText(window, height=10)
text_box.pack()

ozet_button = Button(window, text="Özetle", command=ozet)
ozet_button.pack()

ozet_label = tk.Label(window, text="Metin Özeti:")
ozet_label.pack()
ozet_box = scrolledtext.ScrolledText(window, height=10)
ozet_box.pack()

window.mainloop()
