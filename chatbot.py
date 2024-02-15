import argparse

arg_parser = argparse.ArgumentParser(usage='python chatbot.py [-h] [options]')
arg_parser.add_argument('-g', '--gui', help='Open the ChatBot in GUI Mode', required=False, action='store_true')
arg_parser.add_argument('-t', '--train', type=str, help='Train the ChatBot using a different Intents File', default=False, metavar='[intent]')

args = arg_parser.parse_args()


if __name__ == "__main__":
    if args.gui:
        from gui import ChatApplication
        app = ChatApplication()
        app.run()
    
    if args.train:
        from train import trainModel
        trainModel(args.train)