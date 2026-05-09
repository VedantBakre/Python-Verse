import time

# Sample data
list = [1, 2, 3, 4, 5]
tup = (1, 2, 3, 4, 5)
set_ = {1, 2, 3, 4, 5}
dict_ = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# --- Adding elements ---
start = time.time()
list.append(6)
print("List:", list, "Time:", time.time() - start)

start = time.time()
tup = tup + (6,)
print("Tuple:", tup, "Time:", time.time() - start)

start = time.time()
set_.add(6)
print("Set:", set_, "Time:", time.time() - start)

start = time.time()
dict_[6] = 'f'
print("Dict:", dict_, "Time:", time.time() - start)

print("-" * 40)

# --- Removing elements ---
start = time.time()
list.remove(3)
print("List:", list, "Time:", time.time() - start)

print("Tuple cannot remove (immutable)")

start = time.time()
set_.discard(3)
print("Set:", set_, "Time:", time.time() - start)

start = time.time()
del dict_[3]
print("Dict:", dict_, "Time:", time.time() - start)

print("-" * 40)

# --- Accessing / Membership ---
print("List[2]:", list[2])
print("Tuple[2]:", tup[2])
print("4 in Set:", 4 in set_)
print("Dict[4]:", dict_[4])

print("-" * 40)

# --- Iteration time ---
start = time.time()
for i in list:
    pass
print("List iteration:", time.time() - start)

start = time.time()
for i in tup:
    pass
print("Tuple iteration:", time.time() - start)

start = time.time()
for i in set_:
    pass
print("Set iteration:", time.time() - start)

start = time.time()
for i in dict_.items():
    pass
print("Dict iteration:", time.time() - start)
