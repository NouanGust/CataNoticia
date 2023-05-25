class Noticia:
    def __init__(self, titulo, descricao, link):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__link = link

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_link(self):
        return self.__link

    def set_link(self, link):
        self.__link = link
