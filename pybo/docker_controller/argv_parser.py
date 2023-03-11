import argparse
def first_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", required = True, type=str)
    parser.add_argument("--model", required=False) 

    parser.add_argument("--cpu", required=True, type = int)
    parser.add_argument("--memory", required=True, type =int)
    parser.add_argument("--gpu", required=True, type =int)

    parser.add_argument("--mode", required=True, type = str)
    parser.add_argument("--tickers", required=True, type=str, help="target ticker group list")
    parser.add_argument("--net", required=True, type = str, help="how to study model")
    parser.add_argument("--backend", required=False, default="torch")
    parser.add_argument("--start_date", required=True, type=str)
    parser.add_argument("--end_date", required=True, type=str)
    parser.add_argument("--lr", default=0.0025, type = float)
    parser.add_argument("--balance", default=10000000, type = int)
    args = parser.parse_args()
    return args