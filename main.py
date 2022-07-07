from PrepRedness import prep_redness
from PrepSwinginess import prep_swinginess
from PrepGov import prep_gov
from GovPartyDict import gov_party_dict
from PrepCOVID_CD import *

readfile = "C:\\Users\\s94da\\Desktop\\Data and Do-files for papers and homework\\Papers\\Median Voter COVID\\CPVI working.txt"

redfile = "C:\\Users\\s94da\\Desktop\\Data and Do-files for papers and homework\\Papers\\Median Voter COVID\\CPVI red.txt"

swingfile = "C:\\Users\\s94da\\Desktop\\Data and Do-files for papers and homework\\Papers\\Median Voter COVID\\CPVI swing.txt"

govfile = "C:\\Users\\s94da\\Desktop\\Data and Do-files for papers and homework\\Papers\\Median Voter COVID\\CPVI gov.txt"

govpartydict = "C:\\Users\\s94da\\Desktop\\Data and Do-files for papers and homework\\Papers\\Median Voter COVID\\GovPartyDict.py"

COVIDread = "C:\\Users\\s94da\\Desktop\\Data and Do-files for papers and homework\\Papers\\Median Voter COVID\\CD COVID Raw epi.txt"

COVIDwrite = "C:\\Users\\s94da\\Desktop\\Data and Do-files for papers and homework\\Papers\\Median Voter COVID\\CD COVID Working epi.txt"

#prep_redness(readfile, redfile)

#prep_swinginess(readfile, swingfile)

#prep_gov(readfile, govfile, gov_party_dict)

prep_CD_COVID(COVIDread, COVIDwrite)

#GovFile Source: https://ballotpedia.org/List_of_governors_of_the_American_states
#CPVI Source: https://cookpolitical.com/pvi-map-and-district-list
#CD Epidemiological Data Source: https://e-jghs.org/DOIx.php?id=10.35500/jghs.2020.2.e22