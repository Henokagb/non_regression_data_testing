from src import get_args, is_valid_args, get_data, construct_output


if __name__ == "__main__":

    # Args from the command line
    args = get_args()

    # Required arguments
    params = {
        "table1": args["t1"],
        "table2": args["t2"],
    }
    if args.get("limit") is not None:
        params["limit"] = args["limit"]
    if args.get("pk-cols") is not None:
        params["pk"] = args["pk-cols"]
    if args.get("ignore_cols") is not None:
        params["column_to_ignore"] = args["ignore_cols"].split(",")

    if is_valid_args(args):
        data = get_data(**params)
        output = construct_output(data)
        print(output)
    else:
        print("Arguments are invalid")
        exit(84)
