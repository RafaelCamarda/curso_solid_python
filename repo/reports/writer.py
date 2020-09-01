from .file_writer import ReportsFileWriter


class ReportsWriter():

    @staticmethod
    def write(report):
        ReportsFileWriter.write_file(report)
