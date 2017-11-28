import recommender
from pprint import PrettyPrinter


class TestRecommender():
    def setUp(self):
        """Simple test setUp Function
        Args: None
        Returns: None"""
        ratings_file = recommender.open_ratings_file()
        self.lines = ratings_file.readlines()
        self.titles = recommender.build_text_list(self.lines)
        self.pp = PrettyPrinter()

    def test_titles(self):
        self.pp.pprint(self.titles)

    def test_build_dict(self):
        self.pp.pprint(recommender.build_user_dict(
            self.lines, self.titles))

    def tearDown(self):
        pass
