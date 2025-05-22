import os
import subprocess


def run_git_command(command, cwd):
    """Запускает команду Git и обрабатывает ошибки."""
    try:
        result = subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Ошибка выполнения Git-команды: {e.stderr.strip()}"


def initialize_git_repo(repo_path):
    """Создаёт локальный Git-репозиторий."""
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)

    os.chdir(repo_path)

    if not os.path.exists(os.path.join(repo_path, ".git")):
        print(run_git_command(["git", "init"], repo_path))
    else:
        print("Репозиторий уже инициализирован.")


def create_readme(repo_path):
    """Запрашивает содержимое README.md и создаёт файл."""
    readme_content = input("Введите содержимое README.md: ")
    readme_path = os.path.join(repo_path, "README.md")

    with open(readme_path, "w") as file:
        file.write(readme_content)

    print("Файл README.md создан.")


def commit_changes(repo_path):
    """Добавляет файл в индекс и создаёт коммит."""
    print(run_git_command(["git", "add", "README.md"], repo_path))
    print(run_git_command(["git", "commit", "-m", "Initial commit"], repo_path))


def show_git_log(repo_path):
    """Выводит историю коммитов."""
    print("\nИстория коммитов:")
    print(run_git_command(["git", "log", "--oneline"], repo_path))


def main():
    """Основной скрипт для выполнения всех шагов."""
    repo_path = input("Введите путь для создания репозитория: ").strip()

    initialize_git_repo(repo_path)
    create_readme(repo_path)
    commit_changes(repo_path)
    show_git_log(repo_path)


if __name__ == "__main__":
    main()
