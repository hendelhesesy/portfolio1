import streamlit as st

# ----------------- Sidebar -----------------
st.sidebar.title("Hend Elhesesy")
menu = ["Home", "About Me", "Skills", "Projects", "Contact"]
choice = st.sidebar.radio("Navigation", menu)

# ----------------- Home -----------------
if choice == "Home":
    # صورة شخصية
    st.image("images/Personal_Photo.png", width=200)
    
    st.title("Hend Elhesesy – AI & Data Science Portfolio")
    st.subheader("Python | Machine Learning | Data Analysis")
    st.write("""
    Welcome to my Portfolio! Here you'll find my projects, skills, and contact information.  
    I'm passionate about turning data into meaningful insights and building practical AI solutions.
    """)

# ----------------- About Me -----------------
elif choice == "About Me":
    st.header("About Me")
    st.write("""
    I am a DEPI AI & Data Science trainee from Faculty of Computers & Artificial Intelligence – Benha University.  
    I focus on analyzing data, building predictive models, and delivering practical solutions using Python and Machine Learning.  
    My goal is to grow as a Data Scientist and AI Engineer, creating projects that solve real-world problems.
    """)

# ----------------- Skills -----------------
elif choice == "Skills":
    st.header("Skills")
    st.write("""
    **Programming:** Python, SQL  
    **Data Analysis:** Pandas, NumPy, Matplotlib, Seaborn  
    **Machine Learning:** Regression, Classification, Model Evaluation, EDA  
    **Tools:** Jupyter Notebook, Git, GitHub, Streamlit
    """)

# ----------------- Projects -----------------
elif choice == "Projects":
    st.header("Projects")

    st.subheader("Customer Churn Prediction")
    st.write("""
    - Performed EDA (Exploratory Data Analysis) on the dataset to understand customer behavior  
    - Built a Linear Regression / Classification model to predict customer churn  
    - Evaluated model using accuracy, confusion matrix, and other metrics  
    - Gained insights to improve customer retention strategies
    """)

    # عرض كل صور الـ EDA
    images = [
        "images/eda1.png",
        "images/eda2.png",
        "images/eda3.png",
        "images/eda4.png",
        "images/eda5.png"
    ]

    for img in images:
        st.image(img, width=500)

    # GitHub Repo
    st.write("[GitHub Repo](https://github.com/hendelhesesy/TelecomeChurn)")

# ----------------- Contact -----------------
elif choice == "Contact":
    st.header("Contact Me")
    st.write("Email: hendelhesesy@gmail.com")
    st.write("LinkedIn: [Hend LinkedIn](https://www.linkedin.com/in/hend-elhesesy-92a760333)")
    st.write("GitHub: [Hend GitHub](https://github.com/hendelhesesy/TelecomeChurn)")
