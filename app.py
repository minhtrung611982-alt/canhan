import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# Cấu hình trang
st.set_page_config(
    page_title="Giới thiệu cá nhân",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh
def load_css():
    st.markdown("""
    <style>
        .main-header {
            font-size: 3rem;
            font-weight: bold;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .sub-header {
            font-size: 1.5rem;
            color: #666;
            text-align: center;
            margin-bottom: 2rem;
        }
        .section-header {
            font-size: 2rem;
            font-weight: bold;
            color: #1f77b4;
            border-bottom: 3px solid #1f77b4;
            padding-bottom: 0.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        .skill-badge {
            display: inline-block;
            background-color: #e3f2fd;
            color: #1976d2;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            margin: 0.3rem;
            font-weight: 500;
        }
        .project-card {
            background-color: #f5f5f5;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            border-left: 4px solid #1f77b4;
        }
        .contact-info {
            font-size: 1.1rem;
            margin: 0.5rem 0;
        }
        .stButton>button {
            width: 100%;
            background-color: #1f77b4;
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

load_css()

# Header chính
st.markdown('<p class="main-header">Xin chào, tôi là [Tên của bạn]</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Lập trình viên | Nhà phát triển phần mềm</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("📋 Menu")
    st.markdown("---")
    
    # Avatar (có thể thay bằng ảnh thật)
    st.image("https://via.placeholder.com/200", width=200, caption="Ảnh đại diện")
    
    st.markdown("### Thông tin liên hệ")
    st.markdown("📧 Email: your.email@example.com")
    st.markdown("📱 Phone: +84 XXX XXX XXX")
    st.markdown("🌐 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com)")
    st.markdown("💻 GitHub: [github.com/yourusername](https://github.com)")
    st.markdown("📍 Địa chỉ: Thành phố, Việt Nam")
    
    st.markdown("---")
    st.markdown("### Tải CV")
    with open("cv.pdf", "w") as f:
        f.write("CV placeholder")
    # st.download_button("📥 Tải CV", "cv.pdf", "application/pdf")

# Tab navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Giới thiệu", "💼 Kinh nghiệm", "🛠️ Kỹ năng", "📁 Dự án", "📧 Liên hệ"])

# Tab 1: Giới thiệu
with tab1:
    st.markdown('<p class="section-header">Về tôi</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Tôi là một lập trình viên đam mê với công nghệ và phát triển phần mềm. 
        Với kinh nghiệm trong việc xây dựng các ứng dụng web và mobile, tôi luôn 
        tìm kiếm những cơ hội để học hỏi và phát triển bản thân.
        
        **Sở thích:**
        - 💻 Lập trình và phát triển phần mềm
        - 📚 Đọc sách về công nghệ
        - 🎮 Chơi game
        - 🏃 Thể thao
        
        **Mục tiêu nghề nghiệp:**
        Trở thành một Full-stack Developer chuyên nghiệp, đóng góp vào các dự án 
        có ý nghĩa và tạo ra những sản phẩm công nghệ chất lượng cao.
        """)
    
    with col2:
        st.markdown("### Thông tin cá nhân")
        st.markdown("**Ngày sinh:** DD/MM/YYYY")
        st.markdown("**Quốc tịch:** Việt Nam")
        st.markdown("**Ngôn ngữ:**")
        st.markdown("- Tiếng Việt (Bản ngữ)")
        st.markdown("- Tiếng Anh (Trung bình - Khá)")

# Tab 2: Kinh nghiệm
with tab2:
    st.markdown('<p class="section-header">Kinh nghiệm làm việc</p>', unsafe_allow_html=True)
    
    exp1, exp2, exp3 = st.columns(3)
    
    with exp1:
        st.markdown("""
        <div class="project-card">
            <h3>🚀 Lập trình viên Full-stack</h3>
            <p><strong>Công ty ABC</strong></p>
            <p><em>2022 - Hiện tại</em></p>
            <ul>
                <li>Phát triển ứng dụng web với React và Node.js</li>
                <li>Thiết kế và quản lý cơ sở dữ liệu</li>
                <li>Làm việc với team Agile</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with exp2:
        st.markdown("""
        <div class="project-card">
            <h3>💻 Lập trình viên Frontend</h3>
            <p><strong>Công ty XYZ</strong></p>
            <p><em>2020 - 2022</em></p>
            <ul>
                <li>Xây dựng giao diện người dùng với React</li>
                <li>Tối ưu hóa hiệu suất website</li>
                <li>Responsive design</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with exp3:
        st.markdown("""
        <div class="project-card">
            <h3>🎓 Thực tập sinh</h3>
            <p><strong>Công ty DEF</strong></p>
            <p><em>2019 - 2020</em></p>
            <ul>
                <li>Học hỏi và thực hành lập trình</li>
                <li>Hỗ trợ team phát triển</li>
                <li>Tham gia các dự án nhỏ</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<p class="section-header">Học vấn</p>', unsafe_allow_html=True)
    
    edu_col1, edu_col2 = st.columns(2)
    
    with edu_col1:
        st.markdown("""
        <div class="project-card">
            <h3>🎓 Đại học Công nghệ</h3>
            <p><strong>Khoa Công nghệ Thông tin</strong></p>
            <p><em>2016 - 2020</em></p>
            <p>Chuyên ngành: Khoa học Máy tính</p>
            <p>GPA: 3.5/4.0</p>
        </div>
        """, unsafe_allow_html=True)
    
    with edu_col2:
        st.markdown("""
        <div class="project-card">
            <h3>📜 Chứng chỉ</h3>
            <ul>
                <li>AWS Certified Developer</li>
                <li>Google Cloud Professional</li>
                <li>React Developer Certification</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Tab 3: Kỹ năng
with tab3:
    st.markdown('<p class="section-header">Kỹ năng kỹ thuật</p>', unsafe_allow_html=True)
    
    st.markdown("### Ngôn ngữ lập trình")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.progress(0.9)
        st.markdown("**Python** - 90%")
        st.progress(0.85)
        st.markdown("**JavaScript** - 85%")
        st.progress(0.8)
        st.markdown("**Java** - 80%")
    
    with col2:
        st.progress(0.75)
        st.markdown("**C++** - 75%")
        st.progress(0.7)
        st.markdown("**TypeScript** - 70%")
        st.progress(0.65)
        st.markdown("**Go** - 65%")
    
    with col3:
        st.progress(0.6)
        st.markdown("**PHP** - 60%")
        st.progress(0.55)
        st.markdown("**Ruby** - 55%")
    
    st.markdown("### Framework & Công nghệ")
    skills = [
        "React", "Node.js", "Django", "Flask", "Express.js",
        "Vue.js", "Angular", "Spring Boot", "FastAPI", "Streamlit",
        "TensorFlow", "PyTorch", "Docker", "Kubernetes", "AWS",
        "MongoDB", "PostgreSQL", "MySQL", "Redis", "Git"
    ]
    
    skills_html = "".join([f'<span class="skill-badge">{skill}</span>' for skill in skills])
    st.markdown(f'<div>{skills_html}</div>', unsafe_allow_html=True)
    
    st.markdown('<p class="section-header">Kỹ năng mềm</p>', unsafe_allow_html=True)
    soft_skills = [
        "Giao tiếp", "Làm việc nhóm", "Giải quyết vấn đề",
        "Quản lý thời gian", "Lãnh đạo", "Sáng tạo",
        "Thích ứng nhanh", "Học hỏi liên tục"
    ]
    
    soft_skills_html = "".join([f'<span class="skill-badge">{skill}</span>' for skill in soft_skills])
    st.markdown(f'<div>{soft_skills_html}</div>', unsafe_allow_html=True)

# Tab 4: Dự án
with tab4:
    st.markdown('<p class="section-header">Dự án nổi bật</p>', unsafe_allow_html=True)
    
    proj1, proj2 = st.columns(2)
    
    with proj1:
        st.markdown("""
        <div class="project-card">
            <h3>🌐 Website E-commerce</h3>
            <p>Ứng dụng web bán hàng trực tuyến với đầy đủ tính năng thanh toán, 
            quản lý đơn hàng và quản trị viên.</p>
            <p><strong>Công nghệ:</strong> React, Node.js, MongoDB, Stripe</p>
            <p><strong>Link:</strong> <a href="#">Xem dự án</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3>📱 Ứng dụng Mobile</h3>
            <p>Ứng dụng quản lý công việc và ghi chú với giao diện đẹp và dễ sử dụng.</p>
            <p><strong>Công nghệ:</strong> React Native, Firebase, Redux</p>
            <p><strong>Link:</strong> <a href="#">Xem dự án</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    with proj2:
        st.markdown("""
        <div class="project-card">
            <h3>🤖 AI Chatbot</h3>
            <p>Chatbot thông minh sử dụng Machine Learning để trả lời câu hỏi 
            và hỗ trợ khách hàng.</p>
            <p><strong>Công nghệ:</strong> Python, TensorFlow, Flask, NLP</p>
            <p><strong>Link:</strong> <a href="#">Xem dự án</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3>📊 Dashboard Analytics</h3>
            <p>Dashboard phân tích dữ liệu với biểu đồ trực quan và báo cáo tự động.</p>
            <p><strong>Công nghệ:</strong> Python, Streamlit, Pandas, Plotly</p>
            <p><strong>Link:</strong> <a href="#">Xem dự án</a></p>
        </div>
        """, unsafe_allow_html=True)

# Tab 5: Liên hệ
with tab5:
    st.markdown('<p class="section-header">Liên hệ với tôi</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📬 Thông tin liên hệ")
        st.markdown("""
        <div class="contact-info">
            <p>📧 <strong>Email:</strong> your.email@example.com</p>
            <p>📱 <strong>Điện thoại:</strong> +84 XXX XXX XXX</p>
            <p>🌐 <strong>Website:</strong> www.yourwebsite.com</p>
            <p>📍 <strong>Địa chỉ:</strong> Thành phố, Việt Nam</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🔗 Mạng xã hội")
        st.markdown("""
        - [LinkedIn](https://linkedin.com)
        - [GitHub](https://github.com)
        - [Facebook](https://facebook.com)
        - [Twitter](https://twitter.com)
        """)
    
    with col2:
        st.markdown("### 💬 Gửi tin nhắn")
        
        contact_form = st.form("contact_form")
        contact_form.text_input("Tên của bạn")
        contact_form.text_input("Email")
        contact_form.text_area("Tin nhắn", height=150)
        submit_button = contact_form.form_submit_button("Gửi tin nhắn")
        
        if submit_button:
            st.success("Cảm ơn bạn đã liên hệ! Tôi sẽ phản hồi sớm nhất có thể.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; padding: 2rem;'>"
    "© 2024 [Tên của bạn]. Được tạo bằng Streamlit ❤️"
    "</div>",
    unsafe_allow_html=True
)

