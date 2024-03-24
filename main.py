import time
import random
import pygame


def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  return merge(left_half, right_half)


def merge(left, right):
  merged = []
  left_idx, right_idx = 0, 0

  while left_idx < len(left) and right_idx < len(right):
    if left[left_idx] < right[right_idx]:
      merged.append(left[left_idx])
      left_idx += 1
    else:
      merged.append(right[right_idx])
      right_idx += 1

  merged.extend(left[left_idx:])
  merged.extend(right[right_idx:])
  return merged


def print_array(arr):
  print("Current state of the array:")
  for num in arr:
    print(f"Variable {num} holds the value {num}")


def generate_sound():
  print("Loading sound file...")
  pygame.mixer.init()
  pygame.mixer.music.load(
      "sound.wav")  # Assuming sound.wav exists in the current directory
  print("Playing sound...")
  pygame.mixer.music.play()


def simulate_merge_sort(arr):
  print("Initial array:", arr)
  sorted_array = merge_sort(arr)
  print("Sorted array:", sorted_array)

  for i in range(len(arr)):
    print_array(arr[:i + 1])
    generate_sound()
    time.sleep(0.2)


arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
simulate_merge_sort(arr)
