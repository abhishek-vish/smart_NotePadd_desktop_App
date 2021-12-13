import os
import string
from tkinter import filedialog


class File_Model:

    def __init__(self):
        self.url = ""
        self.key = string.ascii_letters + ''.join([str(x) for x in range(0, 10)])

        # can also be
        # self.key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        self.offset = 5

    def encrypt(self, plaintext):
        result = ""
        for l1 in plaintext:
            try:
                i = (self.key.index(l1) + self.offset) % 62
                result += self.key[i]
            except ValueError:
                result += l1
        return result

    def decrypt(self, chiphertext):
        result = ''
        for l2 in chiphertext:
            try:
                i = (self.key.index(l2) - self.offset) % 62
                result += self.key[i]
            except ValueError:
                result += l2
        return result

    def open_file(self):
        self.url = filedialog.askopenfilename(title="Select File", filetypes=[("Text Documents", "*.*")])

    def newfile(self):
        self.url = ""

    def save_as(self, msg):
        content = msg
        encrypted = self.encrypt(content)
        self.url = filedialog.asksaveasfile(mode="w", defaultextension='.ntxt',
                                            filetypes=([("All Files", ("Text Documents", "*.txt"))]))
        self.url.write(encrypted)
        filepath = self.url.name
        self.url.close()
        self.url = filepath

    def save_file(self, msg):
        content = ""
        if self.url == "":
            self.url = filedialog.asksaveasfilename(title="Select Files", defaultextension=".ntxt",
                                                    filetypes=[("Text Documents", "*.*")])
        filename = msg
        if file_extension == '.ntxt':  # in NotepadFileModel in palce of "is" there is a "in" keyword
            content = ""
            content = self.encrypt(content)
        with open(self.url, 'w', encoding='utf-8') as fw:
            fw.write(content)

    def read_file(self, url=""):
        if url != '':
            self.url = url
        else:
            self.open_file()
            base = os.path.basename(self.url)
            file_name, file_extension = os.path.splitext(self.url)
            fr = open(self.url, "r")
            contents = fr.read()
            if file_extension == '.ntxt':
                contents = self.decrypt(contents)
            fr.close()
            return contents, base
