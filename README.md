This paper tested the hypothesis that COVID relief spending would conform to the public choice interpretation of the median voter theorem, that more relief money would go to swing districts rather than solidly partisan districts after controlling for actual COVID impacts. The hypothesis was apparently falsified, though this may have been due to a data coding issue rather than an actual result. I ran my final regression as a horse race between the theories that spending was due to copartisanship with the then-current president, Donald Trump; copartisanship with the then-current state governor; and swinginess/nonpartisanship. Of these, a negative correlation between Republican partisanship and COVID spending (meaning more money went to more Democrat-partisan districts) was the only significant result. Data issues which I believe caused this result are discussed below.

NB: The LaTeX and PDF files discussed below have been lost to data corrution. Recovery efforts are ongoing. They will be added to this repository and this note removed if they are successfully recovered.

GovDictPrep.py took in a plain text list of state governors with a given formatting (conforming to the then-current ballotpdia.org list of governors of American States) and returned GovPartyDict.py, a dictionary file with the list formatted as \[two-letter state code\] : \[one-letter party code\]

PrepCOVID_CD.py prepared the epidemiological data from the original formatting to standard congressional district formatting, so the file would properly merge with the partisanship data.

PrepGov.py converted my raw data of standard-formatted Cook Partisanship Voting Index (CPVI) data into regressable data where a higher value denoted a district which was more highly copartisan to the governor of the state the district was contained in, a large negative value denoted a district which was highly partisan in opposition to the state governor, and low-absolute-value numbers denoted swing/nonpartisan districts.

PrepRedness.py converted raw, standard-formatted CPVI data into copartisanship with the then-sitting president, Donald Trump, meaning higher numbers denoted partisan republican districts, large negative numbers denoted partisan Democrat districts, and low-absolute-value numbers denoted swing/nonpartisan districts.

PrepSwinginess.py converted raw, standard formatted CPVI data into a total-partisanship measurement, where high numbers denoted districts which were highly partisan either Republican or Democrat, and low numbers denote swing districts.

StateLAUSToCode.py is a dictionary file which converts state-level Local Area Unemployment Statistics codes to two-digit state codes.

StateNameToCode.py is a public domain dictionary to convert plain-text state names to two-digit codes, pulled from Roger Allen's GitHub with attribution.

Convert_to_Stata.do batch-converted the CSV files I used to preprocess my data in python into Stata data files.

Format.do cleaned up variable names which were distorted by the conversion process.

unemp processing.do did some final cleanup for the unemployment data which would have been difficult to do in python.

merge.do merged my cleaned and prepared datasets into a single file, did a final clean of the data to remove some superfluous variables, then saved it to a final working file.

Finally, process.do ran the horse race regression on my final file and outputted it to a LaTeX table.

This paper used conventional statistical methods to analyse COVID relief spending data, and as such used fairly conventional data visualization methods, mainly relying on a regression output table.

The results of this paper disconfirmed my hypothesis. However, it was only after I performed my final analysis that I realized that funding which had been allocated to the state as a whole were encoded in my data as going to whichever district contained the state capitol. As these are all located in major metropolitan areas, and major metropolitan areas are almost always significantly democrat-partisan, this control ended up swamping the rest of my potential findings. Attempts to find more usefully-coded spending data failed. Therefore, this project did not yield any useful results.
