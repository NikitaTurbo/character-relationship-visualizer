import re
import itertools
import collections

import pymorphy2

import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

morph = pymorphy2.MorphAnalyzer(lang="ru")

def split_into_sentences(text):
    ntext = text.translate(str.maketrans(dict(zip(list('''“`'_-—,():;*"\n«»'''), itertools.repeat(' '))))).strip()
    sentences = re.split(r"\.|\?|!", ntext)
    return sentences

def find_characters(sentences):
    characters_list = []
    words = list(filter(lambda x: len(x) > 2, (' '.join([i[1:].strip() for i in sentences])).split()))
    parts_disable = {"PRON", "ADV", "CONJ", "PRED", "PRCL", "NPRO", "INTJ", "DET", "X"}
    parts_available = {"INF", "VERB", "INFN"}
    for i in range(len(words)):
        try:
            words[i] = morph.parse(words[i])[0].inflect({"nomn"}).normal_form.title() if words[i].istitle() else morph.parse(words[i])[0].inflect({"nomn"}).normal_form
        except: None
    for i in range((len(words) - 1)):
        parts_of_speech_next = set(str(morph.parse(words[i + 1])[0].tag).split(','))
        parts_of_speech_this = set(str(morph.parse(words[i])[0].tag).split(','))
        if words[i].istitle() and len(parts_available & parts_of_speech_next) > 0:
            if len(parts_disable & parts_of_speech_this) == 0:
                characters_list.append(words[i])
    return [i[0] for i in collections.Counter(characters_list).most_common(12)]

def calc_count_of_character_pairs(names, sentences):
    pairs = dict(zip(names, [dict(zip(names, [0 for _ in range(len(names))])) for _ in range(len(names))]))
    for sentence in sentences:
        for i in names:
            for j in names:
                if i != j and i in sentence and j in sentence:
                    pairs[i][j] += 1

    return pairs

def visualize(pairs):
    G = nx.Graph()
    cmap = plt.cm.RdYlGn

    for person, d in pairs.items():
        for name, weight in d.items():
            if weight > 0:
                G.add_edge(person, name, weight=weight * 0.33)

    pos = nx.shell_layout(G)
    weights = list(nx.get_edge_attributes(G, "weight").values())
    labels = nx.draw_networkx_labels(G, pos, font_size=6, font_color="white")
    nodes = nx.draw_networkx_nodes(G, pos, node_color="indigo", node_size=1200)
    edges = nx.draw_networkx_edges(G, pos, edge_color=weights, edge_cmap=cmap, width=weights)

    plt.axis("off")
    plt.show()

