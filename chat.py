import streamlit as st
import math

st.set_page_config(page_title="CREVA AI", layout="centered")

st.title("🤖 CREVA Financial Planner")

# -------- SESSION STATE --------
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "data" not in st.session_state:
    st.session_state.data = {}

# -------- STEP 1: FORM --------
if not st.session_state.form_submitted:

    st.subheader("📋 Enter Your Details")

    with st.form("user_form"):
        name = st.text_input("Name")
        contact = st.text_input("Contact Number")
        salary = st.number_input("Monthly Salary", min_value=0.0)
        expenses = st.number_input("Monthly Expenses", min_value=0.0)
        savings = st.number_input("Current Savings", min_value=0.0)
        job = st.selectbox("Job Stability", ["Low", "Medium", "High"])
        risk = st.selectbox("Risk Level", ["Low", "Medium", "High"])

        submit = st.form_submit_button("Create Plan 🚀")

        if submit:
            st.session_state.data = {
                "name": name,
                "contact": contact,
                "salary": salary,
                "expenses": expenses,
                "savings": savings,
                "job": job,
                "risk": risk
            }

            st.session_state.form_submitted = True
            st.rerun()

# -------- STEP 2: CHAT --------
else:

    st.subheader(f"👋 Welcome {st.session_state.data['name']}")

    # Show previous messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # First message
    if len(st.session_state.messages) == 0:
        st.session_state.messages.append({
            "role": "assistant",
            "content": "What do you want to buy?"
        })
        st.rerun()

    # Chat input
    user_input = st.chat_input("Type your goal...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # If goal not set
        if "goal" not in st.session_state:
            st.session_state.goal = user_input
            response = "What is its cost?"

        # If amount not set
        elif "amount" not in st.session_state:
            try:
                amount = float(user_input)
                st.session_state.amount = amount

                data = st.session_state.data
                salary = data["salary"]
                expenses = data["expenses"]
                savings = data["savings"]
                risk = data["risk"]

                free_money = salary - expenses
                monthly_saving = free_money * 0.5

                if monthly_saving <= 0:
                    response = "⚠️ Your expenses are too high!"
                else:
                    months = math.ceil(amount / monthly_saving)

                    if months <= 6:
                        goal_type = "SHORT TERM"
                    elif months <= 36:
                        goal_type = "MID TERM"
                    else:
                        goal_type = "LONG TERM"

                    response = f"""
📊 **Your Plan**

💰 Monthly Saving: ₹{monthly_saving:.2f}  
⏳ Time Needed: {months} months  
🎯 Goal Type: {goal_type}
"""

                    if savings < 6 * expenses:
                        response += "\n⚠️ Build emergency fund first!"

                    if goal_type == "SHORT TERM":
                        response += "\nAdvice: Use RD / Savings"
                    elif goal_type == "MID TERM":
                        response += "\nAdvice: RD + Mutual Funds"
                    else:
                        if risk.lower() == "high":
                            response += "\nAdvice: SIP + Equity"
                        else:
                            response += "\nAdvice: SIP + Safe"

                response += "\n\nDo you want another plan? (yes/no)"

            except:
                response = "⚠️ Please enter a valid number."

        # Restart logic
        else:
            if user_input.lower() == "yes":
                del st.session_state.goal
                del st.session_state.amount
                response = "What do you want to buy?"
            else:
                response = "Goodbye 👋"

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()