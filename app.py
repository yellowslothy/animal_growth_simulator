import streamlit as st
from animals import Animal

st.set_page_config(page_title="동물 성장 시뮬레이터", page_icon="🐾", layout="centered")

st.title("🐾 동물 성장 시뮬레이터")
st.markdown("먹이를 주고 동물을 성장시켜보세요!")

if 'animal' not in st.session_state:
    animal_choice = st.selectbox("동물을 선택하세요", ["강아지", "고양이", "토끼"])
    st.session_state.animal = Animal(animal_choice)

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
    st.session_state.animal = Animal(animal.name)
    st.experimental_rerun()
