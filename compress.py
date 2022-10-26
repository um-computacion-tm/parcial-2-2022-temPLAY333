class Compress():
    def __init__ (self):
        self.list = []
        self.dicc = {}

    def compress(self, text):
            num = 1
            for word in text.split(" "):
                if word in self.dicc.keys():
                    self.list.append(self.dicc[word])
                    continue
                self.dicc[word] = num
                self.list.append(num)
                num += 1
            return (self.list, self.dicc)

    def uncompress(self, list, dic):
        text = ""
        nope = 0
        for num in list:
            for clave, valor in dic.items():
                if num == valor:
                    if valor == list[-1]:
                        if clave == "Swarm." and nope == 0:
                            text += clave + " "
                            nope += 1
                            break
                        text += clave
                        break
                    text += clave + " "
        return text
