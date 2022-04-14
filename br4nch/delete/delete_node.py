# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_uids, existing_paint_nodes
from br4nch.utility.utility_handler import InstanceStringError, NotExistingTreeError
from br4nch.utility.utility_positioner import UtilityPositioner


class DeleteNode:
    def __init__(self, tree, node):
        self.trees = tree
        self.nodes = node

        self.validate_arguments()
        self.build_parent()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index] not in list(map(str.lower, existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(map(str.lower, existing_trees)):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(existing_trees):
                self.trees.append(existing_tree)

        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes]

    def build_parent(self):
        for tree in self.trees:
            queue_delete = []

            for parent in UtilityPositioner(tree, self.nodes.copy()):
                child = self.get_nodes(tree, parent, existing_trees[tree][list(existing_trees[tree])[0]])
                queue_delete.append(child)

            for delete_child in queue_delete:
                if delete_child:
                    for parent_node, child_nodes in delete_child.items():
                        existing_uids[tree].remove(str(parent_node[-10:]))
                        existing_paint_nodes[tree].pop(parent_node)

                        self.delete_node_attributes(tree, child_nodes[parent_node])
                        del child_nodes[parent_node]

    def get_nodes(self, tree, parent, child):
        count = 0
        for parent_node, child_nodes in child.items():
            count = count + 1

            if count == int(parent[0]):
                if len(parent) == 1:
                    return {parent_node: child}
                else:
                    if child_nodes:
                        parent.pop(0)
                        return self.get_nodes(tree, parent, child_nodes)

    def delete_node_attributes(self, tree, child):
        for parent_node, child_nodes in child.items():
            if parent_node[-10:] in existing_uids[tree]:
                existing_uids[tree].remove(str(parent_node[-10:]))

            if parent_node in existing_paint_nodes[tree]:
                existing_paint_nodes[tree].pop(parent_node)

            if child_nodes:
                self.delete_node_attributes(tree, child_nodes)