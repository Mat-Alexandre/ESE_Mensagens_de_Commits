import csv
from datetime import datetime
from pydriller import Repository

def collect_commits(repo_path: str, since: datetime, to: datetime) -> list:
  """Retorna informações de um determinado repositório.
    Parâmetros
    ----------
    repo_path : str
        Link do repositório
    since : datetime, default=None
        Data de início da coleta das informações.
        Por padrão todos os commits serão coletados.
    to : datetime, default=None
        Data limite da coleta das informações.
        Por padrão todos os commits serão coletados.
  """
  commit_list = list()

  driller_repo = Repository(
    repo_path, 
    since=since, 
    to=to
  )
  
  for commit in driller_repo.traverse_commits():
    commit_list.append({
      'message': commit.msg,
      'msg_len': len(commit.msg),
      'msg_date': commit.author_date.isoformat(),
      'repo': repo_path,
      'author': commit.author.name,
      'commiter': commit.committer.name
    })
    
  return commit_list

def write_messages(commit_list: list, file_name: str = 'out.csv') -> None:
  """Escreve as informações em um arquivo csv especificado.
    Parâmetros
    ----------
    commit_list : list
        Lista de informações sobre os commits
    file_name : str
        Nome do arquivo de saída.
  """
  fieldnames = ['message', 'msg_len', 'msg_date', 'repo', 'author', 'commiter']
  with open(file_name, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames, dialect='unix')
    writer.writeheader()
    for commits_by_repo in commit_list:
      for commits in commits_by_repo:
        writer.writerow(commits)