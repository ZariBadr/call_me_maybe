import argparse
from src.loader import load_func_def
from src.loader import loading_prompts

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Translator"
    )

    parser.add_argument(
        "--input",
        type=str,
        default="data/input/function_calling_tests.json"
    )

    parser.add_argument(
        "--functions_definition",
        type=str,
        default="data/input/function_definitions.json"
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


def main():
    print(">>>>>>>> Starting function and prompts <<<<<<<<<")
    args = parse_arguments()
    # print(args.input)
    # print(args.output)
    print(">>>>>>>> Loading functions and prompts <<<<<<<<<")
    func = load_func_def(args.functions_definition)
    if not func:
        raise RuntimeError(f"There is no function definition.")
    prompts = loading_prompts(args.input)
    if not prompts:
        raise RuntimeError(
            f"prompts file is empty!"
        )

    sys = build_sys_prompts(func)
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)