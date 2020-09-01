from .file_writer import ReportFileWriter


class ReportWriter():

    @staticmethod
    def write(report, writer=ReportFileWriter):
        # Lógica...
        # Lógica...
        # report = faz_alguma_operacao
        writer.write(report)
