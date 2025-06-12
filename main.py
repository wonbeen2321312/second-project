import streamlit as st

# 🎨 페이지 꾸미기
st.set_page_config(
    page_title="드라마 장르 추천기 🎬",
    page_icon="🎭",
    layout="centered"
)

st.markdown("# 🎬 드라마 장르 추천기")
st.markdown("## 어떤 장르의 드라마를 보고 싶으신가요? 🤔")

# 🌈 스타일 강조 (이모지 포함)
st.markdown("### 💡 장르를 선택하시면 추천 드라마를 보여드려요!")
st.markdown("---")

# 🎯 장르 선택
genre = st.selectbox(
    "장르를 선택하세요 🎈",
    ["로맨스 💕", "스릴러 😱", "코미디 😂", "액션 🔥", "SF 🚀", "시대극 👘", "판타지 🧚‍♂️"]
)

# 🎁 추천 딕셔너리
recommendations = {
    "로맨스 💕": [
        "💖 사랑의 불시착 (Crash Landing on You)",
        "🌸 그 해 우리는 (Our Beloved Summer)",
        "🎶 이태원 클라쓰 (Itaewon Class)"
    ],
    "스릴러 😱": [
        "🧠 시그널 (Signal)",
        "🔪 악의 마음을 읽는 자들",
        "🕵️ 보이스 (Voice)"
    ],
    "코미디 😂": [
        "🤣 미생 (Incomplete Life)",
        "📺 고백부부",
        "😆 환상의 타이밍"
    ],
    "액션 🔥": [
        "💥 배드 앤 크레이지 (Bad and Crazy)",
        "🔫 태양의 후예 (Descendants of the Sun)",
        "🚓 보이스 (Voice)"
    ],
    "SF 🚀": [
        "🛸 승리호 (Space Sweepers)",
        "🤖 너의 시간 속으로",
        "📡 써클: 이어진 두 세계"
    ],
    "시대극 👘": [
        "👑 해를 품은 달",
        "🦢 구르미 그린 달빛",
        "🥋 킹덤"
    ],
    "판타지 🧚‍♂️": [
        "🦄 도깨비 (Goblin)",
        "🪄 알함브라 궁전의 추억",
        "🌌 호텔 델루나"
    ]
}

# ✨ 결과 보여주기
st.markdown("### 🎉 추천 드라마 리스트 🎉")

for drama in recommendations.get(genre, []):
    st.markdown(f"- {drama}")

st.markdown("---")
st.markdown("📺 **드라마는 마음의 휴식입니다! 좋은 시간 보내세요! 🧘‍♂️**")
