class ThirdOption:
    def __init__(self, msg):
        self.msg = msg


    def text_one_line(self):
        file = open("text.txt", "r")
        text_one_line = ""
        for line in file:
            stripped_line = line.rstrip()
            text_one_line = text_one_line + " " + stripped_line

        result = text_one_line[1:]
        return result

    def cut_msg(self):
        cutted_msg = [self.msg[i:i + 6] for i in range(0, len(self.msg), 6)]
        return cutted_msg


    def encrypt(self):
        text = self.text_one_line()
        cutted_msg = self.cut_msg()

        file_cover = open('cover.html', 'r')
        text_cover = file_cover.readlines()
        f = open("watermark.html", "w")
        for element in text_cover:
            f.write(element)

        new_text = ''
        for i in range(len(cutted_msg)):
            new_text = new_text + '.zadanie-3 h' + str(i+1) + '{ \n color:#' + cutted_msg[i] + ';\n } \n'

        for i in range(len(cutted_msg)):
            if "CSS code" in text_cover[i]:
                text_cover[i] = new_text


        f = open("watermark.html", "w")
        for element in text_cover:
            f.write(element)

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
        hex_code = []
        start = self.ciphr_find()

        with open(r"cover.html", 'r') as fp:
            count_lines = len(fp.readlines())
        file_watermark = open("watermark.html", "r")

        lines_watermark = file_watermark.readlines()


        for i in range(0, count_lines):
            if "color:#" in lines_watermark[i]:
                hex_code.append(lines_watermark[i][lines_watermark[i].index("#")+1:lines_watermark[i].index("#")+7])

        result = "".join(hex_code)
        result = result.replace(";", "")

        f = open("detect.txt", "w")
        f.write(result)
        f.close()
