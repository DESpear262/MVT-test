from StateNameToCode import us_state_abbrev

readfile = "C:\\Users\\s94da\\Desktop\\Data and Do-files for papers and homework\\Papers\\Median Voter COVID\\GovFile.txt"
writefile = "C:\\Users\\s94da\\Desktop\\Data and Do-files for papers and homework\\Papers\\Median Voter COVID\\GovPartyDict.py"

#Takes in a list of governors formatted:
#[Governor of (state) 	(Governor's name) 	(Long-form party name) 	(Date elected)]
#Returns dictionary of governors' parties by state formatted ['(two-letter state code)': '(one-letter party code)']
#Removes non-state territories

gov_party_dict = {}

us_state_abbrev.pop("American Samoa")
us_state_abbrev.pop("District of Columbia")
us_state_abbrev.pop("Guam")
us_state_abbrev.pop("Northern Mariana Islands")
us_state_abbrev.pop("Virgin Islands")
us_state_abbrev.pop("Puerto Rico")

with open(readfile, "r") as rf:
    with open(writefile, "w") as wf:
        wf.write("gov_party_dict = ")
        for line in rf:
            line = line.replace("Governor of ", "")
            if "Republican" in line:
                line = line.replace("Republican", "R")
            if "Democrat" in line:
                line = line.replace("Democratic", "D")
            state = ""
            i = 0
            while i < (line.find("\t") - 1):
                state = state + line[i]
                i = i + 1
            if state in us_state_abbrev:
                line = line.replace(state, us_state_abbrev[state])

                res = [ndx for ndx in range(len(line)) if line.startswith("\t", ndx)]

                i = res[0]
                substr=""
                while i <= res[1]:
                    substr = substr + line[i]
                    i = i + 1
                line = line.replace(substr, "")

                res = [ndx for ndx in range(len(line)) if line.startswith("\t", ndx)]

                i = res[0]
                substr=""
                while i < len(line):
                    substr = substr + line[i]
                    i = i + 1
                line = line.replace(" " + substr, "")

                gov_party_dict[line[0: 2]] = line[-1]
            else:
                line = ""
        wf.write(str(gov_party_dict))
