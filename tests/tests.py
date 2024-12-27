import unittest
from pyaiagent.agent import AIAgent

class TestAIAgent(unittest.TestCase):
    """
    Unit tests for the AIAgent class.
    """

    def test_generate_response(self):
        """
        Test if the generate_response method returns a string response.
        """
        agent = AIAgent()
        response = agent.generate_response("Hello, how are you?")
        self.assertIsInstance(response, str)

if __name__ == "__main__":
    unittest.main()