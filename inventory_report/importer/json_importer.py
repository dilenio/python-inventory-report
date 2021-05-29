from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith('.json'):
            json = Inventory.open_json_file(file_name)
            return json
        else:
            raise ValueError("Arquivo inválido")
