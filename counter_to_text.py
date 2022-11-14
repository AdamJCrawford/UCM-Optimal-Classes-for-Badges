def make_txt_file(counter):
    sorted_counter_data = sorted(
        zip(counter.keys(), counter.values()), key=lambda x: x[1], reverse=True)
    x_axis = [x[0] for x in sorted_counter_data]
    y_axis = [y[1] for y in sorted_counter_data]

    with open("output.txt", "w") as f:
        for x, y in zip(x_axis, y_axis):
            line = x + ": " + str(y)
            f.write(line)
            f.write("\n")
