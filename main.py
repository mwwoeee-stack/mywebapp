import streamlit as st
import time
import hashlib

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="영혼의 거울 | 전생 직업·신분 판독기",
    page_icon="🔮",
    layout="centered"
)

# 2. 마법 고서 / 앤티크 양피지 감성 커스텀 CSS
st.markdown("""
<style>
    /* 전체 배경: 어두운 신비로운 서재 톤 */
    .stApp {
        background: radial-gradient(circle at top, #231d2b 0%, #110d16 100%);
        color: #e2d9cc;
        font-family: 'Pretendard', sans-serif;
    }

    /* 상단 마법서 타이틀 */
    .magic-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #e5b567;
        text-shadow: 0 0 15px rgba(229, 181, 103, 0.4);
        margin-bottom: 6px;
        letter-spacing: 0.05em;
    }
    
    .magic-sub {
        text-align: center;
        color: #a89bb5;
        font-size: 0.95rem;
        margin-bottom: 28px;
    }

    /* 양피지 문서 스타일 카드 */
    .parchment-card {
        background: linear-gradient(135deg, #fdfbf7 0%, #f4ebd9 100%);
        color: #2b1f14;
        border: 2px solid #c8a365;
        border-radius: 12px;
        padding: 30px 24px;
        margin: 20px 0;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.7), inset 0 0 40px rgba(184, 134, 11, 0.15);
        position: relative;
    }

    .badge-rank {
        display: inline-block;
        background-color: #8c2d19;
        color: #fff;
        padding: 4px 14px;
        border-radius: 4px;
        font-size: 0.85rem;
        font-weight: bold;
        letter-spacing: 0.1em;
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

    /* 버튼 스타일 */
    .stButton > button {
        background: linear-gradient(135deg, #8c2d19 0%, #d45d3a 100%) !important;
        color: #fff !important;
        border: 1px solid #e5b567 !important;
        border-radius: 8px !important;
        padding: 0.7rem 2rem !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.1em !important;
        width: 100% !important;
        box-shadow: 0 4px 20px rgba(212, 93, 58, 0.4) !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(229, 181, 103, 0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. 전생 데이터베이스 (유쾌하고 다양한 결과 목록)
PAST_LIVES = [
    {
        "rank": "🏛️ 왕실 귀족 계급",
        "job": "궁궐 시식 기미상궁 🍲",
        "quote": "“한 입만 더 먹어보면 독이 있는지 확실히 알 수 있겠사옵니다.”",
        "story": "수라상에 올라오는 모든 산해진미를 임금보다 먼저 맛보던 절대 미각의 소유자였습니다. 뛰어난 미각과 남다른 식탐으로 왕의 총애를 받았으며, 늘 '배부르다'면서도 마지막 디저트까지 싹 비우던 전설이 전해집니다.",
        "trait": "현생의 흔적: 친구 떡볶이 한 입 뺏어먹을 때 가장 눈빛이 날카로움.",
        "synergy": "최고의 궁합: 주방장 영혼을 가진 사람 / 상극: 맛집 줄 서기 싫어하는 사람"
    },
    {
        "rank": "⚔️ 방랑 무림 / 용병단",
        "job": "전설의 낮잠 자는 방랑 무사 🗡️",
        "quote": "“칼을 뽑는 건 귀찮지만, 낮잠을 방해받는 건 더 귀찮다.”",
        "story": "검 한 자루로 일대를 평정했으나, 나무 그늘 아래서 낮잠 자는 것을 천하통일보다 좋아했던 풍운아였습니다. 평소엔 멍하니 누워있다가도 동료가 위험에 처하면 반사적으로 칼을 휘둘러 승리하던 게으른 천재였습니다.",
        "trait": "현생의 흔적: 알람을 5분 간격으로 10개 맞추고도 다시 잠듦.",
        "synergy": "최고의 궁합: 조용히 덮을 이불 챙겨주는 사람 / 상극: 아침 6시에 깨우는 사람"
    },
    {
        "rank": "📜 지식인 / 비밀 결사",
        "job": "황실 도서관 금서 밀반출 총책 📚",
        "quote": "“쉿, 읽지 말라면 더 읽고 싶어지는 게 인간의 본성이지.”",
        "story": "황제가 지정한 수천 권의 금지된 마법서와 비밀 일기장을 몰래 복사해 백성들에게 은밀히 퍼뜨리던 지하 지식인이었습니다. 언제나 밤새 책을 읽고 호기심을 주체하지 못해 위험한 음모론을 먼저 간파하곤 했습니다.",
        "trait": "현생의 흔적: 새벽 3시에 인터넷 나무위키나 음모론 채널 정독 중.",
        "synergy": "최고의 궁합: 비밀 공유할 수 있는 수다쟁이 / 상극: 스포일러 하는 사람"
    },
    {
        "rank": "🐾 정령계 / 신수",
        "job": "성주님 무릎 위 낮잠 고양이 🐱",
        "quote": "“골골골... 인간아, 츄르나 내놓거라.”",
        "story": "전생에 인간이 아니었을 가능성이 높습니다! 쌀쌀맞은 태도로 성주의 마음을 쥐락펴락하며 따뜻한 난로 앞에서 온종일 뒹굴거리던 영물 고양이였습니다. 아무것도 안 하고 숨만 쉬어도 모두가 예뻐해 주던 완벽한 생애였습니다.",
        "trait": "현생의 흔적: 집 밖으로 나가는 순간 급속도로 기력이 방전됨.",
        "synergy": "최고의 궁합: 집안일 다 해주는 집사 성향 / 상극: 잔소리 많은 사람"
    },
    {
        "rank": "✨ 신비주의 / 연금술",
        "job": "황금 대신 불꽃놀이만 터뜨린 연금술사 🧪",
        "quote": "“돌을 금으로 바꾸려다 실험실을 또 태워먹었군요! 하지만 빛깔이 참 예쁘죠?”",
        "story": "황제의 막대한 후원을 받으며 연구했으나 매번 레시피를 잘못 조합해 폭발과 함께 알록달록한 연기만 피워 올리던 엉뚱한 연금술사였습니다. 결과는 망해도 특유의 당당함과 긍정적인 말솜씨로 처벌을 피해 갔습니다.",
        "trait": "현생의 흔적: 요리할 때 계량 안 하고 감으로 넣다가 신메뉴 창조함.",
        "synergy": "최고의 궁합: 뒷수습 잘해주는 현실주의자 / 상극: 융통성 없는 완벽주의자"
    },
    {
        "rank": "🏰 제국 고위 관직",
        "job": "영지 예산 횡령(?) 의혹의 천재 재정관 💰",
        "quote": "“이건 영지의 미래를 위한 필수 복지 비용입니다. (영수증 파쇄)”",
        "story": "모든 영지의 세금과 재정을 한 치의 오차도 없이 계산하던 냉철한 관료였습니다. 다만 '내 간식비' 항목만큼은 예술적인 분식회계로 숨겨놓아 누구도 찾지 못했던 치밀하고 앙큼한 브레인의 소유자였습니다.",
        "trait": "현생의 흔적: 할인 쿠폰과 포인트 적립률을 칼같이 계산함.",
        "synergy": "최고의 궁합: 돈 쓸 때 시원시원한 호구(?) / 상극: 1원 단위까지 더치페이 따지는 사람"
    }
]

# 4. 상단 헤더
st.markdown('<div class="magic-title">🔮 고대 영혼의 거울 🔮</div>', unsafe_allow_html=True)
st.markdown('<div class="magic-sub">당신의 현생 습관 뒤에 숨겨진 전생의 신분과 비밀 직업을 소환합니다.</div>', unsafe_allow_html=True)

# 5. 질문 폼
with st.form("past_life_form"):
    user_name = st.text_input("당신의 현생 이름(또는 닉네임)을 입력하세요", placeholder="예: 홍길동, 냥냥이")
    
    q1 = st.selectbox(
        "Q1. 주말 아침, 눈을 떴을 때 당신의 진짜 첫 행동은?",
        [
            "선택해주세요...",
            "스마트폰 쥐고 침대에서 뒹굴거리며 1시간 이상 멍때리기",
            "냉장고 문부터 열어보고 뭘 먹을지 진지하게 고민하기",
            "밀린 계획이나 청소부터 척척 해치우기",
            "어제 못 본 유튜브, 커뮤니티, 책 몰아보기"
        ]
    )
    
    q2 = st.selectbox(
        "Q2. 친구들과 무인도에 표류했을 때 당신이 맡을 역할은?",
        [
            "선택해주세요...",
            "누가 시키지 않아도 제일 그늘진 명당 자리 찾아서 누워있기",
            "섬에 먹을 수 있는 열매나 물고기가 어디 있는지 탐색하기",
            "남은 식량 배급 규칙과 탈출 계획표 세우기",
            "나뭇가지로 신기한 무기나 불 피우는 장치 발명해보기"
        ]
    )
    
    q3 = st.selectbox(
        "Q3. 화가 나거나 스트레스를 극도로 받을 때 당신의 대처법은?",
        [
            "선택해주세요...",
            "맛있는 매운 음식이나 달콤한 디저트를 잔뜩 먹는다",
            "동굴 속으로 들어가 아무와도 말하지 않고 혼자 잠잔다",
            "쇼핑을 하거나 통장 잔고를 보며 금융 치료를 한다",
            "밤새 다른 일이나 취미에 몰두하며 잊어버린다"
        ]
    )
    
    submit_button = st.form_submit_button("📜 전생의 영혼 판독하기")

# 6. 결과 도출 로직
if submit_button:
    if not user_name.strip():
        st.warning("⚠️ 그대의 영혼을 호명할 이름(닉네임)을 먼저 적어주셔야 합니다!")
    elif q1.startswith("선택") or q2.startswith("선택") or q3.startswith("선택"):
        st.warning("⚠️ 고대의 거울이 반응하도록 모든 질문에 솔직히 답해주세요!")
    else:
        # 몰입감을 주는 딜레이 연출
        with st.spinner("🌌 시간의 강을 거슬러 전생의 기억을 소환하는 중..."):
            time.sleep(1.2)
        
        # 입력값들을 조합하여 고유한 해시값 생성 (같은 이름과 응답이면 일관된 결과 도출)
        seed_str = f"{user_name.strip()}-{q1}-{q2}-{q3}"
        idx = int(hashlib.md5(seed_str.encode('utf-8')).hexdigest(), 16) % len(PAST_LIVES)
        result = PAST_LIVES[idx]
        
        st.snow()  # 신비로운 효과 연출
        
        # 양피지 판독서 렌더링
        st.markdown(f"""
        <div class="parchment-card">
            <span class="badge-rank">{result['rank']}</span>
            <div class="job-title">{user_name}님의 전생은...<br>『{result['job']}』</div>
            <div class="quote-box">{result['quote']}</div>
            <p class="story-text"><strong>[영혼의 기록]</strong><br>{result['story']}</p>
            <div class="trait-item"><strong>🔍 {result['trait']}</strong></div>
            <div class="trait-item"><strong>💫 {result['synergy']}</strong></div>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 전생의 카르마가 강하게 느껴지신다면 친구들에게도 공유해 그들의 전생을 확인해보세요!")

# 7. 하단 푸터
st.markdown("""
<div style="text-align: center; color: #6a5e78; font-size: 0.8rem; margin-top: 40px;">
    Chronicles of Past Souls · 순수 오락용 판독기입니다.
</div>
""", unsafe_allow_html=True)
