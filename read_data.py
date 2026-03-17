"""A python class to read in the planet data for the Solar System Project."""
import csv


class ReadPlanets:
    """ReadPlanets reads planet records from a CSV file and returns a mapping:

    Example:
        reader = ReadPlanets("data.csv")
        planets = reader.read()
        print(planets["Earth"]["mass"])

    """

    def __init__(
            self,
            file_path = "planet_data.csv",
            delimiter = ",",
            encoding = "utf-8"
    ):
        """ReadPlanets contructor to set the attributes.

        Args:
            file_path : Optional str
                default: "planet_data.csv"
            delimiter : Optional str
                default: ","
            encoding : Optional str
                default: "utf-8"

        """
        self.file_path = file_path
        self.delimiter = delimiter
        self.encoding = encoding

    def read(self):
        """Read the CSV file and returns the planets mapping.

        Returns:
            dict : dictionary or a mapping of the planets name to its attributes

        """
        planets = {}
        with open(self.file_path, newline="", encoding=self.encoding) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=self.delimiter)
            for row in reader:
                name = row.get("Name", "")
                if not name:
                    print("missing row name, this row is skipped")
                    continue
                if name in planets:
                    print(f"Duplicate row data for {name}, the last row is used.")
                planets[name.capitalize()] = {
                    k.lower(): v for k, v in row.items() if k != "Name"
                    }

        return planets
