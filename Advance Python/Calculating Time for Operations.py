import time

# Sample data structures
list_ds = [1, 2, 3, 4, 5]
tuple_ds = (1, 2, 3, 4, 5)
set_ds = {1, 2, 3, 4, 5}
dict_ds = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# --- Adding an element ---
start = time.time()
list_ds.append(6)
print("List after adding:", list_ds)
print("Time for List add:", time.time() - start)

start = time.time()
# tuple_ds cannot be modified, must recreate
tuple_ds = tuple_ds + (6,)
print("Tuple after adding:", tuple_ds)
print("Time for Tuple add:", time.time() - start)

start = time.time()
set_ds.add(6)
print("Set after adding:", set_ds)
print("Time for Set add:", time.time() - start)

start = time.time()
dict_ds[6] = 'f'
print("Dictionary after adding:", dict_ds)
print("Time for Dict add:", time.time() - start)

print("-" * 60)

# --- Removing an element ---
start = time.time()
list_ds.remove(3)
print("List after remove:", list_ds)
print("Time for List remove:", time.time() - start)

start = time.time()
# Tuples are immutable — cannot remove
print("Tuple cannot remove (immutable)")
print("Time for Tuple remove: Not Applicable")

start = time.time()
set_ds.discard(3)
print("Set after remove:", set_ds)
print("Time for Set remove:", time.time() - start)

start = time.time()
del dict_ds[3]
print("Dictionary after remove:", dict_ds)
print("Time for Dict remove:", time.time() - start)

print("-" * 60)

# --- Accessing elements ---
start = time.time()
print("Access List element:", list_ds[2])
print("Time for List access:", time.time() - start)

start = time.time()
print("Access Tuple element:", tuple_ds[2])
print("Time for Tuple access:", time.time() - start)

start = time.time()
print("Check if 4 in Set:", 4 in set_ds)
print("Time for Set access:", time.time() - start)

start = time.time()
print("Access Dict element:", dict_ds[4])
print("Time for Dict access:", time.time() - start)

print("-" * 60)

# --- Iterating through elements ---
start = time.time()
for i in list_ds:
    pass
print("Time for List iteration:", time.time() - start)

start = time.time()
for i in tuple_ds:
    pass
print("Time for Tuple iteration:", time.time() - start)

start = time.time()
for i in set_ds:
    pass
print("Time for Set iteration:", time.time() - start)

start = time.time()
for k, v in dict_ds.items():
    pass
print("Time for Dict iteration:", time.time() - start)
