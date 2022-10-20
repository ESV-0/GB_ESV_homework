"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
""" вариант решения через ООП """

from collections import Counter, deque

class HuffmanCoding:
    def __init__(self, r=None, l=None):
        self.right = r
        self.left = l
        self.text_prob = {}
        self.text = ''

    def make_encoding_dict(self, text):
        """ create encoding dictionary """
        self.text = text
        self.text_prob = Counter(text)
        prob = deque(sorted(self.text_prob.items(), key=lambda el: el[1]))
        nodes = []

        while len(prob) > 1:
            create_node = HuffmanCoding(prob[0][0], prob[1][0])
            new_node_val = prob[0][1] + prob[1][1]
            prob.popleft()
            prob.popleft()

            for i in range(0, len(prob)):
                if prob[i][1] >= new_node_val:
                    prob.insert(i, (create_node, new_node_val))
                    break
            else:
                if len(prob) > 0 and prob[0][1] >= new_node_val:
                    prob.appendleft((create_node, new_node_val))
                else:
                    prob.append((create_node, new_node_val))

        self.left = prob[0][0].left
        self.right = prob[0][0].right
        return self

    def show_dict(self, huff_dict={}, code=''):
        """ the coding dictionary """
        if isinstance(self.left, HuffmanCoding):
            self.left.show_dict(huff_dict, code + '0')
        else:
            huff_dict[self.left] = code + '0'
        if isinstance(self.right, HuffmanCoding):
            self.right.show_dict(huff_dict, code + '1')
        else:
            huff_dict[self.right] = code + '1'
        return huff_dict

    def show_probs(self):
        """ frequiencies"""
        return sorted(self.text_prob.items(), key=lambda el: el[1])

    def output_encoded(self):
        """ obtain the encrypted text """
        return ''.join([self.show_dict()[c] for c in self.text if c in self.show_dict()])

    @property
    def result_analysis(self):
        before_compression = len(self.text) * 8
        after_compression = 0
        for symbol in self.show_dict().keys():
            count = self.text.count(symbol)
            after_compression += count * len(self.show_dict()[symbol])
        return f"Расход памяти до сжатия: {before_compression} бит\n" \
               f"Расход памяти после сжатия: {after_compression} бит"

h = HuffmanCoding()
h.make_encoding_dict('beep boop beer!')

print(f'Частотный анализ: {h.show_probs()}')
print(f'Словарь кодировок: {h.show_dict()}')
print(f'Закодированный текст: {h.output_encoded()}')
print(h.result_analysis)

"""
Частотный анализ: [('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)]
Словарь кодировок: {'e': '00', 'p': '010', '!': '0110', 'r': '0111', 'o': '100', ' ': '101', 'b': '11'}
Закодированный текст: 1100000101011110010001010111000001110110
Расход памяти до сжатия: 120 бит
Расход памяти после сжатия: 40 бит
"""
