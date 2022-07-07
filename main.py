from PrepRedness import prep_redness
from PrepSwinginess import prep_swinginess
from PrepGov import prep_gov
from GovPartyDict import gov_party_dict
from PrepCOVID_CD import *

readfile = "C:\\path\\to\\data\\files\\CPVI working.txt"

redfile = "C:\\path\\to\\data\\files\\CPVI red.txt"

swingfile = "C:\\path\\to\\data\\files\\CPVI swing.txt"

govfile = "C:\\path\\to\\data\\files\\CPVI gov.txt"

govpartydict = "C:\\path\\to\\data\\files\\GovPartyDict.py"

COVIDread = "C:\\path\\to\\data\\files\\CD COVID Raw epi.txt"

COVIDwrite = "C:\\path\\to\\data\\files\\CD COVID Working epi.txt"

prep_redness(readfile, redfile)

prep_swinginess(readfile, swingfile)

prep_gov(readfile, govfile, gov_party_dict)

prep_CD_COVID(COVIDread, COVIDwrite)

#GovFile Source: https://ballotpedia.org/List_of_governors_of_the_American_states
#CPVI Source: https://cookpolitical.com/pvi-map-and-district-list
#CD Epidemiological Data Source: https://e-jghs.org/DOIx.php?id=10.35500/jghs.2020.2.e22
