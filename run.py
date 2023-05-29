from bardapi.core import Bard
import os

print(Bard().get_answer("how are you?")['content'])

print("Done")
