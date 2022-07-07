from StateNameToCode import us_state_abbrev
def prep_CD_COVID(readfile, writefile):
    """This converts the COVID epidemiological data from https://e-jghs.org/DOIx.php?id=10.35500/jghs.2020.2.e22 into standard congressional district format"""
    with open(readfile, "r") as rf:
        with open(writefile, "w") as wf:
            for line in rf:
                statename = line[0: (line.find(","))]
                try:
                    line = us_state_abbrev[statename] + "-" + line[line.find(",")+1: len(line)]
                except KeyError:
                    pass
                else:
                    if line.find(",")==4:
                        line = line[0: 3] + "0" + line[3: len(line)]
                    line = line[0: 5].replace("00", "AK") + line[5: len(line)]
                    wf.write(line)
    return
