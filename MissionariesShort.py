def bfsFindGoal(initLeft, initRight, boat):
    visited = []
    queue = []
    queue.append([initLeft, initRight, boat, []])

    while queue:
        currentLeft, currentRight, b, operations = queue.pop(0)

        if currentLeft == [0, 0]:  # Check if the current state is the goal state
            return operations

        moves = [[1, 0], [0, 1], [2, 0], [0, 2], [1, 1]]

        for move in moves:
            l = [currentLeft[0] - move[0], currentLeft[1] - move[1]]#l=l-move
            r = [currentRight[0] + move[0], currentRight[1] + move[1]]

            if b:
                l = [currentLeft[0] - move[0], currentLeft[1] - move[1]]#l=l+move
                r = [currentRight[0] + move[0], currentRight[1] + move[1]]
            else:
                l = [currentLeft[0] + move[0], currentLeft[1] + move[1]]
                r = [currentRight[0] - move[0], currentRight[1] - move[1]]

            if (
                0 <= l[0] and 0 <= l[1]
                and 0 <= r[0]  and 0 <= r[1]
                and (l[0] >= l[1] or l[0] == 0)
                and (r[0] >= r[1] or r[0] == 0)
                and ([l,r,b] not in visited)
            ):
                visited.append([l,r,b])
                queue.append([l, r, not b, operations + [(l, r, not b)]])
    return None

if _name_ == "_main_":
    x,y = map(int,input("Enter the capacities: ").split())
    operations = bfsFindGoal([x, y], [0, 0], True)

    if operations is None:
        print("Not possible!")
    else:
        print("The sequence of operations is:")
        for i in operations:
            print(i)