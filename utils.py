from exceptions import MismatchReportFormat


def validate_report_format(report_file_name: str, report_format: str) -> None:
    expected_extensions = {
        "markdown": ".md",
        "json": ".json",
    }

    expected_extension = expected_extensions.get(report_format)

    if not expected_extension:
        raise MismatchReportFormat(
            f"Unsupported report format: {report_format}"
        )

    if not report_file_name.lower().endswith(expected_extension):
        raise MismatchReportFormat(
            "The output file extension does not match "
            f"the selected format: {report_format}"
        )
