# Doubly Linked List in Python

This project implements a **Doubly Linked List (DLL)** in Python with the following operations:  
- Insert values (at beginning, end, or specific index)  
- Remove values (from beginning, end, by index, or by value)  
- Change a node’s value at a given index  
- Reverse the list  
- Search for values  
- Get value at a specific index  
- String representation of the list  

---

## 🐍 1. Basic Usage (easiest way)

If you just want to try the list without installing anything, copy **`doubly_linked_list.py`** into the same folder as your project and use:

```python
from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_beginning(5)

print(dll)  # Output: 5 <-> 10 <-> 20
```

---

## 📦 2. Advanced Usage (install as a package)

If you want to use this as a Python package, you first need **Git installed**.  
👉 [Download Git](https://git-scm.com/downloads) if you don’t already have it.

Then install directly from GitHub using pip:

```bash
pip install git+https://github.com/Ahmedhm1/DLL---Doubly-Linked-List-Python.git
```

Now you can import it anywhere:

```python
from dll import DoublyLinkedList

dll = DoublyLinkedList()
dll.insert_at_end(100)
dll.insert_at_end(200)
dll.insert_at_end(300)
print(dll)  # Output: 100 <-> 200 <-> 300
```

---

## 🔎 Example Usage

```python
from dll import DoublyLinkedList

# Create list and insert values
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_beginning(5)
dll.insert_at_index(15, 2)  # Insert 15 at index 2

print(dll)  # 5 <-> 10 <-> 15 <-> 20

# Remove values
dll.remove_start()   # Removes 5
dll.remove_end()     # Removes 20
dll.remove_value(15) # Removes node with value 15

# Change a value
dll.change_value(99, 0)  # Change first element to 99

# Reverse the list
dll.reverse()
print(dll)

# Search and get value
print(dll.search(99))       # Get index of value
print(dll.get_at_index(0))  # Get value at index 0
```

---

## 📂 Project Structure
```
Doubly-Linked-List/
│
├── dll/       # Package source code
│   ├── __init__.py           # Exports DoublyLinkedList
│   └── doubly_linked_list.py # DLL implementation
│
├── test.py                   # Example test file
├── setup.py                  # Package setup script
├── pyproject.toml            # (Optional) modern build file
└── README.md
```

---

## 📖 Source Code
➡️ [View `doubly_linked_list.py`](./dll/doubly_linked_list.py) directly if you just want to read the implementation.
