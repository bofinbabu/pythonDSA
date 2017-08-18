class hash_table(object):
    def __init__(self, table_size=5000):
        self.table = {}
        self.size = table_size

    def insert(self, item):
        bucket_index = hash(unicode(item)) % self.size
        if bucket_index in self.table:
            self.table[bucket_index].append(item)
        else:
            self.table[bucket_index] = [item]

    def search(self, key):
        key_bucket_index = hash(unicode(key)) % self.size
        if key_bucket_index in self.table:
            if key in self.table[key_bucket_index]:
                return True
        return False

    def show_table(self):
        for bucket, val in (self.table).iteritems():
            print bucket, val





