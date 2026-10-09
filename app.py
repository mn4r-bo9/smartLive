import streamlit as st
import datetime
import random

# --- إعدادات الصفحة الأساسية ---
st.set_page_config(
    page_title="Smart Life OS | المنظم الذكي",
    page_icon="🌿",
    layout="wide"
)

# --- تصميم الألوان والواجهة (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #F8F9FA;
        color: #2C3E50;
    }
    
    /* بطاقات العرض الإحصائي */
    .metric-card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.04);
        border: 1px solid #E2E8F0;
        text-align: center;
    }
    
    /* نصائح الذكاء الاصطناعي */
    .ai-box {
        background-color: #F0F4FF;
        border-right: 4px solid #4C51BF;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
        color: #2C5282;
    }

    /* أزرار وعناوين */
    h1, h2, h3 {
        color: #2D3748 !important;
        font-weight: 600;
    }
    
    .stButton>button {
        border-radius: 8px;
        background-color: #4A5568;
        color: white;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- التهيئة وإدارة البيانات (Session State) ---
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "workout_plan" not in st.session_state:
    st.session_state.workout_plan = []
if "meals" not in st.session_state:
    st.session_state.meals = []
if "sleep_hours" not in st.session_state:
    st.session_state.sleep_hours = 8.0

# --- رأس الصفحة والهيدر ---
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.title("🌿 Smart Life OS")
    st.caption("منصتك الذكية لتنظيم الوقت، التمارين، التغذية، والنوم")
with col_head2:
    st.write("")
    st.info(f"📅 اليوم: {datetime.date.today().strftime('%A, %d %B')}")

st.divider()

# --- قسم لوحة المؤشرات السريعة (Dashboard) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
        <div class="metric-card">
            <h4>😴 ساعات النوم</h4>
            <h2>{} ساعات</h2>
        </div>
    """.format(st.session_state.sleep_hours), unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-card">
            <h4>🏃 التمارين</h4>
            <h2>{} تمارين</h2>
        </div>
    """.format(len(st.session_state.workout_plan)), unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="metric-card">
            <h4>🥗 الوجبات</h4>
            <h2>{} وجبات</h2>
        </div>
    """.format(len(st.session_state.meals)), unsafe_allow_html=True)

with col4:
    completed = len([t for t in st.session_state.tasks if t.get('done')])
    st.markdown("""
        <div class="metric-card">
            <h4>✅ المهام المكتملة</h4>
            <h2>{}/{}</h2>
        </div>
    """.format(completed, len(st.session_state.tasks)), unsafe_allow_html=True)

st.write("")
st.write("")

# --- التبويبات الرئيسة للتطبيق ---
tab_ai, tab_workout, tab_nutrition, tab_sleep, tab_tasks = st.tabs([
    "🤖 المساعد الذكي", 
    "🏋️ جدول التمارين", 
    "🥗 النظام الغذائي", 
    "😴 تنظيم النوم", 
    "📌 المهام اليومية"
])

# -------------------------------------------------------------
# 1. المساعد الذكي (AI Assistant)
# -------------------------------------------------------------
with tab_ai:
    st.subheader("💡 نصائح واقترحات من الذكاء الاصطناعي")
    
    st.markdown("""
        <div class="ai-box">
            <b>توصية اليوم الذكية:</b> شرب 500 مل من الماء فور الاستيقاظ يرفع مستوى الطاقة ويحسن عملية الأيض أثناء التمارين اليومية.
        </div>
    """, unsafe_allow_html=True)

    st.write("### 💬 اسأل المساعد الذكي لتحسين جدولك")
    user_query = st.text_input("أدخل ما تبحث عنه (مثال: اقترح لي جدول تمارين للمبتدئين، أو وجبة عشاء صحية)...")
    
    if st.button("طلب اقتراح ذكي"):
        if user_query:
            # محاكاة لرد الذكاء الاصطناعي الذكي
            responses = [
                "بناءً على طلبك، يفضل أداء 20 دقيقة تمارين كارديو خفيفة عصراً، مع شرب الماء بكثرة.",
                "اقتراح وجبة: صدر دجاج مشوي + أرز بني + سلطة خضراء مع زيت الزيتون (حوالي 500 سعرة).",
                "لتحسين جودة نومك اليوم: حاول إيقاف استخدام الشاشات والأجهزة قبل النوم بـ 45 دقيقة."
            ]
            st.success(f"🤖 **اقتراح الذكاء الاصطناعي:** {random.choice(responses)}")
        else:
            st.warning("يرجى كتابة سؤالك أو طلبك أولاً.")

# -------------------------------------------------------------
# 2. جدول التمارين الرياضية
# -------------------------------------------------------------
with tab_workout:
    st.subheader("🏃 تنظيم التمارين والأنشطة")
    
    with st.form("workout_form", clear_on_submit=True):
        col_w1, col_w2, col_w3 = st.columns([2, 1, 1])
        with col_w1:
            ex_name = st.text_input("اسم التمرين", placeholder="مثال: مشي سريع، تمرين ضغط...")
        with col_w2:
            ex_time = st.time_input("التوقيت", value=datetime.time(17, 0))
        with col_w3:
            ex_duration = st.number_input("المدة (بالدقائق)", min_value=10, max_value=180, value=30)
        
        submit_workout = st.form_submit_button("إضافة التمرين ➕")
        if submit_workout and ex_name:
            st.session_state.workout_plan.append({
                "name": ex_name, 
                "time": ex_time.strftime("%I:%M %p"), 
                "duration": ex_duration
            })
            st.rerun()

    if st.session_state.workout_plan:
        st.write("---")
        for idx, item in enumerate(st.session_state.workout_plan):
            col_a, col_b = st.columns([5, 1])
            col_a.write(f"⏰ **{item['time']}** — {item['name']} ({item['duration']} دقيقة)")
            if col_b.button("🗑️", key=f"del_w_{idx}"):
                st.session_state.workout_plan.pop(idx)
                st.rerun()

# -------------------------------------------------------------
# 3. النظام الغذائي والوجبات
# -------------------------------------------------------------
with tab_nutrition:
    st.subheader("🥗 مخطط الوجبات والسعرات الحرارية")
    
    with st.form("meal_form", clear_on_submit=True):
        col_m1, col_m2, col_m3 = st.columns([2, 1, 1])
        with col_m1:
            meal_name = st.text_input("اسم الوجبة/المكونات", placeholder="مثال: شوفان بالفواكه والنعناع...")
        with col_m2:
            meal_type = st.selectbox("نوع الوجبة", ["إفطار", "غداء", "عشاء", "وجبة خفيفة"])
        with col_m3:
            calories = st.number_input("السعرات المقدرة", min_value=0, max_value=2000, value=350)
            
        submit_meal = st.form_submit_button("إضافة الوجبة 🍽️")
        if submit_meal and meal_name:
            st.session_state.meals.append({"name": meal_name, "type": meal_type, "cal": calories})
            st.rerun()

    if st.session_state.meals:
        st.write("---")
        for idx, meal in enumerate(st.session_state.meals):
            col_a, col_b = st.columns([5, 1])
            col_a.write(f"🍲 **[{meal['type']}]** {meal['name']} — *{meal['cal']} سعرة حرارية*")
            if col_b.button("🗑️", key=f"del_m_{idx}"):
                st.session_state.meals.pop(idx)
                st.rerun()

# -------------------------------------------------------------
# 4. تنظيم النوم
# -------------------------------------------------------------
with tab_sleep:
    st.subheader("😴 تتبع وتنظيم النوم")
    
    sleep_val = st.slider("حدد عدد ساعات النوم المتوقعة أو الفعلية لليوم:", 4.0, 12.0, st.session_state.sleep_hours, 0.5)
    st.session_state.sleep_hours = sleep_val
    
    if sleep_val < 7:
        st.warning("⚠️ ينصح بزيادة ساعات النوم إلى 7-8 ساعات يومياً لتحسين التركيز والاستشفاء العضلي.")
    else:
        st.success("🎉 ممتاز! عدد ساعات النوم هذه مثالية جداً للصحة والإنتاجية.")

# -------------------------------------------------------------
# 5. المهام اليومية
# -------------------------------------------------------------
with tab_tasks:
    st.subheader("📌 قائمة المهام والإنجازات")
    
    with st.form("task_form", clear_on_submit=True):
        new_task = st.text_input("أضف مهمة جديدة...", placeholder="مثال: قراءة 15 دقيقة، إنهاء التقرير...")
        submit_task = st.form_submit_button("إضافة ➕")
        if submit_task and new_task:
            st.session_state.tasks.append({"task": new_task, "done": False})
            st.rerun()

    if st.session_state.tasks:
        st.write("---")
        for idx, task in enumerate(st.session_state.tasks):
            col_c, col_d = st.columns([5, 1])
            is_done = col_c.checkbox(task["task"], value=task["done"], key=f"t_{idx}")
            st.session_state.tasks[idx]["done"] = is_done
            if col_d.button("🗑️", key=f"del_t_{idx}"):
                st.session_state.tasks.pop(idx)
                st.rerun()