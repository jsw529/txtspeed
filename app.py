import streamlit as st
from moviepy.editor import AudioFileClip
from moviepy.video.fx import all as vfx
import io
import tempfile

st.title("🎧 음성파일 배속 조절기")

uploaded_file = st.file_uploader("음성 파일 업로드 (mp3, wav)", type=["mp3", "wav"])
speed = st.selectbox("배속 선택", [0.5, 0.75, 1.0, 1.25, 1.5, 2.0], index=2)

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    clip = AudioFileClip(temp_file_path)
    sped_up_clip = clip.fx(vfx.speedx, speed)

    output_buffer = io.BytesIO()
    sped_up_clip.write_audiofile("output.mp3")
    with open("output.mp3", "rb") as f:
        output_buffer.write(f.read())
    output_buffer.seek(0)

    st.audio(output_buffer, format="audio/mp3")
    st.download_button("🎵 배속된 음성 다운로드", output_buffer, f"output_{speed}x.mp3", "audio/mp3")