import pytest

from report_logic import generate_markdown_report, generate_json_report
import json


def test_markdown_report(tmp_path):
    output_file = tmp_path / "report.md"

    generate_markdown_report(
        3,
        4700,
        [{"product": "Laptop", "price": 1000}],
        [("Alice", 2000)],
        [("Electronics", 3000)],
        output_file,
    )

    assert output_file.exists()

    content = output_file.read_text(encoding="utf-8")

    assert "Brightstone Logistics Report" in content
    assert "€4,700.00" in content


def test_markdown_invalid_output_path():
    with pytest.raises(OSError):
        generate_markdown_report(
            3,
            4700,
            [],
            [],
            [],
            "nonexistent_folder/report.json",
        )


def test_json_report(tmp_path):
    output_file = tmp_path / "report.json"

    generate_json_report(
        3,
        4700,
        [{"product": "Laptop", "price": 1000}],
        [("Alice", 2000)],
        [("Electronics", 3000)],
        output_file,
    )

    assert output_file.exists()

    data = json.loads(output_file.read_text(encoding="utf-8"))
    print(data)

    assert data["total_number_of_order"] == 3
    assert data["total_revenue"] == 4700


def test_json_invalid_output_path():
    with pytest.raises(OSError):
        generate_json_report(
            3,
            4700,
            [],
            [],
            [],
            "nonexistent_folder/report.json",
        )
