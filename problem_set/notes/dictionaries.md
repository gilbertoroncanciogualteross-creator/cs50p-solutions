# Dictionaries

## Counting things I don't know in advance
In October 27, I tried to count the number of times a word is repeated in a text. It didn't work because before I didn't know the words and had to write them on my own, which doesn't work. A dictionary solves it because we have several key-value pairs, and each word could be interpreted as a key.

```python
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
```

## = creates a key, += needs it to exist
count["dog"] fails because += 1 doesn't create a new key. The reason is that += 1 means "take the current value and add one".   

```python
counts = {}
counts["dog"] = 1     # works
counts["cat"] += 1    # KeyError
```

## Other things I learned today
- for x in list gives the item, not the index — unlike JS
- (in) on a dictionary checks keys