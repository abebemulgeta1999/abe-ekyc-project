import streamlit as st

# Page configuration
st.set_page_config(
    page_title="eKYC Portal - Coop Bank", 
    page_icon="🔐", 
    layout="centered"
)

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.markdown("<h2 style='text-align: center; color: #006633;'>Cooperative Bank of Oromia</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>eKYC Staff Portal Login</h4>", unsafe_allow_html=True)
        
        st.write("---")

        with st.form("login_form"):
            username = st.text_input("Username / Staff ID")
            password = st.text_input("Password", type="password")
            
            submit_btn = st.form_submit_button("Seeni (Login)")

            if submit_btn:
                if username == "admin" and password == "password123":
                    st.session_state.logged_in = True
                    st.success("Seensa Milkaa'eera!")
                    st.rerun()
                else:
                    st.error("Username ykn Password dogoggoraadha! Irra deebisi ilaali.")
    else:
        # Navigation Sidebar
        st.sidebar.title("Navigation")
        menu = st.sidebar.radio("Filannoo", [
            "Customer Registration", 
            "ID Document Upload & OCR", 
            "Face Verification", 
            "KYC Approval & Dashboard",
            "Logout"
        ])

        if menu == "Customer Registration":
            st.title("📋 Customer Registration (Maamilcha Galchuuf)")
            st.write("Odeeffannoo bu'uuraa maamilichaa asitti galchaa:")

            with st.form("reg_form"):
                full_name = st.text_input("Maqaa Guutuu")
                father_name = st.text_input("Maqaa Abbaa")
                grand_father_name = st.text_input("Maqaa Abbaa Abbaa")
                
                col1, col2 = st.columns(2)
                with col1:
                    gender = st.selectbox("Saala", ["Dhiira", "Dubarti"])
                    dob = st.date_input("Guyyaa Dhalootaa")
                with col2:
                    phone = st.text_input("Lakkoofsa Bilbilaa")
                    account_type = st.selectbox("Gosa Herregaa", ["Standard Savings", "Interest-Free Banking (IFB)", "Current Account"])

                address = st.text_area("Teessoo (Godina, Aanaa, Ganda)")
                
                submit_button = st.form_submit_button(label="Galmeessi & Itti Aani")

                if submit_button:
                    if full_name and phone:
                        st.success(f"Maamilchi {full_name} milkaa'inaan galmeeffameera!")
                    else:
                        st.warning("Maqaa guutuu fi lakkoofsa bilbilaa guutuun dirqama!")

        elif menu == "ID Document Upload & OCR":
            st.title("🪪 National ID & OCR Processing")
            st.write("Suuraa Kaardii Eenyummaa (ID) maamilaa fe'aa:")
            
            uploaded_file = st.file_uploader("Kaardii Eenyummaa (JPG/PNG)", type=["jpg", "png", "jpeg"])
            
            if uploaded_file is not None:
                st.image(uploaded_file, caption="ID Maamilaa Fe'ame", use_container_width=True)
                if st.button("OCR Dubbisi (Scan ID)"):
                    with st.spinner("Odeeffannoon ID irraa dubbifamaa jira..."):
                        st.success("Odeeffannoon ID milkaa'inaan irraa fuudhameera!")
                        st.json({
                            "ID Number": "ET-3756439638621472",
                            "Full Name": "Abebe Mulgeta Senbeto",
                            "Date of Birth": "1999/01/11",
                            "Address": "Burayu"
                        })

        elif menu == "Face Verification":
            st.title("👤 Face Verification & Liveness Check")
            st.write("Suuraa fuula maamilaa Kaameraan fudhachuun mirkaneessaa:")
            
            camera_photo = st.camera_input("Suuraa Kaasaa (Take a picture)")
            
            if camera_photo:
                st.success("Suuraan fuulaa milkaa'inaan fuudhameera!")
                if st.button("Liveness Check & Verify"):
                    with st.spinner("Mirkaneessi gaggeeffamaa jira..."):
                        st.success("Match Successful! 98.5% wal simateera. Eenyummaan maamilaa mirkanaa'eera!")

        elif menu == "KYC Approval & Dashboard":
            st.title("📊 KYC Approval Dashboard & Status")
            st.write("Gamaaggama qabxii eKYC maamilaa fi murtoo herregaa:")

            st.info("Maamila: Abebe Mulgeta | Herrega: Interest-Free Banking (IFB)")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("ID Verification", "Passed", "100%")
            col2.metric("Face Match", "Passed", "98.5%")
            col3.metric("Liveness Score", "Secure", "Active")

            st.write("---")
            
            c1, c2 = st.columns(2)
            with c1:
                if st.button("✅ Approve KYC Account"):
                    st.success("Herregni maamilaa milkaa'inaan ragga'eera (Approved)! Account number uumameera.")
            with c2:
                if st.button("❌ Reject KYC Account"):
                    st.error("KYC inni dhiyeesse fudhatama dhabeera (Rejected).")

        elif menu == "Logout":
            st.session_state.logged_in = False
            st.rerun()

if __name__ == '__main__':
    main()