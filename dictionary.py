import hashlib


class Dictionary:

    # 0(1) compared to Linked Lists which are 0(n)

    def set(self, key, value):
        '''

        :param key:
        :param value:
        :return:
        '''

        self.data[key] = [value]

    def get(self, key):
        '''

        :param key:
        :return:
        '''

        return self.data[key]

    def contains(self, key):
        '''

        :param key:
        :return: bool
        '''

    def get_index(key):
        '''
        
        :return: index
        '''

    def __init__(self):
        self.data = dict()

    def __del__(self, key):
        '''

        :param key:
        :return:
        '''

    def __len__(self):
        '''

        :return:
        '''

    def __repr__(self):
        '''

        :return:
        '''


  #   Hash - maps a string to a number
  #   same string = same number
  #     secure hash function
  #
  # Secure Hash Functions are ireversable
  #





print(hash("Hello"))
print(hash("Hello"))




# print(hash("hello"))