import streamlit as st
import time

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="영혼의 거울 | 전생 직업·신분 판독기",
    page_icon="🔮",
    layout="centered"
)

# 2. 마법 고서 / 앤티크 양피지 감성 커스텀 CSS
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at top, #231d2b 0%, #110d16 100%);
        color: #e2d9cc;
        font-family: 'Pretendard', sans-serif;
    }
    .magic-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #e5b567;
        text-shadow: 0 0 15px rgba(229, 181, 103, 0.4);
        margin-bottom: 6px;
    }
    .magic-sub {
        text-align: center;
        color: #a89bb5;
        font-size: 0.95rem;
        margin-bottom: 28px;
    }
    .parchment-card {
        background: linear-gradient(135deg, #fdfbf7 0%, #f4ebd9 100%);
        color: #2b1f14;
        border: 2px solid #c8a365;
        border-radius: 12px;
        padding: 30px 24px;
        margin: 20px 0;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.7);
    }
    .badge-rank {
        display: inline-block;
        background-color: #8c2d19;
        color: #fff;
        padding: 4px 14px;
        border-radius: 4px;
        font-size: 0.85rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .job-title {
        font-size: 1.9rem;
        font-weight: 800;
        color: #1f140e;
        margin-bottom: 12px;
    }
    .quote-box {
        font-style: italic;
        color: #6e4e37;
        border-left: 3px solid #c8a365;
        padding-left: 12px;
        margin: 12px 0 16px 0;
        font-size: 1rem;
        font-weight: 600;
    }
    .story-text {
        font-size: 0.95rem;
        line-height: 1.7;
        color: #3d2e24;
        word-break: keep-all;
    }
    .trait-item {
        background: rgba(200, 163, 101, 0.2);
        border: 1px solid rgba(140, 45, 25, 0.3);
        border-radius: 6px;
        padding: 8px 12px;
        margin-top: 8px;
        font-size: 0.9rem;
    }
    .stButton > button {
        background: linear-gradient(135deg, #8c2d19 0%, #d45d3a 100%) !important;
        color: #fff !important;
        border: 1px solid #e5b567 !important;
        border-radius: 8px !important;
        padding: 0.7rem 2rem !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. 6가지 전생 결과 데이터
PAST_LIVES = {
    0: {
        "rank": "🏛️ 왕실 절대 미각",
        "job": "궁궐 시식 기미상궁 🍲",
        "quote": "“한 입만 더 먹어보면 독이 있는지 확실히 알 수 있겠사옵니다.”",
        "story": "수라상에 올라오는 온갖 산해진미를 임금보다 먼저 맛보던 궁궐 최고의 미식가였습니다. 남다른 식탐과 예민한 미각으로 '배부르다'면서도 후식 배는 따로 남겨두던 전설의 인물입니다.",
        "trait": "현생의 흔적: 맛없는 걸로 배 채우면 극도로 화가 남.",
        "synergy": "최고의 궁합: 주방장 영혼을 가진 사람 / 상극: 맛집 줄 서기 싫어하는 사람"
    },
    1: {
        "rank": "⚔️ 방랑 무림의 풍운아",
        "job": "전설의 낮잠 자는 방랑 무사 🗡️",
        "quote": "“칼을 뽑는 건 귀찮지만, 낮잠을 방해받는 건 더 용서 못 한다.”",
        "story": "검 한 자루로 일대를 평정했으나 나무 그늘 아래서의 오침을 더 사랑했던 게으른 천재 검객입니다. 평소엔 멍하니 누워만 있다가도 결정적인 순간에만 한 방을 보여주었습니다.",
        "trait": "현생의 흔적: 알람을 5분 단위로 맞춰놓고 귀신같이 다 끄고 잠듦.",
        "synergy": "최고의 궁합: 조용히 이불 덮어주는 사람 / 상극: 아침 7시에 깨우는 사람"
    },
    2: {
        "rank": "📜 지하 지식인 / 결사대",
        "job": "황실 도서관 금서 밀반출 총책 📚",
        "quote": "“쉿, 읽지 말라고 봉인해 둔 책이 가장 짜릿한 법이지.”",
        "story": "황제가 감춰둔 마법서와 비밀 일기를 몰래 빼돌려 지하실에서 밤새 독파하던 호기심 대마왕이었습니다. 지루한 건 1초도 못 참으며 세상의 모든 비밀을 알아야 직성이 풀렸습니다.",
        "trait": "현생의 흔적: 새벽 3시에 나무위키나 음모론 유튜브를 정주행 중임.",
        "synergy": "최고의 궁합: 비밀 이야기 털어놓기 좋은 친구 / 상극: 스포일러 날리는 사람"
    },
    3: {
        "rank": "🐾 전생 비인간계 / 신수",
        "job": "성주님 무릎 위 귀족 뚱냥이 🐱",
        "quote": "“골골골... 인간아, 간식이나 바치거라.”",
        "story": "전생에 사람이 아니었습니다! 난로 앞 푹신한 방석에서 뒹굴거리며 쌀쌀맞은 표정 하나로 온 성 사람들을 조종하던 마성의 영물 고양이였습니다. 아무것도 안 해도 모두가 떠받들어 주었습니다.",
        "trait": "현생의 흔적: 집 밖으로 나가는 순간부터 배터리가 1%로 급감함.",
        "synergy": "최고의 궁합: 간식 챙겨주는 집사 성향 / 상극: 잔소리 많은 사람"
    },
    4: {
        "rank": "🧪 신비주의 / 실패의 미학",
        "job": "폭발 전문 엉뚱 연금술사 💥",
        "quote": "“돌을 금으로 바꾸려다 실험실을 또 날려먹었군요! 하지만 불꽃이 예쁘죠?”",
        "story": "매번 정해진 제조법을 무시하고 감대로 약초를 섞다가 연구실을 폭파시켰던 괴짜 학자였습니다. 결과는 늘 대참사였지만 특유의 능청스러움과 해맑음으로 처벌을 요리조리 피해 갔습니다.",
        "trait": "현생의 흔적: 요리할 때 레시피 안 보고 '내 감'대로 넣다가 괴작 탄생.",
        "synergy": "최고의 궁합: 사고 치면 뒷수습해 주는 어른 / 상극: 매뉴얼 강박증 환자"
    },
    5: {
        "rank": "💰 제국 권력 실세",
        "job": "영지 예산 빼돌린 앙큼한 재정관 🧾",
        "quote": "“이건 영지의 복지를 위해 꼭 필요한 간식비였습니다. (영수증 삼킴)”",
        "story": "복잡한 세금과 장부를 칼같이 계산하면서도 교묘하게 자기 몫의 비상금을 챙겨두던 치밀한 전략가였습니다. 두뇌 회전이 빠르고 현실 감각이 남달라 절대 손해 보는 장사를 하지 않았습니다.",
        "trait": "현생의 흔적: 10원 단위 포인트 적립과 최저가 쿠폰을 귀신같이 찾아냄.",
        "synergy": "최고의 궁합: 밥 잘 사주는 통 큰 사람 / 상극: 100원 단위로 더치페이 따지는 사람"
    }
}

# 4. 헤더
st.markdown('<div class="magic-title">🔮 고대 영혼의 거울 🔮</div>', unsafe_allow_html=True)
st.markdown('<div class="magic-sub">당신의 현생 본능을 분석해 진짜 전생의 신분을 소환합니다.</div>', unsafe_allow_html=True)

# 5. 질문 폼 (선택지마다 직업 인덱스 점수 부여)
with st.form("past_life_form"):
    user_name = st.text_input("당신의 현생 이름(닉네임)을 입력하세요", placeholder="예: 홍길동")
    
    # 각 선택지마다 다른 성향(인덱스 0~5)으로 유도
    q1_choice = st.radio(
        "Q1. 주말 아침, 눈을 떴을 때 당신의 가장 솔직한 행동은?",
        options=[
            "냉장고부터 열어보고 뭘 먹을지 진지하게 고민한다 (식탐)",
            "알람 다 끄고 침대에서 뒹굴거리며 1시간 더 잔다 (낮잠)",
            "스마트폰 켜서 흥미진진한 핫게 글/유튜브부터 정독한다 (지식 탐구)",
            "이불 돌돌 말아서 사람 구경하며 멍때린다 (고양이 본능)",
            "갑자기 삘 꽂혀서 방 구조 바꾸거나 딴짓 시작한다 (엉뚱 창작)",
            "이번 달 카드값과 남은 잔고를 확인하며 하루 계획을 짠다 (재정 계산)"
        ]
    )
    
    q2_choice = st.radio(
        "Q2. 친구들과 무인도에 조난당했다! 당신의 역할은?",
        options=[
            "섬에 먹을 수 있는 버섯, 열매, 물고기가 어디 있는지 탐색한다",
            "가장 시원하고 그늘진 명당자리 찾아 누워 있는다",
            "탈출선 지도나 별자리 보며 비밀 탈출로를 연구한다",
            "모래사장에 누워 친구들이 구해오는 식량을 기다린다",
            "나뭇가지와 돌로 신기한 무기나 탈출 도구를 발명해본다",
            "남은 비상식량 분배 규칙을 정하고 배급 장부를 적는다"
        ]
    )

    q3_choice = st.radio(
        "Q3. 극심한 스트레스를 받았을 때 나만의 해소법은?",
        options=[
            "자극적이고 맛있는 배달 음식 잔뜩 시켜서 먹방 찍기",
            "휴대폰 비행기 모드 해놓고 하루 종일 암막 커튼 치고 자기",
            "혼자 서점 가거나 미결 사건·음모론 영상 보며 뇌 비우기",
            "집에서 혼자 조용히 골골송 부르며 아무것도 안 하기",
            "DIY 키트 만들기나 충동적인 새로운 취미 시작하기",
            "장바구니 담아뒀던 거 결제하며 금융 치료하기"
        ]
    )
    
    submit_button = st.form_submit_button("📜 전생의 영혼 판독하기")

# 6. 결과 계산
if submit_button:
    if not user_name.strip():
        st.warning("⚠️ 그대의 영혼을 호명할 이름을 먼저 적어주셔야 합니다!")
    else:
        # 선택지 인덱스 추출 (0 ~ 5)
        # 라디오 버튼 목록 내 순서를 그대로 점수로 환산
        q1_score = [
            "냉장고부터", "알람 다 끄고", "스마트폰 켜서", 
            "이불 돌돌", "갑자기 삘", "이번 달 카드값"
        ]
        q2_score = [
            "버섯, 열매", "그늘진 명당", "비밀 탈출로", 
            "친구들이 구해오는", "도구를 발명", "배급 장부"
        ]
        q3_score = [
            "배달 음식", "암막 커튼", "음모론 영상", 
            "골골송", "새로운 취미", "금융 치료"
        ]
        
        s1 = next(i for i, key in enumerate(q1_score) if key in q1_choice)
        s2 = next(i for i, key in enumerate(q2_score) if key in q2_choice)
        s3 = next(i for i, key in enumerate(q3_score) if key in q3_choice)
        
        # 이름의 첫 글자 코드도 살짝 가미하여 같은 답변이라도 이름에 따라 변주 생성
        name_seed = sum(ord(c) for c in user_name.strip())
        
        # 최종 인덱스 산출 (0~5 사이 골고루 도출)
        final_idx = (s1 * 3 + s2 * 2 + s3 + name_seed) % 6
        result = PAST_LIVES[final_idx]

        with st.spinner("🌌 시간의 강을 거슬러 전생의 기억을 정밀 추적 중..."):
            time.sleep(1.0)

        # 결과에 따라 축하 효과 변경
        if final_idx == 0:
            st.balloons()
        elif final_idx == 3:
            st.snow()
        else:
            st.toast("🔮 전생 소환 완료!")

        # 양피지 판독서 렌더링
        st.markdown(f"""
        <div class="parchment-card">
            <span class="badge-rank">{result['rank']}</span>
            <div class="job-title">{user_name.strip()}님의 전생은...<br>『{result['job']}』</div>
            <div class="quote-box">{result['quote']}</div>
            <p class="story-text"><strong>[영혼의 기록]</strong><br>{result['story']}</p>
            <div class="trait-item"><strong>🔍 {result['trait']}</strong></div>
            <div class="trait-item"><strong>💫 {result['synergy']}</strong></div>
        </div>
        """, unsafe_allow_html=True)
