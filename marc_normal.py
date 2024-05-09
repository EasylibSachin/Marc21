def parse_directory(directory):
    entries = {}
    entry_length = 12  # Each directory entry is 12 characters long
    num_entries = int(directory[0:5])  # Extract number of directory entries
    print("Number of directory entries:", num_entries)

    for i in range(num_entries):
        start = 24 + i * entry_length
        tag = directory[start:start+3]
        length = int(directory[start+3:start+7])
        position = int(directory[start+7:start+12])
        print("Tag:", tag, "Length:", length, "Position:", position)
        entries[tag] = (length, position)

    return entries

def parse_variable_fields(record, directory):
    fields = {}
    for tag, (length, position) in directory.items():
        data = record[position:position+length]
        fields[tag] = data
    return fields

def marc_to_dict(marc_data):
    leader = marc_data[:24]  # Leader is always the first 24 characters
    directory = parse_directory(marc_data[24:24+12*int(leader[0:5])])
    variable_fields = parse_variable_fields(marc_data, directory)

    print("Leader:", leader)
    print("Directory:", directory)
    print("Fields:", variable_fields)

    return {
        "leader": leader,
        "fields": variable_fields
    }

def main():
    marc_data = "01041cam  2200265 a 4500001002000000003000400020005001700024008004100041010002400082020002500106020004400131040001800175050002400193082001800217100003200235245008700267246003600354250001200390260003700402300002900439500004200468520022000510650003300730650001200763^###89048230#/AC/r91^DLC^19911106082810.9^891101s1990####maua###j######000#0#eng##^##$a###89048230#/AC/r91^##$a0316107514 :$c$12.95^##$a0316107506 (pbk.) :$c$5.95 ($6.95 Can.)^##$aDLC$cDLC$dDLC^00$aGV943.25$b.B74 1990^00$a796.334/2$220^10$aBrenner, Richard J.,$d1941-^10$aMake the team.$pSoccer :$ba heads up guide to super soccer! /$cRichard J. Brenner.^30$aHeads up guide to super soccer.^##$a1st ed.^##$aBoston :$bLittle, Brown,$cc1990.^##$a127 p. :$bill. ;$c19 cm.^##$a\"A Sports illustrated for kids book.\"^##$aInstructions for improving soccer skills. Discusses dribbling, heading, playmaking, defense, conditioning, mental attitude, how to handle problems with coaches, parents, and other players, and the history of soccer.^#0$aSoccer$vJuvenile literature.^#1$aSoccer.^\\"
    result = marc_to_dict(marc_data)
    print("Converted data:")
    print(result)

if __name__ == "__main__":
    main()
