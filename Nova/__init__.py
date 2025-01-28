import logging
import os
import sys
import time

ENV = bool(os.environ.get("ENV", False))

if ENV:
    API_ID = int(os.environ.get("API_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "Phoenix_HLP")