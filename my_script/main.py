from src import get_args, is_valid_args, get_data, construct_output


if __name__ == "__main__":

    # Args from the command line
    args = get_args()
    if is_valid_args(args):
        data = get_data(args["t1"], args["t2"])
        output = construct_output(data)
    else:
        print("Arguments are invalid")
        exit(84)
