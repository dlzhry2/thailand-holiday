class Validator:

    def __init__(self, request: dict):
        self.payload = request
        self.errors = {}

    def validate_save_photos(self):
        for field in self.payload.keys():
            if field not in ["base64Image", "imageName", "location", "caption"]:
                self.errors = {"error": "Invalid request"}
                return False

            if not isinstance(self.payload[field], str):
                self.errors = {"error": "Invalid request"}
                return False

        return True

    def get_errors(self):
        return self.errors
