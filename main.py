import random
import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="퐁당퐁당 MBTI 여행 연구소 ✨",
    page_icon="✈️",
    layout="centered"
)

# 2. 러블리한 파스텔 핑크/크림 테마 커스텀 스타일 (순수 CSS 인라인 주입)
st.markdown("""
<style>
    /* 전체 배경 톤 */
    .stApp {
        background: linear-gradient(135deg, #fff5f7 0%, #fcf0f8 50%, #f5f3ff 100%);
        font-family: 'Pretendard', sans-serif;
    }
    
    /* 카드 컴포넌트 */
    .cute-card {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 24px;
        margin: 16px 0;
        box-shadow: 0 8px 24px rgba(255, 182, 193, 0.25);
        border: 2px dashed #ffb6c1;
    }
    
    /* 귀여운 헤더 텍스트 */
    .cute-title {
        color: #ff6584;
        font-size: 2.2rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 8px;
    }
    .cute-sub {
        color: #7d6b7d;
        text-align: center;
        font-size: 1.05rem;
        margin-bottom: 24px;
    }
    
    /* 뱃지 */
    .pill-badge {
        display: inline-block;
        background-color: #ffe4e9;
        color: #ff477e;
        padding: 6px 14px;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-right: 6px;
        margin-bottom: 8px;
    }
    
    /* 버튼 스타일 오버라이드 */
    .stButton > button {
        background: linear-gradient(90deg, #ff758c 0%, #ff7eb3 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 30px !important;
        padding: 0.6rem 2rem !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(255, 117, 140, 0.4) !important;
        transition: transform 0.1s ease-in-out !important;
    }
    .stButton > button:hover {
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# 3. MBTI별 귀여운 여행 데이터
DESTINATIONS = {
    "INFP": {
        "place": "오스트리아 할슈타트 🦢",
        "tagline": "동화 속 호숫가에서 쓰는 감성 다이어리",
        "desc": "조용한 백조들과 반짝이는 호수를 바라보며 나만의 몽글몽글한 상상에 빠져보세요.",
        "tips": ["필름 카메라 챙기기", "호숫가 벤치에서 좋아하는 노래 듣기", "동화풍 엽서 사기"]
    },
    "ENFP": {
        "place": "인도네시아 발리 우붓 🌴",
        "tagline": "자유로운 영혼의 우당탕탕 힐링 모험",
        "desc": "요가 클래스에서 친구도 사귀고, 푸르른 정글 그네를 타며 긍정 에너지를 100% 충전해요!",
        "tips": ["정글 그네 타기", "현지 마켓에서 알록달록 원피스 사기", "우연히 만난 여행자와 수다떨기"]
    },
    "ISFJ": {
        "place": "일본 교토 아라시야마 🍵",
        "tagline": "포근하고 정갈한 골목길 산책",
        "desc": "사각사각 대나무 숲 소리와 따뜻한 말차 라떼가 지친 마음을 다정하게 안아줍니다.",
        "tips": ["아침 일찍 대나무 숲 걷기", "아기자기한 도자기 소품 구경", "따뜻한 당고 먹기"]
    },
    "ESFJ": {
        "place": "스페인 바르셀로나 ☀️",
        "tagline": "따사로운 햇살과 활기찬 타파스 파티",
        "desc": "누구와 가도 행복해지는 마법 같은 도시! 소중한 사람들과 맛있는 음식을 나누며 추억을 쌓아요.",
        "tips": ["보케리아 시장 먹방 투어", "가우디 건축물 앞에서 인생샷 찍어주기", "플라멩코 공연 관람"]
    },
    "INTJ": {
        "place": "스위스 체르마트 🏔️",
        "tagline": "완벽하고 고요한 알프스 설경",
        "desc": "완벽하게 정돈된 기차를 타고 마터호른을 마주하며 혼자만의 사색을 깊이 즐겨보세요.",
        "tips": ["산악열차 시간표 사전 체크", "조용한 산장에서 따뜻한 퐁뒤 먹기", "별빛 쏟아지는 밤하늘 보기"]
    },
    "ENTJ": {
        "place": "미국 뉴욕 맨해튼 🗽",
        "tagline": "반짝이는 야경과 심장을 뛰게 하는 빌딩숲",
        "desc": "세상의 중심에서 끝없는 영감을 얻고, 효율적인 루트로 알차게 뉴욕을 정복해보세요!",
        "tips": ["탑오브더락 전망대 야경", "브로드웨이 뮤지컬 명당 예매", "센트럴파크 아침 조깅"]
    },
    "INFJ": {
        "place": "체코 프라하 🏰",
        "tagline": "돌담길에 스며든 낭만과 깊은 위로",
        "desc": "노을 지는 카를교를 걸으며 마음속 깊은 생각들을 천천히 정리하기 가장 좋은 도시예요.",
        "tips": ["새벽 카를교 산책", "프라하성 뷰 카페에서 글쓰기", "오르골 가게 구경하기"]
    },
    "ENFJ": {
        "place": "이탈리아 피렌체 🎨",
        "tagline": "르네상스 감성과 낭만적인 붉은 지붕",
        "desc": "두오모 쿠폴라에 올라 따스한 주황빛 도시를 내려다보며 벅찬 사랑과 감동을 느껴보세요.",
        "tips": ["미켈란젤로 광장에서 와인 마시기", "가죽 시장에서 귀여운 키링 맞추기", "젤라또 맛집 도장깨기"]
    },
    "ISTP": {
        "place": "뉴질랜드 퀸스타운 🪂",
        "tagline": "스릴 만점 자연 속 액티비티 천국",
        "desc": "말보다는 행동! 번지점프, 루지, 제트보트로 일상의 지루함을 한 방에 날려버려요.",
        "tips": ["퍼그버거 먹기", "스카이라인 루지 연속 3번 타기", "호숫가 잔디밭에서 멍때리기"]
    },
    "ESTP": {
        "place": "태국 방콕 툭툭 🛺",
        "tagline": "화려한 야시장과 도파민 팡팡 나이트라이프",
        "desc": "맛있는 길거리 음식, 신나는 루프탑 바, 반짝이는 불빛 속에서 순간을 만끽하세요!",
        "tips": ["야시장에서 똠얌꿍 & 로띠 먹기", "화려한 루프탑 바 가기", "시원한 타이 마사지 받기"]
    },
    "ISFP": {
        "place": "프랑스 니스 & 에즈 🌊",
        "tagline": "지중해의 푸른 바다와 여유로운 낮잠",
        "desc": "아무 계획 없이 해변가 자갈밭에 누워 파도 소리를 듣고 젤라또를 먹는 것만으로도 충전 완료!",
        "tips": ["해변 파라솔 아래서 낮잠", "골목길 빈티지 상점 구경", "바다 보며 납작복숭아 먹기"]
    },
    "ESFP": {
        "place": "미국 하와이 와이키키 🌺",
        "tagline": "알로하! 훌라 댄스와 유쾌한 서핑",
        "desc": "우쿨렐레 음악과 시원한 파도! 보는 사람까지 기분 좋아지는 발랄한 에너지를 뿜어내봐요.",
        "tips": ["초보 서핑 강습 받기", "꽃핀 꽂고 셀카 남기기", "시원한 아사이볼 먹기"]
    },
    "INTP": {
        "place": "아이슬란드 레이캬비크 🌌",
        "tagline": "신비로운 오로라와 지구 밖 풍경",
        "desc": "화산, 빙하, 간헐천, 오로라까지! 자연의 경이로운 원리를 관찰하며 조용히 탐험해요.",
        "tips": ["블루라군 온천욕", "오로라 헌팅 투어 참여", "검은 모래 해변 산책"]
    },
    "ENTP": {
        "place": "영국 런던 🎡",
        "tagline": "클래식과 펑키함이 공존하는 아이디어의 장",
        "desc": "전통적인 박물관부터 힙한 쇼디치 골목까지, 지루할 틈 없이 새로운 자극이 넘쳐나요.",
        "tips": ["대영박물관 둘러보기", "쇼디치 빈티지 마켓 탐험", "런던아이 타고 야경 보기"]
    },
    "ISTJ": {
        "place": "독일 뮌헨 🍺",
        "tagline": "질서정연하고 클래식한 매력",
        "desc": "신뢰감 넘치는 도시 환경과 정확한 대중교통! 마음 편안하게 시원한 맥주와 학세를 즐겨요.",
        "tips": ["마리엔 광장 시계탑 공연 보기", "전통 브루어리에서 시원한 라거 마시기", "BMW 박물관 방문"]
    },
    "ESTJ": {
        "place": "싱가포르 🏙️",
        "tagline": "완벽하고 쾌적한 도심 속 가든",
        "desc": "치안 최고, 인프라 최고! 계획대로 척척 맞아떨어지는 깔끔하고 화려한 시티 라이프를 즐겨보세요.",
        "tips": ["가든스 바이 더 베이 야경 쇼", "인피니티 풀에서 인생샷", "칠리크랩 알차게 즐기기"]
    }
}

# 4. 헤더 뷰
st.markdown('<div class="cute-title">🎀 퐁당! MBTI 여행 연구소 ✈️</div>', unsafe_allow_html=True)
st.markdown('<div class="cute-sub">너의 MBTI를 콕 찌르면 가장 어울리는 러블리 여행지를 찾아줄게! (｡♥‿♥｡)</div>', unsafe_allow_html=True)

# 5. MBTI 선택 인풋
mbti_list = sorted(list(DESTINATIONS.keys()))
selected_mbti = st.selectbox(
    "💖 당신의 MBTI를 골라주세요:",
    options=mbti_list,
    index=0
)

# 6. 추천 버튼 클릭 시 인터랙션
if st.button("✨ 나만의 찰떡 여행지 찾기 뿅! ✨"):
    # 귀여운 축하 효과
    st.balloons()
    
    info = DESTINATIONS[selected_mbti]
    
    badges_html = "".join([f'<span class="pill-badge"># {tip}</span>' for tip in info["tips"]])
    
    # 결과 카드 렌더링
    st.markdown(f"""
    <div class="cute-card">
        <h3 style="color: #ff6584; margin-top:0;">💌 {selected_mbti} 맞춤 티켓 도착!</h3>
        <h2 style="color: #2c3e50; font-size: 1.8rem; margin: 8px 0;">{info['place']}</h2>
        <p style="color: #8e7dbe; font-weight: 600; font-size: 1.1rem; margin-bottom: 12px;">"{info['tagline']}"</p>
        <p style="color: #555; line-height: 1.6; font-size: 0.98rem;">{info['desc']}</p>
        <hr style="border: 0; border-top: 1px dashed #ffd1dc; margin: 16px 0;">
        <p style="font-weight: 700; color: #ff6584; margin-bottom: 8px;">🎀 연구소가 추천하는 즐길거리:</p>
        <div>{badges_html}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 귀여운 행운 메시지
    lucky_phrases = [
        "비행기 옆자리에 귀여운 고양이가 타는 행운이 따를지도 몰라요! 🐾",
        "여행지에서 평생 잊지 못할 노을을 만나게 될 거예요! 🌅",
        "가장 맛있는 디저트 가게가 우연히 눈앞에 나타날 거예요! 🍰"
    ]
    st.success(f"🍀 오늘의 여행 행운 포춘: {random.choice(lucky_phrases)}")

# 7. 푸터
st.markdown("""
<div style="text-align: center; color: #c0b0c5; font-size: 0.85rem; margin-top: 40px;">
    Made with 💖 for cozy travelers | Have a lovely trip!
</div>
""", unsafe_allow_html=True)
