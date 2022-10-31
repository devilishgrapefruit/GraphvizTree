"""Библиотека для работы с путями в операционной системе."""
import os
from graphviz import Digraph


def get_graph_for_dir(dot, path):
    """Вспомогательная функция построения дерева."""
    for root, dirs, files in os.walk(path):
        list_dirs = os.listdir(root)  # список файлов внутри текущей директории
        # добавляем в граф текущую директорию
        dot.node(root.split('\\')[-1], root.split('\\')[-1])
        for dir0 in list_dirs:
            dot.node(dir0, dir0)  # добавляем в граф вложенную директорию/файл
            dot.edge(root.split('\\')[-1], dir0)  # соединяем


def show_tree(dot):
    """Функция вывода дерева в формате pdf."""
    dot.view()


def get_graph(path):
    """Функция построения дерева."""
    dot = Digraph()
    path = path.replace(' ', '')
    if os.path.exists(path):
        if os.path.isfile(path):  # путь к файлу
            dir_file = path.split('\\')[len(path.split('\\')) - 3]
            if dir_file in {"D:", "C:"}:
                dot.node(path.split('\\')[-1], path.split('\\')[-1])
            else:
                get_graph_for_dir(dot, path[:path.rfind('\\') - 1])
        elif os.path.isdir(path):
            get_graph_for_dir(dot, path)
        show_tree(dot)
        print('Полученное дерево каталогов и файлов:\n' + dot.source)
        return 1
    print('Такого пути не существует!')
    return -1


def main():
    """Функция для ввода пути и возвращающая полученное дерево."""
    path = input('Введите путь: ')
    return get_graph(path)

if __name__ == '__main__':
    main()
