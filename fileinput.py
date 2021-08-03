# for input file and processing 

class FileInput:
    def __init__(self, filename=None):
        self.m_filename = []
        self.m_lines = []
        self.m_lineIndices = []

        if filename:
            self.push(filename)

    def push(self, filename):
        try:
            lines = []
            with open(filename) as file:
                for line in file:
                    lines.append(line)

            self.m_filename.append(filename)
            self.m_lines.append(lines)
            self.m_lines.append(0)

        except:
            raise Exception(str.format("Could not open{0}", filename))

    def nextLine(self):
        if len(self.m_lineIndices) == 0:
            return None

        if self.m_lineIndices[-1] >= len(self.m_lines[-1]):
            self.pop()
            return self.nextLine()

        lineIndex = self.m_lineIndices[-1]
        self.m_lineIndices[-1] = lineIndex + 1

        return self.m_lines[-1][lineIndex]

    def pop(self):
        if len(self.m_lineIndices) > 0:
            self.m_filename.pop()
            self.m_lines.pop()
            self.m_lineIndices.pop()

    def file(self):
        if len(self.m_filenames) > 0:
            return self.m_filenames[-1]

        else:
            return "(top level)"

    def line(self):
        if len(self.m_lineIndices) > 0:
            return self.m_lineIndices[-1]

        else:
            return 1



