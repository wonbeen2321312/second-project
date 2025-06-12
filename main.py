import streamlit as st
import random

# 🌟 페이지 설정
st.set_page_config(
    page_title="가위바위보 대결! 🎮",
    page_icon="✌️",
    layout="centered"
)

# 🎈 타이틀 및 설명
st.title("✊ ✌️ 🖐️ 가위바위보 게임")
st.markdown("### 당신의 선택은? 컴퓨터와 대결해보세요! 🤖")

# ✨ 선택지
options = {
    "가위 ✌️": "scissors",
    "바위 ✊": "rock",
    "보 🖐️": "paper"
}

# 🎮 유저 선택
user_choice_display = st.radio("무엇을 내시겠어요? 🎯", list(options.keys()))

# 컴퓨터 선택 (랜덤)
computer_choice = random.choice(list(options.values()))

# 변환
user_choice = options[user_choice_display]

# 🧠 승패 판단 함수
def determine_winner(user, computer):
    if user == computer:
        return "😐 무승부!", "🤝 다시 도전해보세요!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "🎉 승리!", "🥳 축하합니다! 당신이 이겼어요!"
    else:
        return "😢 패배...", "💪 다시 도전하세요!"

# 버튼 클릭 시 결과 출력
if st.button("결과 보기 🎲"):
    result, message = determine_winner(user_choice, computer_choice)
    
    # 🖥️ 선택 결과 표시
    st.markdown("---")
    st.markdown(f"🧑 당신의 선택: **{user_choice_display}**")
    comp_key = [k for k, v in options.items() if v == computer_choice][0]
    st.markdown(f"🤖 컴퓨터의 선택: **{comp_key}**")
    
    # 결과 출력
    st.markdown(f"## {result}")
    st.markdown(f"### {message}")
    st.balloons() if result == "🎉 승리!" else st.snow()
