import argparse

parser = argparse.ArgumentParser(description='Obtém informações de repositórios do GitHub')
parser.add_argument(
    '-s', 
    '--since', 
    metavar='DATE',
    type=str, 
    help='Data inicial da coleta das informações. Deve estar no formato: dd/mm/aaaa'
)

parser.add_argument(
    '-t', 
    '--to', 
    metavar='DATE',
    type=str, 
    help='Data final da coleta das informações. Deve estar no formato: dd/mm/aaaa'
)

arguments = parser.parse_args()