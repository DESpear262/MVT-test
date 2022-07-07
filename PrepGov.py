def prep_gov(readfile, writefile, govpartydict):
    """This converts a CPVI into a partisanship measure where higher numbers correspond to the partisanship of the party of the state governor"""
    with open(readfile, "r") as rf:
        with open(writefile, "w") as wf:
            for line in rf:
                key = line[0: 2]
                if line[line.find("),") + 2] == govpartydict.get(key):
                    line = line[0: line.find("),") + 2] + line[(line.find("),") + 4): len(line)]
                    pass
                elif line.startswith("EVEN", line.find("),") + 2):
                    line = line[0: line.find("),") + 2] + "0" + line[(line.find("),") + 6): len(line)]
                else:
                    line = line[0: line.find("),") + 2] + "-" + line[(line.find("),") + 4): len(line)]
                wf.write(line)
    return