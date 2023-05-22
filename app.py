
import pickle
import streamlit as st

pickle_in = open('classifier', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()

# Define the function which will make the prediction using data
# inputs from users
def prediction(senior_citizen, has_dependents,
               months_as_customer, has_internet_service, has_month_to_month_contract):
    
    # Make predictions
    prediction = classifier.predict(
        [[senior_citizen, has_dependents, months_as_customer, has_internet_service, has_month_to_month_contract]])
    
    if prediction == 0:
        pred = 'Customer is most likely NOT CHURNING'
    else:
        pred = 'Customer is most likely CHURNING'
    return pred

# This is the main function in which we define our webpage
def main():
    
    st.title("Telco Customer Churn Predictor")
    st.write("Please enter the Customer profile values below:")
    col1, col2 = st.columns(2)
    # Create input fields
    with col1:
        st.subheader("Personal Parameters")
        senior_citizen = st.number_input("Senior Citizen?",
                                  min_value=0,
                                  max_value=1,
                                  value=0,
                                  step=1,
                                 )
        has_dependents = st.number_input("Has Dependents?",
                              min_value=0,
                              max_value=1,
                              value=0,
                              step=1
                             )

        
    with col2:
        st.subheader("Relationship Parameters")
        months_as_customer = st.number_input("Months as Customer?",
                              min_value=0,
                              #max_value=850,
                              value=12,
                              step=1
                             )
        has_internet_service = st.number_input("Has Internet Service?",
                          min_value=0,
                          max_value=1,
                          value=1,
                          step=1
                         )
        has_month_to_month_contract = st.number_input("Has Month to Month Contract?",
                          min_value=0,
                          max_value=1,
                          value=1,
                          step=1
                         )

    result = ""
    
    # When 'Predict' is clicked, make the prediction and store it
    if st.button("ㅤㅤㅤPredictㅤㅤㅤ"):
        result = prediction(senior_citizen, has_dependents, months_as_customer, has_internet_service, has_month_to_month_contract)
        if result == "Customer is most likely NOT CHURNING":
            st.success(result)
        else:
            st.error(result)
        
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/f3/W._P._Carey_School_of_Business_logo.png", width = 150)
    st.write("Built by David Joseph Attokaren")
    st.write("Version 1.0.0")
    
if __name__=='__main__':
    main()
    
