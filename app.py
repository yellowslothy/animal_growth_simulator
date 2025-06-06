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

if hasattr(animal, 'is_alive') and not animal.is_alive:
    # 고양이가 죽었을 때 큰 글씨로 메시지 표시
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
