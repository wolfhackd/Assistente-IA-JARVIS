import pyaudio

class Microphone:
    def __init__(self):
        # Start config
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 48000
        self.chunk = 1024
        
        # Pyaudio
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.frames = []

    def record(self):
        self.stream = self.p.open(format=self.format,
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)
        self.frames = []
        print("Recording...")

    def record_chunk(self):
        if self.stream:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

    def stop(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
            print("Recording stopped.")

    def finish(self):
        self.stop()
        self.p.terminate()


    def __exit__(self, exc_type, exc, tb):
        self.finish()