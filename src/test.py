#! /usr/bin/env python3

import time

from __core.plugins.cache import Memory

if __name__ == "__main__":
  Memory.Init()

  cache = Memory()
  cache.write("test", "hello", 3)
  print(cache.read("test"))
  print(cache.ttl("test"))
  time.sleep(1)
  print(cache.read("test"))
  time.sleep(1)
  print(cache.read("test"))
  time.sleep(1)
  print(cache.read("test"))
  print(cache.ttl("test"))
