import os.path
import sys

# internal modules
import const
from nodetree import NodeTree


def do_command(command_name: str, params: tuple, node: NodeTree=None) -> None:
    """
    This function allow us to show list of store directories in the NodeTree object.
    The function did not return any data.

    Parameters:
        command_name: str -  name of command which will executed
        params: tuple - additional parameters for execution of the command

    Option parameters:
        node: NodeTree - you should initialize node before use this function"""
    if command_name == const.C_CREATE:
        command_create(params, node)
    elif command_name == const.C_MOVE:
        command_move(params, node)
    elif command_name == const.C_DELETE:
        command_delete(params, node)
    elif command_name == const.C_LIST:
        command_list(params, node)
    elif command_name == const.C_HELP:
        print(const.HELP)
    else:
        print(const.E_COMMAND)
        print(const.HINT)


def command_create(param: tuple, node: NodeTree = None) -> None:
    """
    This function executes command to create new node in the NodeTree.
    The function did not return any data.

    Parameters:
        param: tuple -  Name of directory in which we begin to show sub directory

    Option parameters:
        node: NodeTree - you should initialize node before use this function """
    if node:
        param1, param2 = param.split('/')
        if not param1:
            raise Exception(const.HELP_CREATE)
        if param1:
            node.insert_node(param2, param1)
        else:
            node.insert_node(param1)


def command_delete(param: tuple, node: NodeTree = None) -> None:
    """
    This function allow us to show list of store directories in the NodeTree object.
    The function did not return any data.

    Parameters:
        param: tuple -  Name of directory in which we begin to show sub directory

    Option parameters:
        node: NodeTree - you should initialize node before use this function"""
    if not param1:
        raise Exception(const.HELP_DELETE)

    if node:
        param1, param2 = param.split('/')

        if param1:
            node.delete_node(param2, param1)
        else:
            node.delete_node(param1)


def command_move(param: tuple, node: NodeTree = None) -> None:
    """
    This function allow us to show list of store directories in the NodeTree object.
    The function did not return any data.
    Parameters:
        param: tuple -  Name of directory in which we begin to show sub directory

    Option parameters:
        node: NodeTree - you should initialize node before use this function"""
    if node:
        if not param:
            raise Exception(const.HELP_MOVE)

        level, value = param.split('/')
        if level:
            node.move_node(value, level)
        else:
            node.move_node(value)


def command_list(param: tuple, node: NodeTree = None) -> None:
    """
    This function allow us to show list of store directories in the NodeTree object.
    The function did not return any data.
    Parameters:
        param: tuple -  Name of directory in which we begin to show sub directory

    Option parameters:
        node: NodeTree - you should initialize node before use this function"""
    if not param:
        raise Exception(const.HELP_LIST)

    if node:
        param1, param2 = param.split('/')
        if value:
            node.move_node(param2, param1)
        else:
            node.move_node(param1)


def main() -> None:
    node_tree = NodeTree(f'\\')
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1], "r") as f:
                for line in f.readline():
                    command, params = line.split(sep=" ")
                    do_command(command, params, node_tree)
        else:
            print(const.E_FILE_NAME)
    else:
        print(const.HINT)
        data = input()
        command, params = data.split(sep=" ")
        while command != const.C_EXIT:
            do_command(command, params, node_tree)
            data = input()
            command, params = data.split(sep=" ")


if __name__ == '__main__':
    main()
