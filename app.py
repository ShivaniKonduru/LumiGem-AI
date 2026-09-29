import streamlit as st

import os
from google import genai

# =========================================================
# LOAD GEMINI
# =========================================================



api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Gemini AI",
    page_icon="🌙",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   BACKGROUND
   ===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 82% 8%,
            rgba(255, 221, 145, 0.20),
            transparent 120px
        ),
        radial-gradient(
            circle at 5% 75%,
            rgba(92, 151, 205, 0.16),
            transparent 220px
        ),
        radial-gradient(
            circle at 95% 85%,
            rgba(151, 111, 185, 0.14),
            transparent 200px
        ),
        linear-gradient(
            135deg,
            #061329 0%,
            #0b203e 42%,
            #123457 72%,
            #0a1a35 100%
        );

    min-height: 100vh;
}


/* =====================================================
   REMOVE DEFAULT TOP SPACE
   ===================================================== */

.block-container {
    max-width: 820px;
    padding-top: 35px;
    padding-bottom: 60px;
}


/* =====================================================
   DECORATIVE STARS
   ===================================================== */

.stars {
    position: fixed;

    top: 0;
    left: 0;

    width: 100%;
    height: 100%;

    pointer-events: none;

    z-index: 0;

    background-image:
        radial-gradient(
            1px 1px at 10% 20%,
            rgba(255,255,255,0.8),
            transparent
        ),
        radial-gradient(
            1px 1px at 25% 70%,
            rgba(255,255,255,0.65),
            transparent
        ),
        radial-gradient(
            2px 2px at 70% 25%,
            rgba(255,255,255,0.7),
            transparent
        ),
        radial-gradient(
            1px 1px at 88% 55%,
            rgba(255,255,255,0.7),
            transparent
        ),
        radial-gradient(
            1px 1px at 55% 85%,
            rgba(255,255,255,0.6),
            transparent
        ),
        radial-gradient(
            2px 2px at 42% 15%,
            rgba(255,235,180,0.7),
            transparent
        );
}


/* =====================================================
   MAIN POSTER
   ===================================================== */

.poster {

    position: relative;

    z-index: 1;

    padding: 38px 42px 40px 42px;

    border-radius: 30px;

    background: rgba(11, 30, 57, 0.72);

    border: 1px solid rgba(166, 205, 230, 0.22);

    box-shadow:
        0 25px 70px rgba(0, 0, 0, 0.35),
        inset 0 1px 0 rgba(255,255,255,0.08);

    backdrop-filter: blur(12px);
}


/* =====================================================
   MOON
   ===================================================== */

.moon {

    position: absolute;

    top: 28px;
    right: 35px;

    width: 82px;
    height: 82px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 35%,
            #fffde9,
            #f9e9ae 65%,
            #e8ca76
        );

    box-shadow:
        0 0 20px rgba(255,231,160,0.65),
        0 0 55px rgba(255,225,135,0.28);
}


/* Moon craters */

.moon::before {

    content: "";

    position: absolute;

    width: 13px;
    height: 13px;

    top: 20px;
    left: 18px;

    border-radius: 50%;

    background: rgba(190,163,91,0.18);

    box-shadow:
        25px 12px 0 rgba(190,163,91,0.14),
        12px 37px 0 rgba(190,163,91,0.12);
}


/* =====================================================
   HEADER
   ===================================================== */

.header-symbol {

    color: #e8ca76;

    text-align: center;

    font-size: 18px;

    letter-spacing: 9px;

    margin-bottom: 10px;
}


h1 {

    color: #f8f3e5 !important;

    text-align: center;

    font-size: 48px !important;

    font-weight: 800;

    letter-spacing: 4px;

    margin: 0;

    text-shadow:
        0 4px 15px rgba(0,0,0,0.35);
}


/* =====================================================
   SUBTITLE
   ===================================================== */

.subtitle {

    text-align: center;

    color: #9fc5df;

    font-size: 14px;

    letter-spacing: 4px;

    margin-top: 10px;

    margin-bottom: 24px;
}


/* =====================================================
   GOLD DIVIDER
   ===================================================== */

.divider {

    display: flex;

    align-items: center;

    gap: 12px;

    margin: 0 auto 28px auto;

    width: 75%;
}


.divider::before,
.divider::after {

    content: "";

    flex: 1;

    height: 1px;

    background: linear-gradient(
        90deg,
        transparent,
        #dcbf72
    );
}


.divider span {

    color: #e8ca76;

    font-size: 14px;
}


/* =====================================================
   INTRO CARD
   ===================================================== */

.intro {

    text-align: center;

    padding: 14px 20px;

    margin-bottom: 25px;

    border-radius: 16px;

    background: rgba(255,255,255,0.055);

    border: 1px solid rgba(159,197,223,0.18);

    color: #dceaf3;

    font-size: 15px;
}


/* =====================================================
   INPUT LABEL
   ===================================================== */

.stTextArea label {

    color: #e7eef5 !important;

    font-weight: 600 !important;

    font-size: 16px !important;
}


/* =====================================================
   INPUT BOX
   ===================================================== */

.stTextArea textarea {

    background: #f7f9fc !important;

    color: #172940 !important;

    border: 2px solid #6e9fbd !important;

    border-radius: 18px !important;

    padding: 17px !important;

    font-size: 16px !important;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.18);

    transition: all 0.25s ease;
}


.stTextArea textarea:focus {

    border-color: #e5c875 !important;

    box-shadow:
        0 0 0 3px rgba(229,200,117,0.12),
        0 10px 30px rgba(0,0,0,0.22);
}


/* =====================================================
   BUTTON
   ===================================================== */

.stButton {

    margin-top: 14px;
}


.stButton > button {

    width: 100%;

    height: 55px;

    border-radius: 17px;

    border: 1px solid #e4c878;

    background:
        linear-gradient(
            100deg,
            #376f96,
            #4f84a8
        );

    color: white;

    font-size: 17px;

    font-weight: 700;

    letter-spacing: 1.5px;

    box-shadow:
        0 8px 22px rgba(0,0,0,0.25);

    transition: all 0.25s ease;
}


.stButton > button:hover {

    transform: translateY(-3px);

    background:
        linear-gradient(
            100deg,
            #4d86aa,
            #6097b8
        );

    box-shadow:
        0 12px 28px rgba(0,0,0,0.32);
}


/* =====================================================
   RESPONSE
   ===================================================== */

.response-box {

    margin-top: 28px;

    padding: 25px 28px;

    background: #f7f9fc;

    border-radius: 20px;

    border: 1px solid #9dbbce;

    border-top: 5px solid #e5c875;

    color: #1b3048;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.25);
}


.response-box .response-title {

    color: #376783;

    font-size: 20px;

    font-weight: 800;

    margin-bottom: 12px;
}


.response-box .response-text {

    color: #263b51;

    font-size: 16px;

    line-height: 1.75;
}


/* =====================================================
   STATUS BOXES
   ===================================================== */

.stSuccess,
.stWarning,
.stError {

    border-radius: 13px !important;

    margin-top: 15px;
}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {

    text-align: center;

    margin-top: 28px;

    color: #789bb5;

    font-size: 12px;

    letter-spacing: 3px;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {

    .poster {
        padding: 30px 20px;
    }

    .moon {
        width: 55px;
        height: 55px;
        right: 20px;
    }

    h1 {
        font-size: 36px !important;
    }

    .subtitle {
        font-size: 11px;
        letter-spacing: 2px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# DECORATIVE BACKGROUND
# =========================================================

st.markdown(
    '<div class="stars"></div>',
    unsafe_allow_html=True
)


# =========================================================
# MAIN POSTER
# =========================================================

st.markdown('<div class="poster">', unsafe_allow_html=True)

st.markdown(
    '<div class="moon"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="header-symbol">✦ · ✦ · ✦</div>',
    unsafe_allow_html=True
)

st.title("GEMINI AI")

st.markdown(
    '<div class="subtitle">YOUR INTELLIGENT AI COMPANION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="divider"><span>✦</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="intro">
        Ask a question, explore an idea, or let Gemini help you think.
        <br>
        <b>Your curiosity starts here.</b>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PROMPT
# =========================================================

prompt = st.text_area(
    "Enter your prompt",
    placeholder="What would you like to know?"
)


# =========================================================
# GENERATE RESPONSE
# =========================================================

if st.button("✦  GENERATE RESPONSE  ✦"):

    if prompt.strip():

        with st.spinner("Gemini is thinking..."):

            try:

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                st.success("Response generated successfully.")

                st.markdown(
                    f"""
                    <div class="response-box">

                        <div class="response-title">
                            ✦ Gemini's Response
                        </div>

                        <div class="response-text">
                            {response.text}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:

                if "503" in str(e) or "UNAVAILABLE" in str(e):

                    st.warning(
                        "Gemini is temporarily busy. "
                        "Please wait a little and try again."
                    )

                else:

                    st.error(f"Error: {e}")

    else:

        st.warning("Please enter a prompt.")


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        ✦ POWERED BY GEMINI AI ✦
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
