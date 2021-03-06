def main():
    files = ["DataA90", "DataA91", "DataA92.0", "DataU06.9"]
    last_weeks = [11, 24, 37, 50]
    out_file = open("diseases.csv", "w")
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
                    out_file.write(",".join(man) + ",epidemiology\n")
                    out_file.write(",".join(woman) + ",epidemiology\n")
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
                out_file.write(",".join(man) + ",epidemiology\n")
                out_file.write(",".join(woman) + ",epidemiology\n")
    
    # reading respiratory.csv
    with open("respiratory.csv") as file_reader:
        state = list(list() for i in range(4))
        file_reader.readline()
        for line in file_reader.readlines():
            line = line.strip("\n").split(",")
            week = int(line[2])
            if week in last_weeks:
                if len(state[0]) != 13:
                    if len(state[0]) > 13:
                        for i in range(4):
                            state[i] = state[i][:13-len(state)]
                    for i in range(4):
                        # if len(state[i]) != 13:
                        #     print("si1", len(state[i]), line[0], line[1])
                        #     print(13 - len(state[i]))
                        state[i] = (["NA"] * (13 - len(state[i])) + state[i])
                        # if len(state[i]) != 13:
                        #     print("si2", len(state[i]), line[0], line[1])
                for i in range(4):
                    out_file.write(",".join(state[i]) + ",respiratory" + "\n")
                    state[i] = [line[i+3]]
            elif week == 53:
                continue
            else:
                for i in range(4):
                    state[i].append(line[i+3])
        if len(state[0]) < 13 and len(state[0]) != 0:
            for i in range(4):
                state[i] = (state[i] + ["NA"] * (13 - len(state[i])))
                out_file.write(",".join(state[i]) + ",respiratory\n")
    
    out_file.close()


if __name__ == '__main__':
    main()
