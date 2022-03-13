
file1 = open('1.log', 'r')
file2 = open('out1.csv', 'w')
file2.write("hotend_ist;hotend_soll;bed_ist;bed_soll\n")

Lines = file1.readlines()
# Strips the newline character
for line in Lines:
    if "Recv"  in line.strip():
        if "T:" in line.strip():
            start = line.find("T")
            ende = line.find("@")
            if start is not -1 and ende is not -1:
                #print("{},{}".format(start, ende))
                text = line[start:ende]
                hotend = text[2:text.find("B")]
                hotend_ist = hotend[0:hotend.find("/")].replace(".",",")
                hotend_soll = hotend[hotend.find("/")+1:].replace(".",",")
                bed = text[text.find("B")+2:]
                bed_ist = bed[0:bed.find("/")].replace(".",",")
                bed_soll = bed[bed.find("/"):].replace(".",",")
                print("Hotend: {} Bed {}".format(hotend, bed))
                file2.write("{};{};{};{}\n".format(hotend_ist,hotend_soll,bed_ist,bed_soll))
file1.close()
file2.close()
