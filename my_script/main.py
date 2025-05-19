from src import get_args, is_valid_args, get_columns




if __name__ == "__main__":

    # Get the args from the command line
    args = get_args()
    if is_valid_args(args):
        get_columns("table1")
    else:
        print("Arguments are invalid")
        exit(84)
