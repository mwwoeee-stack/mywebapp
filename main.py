import streamlit as st

# 1. 페이지 레이아웃 및 탭 설정
st.set_page_config(
    page_title="L'Étoile Joaillerie | 탄생석 살롱",
    page_icon="💎",
    layout="centered"
)

# 2. 고급스러운 딥 네이비 & 샴페인 골드 테마 커스텀 CSS
st.markdown("""
<style>
    /* 전체 배경 및 폰트 */
    .stApp {
        background: radial-gradient(circle at top, #141b2d 0%, #0a0d16 100%);
        color: #e5e5e5;
        font-family: 'Cinzel', 'Pretendard', -apple-system, sans-serif;
    }

    /* 서브타이틀 및 헤더 */
    .brand-title {
        text-align: center;
        color: #d4af37;
        font-size: 2.2rem;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        margin-bottom: 4px;
        font-weight: 300;
    }
    
    .brand-sub {
        text-align: center;
        color: #a3aab8;
        font-size: 0.95rem;
        letter-spacing: 0.12em;
        margin-bottom: 36px;
    }

    /* 럭셔리 카드 박스 */
    .gem-card {
        background: linear-gradient(145deg, rgba(26, 34, 53, 0.85) 0%, rgba(15, 20, 32, 0.9) 100%);
        border: 1px solid rgba(212, 175, 55, 0.35);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6), inset 0 0 15px rgba(212, 175, 55, 0.05);
        border-radius: 12px;
        padding: 32px 28px;
        margin-top: 24px;
        text-align: center;
    }

    .gem-icon {
        font-size: 3.5rem;
        margin-bottom: 12px;
        filter: drop-shadow(0 0 12px rgba(212, 175, 55, 0.4));
    }

    .gem-name {
        color: #f7e7ce;
        font-size: 1.8rem;
        letter-spacing: 0.15em;
        margin-bottom: 6px;
        font-weight: 600;
    }

    .gem-eng {
        color: #d4af37;
        font-size: 0.85rem;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        margin-bottom: 20px;
    }

    .gem-divider {
        width: 60px;
        height: 1px;
        background: linear-gradient(90deg, transparent, #d4af37, transparent);
        margin: 16px auto;
    }

    .gem-meaning {
        color: #e5cf92;
        font-size: 1.05rem;
        letter-spacing: 0.08em;
        font-weight: 500;
        margin-bottom: 14px;
    }

    .gem-desc {
        color: #b0b8c4;
        font-size: 0.95rem;
        line-height: 1.8;
        letter-spacing: 0.02em;
        text-align: justify;
        word-break: keep-all;
        padding: 0 10px;
    }

    /* 우아한 키워드 태그 */
    .tag-container {
        margin-top: 22px;
    }

    .gem-tag {
        display: inline-block;
        border: 1px solid rgba(212, 175, 55, 0.45);
        color: #d4af37;
        background-color: rgba(212, 175, 55, 0.08);
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        letter-spacing: 0.08em;
        margin: 4px;
    }

    /* 버튼 스타일 오버라이드 */
    .stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #aa820a 100%) !important;
        color: #0d121c !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.65rem 2.2rem !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.15em !important;
        width: 100% !important;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.25) !important;
        transition: all 0.25s ease-in-out !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.45) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. 12개월 탄생석 데이터 (원석의 스토리와 상징성)
BIRTHSTONES = {
    1: {
        "name": "가넷",
        "eng": "Garnet",
        "icon": "🍷",
        "symbol": "진실과 변치 않는 우정, 충성",
        "color": "딥 버건디 레드",
        "desc": "라틴어의 '씨앗(Granum)'에서 유래한 가넷은 어둠 속에서도 빛을 잃지 않는 등불처럼 착용자를 지켜준다고 전해집니다. 고결한 충정과 흔들리지 않는 사랑을 약속하는 보석입니다.",
        "keywords": ["진실", "불변의 신의", "지혜", "권위"]
    },
    2: {
        "name": "자수정",
        "eng": "Amethyst",
        "icon": "🔮",
        "symbol": "평화와 고결함, 맑은 정신",
        "color": "로열 바이올렛",
        "desc": "과거 왕실과 귀족의 상징이었던 짙은 보랏빛의 자수정은 마음을 평온하게 가라앉히고 직관을 맑게 깨워줍니다. 차분한 통찰력과 내면의 깊은 평화를 선사합니다.",
        "keywords": ["성실", "내면의 평화", "직관", "고결"]
    },
    3: {
        "name": "아쿠아마린",
        "eng": "Aquamarine",
        "icon": "🌊",
        "symbol": "영원한 젊음과 행복, 총명",
        "color": "시스루 오션 블루",
        "desc": "'바다의 물'이라는 어원을 지닌 아쿠아마린은 고대 뱃사람들의 안전한 항해를 지키는 부적이었습니다. 흐르는 물처럼 유연한 지혜와 영원한 청춘의 온기를 품고 있습니다.",
        "keywords": ["영원한 청춘", "행복", "치유", "화합"]
    },
    4: {
        "name": "다이아몬드",
        "eng": "Diamond",
        "icon": "💎",
        "symbol": "영원불멸의 사랑과 순결, 승리",
        "color": "프리즘 클리어",
        "desc": "지구상에서 가장 견고하며 순수한 빛을 품은 광물입니다. 세월의 흐름에도 마모되지 않는 완벽한 순결함과 승리, 그리고 무엇과도 바꿀 수 없는 불멸의 서약을 의미합니다.",
        "keywords": ["불멸", "승리", "고결한 사랑", "순결"]
    },
    5: {
        "name": "에메랄드",
        "eng": "Emerald",
        "icon": "🌿",
        "symbol": "생명력과 부활, 찬란한 행운",
        "color": "딥 벨벳 그린",
        "desc": "클레오파트라가 가장 사랑했던 보석으로, 만물이 소생하는 5월의 짙은 녹음을 상징합니다. 지친 시야와 영혼을 달래주며 새로운 시작을 축복하는 신비로운 에너지를 지닙니다.",
        "keywords": ["새로운 시작", "행운", "영원한 생명", "통찰"]
    },
    6: {
        "name": "진주",
        "eng": "Pearl",
        "icon": "🦪",
        "symbol": "순결과 건강, 기품 있는 아름다움",
        "color": "루미너스 아이보리",
        "desc": "바다의 품에서 오랜 인내 끝에 탄생하는 유일한 유기질 보석입니다. 은은하고 우아한 오리엔트 광채는 시간이 흘러도 변하지 않는 클래식한 기품과 순수를 보여줍니다.",
        "keywords": ["청순", "건강", "고귀한 기품", "인내"]
    },
    7: {
        "name": "루비",
        "eng": "Ruby",
        "icon": "🌹",
        "symbol": "열정과 용기, 꺼지지 않는 사랑",
        "color": "피죤 블러드 레드",
        "desc": "'보석의 여왕'이라 불리는 루비는 타오르는 불꽃 같은 붉은빛으로 착용자에게 강력한 생명력과 용기를 북돋아 줍니다. 운명적인 매력과 불타는 정열의 표상입니다.",
        "keywords": ["열정", "정의", "불타는 사랑", "위엄"]
    },
    8: {
        "name": "페리도트",
        "eng": "Peridot",
        "icon": "✨",
        "symbol": "부부의 화합과 희망, 어둠의 극복",
        "color": "올리브 라임 골드",
        "desc": "운석 속에서도 발견되어 '우주의 보석'이라 불리는 황록색 결정입니다. 밤에도 빛을 잃지 않아 불안과 공포를 씻어내고, 가정의 화목과 따스한 희망을 전합니다.",
        "keywords": ["화합", "희망", "지혜", "안식"]
    },
    9: {
        "name": "사파이어",
        "eng": "Sapphire",
        "icon": "🌌",
        "symbol": "진실과 성실, 지혜와 불변",
        "color": "로열 미드나잇 블루",
        "desc": "가장 깊은 밤하늘을 닮은 사파이어는 예로부터 사제와 왕실의 신뢰를 상징했습니다. 흔들리지 않는 도덕적 지조와 현명한 판단력을 상징하는 품격 있는 보석입니다.",
        "keywords": ["성실", "지조", "진실", "고결한 영혼"]
    },
    10: {
        "name": "오팔",
        "eng": "Opal",
        "icon": "🪞",
        "symbol": "환희와 창의성, 다채로운 순수",
        "color": "오로라 무지갯빛",
        "desc": "빛의 각도에 따라 무지갯빛 스펙트럼이 춤추는 유색효과(Play of Color)를 지녔습니다. 자유로운 상상력과 아티스틱한 영감, 순수한 환희의 세계를 비춰줍니다.",
        "keywords": ["영감", "희망", "창의성", "행복"]
    },
    11: {
        "name": "토파즈",
        "eng": "Topaz",
        "icon": "🍂",
        "symbol": "건강과 우정, 찬란한 희망",
        "color": "임페리얼 앰버 골드",
        "desc": "태양의 눈부신 에너지를 머금은 듯 온화한 황금빛을 발산합니다. 슬픔을 걷어내고 따뜻한 우정을 맺어주며, 신체와 마음에 든든한 활력을 불어넣습니다.",
        "keywords": ["우정", "활력", "희망", "결백"]
    },
    12: {
        "name": "탄자나이트",
        "eng": "Tanzanite",
        "icon": "❄️",
        "symbol": "신비로운 변혁과 영성, 고귀함",
        "color": "벨벳 블루-바이올렛",
        "desc": "킬리만자로의 석양빛을 담아낸 20세기 최고의 발견으로 꼽힙니다. 푸른빛과 자줏빛이 매혹적으로 교차하며, 새로운 차원의 시작과 의식의 성장을 이끌어줍니다.",
        "keywords": ["변혁", "신비", "지성", "고귀한 성공"]
    }
}

# 4. 브랜딩 헤더
st.markdown('<div class="brand-title">L\'Étoile Joaillerie</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-sub">당신이 태어난 순간에 깃든 영원의 빛을 마주해보세요</div>', unsafe_allow_html=True)

# 5. 월 선택 셀렉트박스
month_options = [f"{i}월 (Month of {i:02d})" for i in range(1, 13)]
selected_str = st.selectbox("당신의 탄생월을 선택하십시오", month_options, index=0)
selected_month = int(selected_str.split("월")[0])

# 6. 감정 버튼 클릭 시 결과 카드 출력
if st.button("EXAMINE YOUR GEMSTONE"):
    gem = BIRTHSTONES[selected_month]
    tags_html = "".join([f'<span class="gem-tag">✦ {kw}</span>' for kw in gem["keywords"]])
    
    st.markdown(f"""
    <div class="gem-card">
        <div class="gem-icon">{gem['icon']}</div>
        <div class="gem-name">{gem['name']}</div>
        <div class="gem-eng">{gem['eng']} · {gem['color']}</div>
        <div class="gem-divider"></div>
        <div class="gem-meaning">"{gem['symbol']}"</div>
        <p class="gem-desc">{gem['desc']}</p>
        <div class="tag-container">
            {tags_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# 7. 품격 있는 푸터
st.markdown("""
<div style="text-align: center; color: #5a6474; font-size: 0.78rem; letter-spacing: 0.15em; margin-top: 50px; text-transform: uppercase;">
    Haute Joaillerie Atelier · Eternal Elegance
</div>
""", unsafe_allow_html=True)
