from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report):
        simple_report = super().generate(report)
        companies = [company["nome_da_empresa"] for company in report]
        list_company = Counter(companies)
        quantity = ""
        for company in list_company:
            count = companies.count(company)
            quantity += f"- {company}: {count}\n"

        full_report = (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{quantity}"
        )
        return full_report
