# hAraCat 🐈
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3677375.svg)](https://doi.org/10.5281/zenodo.3677375)

hAraCat is a Python library for adding diacritics automatically to Medieval Arabic text.

# Install 😻

    pip3 install haracat
    python3 -m haracat.download

# Use 🐱

Diacritics can be added as follows

    from haracat import diacritics_sentence
    diacritics_sentence("الإجاج، مثلثة الأول: الستر.".split(" "))
    >> الْإِجاجُ، مُثَلَّثَةَ الْأَوَّلِ: السِّتْرُ.

First the sentence is tokenized before the diacritics are predicted.

# Credits

Khalid Alnajjar, Mika Hämäläinen, Niko Partanen and Jack Rueter
