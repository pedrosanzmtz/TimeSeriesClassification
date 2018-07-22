def main():
    files = ["DataA90", "DataA91", "DataA92.0", "DataU06.9"]
    last_weeks = [11, 24, 37, 50]
    out_file = open("epidemiologies.csv", "w")
    out_file.write(",".join(map(str, list(range(1, 14))))+ ",class\n")
    for file_name in files:
        with open(file_name + ".csv", "r") as file_reader:
            file_reader.readline()
            man = list()
            woman = list()
            for line in file_reader.readlines():
                line = line.strip("\n").split(",")
                week = int(line[2])
                if week in last_weeks:
                    if len(man) != 13:
                        man = (["NA"] * (13 - len(man)) + man)
                        woman = (["NA"] * (13 - len(woman)) + woman)
                    out_file.write(",".join(man) + "," + file_name + "\n")
                    out_file.write(",".join(woman) + "," + file_name + "\n")
                    man = [line[3]]
                    woman = [line[4]]
                elif week == 53:
                    continue
                else:
                    man.append(line[3])
                    woman.append(line[4])
            if len(man) < 13 and len(man) != 0:
                man = (man + ["NA"] * (13 - len(man)))
                woman = (woman + ["NA"] * (13 - len(woman)))
                out_file.write(",".join(man) + "," + file_name + "\n")
                out_file.write(",".join(woman) + "," + file_name + "\n")
    out_file.close()


if __name__ == '__main__':
    main()
