import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('/Users/san./Documents/mulitidisses/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('/Users/san./Documents/mulitidisses/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('/Users/san./Documents/mulitidisses/parkinsons_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=1)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # page title
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregancies = st.text_input('Number of Pregancies')
        # This refers to the number of times a woman has been pregnant.
        SkinThickness = st.text_input('Skin Thickness value')
        # Skin thickness may be linked to insulin resistance, which is a key factor in the development of diabetes.

    with col2:
        Glucose = st.text_input('Glucose Level')
        # This refers to the concentration of glucose (sugar) in the blood. It's measured in milligrams per deciliter (mg/dL).
        Insulin = st.text_input('Insulin Level')
        # This feature is important because insulin resistance is a major factor in the development of diabetes.

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        # This refers to the pressure of blood against the walls of the arteries. It's measured in millimeters of mercury (mmHg).
        BMI = st.text_input('BMI value')
        # BMI is a measure of body fat and is important because obesity is a significant risk factor for diabetes.
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        # This feature is a measure of the prevalence of diabetes in an individual's family history. It can indicate a genetic predisposition to the disease.

    # Age is a crucial feature in diabetes prediction because the risk of developing the disease increases with age. As we get older, our bodies become less effective at using insulin, which can lead to the onset of diabetes.
    Age = st.text_input('Age of the Person')

    # prediction
    diab_diagnosis = ""

    # creating a button for prediction
    if st.button("Let's see"):
        if Pregancies == '' and Glucose == '' and BloodPressure == '' and SkinThickness == '' and Insulin == '' and BMI == '' and DiabetesPedigreeFunction == '' and Age == '':
            st.write("Please enter some input to predict.")
        else:
            diab_prediction = diabetes_model.predict([[Pregancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            if diab_prediction[0] == 1:
                diab_diagnosis = "You have Diabetes. It is recommended that you seek medical advice."
                st.write(diab_diagnosis)
                st.write("[Click here](https://www.diabetes.org.uk/) to find a healthcare professional and we hope you get better.")
            else:
                diab_diagnosis = "You are not Diabetic."
                st.write(diab_diagnosis)

        
if(selected == "Heart Disease Prediction"):
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age')

    with col2:
        sex = st.number_input('Sex (0 for Female, 1 for Male)')

    with col3:
        cp = st.number_input('Chest Pain types (1 for Typical Angina, 2 for Atypical Angina, 3 for Non-Anginal Pain, 4 for Asymptomatic)')

    with col1:
        trestbps = st.number_input('Resting Blood Pressure (mmHg)')

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (0 for False, 1 for True)')

    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (0 for Normal, 1 for ST-T wave abnormality, 2 for Left ventricular hypertrophy)')

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.number_input('Exercise Induced Angina (0 for No, 1 for Yes)')

    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')

    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment (1 for Upsloping, 2 for Flat, 3 for Downsloping)')

    with col3:
        ca = st.number_input('Major vessels colored by flourosopy (0-3)')

    with col1:
        thal = st.number_input('Thalassemia (1 for Normal, 2 for Fixed Defect, 3 for Reversable Defect)')

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is likely to have heart disease'
        else:
            heart_diagnosis = 'The person is unlikely to have heart disease'

        st.success(heart_diagnosis)
if selected == "Parkinsons Prediction":
    st.title('Parkinsons Prediction using ML')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.number_input('MDVP:RAP')

    with col2:
        PPQ = st.number_input('MDVP:PPQ')

    with col3:
        DDP = st.number_input('Jitter:DDP')

    with col4:
        Shimmer = st.number_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.number_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.number_input('Shimmer:APQ5')

    with col3:
        APQ = st.number_input('MDVP:APQ')

    with col4:
        DDA = st.number_input('Shimmer:DDA')

    with col5:
        NHR = st.number_input('NHR')

    with col1:
        HNR = st.number_input('HNR')

    with col2:
        RPDE = st.number_input('RPDE')

    with col3:
        DFA = st.number_input('DFA')

    with col4:
        spread1 = st.number_input('spread1')

    with col5:
        spread2 = st.number_input('spread2')

    with col1:
        D2 = st.number_input('D2')

    with col2:
        PPE = st.number_input('PPE')

    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease. We hope you get the support and treatment you need. Please visit the following link for resources: [https://www.parkinson.org/]"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
        st.success(parkinsons_diagnosis)
