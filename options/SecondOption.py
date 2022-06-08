class SecondOption:
    def __init__(self, msg):
        self.msg = str("{0:08b}".format(int(msg, 16)))
        if len(self.msg) < 128:
            x = 128 - len(self.msg)
            self.msg = x*"0" +self.msg

    def text_one_line(self):
        file = open("text.txt", "r")
        text_one_line = ""
        for line in file:
            stripped_line = line.rstrip()
            text_one_line = text_one_line + " " + stripped_line

        result = text_one_line[1:]
        return result


    def encrypt(self):
        text = self.text_one_line()
        file_cover = open('cover.html', 'r')
        text_cover = file_cover.readlines()

        f = open("watermark.html", "w")
        for element in text_cover:
            f.write(element)

        new_text = ''
        counter = 0
        for i in range(len(text)):
            if counter == len(self.msg):
                break
            new_text = new_text + text[i]
            if text[i] == " ":
                if self.msg[counter] == "1":
                    new_text = new_text + " "
                    counter = counter + 1
                else:
                    counter = counter + 1

        with open(r"cover.html", 'r') as fp:
            count_lines = len(fp.readlines())

        for i in range(0, count_lines):
            if "<p>Zadanie_2</p>" in text_cover[i]:
                text_cover[i] = "<p>" + new_text + "</p>\n"

        f = open("watermark.html", "w")
        for element in text_cover:
            f.write(element)

        f.write(new_text)
        f.close()

    def ciphr_find(self):
        file_watermark = open("watermark.html", "r")
        lines_watermark = file_watermark.readlines()

        with open(r"watermark.html", 'r') as fp:
            count_lines = len(fp.readlines())

        for i in range(0, count_lines):
            if 'id="zadanie2"' in lines_watermark[i]:
                return int(i + 6)


    def decrypt(self):
        file_watermark = open("watermark.html", "r")
        text_watermark = file_watermark.readlines()
        binary_code = []
        start = self.ciphr_find()

        text = text_watermark[start]
        for i in range(1, len(text)-1):
            if "  " == text[i]+text[i+1]:
                binary_code.append("1")
            elif " " == text[i] and text[i-1] != " ":
                binary_code.append("0")


        result = "".join(binary_code)
        result = hex(int(result, 2))[2:]

        f = open("detect.txt", "w")
        f.write(result)
        f.close()
