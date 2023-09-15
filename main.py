from gtts import gTTS
import fitz


def pdf_to_text():
    with fitz.open("James Payne - Beginning Python. Using Python 2.6 And Python 3.1 (2010).pdf") as doc:
        text_for_convert = ""
        for page in doc:
            text_for_convert += page.get_text()
        return text_for_convert


def text_to_mp3(text):
    language = "en"
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("output.mp3")

text = pdf_to_text()
text_to_mp3(text)
