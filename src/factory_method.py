import abc
import enum


class ReportType(enum.StrEnum):
    PDF = enum.auto()
    HTML = enum.auto()
    XML = enum.auto()


class ReportGenerator(abc.ABC):
    @abc.abstractmethod
    def generate_monthly_report(self, user_id: str, account_id: str) -> str: ...


class PDFReportGenerator(ReportGenerator):
    def generate_monthly_report(self, user_id: str, account_id: str) -> str:
        print("Generating PDF report")
        return "PDF REPORT GENERATED"


class HTMLReportGenerator(ReportGenerator):
    def generate_monthly_report(self, user_id: str, account_id: str) -> str:
        print("Generating HTML report")
        return "HTML REPORT GENERATED"


class XMLReportGenerator(ReportGenerator):
    def generate_monthly_report(self, user_id: str, account_id: str) -> str:
        print("Generating XML report")
        return "XML REPORT GENERATED"


class ReportGeneratorFactory:
    @staticmethod
    def get_report_generator(report_type: ReportType) -> ReportGenerator:
        match report_type:
            case ReportType.PDF:
                return PDFReportGenerator()
            case ReportType.HTML:
                return HTMLReportGenerator()
            case ReportType.XML:
                return XMLReportGenerator()
            case _:
                print("Not valid report generator found")
                raise ValueError(f"Unsupported report type: {report_type}")
