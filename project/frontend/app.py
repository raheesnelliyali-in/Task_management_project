import requests
import pandas as pd
import streamlit as st
from datetime import date, datetime

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Task Manager", page_icon="✅", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(59, 130, 246, 0.28), transparent 32%),
        radial-gradient(circle at bottom right, rgba(14, 165, 233, 0.18), transparent 30%),
        linear-gradient(135deg, #06111f 0%, #0f172a 50%, #111827 100%);
    color: #f8fafc;
}

.main .block-container {
    padding-top: 0.8rem;
    padding-bottom: 1.4rem;
    max-width: 1250px;
}

section[data-testid="stSidebar"] {
    background: rgba(2, 6, 23, 0.88);
    border-right: 1px solid rgba(148, 163, 184, 0.16);
}

.hero-card, .auth-card, .title-box, .task-card, .profile-card {
    background: rgba(15, 23, 42, 0.74);
    border: 1px solid rgba(148, 163, 184, 0.18);
    box-shadow: 0 22px 60px rgba(0,0,0,0.28);
    backdrop-filter: blur(18px);
    border-radius: 26px;
}

.hero-card {
    padding: 38px 34px;
    min-height: 440px;
}

.auth-card {
    padding: 30px;
}

.title-box {
    padding: 24px 28px;
    margin-bottom: 18px;
}

.title-text {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 6px;
    letter-spacing: -1px;
}

.subtitle-text {
    color: #cbd5e1;
    font-size: 16px;
}

.logo-circle {
    width: 56px;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 18px;
    background: linear-gradient(135deg, #2563eb, #38bdf8);
    font-size: 27px;
    margin-bottom: 18px;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -1.5px;
    margin-bottom: 18px;
}

.hero-subtitle {
    color: #cbd5e1;
    font-size: 18px;
    line-height: 1.7;
    margin-bottom: 26px;
}

.feature-pill {
    display: inline-block;
    padding: 9px 13px;
    margin: 5px 5px 5px 0;
    border-radius: 999px;
    background: rgba(59, 130, 246, 0.16);
    border: 1px solid rgba(96, 165, 250, 0.25);
    color: #dbeafe;
    font-size: 13px;
    font-weight: 600;
}

.auth-title {
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 4px;
}

.auth-subtitle {
    color: #94a3b8;
    margin-bottom: 18px;
}


.metric-card {
    background: rgba(15, 23, 42, 0.74);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 22px;
    padding: 18px 18px;
    min-height: 118px;
    box-shadow: 0 16px 38px rgba(0,0,0,0.18);
    transition: transform 0.18s ease, border 0.18s ease;
}
.metric-card:hover {
    transform: translateY(-2px);
    border: 1px solid rgba(96, 165, 250, 0.38);
}
.metric-icon {
    font-size: 22px;
    margin-bottom: 8px;
}
.metric-label {
    color: #94a3b8;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.metric-value {
    color: #f8fafc;
    font-size: 34px;
    font-weight: 800;
    line-height: 1.1;
    margin-top: 6px;
}
.section-card {
    background: rgba(15, 23, 42, 0.50);
    border: 1px solid rgba(148, 163, 184, 0.14);
    border-radius: 24px;
    padding: 22px;
    min-height: 415px;
}
.top-spacer-fix {
    margin-top: -8px;
}

div[data-testid="metric-container"] {
    background: rgba(15, 23, 42, 0.72);
    border: 1px solid rgba(148, 163, 184, 0.18);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.16);
}

div[data-testid="metric-container"] label {
    color: #cbd5e1 !important;
}

div[data-testid="stForm"] {
    background: rgba(15, 23, 42, 0.64);
    border: 1px solid rgba(148, 163, 184, 0.16);
    padding: 22px;
    border-radius: 22px;
}

.stTextInput input, .stTextArea textarea, .stDateInput input, div[data-baseweb="select"] > div {
    background-color: rgba(15, 23, 42, 0.88) !important;
    color: #f8fafc !important;
    border-radius: 14px !important;
    border: 1px solid rgba(148, 163, 184, 0.25) !important;
}

.stButton button, .stDownloadButton button, .stFormSubmitButton button {
    width: 100%;
    border-radius: 14px;
    min-height: 45px;
    font-weight: 700;
    border: 1px solid rgba(96, 165, 250, 0.28);
    background: linear-gradient(135deg, #2563eb, #0ea5e9);
    color: white;
}

.stButton button:hover, .stDownloadButton button:hover, .stFormSubmitButton button:hover {
    border: 1px solid rgba(125, 211, 252, 0.65);
    filter: brightness(1.08);
}

.task-card {
    padding: 20px 22px;
    margin: 14px 0 8px 0;
}

.task-title {
    font-size: 21px;
    font-weight: 800;
    margin-bottom: 8px;
}

.task-desc {
    color: #cbd5e1;
    line-height: 1.5;
    margin-bottom: 14px;
}

.badge {
    display: inline-block;
    padding: 6px 11px;
    margin: 3px 6px 3px 0;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 800;
    border: 1px solid rgba(148, 163, 184, 0.18);
}

.badge-blue { background: rgba(59, 130, 246, 0.16); color: #bfdbfe; }
.badge-green { background: rgba(34, 197, 94, 0.16); color: #bbf7d0; }
.badge-yellow { background: rgba(234, 179, 8, 0.16); color: #fef08a; }
.badge-red { background: rgba(239, 68, 68, 0.16); color: #fecaca; }
.badge-gray { background: rgba(148, 163, 184, 0.14); color: #e2e8f0; }

.footer-text {
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
    padding-top: 25px;
}

hr {
    border-color: rgba(148, 163, 184, 0.18) !important;
}


/* Improved professional sidebar */
section[data-testid="stSidebar"] {
    background:
        radial-gradient(circle at top left, rgba(37, 99, 235, 0.22), transparent 32%),
        linear-gradient(180deg, #020617 0%, #07111f 52%, #0f172a 100%);
    border-right: 1px solid rgba(148, 163, 184, 0.18);
}
section[data-testid="stSidebar"] > div {
    padding-top: 1.4rem;
}
.sidebar-brand-card {
    padding: 22px 18px;
    border-radius: 24px;
    background: rgba(15, 23, 42, 0.72);
    border: 1px solid rgba(148, 163, 184, 0.16);
    box-shadow: 0 18px 40px rgba(0,0,0,0.22);
    margin-bottom: 18px;
}
.sidebar-logo {
    width: 52px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 17px;
    background: linear-gradient(135deg, #2563eb, #0ea5e9);
    font-size: 25px;
    margin-bottom: 14px;
}
.sidebar-title {
    font-size: 24px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 3px;
    letter-spacing: -0.5px;
}
.sidebar-subtitle {
    color: #94a3b8;
    font-size: 13px;
    line-height: 1.5;
}
.sidebar-user-card {
    padding: 15px 16px;
    border-radius: 18px;
    background: rgba(34, 197, 94, 0.11);
    border: 1px solid rgba(34, 197, 94, 0.24);
    margin: 10px 0 18px 0;
}
.sidebar-user-label {
    color: #86efac;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.7px;
}
.sidebar-user-name {
    color: #f0fdf4;
    font-size: 17px;
    font-weight: 800;
    margin-top: 4px;
}
.sidebar-section-title {
    color: #64748b;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 18px 0 8px 2px;
}
.sidebar-note {
    color: #94a3b8;
    font-size: 12.5px;
    line-height: 1.55;
    padding: 14px 15px;
    border-radius: 16px;
    background: rgba(15, 23, 42, 0.52);
    border: 1px solid rgba(148, 163, 184, 0.13);
    margin-top: 16px;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: rgba(15, 23, 42, 0.58);
    border: 1px solid rgba(148, 163, 184, 0.13);
    border-radius: 15px;
    padding: 10px 13px;
    margin-bottom: 9px;
    transition: all 0.2s ease;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: rgba(37, 99, 235, 0.18);
    border: 1px solid rgba(96, 165, 250, 0.34);
}
section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
    background: linear-gradient(135deg, rgba(37, 99, 235, 0.32), rgba(14, 165, 233, 0.22));
    border: 1px solid rgba(125, 211, 252, 0.55);
}
section[data-testid="stSidebar"] div[role="radiogroup"] label p {
    font-weight: 700;
    color: #e2e8f0;
}
section[data-testid="stSidebar"] .stButton button {
    background: linear-gradient(135deg, #ef4444, #f97316);
    border: none;
    box-shadow: 0 10px 24px rgba(239, 68, 68, 0.18);
}


[data-testid="stToolbar"] { visibility: hidden; height: 0%; position: fixed; }
header[data-testid="stHeader"] { background: transparent; }
</style>
""", unsafe_allow_html=True)


def api_get(endpoint: str, params: dict | None = None):
    try:
        response = requests.get(f"{API_URL}{endpoint}", params=params, timeout=5)
        if response.status_code >= 400:
            st.error(response.json().get("detail", "Something went wrong"))
            return None
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error("Backend is not running. Start FastAPI first: uvicorn main:app --reload")
    except Exception as error:
        st.error(f"Error: {error}")
    return None


def api_post(endpoint: str, data: dict):
    try:
        response = requests.post(f"{API_URL}{endpoint}", json=data, timeout=5)
        if response.status_code >= 400:
            st.error(response.json().get("detail", "Something went wrong"))
            return None
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error("Backend is not running. Start FastAPI first: uvicorn main:app --reload")
    except Exception as error:
        st.error(f"Error: {error}")
    return None


def api_put(endpoint: str, data: dict):
    try:
        response = requests.put(f"{API_URL}{endpoint}", json=data, timeout=5)
        if response.status_code >= 400:
            st.error(response.json().get("detail", "Something went wrong"))
            return None
        return response.json()
    except Exception as error:
        st.error(f"Error: {error}")
    return None


def api_patch(endpoint: str, data: dict):
    try:
        response = requests.patch(f"{API_URL}{endpoint}", json=data, timeout=5)
        if response.status_code >= 400:
            st.error(response.json().get("detail", "Something went wrong"))
            return None
        return response.json()
    except Exception as error:
        st.error(f"Error: {error}")
    return None


def api_delete(endpoint: str):
    try:
        response = requests.delete(f"{API_URL}{endpoint}", timeout=5)
        if response.status_code >= 400:
            st.error(response.json().get("detail", "Something went wrong"))
            return None
        return response.json()
    except Exception as error:
        st.error(f"Error: {error}")
    return None


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None


def header():
    st.markdown("""
    <div class='title-box'>
        <div class='title-text'>Task Manager</div>
        <div class='subtitle-text'>Organize, track and complete your daily tasks efficiently.</div>
    </div>
    """, unsafe_allow_html=True)


def footer():
    st.markdown("<div class='footer-text'>Task Manager • Built with FastAPI, SQLite and Streamlit</div>", unsafe_allow_html=True)


def auth_page():
    left, right = st.columns([1.1, 0.9], gap="large")

    with left:
        st.markdown("""
        <div class='hero-card'>
            <div class='logo-circle'>✅</div>
            <div class='hero-title'>Task Manager</div>
            <div class='hero-subtitle'>
                Manage internship tasks, study work and personal goals from one clean dashboard.
                Create, update, complete, search and filter tasks with a FastAPI backend and SQLite database.
            </div>
            <span class='feature-pill'>FastAPI REST API</span>
            <span class='feature-pill'>SQLite Database</span>
            <span class='feature-pill'>Streamlit Frontend</span>
            <span class='feature-pill'>Task Analytics</span>
            <span class='feature-pill'>Search & Filters</span>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("<div class='auth-title'>Welcome Back</div>", unsafe_allow_html=True)
        st.markdown("<div class='auth-subtitle'>Login or create a new account to continue.</div>", unsafe_allow_html=True)

        login_tab, register_tab = st.tabs(["Login", "Register"])

        with login_tab:
            with st.form("login_form"):
                username = st.text_input("Username", placeholder="Enter your username")
                password = st.text_input("Password", type="password", placeholder="Enter your password")
                submitted = st.form_submit_button("Login")

            if submitted:
                if not username.strip() or not password.strip():
                    st.error("Please enter username and password")
                else:
                    result = api_post("/auth/login", {"username": username, "password": password})
                    if result:
                        st.session_state.logged_in = True
                        st.session_state.current_user = username
                        st.success("Login successful")
                        st.rerun()

        with register_tab:
            with st.form("register_form"):
                new_username = st.text_input("Create Username", placeholder="Choose a username")
                new_password = st.text_input("Create Password", type="password", placeholder="Create password")
                confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")
                submitted = st.form_submit_button("Create Account")

            if submitted:
                if not new_username.strip() or not new_password.strip() or not confirm_password.strip():
                    st.error("Please fill all fields")
                elif new_password != confirm_password:
                    st.error("Passwords do not match")
                else:
                    result = api_post("/auth/register", {
                        "username": new_username,
                        "email": f"{new_username}@taskmanager.local",
                        "password": new_password,
                    })
                    if result:
                        st.success("Registration successful. Now login.")

    footer()


def get_tasks(username: str, params_extra: dict | None = None) -> list:
    params = {"username": username}
    if params_extra:
        params.update(params_extra)
    return api_get("/tasks/", params) or []


def is_overdue(task: dict) -> bool:
    due = task.get("due_date") or ""
    try:
        return bool(due) and datetime.strptime(due, "%Y-%m-%d").date() < date.today() and not task.get("completed")
    except ValueError:
        return False


def task_status_text(task: dict) -> str:
    return "Completed" if task.get("completed") else "Pending"


def priority_badge_html(priority: str) -> str:
    if priority == "High":
        return "<span class='badge badge-red'>High Priority</span>"
    if priority == "Medium":
        return "<span class='badge badge-yellow'>Medium Priority</span>"
    return "<span class='badge badge-green'>Low Priority</span>"


def status_badge_html(task: dict) -> str:
    if is_overdue(task):
        return "<span class='badge badge-red'>Overdue</span>"
    if task.get("completed"):
        return "<span class='badge badge-green'>Completed</span>"
    return "<span class='badge badge-blue'>Pending</span>"



def metric_card(icon: str, label: str, value) -> None:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-icon'>{icon}</div>
        <div class='metric-label'>{label}</div>
        <div class='metric-value'>{value}</div>
    </div>
    """, unsafe_allow_html=True)

def dashboard_page():
    header()
    username = st.session_state.current_user

    st.markdown(f"### Welcome, **{username}**")
    st.caption("Here is your task overview for today.")

    summary = api_get("/tasks/summary", {"username": username}) or {}
    tasks = get_tasks(username)
    overdue_count = sum(1 for task in tasks if is_overdue(task))

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        metric_card("📋", "Total", summary.get("total", 0))
    with col2:
        metric_card("✅", "Completed", summary.get("completed", 0))
    with col3:
        metric_card("⏳", "Pending", summary.get("pending", 0))
    with col4:
        metric_card("🔥", "High Priority", summary.get("high_priority", 0))
    with col5:
        metric_card("⚠️", "Overdue", overdue_count)

    progress = int(summary.get("progress", 0))
    st.markdown("#### Completion Progress")
    st.progress(progress)
    st.caption(f"{progress}% of your tasks are completed")

    st.divider()
    col_a, col_b = st.columns([0.95, 1.05], gap="large")

    with col_a:
        st.subheader("Create New Task")
        st.caption("Add a task with priority, category and due date.")
        with st.form("create_task_form"):
            title = st.text_input("Task Title", placeholder="Example: Complete FastAPI CRUD API")
            description = st.text_area("Description", placeholder="Add short task details")
            c1, c2, c3 = st.columns(3)
            priority = c1.selectbox("Priority", ["Low", "Medium", "High"], index=1)
            category = c2.selectbox("Category", ["General", "Study", "Internship", "Personal", "Work"])
            due_date = c3.date_input("Due Date", value=date.today())
            submitted = st.form_submit_button("Add Task")

        if submitted:
            if not title.strip():
                st.error("Task title is required")
            else:
                result = api_post("/tasks/", {
                    "username": username,
                    "title": title,
                    "description": description,
                    "priority": priority,
                    "category": category,
                    "due_date": str(due_date),
                })
                if result:
                    st.success("Task added successfully")
                    st.rerun()

    with col_b:
        st.subheader("Recent Tasks")
        st.caption("Latest tasks from your workspace.")
        recent_tasks = tasks[:4]
        if not recent_tasks:
            st.info("No tasks yet. Create your first task.")
        for task in recent_tasks:
            render_task_card(task, show_actions=False)


def render_task_card(task: dict, show_actions: bool = True):
    desc = task.get("description", "") or "No description added"
    due = task.get("due_date") or "Not set"
    category = task.get("category", "General")
    task_id = task.get("id")

    st.markdown(f"""
    <div class='task-card'>
        <div class='task-title'>#{task_id} • {task.get('title', 'Untitled Task')}</div>
        <div class='task-desc'>{desc}</div>
        {priority_badge_html(task.get('priority', 'Medium'))}
        {status_badge_html(task)}
        <span class='badge badge-gray'>{category}</span>
        <span class='badge badge-gray'>Due: {due}</span>
    </div>
    """, unsafe_allow_html=True)

    if not show_actions:
        return

    action1, action2, action3 = st.columns([1, 1, 1])
    mark_clicked = action1.button("Mark Complete", key=f"mark_{task_id}", disabled=bool(task.get("completed")))
    edit_clicked = action2.button("Edit Task", key=f"edit_btn_{task_id}")
    delete_clicked = action3.button("Delete", key=f"delete_{task_id}")

    if mark_clicked:
        result = api_patch(f"/tasks/{task_id}/complete", {"completed": True})
        if result:
            st.success("Task completed")
            st.rerun()

    if delete_clicked:
        result = api_delete(f"/tasks/{task_id}")
        if result:
            st.success("Task deleted")
            st.rerun()

    if edit_clicked:
        st.session_state[f"editing_{task_id}"] = not st.session_state.get(f"editing_{task_id}", False)

    if st.session_state.get(f"editing_{task_id}", False):
        with st.form(f"edit_form_{task_id}"):
            new_title = st.text_input("Title", value=task.get("title", ""), key=f"title_{task_id}")
            new_description = st.text_area("Description", value=task.get("description", ""), key=f"desc_{task_id}")
            c1, c2, c3 = st.columns(3)
            priorities = ["Low", "Medium", "High"]
            categories = ["General", "Study", "Internship", "Personal", "Work"]
            current_priority = task.get("priority", "Medium")
            if current_priority not in priorities:
                current_priority = "Medium"
            new_priority = c1.selectbox("Priority", priorities, index=priorities.index(current_priority), key=f"priority_{task_id}")
            current_category = task.get("category", "General")
            if current_category not in categories:
                categories.append(current_category)
            new_category = c2.selectbox("Category", categories, index=categories.index(current_category), key=f"cat_{task_id}")
            current_due = date.today()
            if task.get("due_date"):
                try:
                    current_due = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
                except ValueError:
                    current_due = date.today()
            new_due_date = c3.date_input("Due Date", value=current_due, key=f"due_{task_id}")
            new_completed = st.checkbox("Completed", value=bool(task.get("completed")), key=f"comp_{task_id}")
            save = st.form_submit_button("Save Changes")

        if save:
            result = api_put(f"/tasks/{task_id}", {
                "title": new_title,
                "description": new_description,
                "priority": new_priority,
                "due_date": str(new_due_date),
                "completed": new_completed,
                "category": new_category,
            })
            if result:
                st.session_state[f"editing_{task_id}"] = False
                st.success("Task updated")
                st.rerun()


def tasks_page():
    header()
    username = st.session_state.current_user
    st.subheader("My Tasks")

    col1, col2, col3 = st.columns(3)
    status_filter = col1.selectbox("Status", ["All", "Pending", "Completed"])
    priority_filter = col2.selectbox("Priority", ["All", "Low", "Medium", "High"])
    search = col3.text_input("Search", placeholder="Search by title")

    params = {}
    if status_filter != "All":
        params["status"] = status_filter.lower()
    if priority_filter != "All":
        params["priority"] = priority_filter
    if search:
        params["search"] = search

    tasks = get_tasks(username, params)

    if not tasks:
        st.info("No tasks found")
        return

    rows = []
    for task in tasks:
        rows.append({
            "ID": task["id"],
            "Title": task["title"],
            "Category": task.get("category", "General"),
            "Priority": task.get("priority", "Medium"),
            "Due Date": task.get("due_date", ""),
            "Status": "Overdue" if is_overdue(task) else task_status_text(task),
        })

    csv_data = pd.DataFrame(rows).to_csv(index=False).encode("utf-8")
    st.download_button("Download Tasks CSV", csv_data, "my_tasks.csv", "text/csv")

    st.divider()
    for task in tasks:
        render_task_card(task, show_actions=True)


def profile_page():
    header()
    st.markdown(f"""
    <div class='profile-card' style='padding: 28px;'>
        <div class='task-title'>User Profile</div>
        <div class='task-desc'>Logged in as <b>{st.session_state.current_user}</b></div>
        <span class='badge badge-blue'>Task Manager User</span>
        <span class='badge badge-gray'>FastAPI + SQLite</span>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.rerun()


def sidebar_brand():
    username = st.session_state.current_user or "User"
    st.sidebar.markdown("""
    <div class='sidebar-brand-card'>
        <div class='sidebar-logo'>✅</div>
        <div class='sidebar-title'>Task Manager</div>
        <div class='sidebar-subtitle'>Plan your work, track progress and complete tasks faster.</div>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown(f"""
    <div class='sidebar-user-card'>
        <div class='sidebar-user-label'>Signed in as</div>
        <div class='sidebar-user-name'>{username}</div>
    </div>
    """, unsafe_allow_html=True)


if st.session_state.logged_in:
    sidebar_brand()
    st.sidebar.markdown("<div class='sidebar-section-title'>Menu</div>", unsafe_allow_html=True)
    menu = st.sidebar.radio("Navigation", ["📊 Dashboard", "📝 My Tasks", "👤 Profile"], label_visibility="collapsed")
    st.sidebar.markdown("<div class='sidebar-section-title'>Account</div>", unsafe_allow_html=True)
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.rerun()
    st.sidebar.markdown("""
    <div class='sidebar-note'>
        <b>Internship Project</b><br>
        FastAPI backend • SQLite database • Streamlit frontend
    </div>
    """, unsafe_allow_html=True)

    if menu == "📊 Dashboard":
        dashboard_page()
    elif menu == "📝 My Tasks":
        tasks_page()
    else:
        profile_page()
else:
    auth_page()
