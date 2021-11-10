This repository is part of the PhD-project "Theology and Piety in Denmark during the 30-years' war. Studies in the theology of Jesper Rasmussen Brochmand (1585-1652)". As part of the project I intend to prepare parts of Brochmand's major theological works in a machine-readable format for use with digital methods. This will be the main repository for the prelimenary editions of the text.
## Content
### Sabbati Sanctificatio - Winter part (1635)
The text from Sabbati Sanctificatio - Winter part has been prepared through the application of a Hand-Written Text Recognition Model using Transkribus. I am deeply grateful for the support of READ-COOP has shown the project by donating credits for the text recognition. I have developed my own model for text recognition using PyLaia and have achieved a theoretical error rate of 0.7 and 0.9 %. The first 120 pages in Transkribus have been through a first proof-reading, while the remaining 685 pages have not been proof-read beyond the initial text-recognition. Additionally, the scan used as a basis for the text-recognition is not of the best quality with several pages having a cut-off point that crosses into the text lines. Do take this into account when reusing the data.

### Tools
A selection of tools designed to work with the base texts in the corpus.

*split_ss_winter*: Divides Sabbati Sanctificatio - Winter part into individual Sundays and Feastdays with an epistle- and gospel-sermon for each day including a prayer, and then separates the prayer, epistle-sermon and gospel-sermon out into individual folders.

*stopword_ss_winter_20p-10p.py*: Generates a stopword list based on the 20 percent most frequently and 10 percent least frequently occurring word forms.

*stopword_ss_winter_1p-10p.py*: Generates a stopword list based on the 1 percent most frequently and 10 percent least frequently occurring word forms.
