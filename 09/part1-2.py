class Node:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self

    def set_next(self, node):
        self.next.prev = node
        node.next = self.next
        self.next = node
        node.prev = self
        return node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next

def get_players(player_count, marble_count):
    players = [0 for i in range(player_count)]
    current_player = -1
    node = Node(0)
    for i in range(1, marble_count + 1):
        current_player = (current_player + 1) % player_count

        if (i % 23) == 0:
            node = node.prev.prev.prev.prev.prev.prev.prev
            players[current_player] += i + node.value
            node = node.remove()
        else:
            node = node.next.set_next(Node(i))

    return players

segments = open("input.txt").readlines()[0].split()
player_count, marble_count = int(segments[0]), int(segments[6])

print(max(get_players(player_count, marble_count)))
print(max(get_players(player_count, marble_count * 100)))