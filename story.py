import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="محتار في تخصصك الجامعي؟",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Add custom CSS to support RTL text and enhance the styling
st.markdown(
    """
    <style>
    body, html {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif; /* Ensure a font that supports Arabic well */
    }
    .main {
        background-color: #f8f9fa;
        padding: 20px;
    }
    .title {
        font-size: 3em;
        color: #fc6c85;
        font-weight: bold;
    }
    .content {
        font-size: 1.2em;
        color: #444444;
        line-height: 1.8; /* Increased line height for better readability */
        margin: 20px 0;
    }
    .footer {
        font-size: 1em;
        color: #777777;
        text-align: center;
        padding: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🤔 محتار في تخصصك الجامعي؟</div>', unsafe_allow_html=True)

st.markdown("""
<div class="content">
إذا كنت تواجه صعوبة في اختيار التخصص الجامعي المناسب، فأنت لست وحدك. العديد من الطلاب يشعرون بالحيرة عند اتخاذ هذا القرار المهم. لكن لا تشيل هم, بستعرض لك معلومات تساعدك على اتخاذ قرارك بناءً على سوق العمل واحتياجاته في المملكة العربية السعودية.
</div>
""", unsafe_allow_html=True)

# Optionally add a dropdown list for more interactive data exploration
option = st.selectbox(
    'اختر تصنيف البيانات لعرضها:',
    ('الوظائف الأكثر طلبًا', 'متوسط الرواتب', 'نوع الشركات', 'توزيع المناطق'),
    index=0
)

if option == 'الوظائف الأكثر طلبًا':
    st.image("Q1.png", caption="أكثر الوظائف طلبًا")
elif option == 'متوسط الرواتب':
    st.image("Q2.png", caption="متوسط الرواتب للوظائف الأكثر طلبًا")
elif option == 'نوع الشركات':
    st.image("Q3.png", caption="توزيع الوظائف بين الشركات الخاصة والحكومية")
elif option == 'توزيع المناطق':
    st.image("Q4.png", caption="توزيع الوظائف حسب المناطق")

st.markdown('في النهاية أتمنى إني ساعدتك في اختيار تخصصك الجامعي بناءً على الوظائف الأكثر طلبًا 😉')

# Conclusion
st.markdown("""
<div class="footer">
© 2024 Hatoon Aloqialy
</div>
""", unsafe_allow_html=True)
