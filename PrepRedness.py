def prep_redness(readfile, writefile):
    """This converts a CPVI into a Republican partisanship measure (higher=redder, negative=blue"""
    with open(readfile, "r") as rf:
        with open(writefile, "w") as wf:
            for line in rf:
                line = line.replace("R+", "")
                line = line.replace("D+", "-")
                line = line.replace("EVEN", "0")
                wf.write(line)
    return
