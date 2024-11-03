from abc import ABC, abstractmethod

class Media(ABC):

    @abstractmethod
    def show_media(self) -> str:
        pass


# create different media classes which will override the media methods
class Dip(Media):
    def show_media(self):
        return "This is Dip Media"

class Book(Media):
    def show_media(self):
        return "This is Book Media"

class Usen(Media):
    def show_media(self):
        return "This is Usen Media"


class MediaFactory(ABC):

    @abstractmethod
    def get_media(self) -> str:
        pass

# create different factory classes which will return the object of the media which is required

class DipFactory(MediaFactory):
    def get_media(self):
        return Dip()


class BookFactory(MediaFactory):
    def get_media(self):
        return Book()

class UsenFactory(MediaFactory):
    def get_media(self):
        return Usen()


if __name__ == '__main__':
    obj1 = DipFactory()
    media1 = obj1.get_media()
    print(media1.show_media())
    obj2 = BookFactory()
    media2 = obj2.get_media()
    print(media2.show_media())
    obj3 = UsenFactory()
    media3 = obj3.get_media()
    print(media3.show_media())