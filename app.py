import streamlit as st
from PIL import Image

# Animal 클래스 코드 여기 넣거나, animals.py에서 import

class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.level = 1
        self.experience = 0
        self.is_alive = True

    def status(self):
        return {
            "Age": self.age,
            "Level": self.level,
            "Experience": self.experience,
        }

    def feed(self, fish=False):
        if not self.is_alive:
            return
        if fish:
            self.experience += 10
            if self.experience >= self.level * 50:
                self.level_up()

    def die(self):
        self.is_alive = False

    def level_up(self):
        self.level += 1
        self.experience = 0

st.set_page_config(page_title="고양이 성장 시뮬레이터", page_icon="🐱", layout="centered")

st.title("🐱 고양이 성장 시뮬레이터")
st.markdown("고양이에게 먹이를 주고 성장시켜보세요!")

animal_name = "고양이"

# 임시 이미지 없으면 주석처리 가능
# image = Image.open("images/cat.png")
# st.image(image, caption=animal_name, use_container_width=True)

if 'animal' not in st.session_state:
    st.session_state.animal = Animal(animal_name)

animal = st.session_state.animal

if not animal.is_alive:
    st.markdown(
        """
        <div style="display:flex; justify-content:center; align-items:center; height:80vh;">
            <h1 style="color:red; font-size:80px; text-align:center;">
                💀 고양이가 죽었습니다...
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.subheader(f"{animal.name}의 상태")
    status = animal.status()
    st.write(f"나이: {status['Age']}살")
    st.write(f"레벨: {status['Level']}")
    st.write(f"경험치: {status['Experience']} / {status['Level'] * 50}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🍣 생선 먹이 주기"):
            animal.feed(fish=True)
            st.success(f"{animal.name}에게 생선을 주었습니다! 경험치가 올랐어요!")

    with col2:
        if st.button("🍫 초콜릿 먹이 주기"):
            animal.die()
            st.error(f"⚠️ {animal.name}가 초콜릿을 먹고 죽었습니다...")

if st.button("🔄 초기화"):
    st.session_state.animal = Animal(animal_name)
    st.experimental_rerun()
    st.stop()
