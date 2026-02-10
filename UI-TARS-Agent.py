#!/usr/bin/env python3
from __future__ import annotations
import logging
import os
import re
import json
import base64
import time
from pathlib import Path

from openai import OpenAI
from io import BytesIO
from typing import Any, Dict, List, Optional, Tuple, cast

