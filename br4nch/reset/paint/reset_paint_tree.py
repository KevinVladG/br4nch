# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_paint_trees
from br4nch.utility.utility_handler import InstanceStringError, NotExistingTreeError


class ResetPaintTree:
    def __init__(self, tree):
        self.trees = tree

        self.validate_arguments()
        self.reset_paint_tree()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(existing_trees):
                self.trees.append(existing_tree)

    def reset_paint_tree(self):
        for tree in self.trees:
            existing_paint_trees.update({tree: []})
