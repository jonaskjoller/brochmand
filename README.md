This repository is part of the PhD-project "Theology and Piety in Denmark during the 30-years' war. Studies in the theology of Jesper Rasmussen Brochmand (1585-1652)". As part of the project I intend to prepare parts of Brochmand's major theological works in a machine-readable format for use with digital methods. This will be the main repository for the prelimenary editions of the text.
## Content
### Sabbati Sanctificatio - Winter part (1635)
The text from Sabbati Sanctificatio - Winter part has been prepared through the application of a Hand-Written Text Recognition Model using Transkribus. I am deeply grateful for the support of READ-COOP has shown the project by donating credits for the text recognition. I have developed my own model for text recognition using PyLaia and have achieved a theoretical error rate of 0.7 and 0.9 %. The first 120 pages in Transkribus have been through a first proof-reading, while the remaining 685 pages have not been proof-read beyond the initial text-recognition. Additionally, the scan used as a basis for the text-recognition is not of the best quality with several pages having a cut-off point that crosses into the text lines. Do take this into account when reusing the data.

### Tools
A selection of tools designed to work with the base texts in the corpus. Note that these are developed for a particular use case, but can be used in other contexts provided that file names and directories are adjusted accordingly.

*split_ss_winter*: Divides Sabbati Sanctificatio - Winter part into individual Sundays and Feastdays with an epistle- and gospel-sermon for each day including a prayer, and then separates the prayer, epistle-sermon and gospel-sermon out into individual folders.

*stopword_20p-10p.py*: Generates a stopword list based on the 20 percent most frequently and 10 percent least frequently occurring word forms. Requires you to be in the same directory as the main text file.

*stopword_1p-10p.py*: Generates a stopword list based on the 1 percent most frequently and 10 percent least frequently occurring word forms. Requires you to be in the same directory as the main text file.

*stopword_05p-10p.py*: Generates a stopword list based on the 0.5 percent most frequently and 10 percent least frequently occurring word forms. Requires you to be in the same directory as the main text file.

*stopword_05p-5.py*: Generates a stopword list based on the 0.5 percent most frequently word forms and word forms occuring 5 times or less. Requires you to be in the same directory as the main text file.

*stopword_05p-10.py*: Generates a stopword list based on the 0.5 percent most frequently word forms and word forms occuring 10 times or less. Requires you to be in the same directory as the main text file.

#### Generic tools
These tools are designed to be generic and can be used with any texts, provided that the base assumptions of the program are followed.

*generate_stopwords.py*: Generates a stopword list based on two parameters. 1. Word forms occurring in more than x% of individual documents. 2. Word forms occurring y times or less in entire corpus. These parameters are based on the article by David Mimno on computational historiography: David Mimno. 2012. Computational historiography: Data mining in a century of classics journals. J. Comput. Cult. Herit. 5, 1, Article 3 (April 2012), 19 pages. DOI:https://doi.org/10.1145/2160165.2160168. (3:4).
In order to run properly it assumes the existence of a single .txt-file containing your entire corpus, a subfolder containing a .txt-file for each individual document in your corpus, and that you run the program in the same folder which contains the single-file corpus.
