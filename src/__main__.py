import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Translator"
    )

    parser.add_argument(
        "--input",
        type=str,
        default="data/input/funtion_calling_tests.json"
    )

    parser.add_argument(
        "--functions_definition",
        type=str,
        default="data/input/functions_definition.json"
    )

    parser.add_argument(
        "--output",
        type=str,
        default="data/output/functions_results.json"
    )

    parser.add_argument(
        "--model",
        type=str,
        default="Qwen/Qwen3-0.6B"
    )

    return parser.parse_args()

def load_func_def(path):
    pass


def main():
    print("Starting")
    args = parse_arguments()
    # print(args.input)
    # print(args.output)
    print(">>> Loading functions and prompts")
    func = load_func_def()

main()