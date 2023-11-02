from tqdm import tqdm

class Node:
    def __init__(self, s, parent=None):
        self.state = s
        self.cost = 0
        self.parent = parent
        self.successors = []

    def __str__(self):
        return ' '.join(map(str, self.state))

    def __eq__(self, other):
        return self.state == other.state

    def get_path(self, v=None):
        if v is None:
            v = []
        v.insert(0, self)
        if self.parent is not None:
            v = self.parent.get_path(v)
        return v


class EightPuzzleSearch:
    def __init__(self, puzzle_data):
        self.space = puzzle_data
        self.open = []
        self.closed = []

    def h1_cost(self, node):
        cost = 0
        for i in range(len(node.state)):
            if node.state[i] != i:
                cost += 1
        return cost

    def h2_cost(self, node):
        cost = 0
        state = node.state
        for i in range(len(state)):
            v0, v1 = i, state[i]
            if v1 == 0:
                continue
            row0, col0 = v0 // 3, v0 % 3
            row1, col1 = v1 // 3, v1 % 3
            c = abs(row0 - row1) + abs(col0 - col1)
            cost += c
        return cost

    def h_cost(self, node):
        return self.h2_cost(node)

    def get_best_node(self, nodes):
        index = 0
        min_cost = float('inf')
        for i in range(len(nodes)):
            node = nodes[i]
            if node.cost < min_cost:
                min_cost = node.cost
                index = i
        best_node = nodes.pop(index)
        return best_node

    def get_previous_cost(self, node):
        i = self.open.index(node) if node in self.open else -1
        cost = float('inf')
        if i != -1:
            cost = self.open[i].cost
        else:
            i = self.closed.index(node) if node in self.closed else -1
            if i != -1:
                cost = self.closed[i].cost
        return cost

    def print_path(self, path):
        for i in range(len(path)):
            node = path[i]
            for j in range(9):
                if j % 3 == 0:
                    print("\n", end='')
                print(node.state[j], end=' ')
            print()

    def print_grid(self, state):
        for i in range(9):
            if i % 3 == 0:
                print("\n", end='')
            print(state[i], end=' ')
        print("\n")

    def is_solvable(self, state):
        inversion_count = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] > state[j] and state[i] != 0 and state[j] != 0:
                    inversion_count += 1
        return inversion_count % 2 == 0  # Check if the number of inversions is even

    def run(self, depth_limit=1000):
        root = self.space.get_root()
        goal = self.space.get_goal()

        if not self.is_solvable(root.state):
            print("The initial state is not solvable.")
            return

        solution = None
        self.open.append(root)
        depth = 0  # Track the depth of the search
        print("\nRoot:")
        self.print_grid(root.state)
        with tqdm(total=depth_limit) as pbar:  # Initialize tqdm progress bar
            while self.open and depth < depth_limit:
                node = self.get_best_node(self.open)
                path_length = len(node.get_path())
                self.closed.append(node)
                if node == goal:
                    solution = node
                    break
                successors = self.space.get_successors(node)
                for successor in successors:
                    cost = self.h_cost(successor) + path_length + 1
                    previous_cost = self.get_previous_cost(successor)
                    in_closed = successor in self.closed
                    in_open = successor in self.open
                    if not (in_closed or in_open) or cost < previous_cost:
                        if in_closed:
                            self.closed.remove(successor)
                        if not in_open:
                            self.open.append(successor)
                        successor.cost = cost
                        successor.parent = node
                depth += 1
                pbar.update(1)  # Update the tqdm progress bar

        if solution is not None:
            path = solution.get_path()
            print("\nSolution found:\n")
            self.print_path(path)
        else:
            print(f"\nSolution not found within depth limit {depth_limit}.")


class EightPuzzleSpace:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def get_root(self):
        return Node(self.initial)

    def get_goal(self):
        return Node(self.goal)

    def get_successors(self, parent):
        successors = []
        for r in range(3):
            for c in range(3):
                if parent.state[(r * 3) + c] == 0:
                    if r > 0:
                        successors.append(self.transform_state(r - 1, c, r, c, parent))
                    if r < 2:
                        successors.append(self.transform_state(r + 1, c, r, c, parent))
                    if c > 0:
                        successors.append(self.transform_state(r, c - 1, r, c, parent))
                    if c < 2:
                        successors.append(self.transform_state(r, c + 1, r, c, parent))
        parent.successors = successors
        return successors

    def transform_state(self, r0, c0, r1, c1, parent):
        s = parent.state
        new_state = s[:]
        new_state[(r1 * 3) + c1] = s[(r0 * 3) + c0]
        new_state[(r0 * 3) + c0] = 0
        return Node(new_state, parent)


if __name__ == "__main__":
    print("+"*30)
    print("Jawaban Nomor 1")
    puzzle = EightPuzzleSpace(initial=[3, 1, 2, 4, 7, 5, 6, 8, 0], goal=[0, 1, 2, 3, 4, 5, 6, 7, 8])
    EightPuzzleSearch(puzzle).run()
    print("+"*30, "\n\n")



    print("+"*30)
    print("Jawaban Nomor 2")
    puzzle1 = EightPuzzleSpace(initial=[3, 1, 2, 4, 7, 5, 6, 8, 0], goal=[1, 2, 3, 4, 0, 8, 5, 6, 7])
    EightPuzzleSearch(puzzle1).run()
    print("+"*30, "\n\n")



    print("+"*30)
    print("Jawaban Nomor 3")
    puzzle2 = EightPuzzleSpace(initial=[1, 5, 3, 4, 6, 8, 2, 7, 0], goal=[7, 6, 5, 8, 0, 4, 1, 2, 3])
    EightPuzzleSearch(puzzle2).run()
    print("+"*30, "\n\n")



    print("+"*30)
    print("Jawaban Nomor 4")
    puzzle3 = EightPuzzleSpace(initial=[1, 2, 3, 4, 5, 6, 7, 8, 0], goal=[1, 2, 3, 4, 0, 5, 6, 7, 8])
    EightPuzzleSearch(puzzle3).run()
    print("+"*30, "\n\n")



    print("+"*30)
    print("Jawaban Nomor 5")
    print("Nilai Harus berupa integer, bukan string sehingga:")
    data = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
    for i in data:
        print(f'{i} : {data[i]}')
    print("\n")
    puzzle4 = EightPuzzleSpace(initial=[4, 2, 5, 1, 6, 7, 8, 3, 0], goal=[1, 8, 7, 3, 0, 6, 3, 4, 5])
    state = [4, 2, 5, 1, 6, 7, 8, 3, 0]
    print("Root:")
    for i in range(9):
        if i % 3 == 0:
            print("\n", end='')
        print(state[i], end=' ')
    print("\n")
    EightPuzzleSearch(puzzle4).run()
    print("+"*30, "\n\n")
