from datetime import datetime
from arguments_parser.arg_parser import arguments
from driller.commit_driller import collect_commits, write_messages

def main():
  repo_list = [
    'https://github.com/vuejs/vue',
    'https://github.com/facebook/react',
    'https://github.com/tensorflow/tensorflow',
    'https://github.com/twbs/bootstrap'
  ]

  commit_msg = list()
  since, to = None, datetime.now()

  if arguments.since:
    d, m, y = arguments.since.split('/')
    since = datetime(int(y), int(m), int(d))
  
  if arguments.to:
    d, m, y = arguments.to.split('/')
    to = datetime(int(y), int(m), int(d))

  for repo in repo_list:
    commit_msg.append(collect_commits(repo, since, to))
    repo_name = repo.split('/')[-1]
    print(f'{repo_name.capitalize()} terminado!')
  
  write_messages(commit_msg, 'ese_tp_results.csv')
  print('Finalizado')
  

if __name__ == '__main__':
  main()