# Character Relationship Visualizer

<img src="https://img.shields.io/github/languages/top/NikitaTurbo/character-relationship-visualizer?color=red" alt="language" />

A tool for visualizing character relationships extracted from text.

## Features
- Parse text into sentences.
- Identify characters using NLP techniques.
- Count co-occurrences of character pairs within sentences.
- Visualize relationships through network graphs.

## Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/NikitaTurbo/character-relationship-visualizer.git
cd character-relationship-visualizer
pip install -r requirements.txt
```

## Usage Example
Here's a basic example to get you started:

```python
from en import split_into_sentences, find_characters, calc_count_of_character_pairs, visualize

# Sample
text = "Alice ventured into Wonderland. Bob later joined her. Together, Alice and Bob encountered many adventures."
sentences = split_into_sentences(text)
characters = find_characters(sentences)
pairs = calc_count_of_character_pairs(characters, sentences)
visualize(pairs)
```

## Output Examples
<p style="display: inline-block;">
  <img width="500" src="https://github.com/NikitaTurbo/character-relationship-visualizer/blob/main/Samples/alice_in_wonderland_en.png" alt="en">
  <img width="500" src="https://github.com/NikitaTurbo/character-relationship-visualizer/blob/main/Samples/alice_in_wonderland_ru.png" alt="ru">
</p>
