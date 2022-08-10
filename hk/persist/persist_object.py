import logging
import os
import pickle


class PersistObject(object):
    """A base-class to create objects with the abilities to persist itself
    and create a readable file with chosen information and format.
    """

    @staticmethod
    def load(folder_path: str, file_name: str) -> 'PersistObject':
        """Loads a persistent object from a source (*.pickle).

        :param folder_path: folder-path to stored object information
        :param file_name: name of the object to recreate
        :return: a persistent object loaded from given source
        """
        file_path: str = os.path.join(folder_path, file_name + '.pickle')

        try:
            with open(file_path, 'rb') as backup:
                return pickle.load(backup)
        except FileNotFoundError:
            logging.error(f'PersistObject could not be loaded from "{file_path}".')

            return None

    def __init__(self, folder_path: str, file_name: str, file_suffix: str = 'txt') -> None:
        """Creates the object.

        :param folder_path: folder-path to store object information
        :param file_name: (file-)name of the object to create
        :param file_suffix: suffix for a readable file with object information
        """
        self.folder_path = folder_path
        self.file_name = file_name
        self.file_suffix = file_suffix

    def write_to_file(self) -> None:
        """Creates a readable file with object-information based on 'str(self)'.
        """
        file_path: str = os.path.join(self.folder_path,
                                      f'{self.file_name}.{self.file_suffix}')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(self))

    def save(self) -> None:
        """The object creates a backup of itself as a *.pickle-file.
        """
        file_path: str = os.path.join(self.folder_path,
                                      self.file_name + '.pickle')
        with open(file_path, 'wb') as backup:
            pickle.dump(self, backup, 5)
