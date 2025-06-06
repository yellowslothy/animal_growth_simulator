import streamlit as st
from animals import Animal
from PIL import Image

st.set_page_config(page_title="고양이 성장 시뮬레이터", page_icon="🐱", layout="centered")

st.title("🐱 고양이 성장 시뮬레이터")
st.markdown("고양이에게 먹이를 주고 성장시켜보세요!")

animal_name = "고양이"

image = Image.open("images/cat.png")
st.image(image, caption=animal_name, use_container_width=True)

if 'animal' not in st.session_state:
    st.session_state.animal = Animal(animal_name)

animal = st.session_state.animal

st.subheader(f"{animal.name}의 상태")

if hasattr(animal, 'is_alive') and not animal.is_alive:
    st.write("💀 고양이가 죽었습니다.")
else:
    status = animal.status()
    st.write(f"나이: {status['Age']}살")
    st.write(f"레벨: {status['Level']}")
    st.write(f"경험치: {status['Experience']} / {status['Level'] * 50}")

    food = st.selectbox("먹이를 선택하세요", ["생선", "초콜릿"])

    if st.button("🍖 먹이 주기"):
        if food == "생선":
            animal.feed(fish=True)  # 경험치 올리기
            st.success(f"{animal.name}에게 생선을 주었습니다! 경험치가 올랐어요!")
        elif food == "초콜릿":
            animal.die()  # 고양이 죽음 처리
            st.error(f"⚠️ {animal.name}가 초콜릿을 먹고 죽었습니다...")

if st.button("🔄 초기화"):
    st.session_state.animal = Animal(animal_name)
    st.experimental_rerun()
