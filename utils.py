from exceptions import MismatchReportFormat

def validate_report_format(report_file_name, report_format):
    if not report_file_name.endswith(f".{report_format}"):
        raise MismatchReportFormat(
            f"The output file extension does not match the selected format : {report_format}"
        )