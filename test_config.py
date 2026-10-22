import os
import unittest

import config


class ConfigTests(unittest.TestCase):
    def test_default_settings_are_sensible(self):
        self.assertEqual(config.SERVICE_NAME, "rt-recall")
        self.assertEqual(config.DEFAULT_HOST, "0.0.0.0")
        self.assertEqual(config.DEFAULT_PORT, 8000)
        self.assertEqual(config.DEFAULT_LOG_LEVEL, "INFO")
        self.assertEqual(config.settings.app_name, "rt-recall")
        self.assertEqual(config.settings.host, "0.0.0.0")
        self.assertEqual(config.settings.port, 8000)
        self.assertEqual(config.settings.log_level, "INFO")

    def test_environment_overrides_are_applied(self):
        original_env = os.environ.get("RT_RECALL_PORT")
        original_debug = os.environ.get("RT_RECALL_DEBUG")
        os.environ["RT_RECALL_PORT"] = "9000"
        os.environ["RT_RECALL_DEBUG"] = "true"
        try:
            settings = config.Settings()
            self.assertEqual(settings.port, 9000)
            self.assertTrue(settings.debug)
        finally:
            if original_env is None:
                os.environ.pop("RT_RECALL_PORT", None)
            else:
                os.environ["RT_RECALL_PORT"] = original_env

            if original_debug is None:
                os.environ.pop("RT_RECALL_DEBUG", None)
            else:
                os.environ["RT_RECALL_DEBUG"] = original_debug


if __name__ == "__main__":
    unittest.main()
