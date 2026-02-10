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
    self.trajectory = {"high_level_task_description": task_description, 'steps':[]}
    for setp in range(max_steps):
      self.current_step = step
      try:
        messages = self.prompt(self.trajectory, step)
        chat_completion = self.predict_desktop(messages)
        raw_response = ''
        for message in chat_completion:
          raw_response += message.choices[0].delta.content
          parsed_dict = parse_action_to_structure_output(
            raw_response,
            factor=1000,
            self.img_width,
            self.img_height,
            model_type="qwen25"
          )
          parsed_pyautogui_code = parsing_response_to_pyautogui_code(
            responses=parsed_dict,
            self.img_width,
            self.img_height
          )
          if not parsed_pyautogui_code:
            continue

          if parsed_pyautogui_code:
            exec(parsed_pyautogui_code)

          time.sleep(time_temp)
          self.trajectory["steps"].append({
            "step_num":self.current_step,
            "image": f"step_{self.current_step}.png",
            "response": f'{raw_response}'
          })
        
      except Exception as e:
        history_path = ''
        try:
          with open(history_path, "w", encoding="utf-8") as f:
            json.dump(self.trajectory, f, ensure_ascii=False, indent=2)
        except Exception as e:
          logging.error(f'{e}')
        continue
    history_path = ''
    try:
      with open(history_path, "w", encoding="utf-8") as f:
        json.dump(self.trajectory, f, ensure_ascii=False, indent=2)
    except Exception as e:
      logging.error(f'{e}')

  def split(self, param):
    pass

if __name__ == "__main__":
  MODEL = "uitars"
  API_KEY = ''
  BASE_URL = ''
  client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
  )

  agent = UITARS(
    MODEL
  )

  try:
    time_temp = float(input())
  except:
    time_temp = 1

  while True:
    task = input().strip()
    max_step = input().strip()
    max_step = int(max_step)
    agent.run_task(task, max_steps, time_temp)
  
