from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, report):
        now = datetime.today()
        cls.older = min(
            [product["data_de_fabricacao"] for product in report]
        )
        cls.closer = min(
            [
                product["data_de_validade"]
                for product in report
                if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                >= now
            ]
        )
        cls.company = max(
            [product["nome_da_empresa"] for product in report]
        )

        return (
            f"Data de fabricação mais antiga: {cls.older}\n"
            f"Data de validade mais próxima: {cls.closer }\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{cls.company}\n"
        )
