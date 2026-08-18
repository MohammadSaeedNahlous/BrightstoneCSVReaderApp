import argparse

parser = argparse.ArgumentParser(
    description="Required. Generate a report from a Brightstone Logistics orders CSV file."
)
parser.add_argument(
    "--input-path", required=True, help="The path of the input CSV file."
)

parser.add_argument(
    "--output-path",
    required=True,
    help="Required. The path where the generated report will be saved.",
)

parser.add_argument(
    "--report-format",
    choices=["markdown", "json"],
    default="markdown",
    help="Optional. The format of the generated report, either markdown(.mk) or JSON (.json). Default markdown.",
)

arguments = parser.parse_args()

# args.input_path
# args.output_path
# args.report_format
