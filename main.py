def make_set(m):
    return [[] for _ in range(m)]

def _hash(key, m):
    return sum(ord(c) for c in key) % m

def add(s, key):
    index = _hash(key, len(s))
    bucket = s[index]
    for k in bucket:
        if k == key:
            return False
    bucket.append(key)
    return True

def contains(s, key):
    index = _hash(key, len(s))
    bucket = s[index]
    return key in bucket

def remove(s, key):
    index = _hash(key, len(s))
    bucket = s[index]
    for i, k in enumerate(bucket):
        if k == key:
            del bucket[i]
            return True
    return False

def size(s):
    return sum(len(bucket) for bucket in s)

if __name__ == "__main__":
    s = make_set(5)
    add(s, "a")
    add(s, "b")
    print(contains(s, "a"))
    remove(s, "a")
    print(size(s))