This repository is part of the PhD-project "Theology and Piety in Denmark during the 30-years' war. Studies in the theology of Jesper Rasmussen Brochmand (1585-1652)". As part of the project I intend to prepare parts of Brochmand's major theological works in a machine-readable format for use with digital methods. This will be the main repository for the preliminary editions of the text.
## Content
### Sabbati Sanctificatio - Winter part (1635)
The text from Sabbati Sanctificatio - Winter part has been prepared through the application of a Hand-Written Text Recognition Model using Transkribus. I am deeply grateful for the support that [READ COOP](https://readcoop.eu/) has shown the project by granting credits for the text recognition. I have developed my own model for text recognition using PyLaia and have achieved a theoretical error rate of 0.7 and 0.9 %. The first 120 pages in Transkribus have been through a first proof-reading, while the remaining 685 pages have not been proof-read beyond the initial text-recognition. Additionally, the scan used as a basis for the text-recognition is not of the best quality with several pages having a cut-off point that crosses into the text lines. Do take this into account when reusing the data.

### Sabbati Sanctificatio - Summer part (1638)
The text from Sabbati Sanctificatio - Summer part has been prepared through the application of a Hand-Written Text Recognition Model using Transkribus. This version has not yet been proofread. The model used is the same as the winter part.

### Universæ Theologiæ Systema I (1633)
The index from Universæ Theologiæ Systema. The index spans 113 pages and covers articles, chapters, and questions for both volumes of UTS. The text recognition is based on the public model Noscemus GM 5 curated by Stephan Zathammer with a theoretical error rate of 0.48 and 0.64 %.

### Tools
A selection of tools designed to work with the base texts in the corpus. Note that these are developed for a particular use case, but can be used in other contexts provided that file names and directories are adjusted accordingly.

*split_ss_winter*: Divides Sabbati Sanctificatio - Winter part into individual Sundays and Feastdays with an epistle- and gospel-sermon for each day including a prayer, and then separates the prayer, epistle-sermon and gospel-sermon out into individual folders.

*split_ss_summer*: Divides Sabbati Sanctificatio - Summer part into individual Sundays and Feastdays with an epistle- and gospel-sermon for each day including a prayer, and then separates the prayer, epistle-sermon and gospel-sermon out into individual folders. Numbered begins at 30 continued from ss-winter. Exceptions are only encoded until 49.

*stopword_20p-10p.py*: Generates a stopword list based on the 20 percent most frequently and 10 percent least frequently occurring word forms. Requires you to be in the same directory as the main text file.

*stopword_1p-10p.py*: Generates a stopword list based on the 1 percent most frequently and 10 percent least frequently occurring word forms. Requires you to be in the same directory as the main text file.

*stopword_05p-10p.py*: Generates a stopword list based on the 0.5 percent most frequently and 10 percent least frequently occurring word forms. Requires you to be in the same directory as the main text file.

*stopword_05p-5.py*: Generates a stopword list based on the 0.5 percent most frequently word forms and word forms occuring 5 times or less. Requires you to be in the same directory as the main text file.

*stopword_05p-10.py*: Generates a stopword list based on the 0.5 percent most frequently word forms and word forms occuring 10 times or less. Requires you to be in the same directory as the main text file.

*i_you_plt_casc.py*: This tool analyses the text in order to identify sections where the frequency of 1st person singular pronouns is higher than frequency of 2nd person singular and plural pronouns. In order to find more contiguous passages, a predetermined number of sections are strung together when calculating the frequency. Finally a plot shows the distribution across the sections. The code is file-specific, but it is easy to tweak the variables, such as folder, length of sections, number of cumulative sections, and plot-details. Since the language is Danish, there are complications because the 2nd person plural pronoun (I) is identical to the preposition 'in' (i). Thus there is included a file-specific list of stopwords intended to identify when 'i' is used as a pronoun instead of a preposition. The lists can be tweaked to fit the source material.

#### Generic tools
These tools are designed to be generic and can be used with any texts, provided that the base assumptions of the program are followed.

*generate_stopwords.py*: Generates a stopword list based on two parameters. 1. Word forms occurring in more than x% of individual documents. 2. Word forms occurring y times or less in entire corpus. These parameters are built from the principles laid out by David Mimno in his article "Computational historiography: Data mining in a century of classics journals," *Journal on Computing and Cultural Heritage*, Vol. 5, Issue 1, Article 3 (April 2012): 4, https://doi.org/10.1145/2160165.2160168. The program allows tweaking of the parameters.
In order to run properly it assumes the existence of a single .txt-file containing your entire corpus, a subfolder containing a .txt-file for each individual document in your corpus, and that you run the program in the same folder which contains the single-file corpus.
