import time
import numpy as np
import pyaudio

p = pyaudio.PyAudio()

fs = 44100  # Sample rate
duration = 0.12  # Duration of one unit in seconds
freq = 440  # Frequency in Hz

while True:
    text = input(str())

    morsecode ={'A': '.-',     'B': '-...',   'C': '-.-.',
                'D': '-..',    'E': '.',      'F': '..-.',
                'G': '--.',    'H': '....',   'I': '..',
                'J': '.---',   'K': '-.-',    'L': '.-..',
                'M': '--',     'N': '-.',     'O': '---',
                'P': '.--.',   'Q': '--.-',   'R': '.-.',
                'S': '...',    'T': '-',      'U': '..-',
                'V': '...-',   'W': '.--',    'X': '-..-',
                'Y': '-.--',   'Z': '--..',

                'А': '.-',     'Б': '-...',   'Ц': '-.-.',
                'Д': '-..',    'Е': '.',      'Ф': '..-.',
                'Г': '--.',    'Х': '....',   'И': '..',
                'Й': '.---',   'К': '-.-',    'Л': '.-..',
                'М': '--',     'Н': '-.',     'О': '---',
                'П': '.--.',   'Щ': '--.-',   'Р': '.-.',
                'С': '...',    'Т': '-',      'У': '..-',
                'Ж': '...-',   'В': '.--',    'Ь': '-..-',
                'Ы': '-.--',   'З': '--..',   'Ш': '----',
                'Ъ': '--.--',  'Э': '..-..',  'Ю': '..--',
                'Я': '.-.-',   'Ч': '---.',   'Ё': '.',

                ' ': '   ',

                '0': '-----',  '1': '.----',  '2': '..---',
                '3': '...--',  '4': '....-',  '5': '.....',
                '6': '-....',  '7': '--...',  '8': '---..',
                '9': '----.',

                '.': '.-.-.-', ',': '--..--', '?': '..--..',
                '!': '..--.',  ':': '---...', '=': '-...-',
                '"': '.-..-.', '/': '-..-.',  "'": '.----.',
                ';': '-.-.-.', '@': '.--.-.',
                }

    morse = ' '.join(morsecode.get(s.upper())for s in text)

    print(morse)

    for s in morse:
        if s == '.':
            # я украл кусок кода
            samples = (np.sin(2 * np.pi * np.arange(fs * duration) * freq / fs)).astype(np.float32).tobytes()
            stream = p.open(format=pyaudio.paFloat32,
                            channels=1,
                            rate=fs,
                            output=True)
            stream.write(samples)

            # time.sleep(duration)
        if s == '-':

            samples = (np.sin(2 * np.pi * np.arange(fs * 3 * duration) * freq / fs)).astype(np.float32).tobytes()
            stream = p.open(format=pyaudio.paFloat32,
                            channels=1,
                            rate=fs,
                            output=True)
            stream.write(samples)

            # time.sleep(duration)
        if s == '   ':
            time.sleep(7*duration)
        if s == ' ':
            time.sleep(3*duration)
