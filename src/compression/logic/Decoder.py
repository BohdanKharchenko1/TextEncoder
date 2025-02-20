class Decoder:
    def __init__(self):
        try:
            self.dictionary = {i: chr(i) for i in range(256)}
            self.next_code = 256
        except Exception as e:
            print(f"Error during Decoder initialization: {str(e)}")

    def decode(self, encoded_data):
        try:
            result = []
            w = ""

            for code in encoded_data:
                if code in self.dictionary:
                    entry = self.dictionary[code]
                elif code == self.next_code:
                    entry = w + w[0] if w else None
                else:
                    raise ValueError("Invalid code in encoded data")

                if entry is not None:
                    result.append(entry)

                    # Update dictionary
                    if w:
                        self.dictionary[self.next_code] = w + entry[0]
                        self.next_code += 1

                    w = entry

            return ''.join(result)
        except Exception as e:
            print(f"Error during decoding: {str(e)}")
            return ""
