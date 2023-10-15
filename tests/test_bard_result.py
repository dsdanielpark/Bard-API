import unittest

from bardapi.models.result import BardResult
from data import t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11


class TestBardResult(unittest.TestCase):
    def test_5images(self):
        img0 = BardResult(t1[0])
        self.assertEqual(len(img0.drafts[0].images), 5)

    def test_topic(self):
        img1 = BardResult(t1[1])
        self.assertEqual(img1.topic, "Orcas in the wild")

    def test_2images(self):
        img2 = BardResult(t2)
        self.assertEqual(
            img2.search_queries,
            [
                ["2 pictures of orcas", 1],
                ["Why is orca called Killer?", 4],
                ["What do orcas look like?", 4],
            ],
        )

        # images can be separated by key
        self.assertEqual(
            "[Image of Two orcas breaching the water]", img2.drafts[0].images[0].key
        )
        self.assertEqual(
            "[Image of Two orcas swimming together]", img2.drafts[0].images[1].key
        )
        # or merged on an album
        self.assertEqual("[2 Images of orcas]", img2.drafts[1].images[0].key)
        self.assertEqual("[2 Images of orcas]", img2.drafts[1].images[1].key)

    def test_map_content(self):
        maps4 = BardResult(t3[4])
        self.assertEqual(
            "http://googleusercontent.com/map_content/0",
            maps4.drafts[0].map_content[0].key,
        )
        self.assertEqual(10, len(maps4.drafts[0].map_content[0].points[4].images))

        maps9 = BardResult(t9)
        self.assertEqual("Rv52", maps9.drafts[0].map_content[1].directions.road_name)
        self.assertTrue(
            maps9.drafts[0]
            .map_content[1]
            .directions.url.startswith("https://www.google.com/maps/dir/")
        )
        self.assertEqual(2, len(maps9.drafts[0].map_content[1].directions.sections))
        self.assertFalse(maps9.drafts[0].python_code)

        self.assertFalse(
            "http://googleusercontent.com/" in maps4.drafts[0].text_with_user_content
        )
        self.assertFalse(
            "http://googleusercontent.com/" in maps9.drafts[0].text_with_user_content
        )

    def test_google_workspace(self):
        drive4 = BardResult(t4[4])
        self.assertEqual(len(drive4.drafts[0].gworkspace), 3)

    def test_youtube(self):
        video4 = BardResult(t5[4])
        self.assertEqual(len(video4.drafts[0].youtube[0]), 5)
        self.assertFalse(
            "http://googleusercontent.com/" in video4.drafts[0].text_with_user_content
        )

    def test_flights(self):
        flights4 = BardResult(t6[4])
        self.assertEqual(len(flights4.drafts[0].flights[0].flights), 5)
        self.assertIsNotNone(flights4.drafts[0].flights[0].markdown_text)

    def test_flights_and_hotel(self):
        res = BardResult(t11)
        self.assertEqual(5, len(res.drafts[0].flights[0].flights))
        self.assertEqual(5, len(res.drafts[0].hotels[0].hotels))

    def test_python(self):
        python = BardResult(t7[0])
        self.assertEqual(len(python.drafts[1].citations), 3)
        self.assertEqual("A\nA str\n", python.drafts[0].python_code[0].output)

    def test_citations(self):
        citations = BardResult(t8[0])
        self.assertEqual(len(citations.drafts[0].citations), 2)
        self.assertFalse(
            "http://googleusercontent.com/"
            in citations.drafts[0].text_with_user_content
        )

    def test_summary(self):
        summary = BardResult(t10)
        self.assertEqual(len(summary.drafts[0].citations), 1)
        json_o = summary.drafts[0].json_content[0].object
        self.assertIsNotNone(json_o)
        self.assertEqual(len(summary.drafts[0].json_content), 1)


if __name__ == "__main__":
    unittest.main()
