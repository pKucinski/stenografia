class FourthOption:
    def __init__(self, msg):
        self.msg = str("{0:08b}".format(int(msg, 16)))


    def encrypt(self):
        file = open("text.txt", "r")
        text_lines = file.readlines()
        for i in range(0, len(self.msg)):
            if self.msg[i] == "1":
                text_lines[i] = '<div>' + text_lines[i][:-1]+' </div>\n'
            elif self.msg[i] == "0":
                text_lines[i] = '<span>' + text_lines[i][:-1] + '</span>\n'

        file_cover = open('cover.html', 'r')
        text_cover = file_cover.readlines()

        f = open("watermark.html", "w")

        with open(r"cover.html", 'r') as fp:
            count_lines = len(fp.readlines())

        for i in range(0, count_lines):
            if "<p>Zadanie_4</p>" in text_cover[i]:
                text_cover[i] = ''.join(text_lines)

        for element in text_cover:
            f.write(element)
        f.close()
        file_cover.close()
        fp.close()

    def ciphr_find(self):
        file_watermark = open("watermark.html", "r")
        lines_watermark = file_watermark.readlines()

        with open(r"watermark.html", 'r') as fp:
            count_lines = len(fp.readlines())

        for i in range(0, count_lines):
            if 'id="zadanie4"' in lines_watermark[i]:
                return int(i + 6)


    def decrypt(self):
        file_watermark = open("watermark.html", "r")
        lines_watermark = file_watermark.readlines()
        binary_code = []
        start = self.ciphr_find()

        for i in range(start, start+127):
            if "<div>" in lines_watermark[i]:
                binary_code.append("1")
            elif "<span>" in lines_watermark[i]:
                binary_code.append("0")
        result = "".join(binary_code)

        result = hex(int(result, 2))[2:]

        f = open("detect.txt", "w")
        f.write(result)
        f.close()
