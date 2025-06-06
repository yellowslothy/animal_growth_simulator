import streamlit as st
from animals import Animal
from PIL import Image

st.set_page_config(page_title="고양이 성장 시뮬레이터", page_icon="🐱", layout="centered")

st.title("🐱 고양이 성장 시뮬레이터")
st.markdown("고양이에게 먹이를 주고 성장시켜보세요!")

# 선택 없이 고양이로 고정
animal_name = "고양이"

# 고양이 이미지 표시
image = Image.open("images/cat.png")
st.image(image, caption=animal_name, use_column_width=True)

# Animal 객체 초기화
if 'animal' not in st.session_state:
    st.session_state.animal = Animal(animal_name)

animal = st.session_state.animal

st.subheader(f"{animal.name}의 상태")
status = animal.status()
st.write(f"나이: {status['Age']}살")
st.write(f"레벨: {status['Level']}")
st.write(f"경험치: {status['Experience']} / {status['Level'] * 50}")

if st.button("🍖 먹이 주기"):
    animal.feed()
    st.success(f"{animal.name}에게 먹이를 주었습니다!")

if st.button("🔄 초기화"):
    st.session_state.animal = Animal(animal_name)
    st.experimental_rerun()
