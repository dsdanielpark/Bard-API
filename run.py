from bardapi.core import Bard
import os

# Close the browser


Bard().get_answer("how are you?")['content']
print(Bard().get_answer("how are you?")['content'])

print("Done")
