import argparse
import pyttsx3


def list_voices(engine):
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(f'{i}: {voice.name} ({voice.id})')
    return voices


def synthesize(text: str, voice_index: int | None = None, rate: int = 180, volume: float = 1.0):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    if voice_index is not None:
        voices = engine.getProperty('voices')
        if 0 <= voice_index < len(voices):
            engine.setProperty('voice', voices[voice_index].id)
        else:
            raise ValueError(f'voice_index must be 0..{len(voices) - 1}')
    engine.say(text)
    engine.runAndWait()


def main():
    parser = argparse.ArgumentParser(description='Offline text-to-speech demo')
    parser.add_argument('text', nargs='?', default='Hello, this is a local text-to-speech demo.')
    parser.add_argument('--voice', type=int, default=None, help='Voice index from --list-voices')
    parser.add_argument('--rate', type=int, default=180, help='Speech rate in words per minute')
    parser.add_argument('--volume', type=float, default=1.0, help='Volume between 0.0 and 1.0')
    parser.add_argument('--list-voices', action='store_true', help='List available voices and exit')
    args = parser.parse_args()

    if args.list_voices:
        engine = pyttsx3.init()
        list_voices(engine)
        return

    synthesize(args.text, args.voice, args.rate, args.volume)


if __name__ == '__main__':
    main()
