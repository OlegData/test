"""
This module consist of the object is store information about of folder
"""


class NodeTree:
    """
    This class is created the node of tree and save all folders that create/move/delete user
    and show list of folders
    """

    def __init__(self, value: str = '\\'):
        """
        The method initialize the object. If you create the object NodeTree without init param
            you will create main node
        """
        self.value = value
        self.sub_nodes = set()
        self.right_child = None

    def insert_node(self, value: str, level: str = '\\') -> None:
        if level == self.value:
            node_not_exist = True
            if self.sub_nodes:
                for sub_node in self.sub_nodes:
                    if value == sub_node.value:
                        node_not_exist = False
            if node_not_exist:
                self.sub_nodes.add(NodeTree(value))
                return value
        else:
            for sub_node in self.sub_nodes:
                sub_node.insert_node(value, level)

    def print_nodes(self, count_level: int = 1) -> str:
        """
        The method print_nodes allows to get the list of folders from level of tree.
            :param count_level: default value is 1 to determine level of data
            :return: list of folders ordered by hierarchy
        """
        list_nodes = ' ' * count_level + self.value + '\n'
        if self.sub_nodes:
            for sub_node in self.sub_nodes:
                list_nodes = list_nodes + sub_node.print_nodes(count_level + 1)

        return list_nodes

    def delete_node(self, value: str, level: str = '\\') -> int:
        """
        The method delete node from determined level. The function is looking for
            the value in the node tree
        after try to delete
            Parameters:
                value: default value is 1 to determine level of data
                level: default value is 1 to determine level of data
            Return parameters:
                -1 - you can delete node because you have sub node. First of all you should delete sub node
                1 - the node deleted successfully
                None - node not found"""
        if level == self.value:
            if self.sub_nodes:
                for sub_node in self.sub_nodes:
                    if sub_node.value == value and sub_node.sub_nodes:
                        return -1
                    elif sub_node.value == value and len(sub_node.sub_nodes) == 0:
                        self.sub_nodes.remove(sub_node)
                        return 1
        else:
            for sub_node in self.sub_nodes:
                sub_node.delete_node(value, level)

    def find_node(self, value: str) -> str:
        if value == self.value:
            pass
        else:
            for sub_node in self.sub_nodes:
                sub_node.find_nide(value)

    def move_node(self, value: str, old_level: str, new_level: str = '\\') -> int:
        if old_level == self.value:
            if self.sub_nodes:
                pass
        else:
            for sub_node in self.sub_nodes:
                sub_node.move_node(value, old_level, new_level)
