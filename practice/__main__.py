from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from practice.demo.kernel import *
from practice.initialization.load_data import *
import logging

logger = logging.getLogger(__name__)

def parse_args():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("-p", "--path",  required=True,default="../input/german_credit_data.csv",
                        help='The path of data file. ')
    args = parser.parse_args()
    config = Config().get_config()
    return args

def main(args):
    Data = load_data_file(args.path)
    print("test result is: ")
    kernel_main(Data)
    fit_result(Data)

if __name__ == "__main__":
    main(parse_args())