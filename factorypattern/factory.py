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

    @staticmethod
    def create_media(media_type):
        if media_type.lower() == 'dip':
            return Dip()
        if media_type.lower() == 'book':
            return Book()
        if media_type.lower() == 'usen':
            return Usen()
        else:
            raise ValueError(f"Unsupported media type: {media_type}")


if __name__ == '__main__':
    try:
        obj1 = MediaFactory.create_media('dip')
        print(obj1.show_media())
        obj2 = MediaFactory.create_media('book')
        print(obj2.show_media())
        obj3 = MediaFactory.create_media('usen')
        print(obj3.show_media())
        obj4 = MediaFactory.create_media('test')

    except Exception as e:
        print(f"Error: {e}")

