class ReportsFileWriter():

    @staticmethod
    def write_file(report):
        file = open('reports.txt', 'w')
        file.write(report)
        file.close()
