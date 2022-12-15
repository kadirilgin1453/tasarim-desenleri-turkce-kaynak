from book_export_visitor import BookExportVisitor
from magazine import Magazine
from encyclopedia import Encyclopedia


class JsonExportVisitor(BookExportVisitor):
    """
    Visitor arayüzünü ve burada tanımlı olan metotları uygular.
    Sonradan eklenmek istenen işlemler burada yer alır.
    UML diyagramındaki ConcreteVisitor yapısına denk gelir.
    """

    def export_visit(self, item):
        # Parametre olarak gelen örneğin JSON'a çevrilmesi işlemleri yer alacaktır.
        if isinstance(item, (Magazine, Encyclopedia)):
            print(f"{item.name} exported by JsonExportVisitor")
        else:
            raise NotImplementedError("Item type is not implemented.")
