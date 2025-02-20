class Encoder:
    def __init__(self):
        try:
            self.dictionary = {chr(i): i for i in range(256)}
            self.next_code = 256
        except Exception as e:
            print(f"Error during Encoder initialization: {str(e)}")

    def encode(self, input_text):
        try:
            result = []
            w = input_text[0]

            for char in input_text[1:]:
                wk = w + char
                if wk in self.dictionary:
                    w = wk
                else:
                    result.append(self.dictionary[w])
                    self.dictionary[wk] = self.next_code
                    self.next_code += 1
                    w = char

            result.append(self.dictionary[w])

            return result
        except Exception as e:
            print(f"Error during encoding: {str(e)}")
            return []
