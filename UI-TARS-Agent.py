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


def ensure_dir(relative_path:str):
  return str(target_dir)

class UITARS:
  def __init__(
    self,
    model:str = '',
    coord_type: str = "qwen25"
  ) -> None:
    super().__init__()
    self.model = model
    self.SYSTEM_PROMPT = ""

  def _encode_image_bytes():
    return

  def _smart_resize_qwen25():
    return 

  def capture_screen(self):
    return img_bytes, img_b64, screen

  def load_image(self, image_file, image_dir):
    return

  def prompt(self, trajectory, current_step):
    return messages

  def parse_response(self, response, trajectory):
    return 

  def _maybe_normalize_coordinates(self, acton_lines, trajectory, step_idx):
    return normalized

  def extract_actions(self, action):
    return actions

  def extract_actions_self(self, action):
    return actions

  def coord_extract(self, imput_string):
    return final_string

  def execute_action(self, actions):
    retrun is_terminate

  def predict_desktop(self, messages):
    return response

  def run_task(self, task_description, max_steps, time_temp):
    

     
  
