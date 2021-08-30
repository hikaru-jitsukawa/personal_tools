import streamlit as st

eva_total = 0
theo_total = 0
hikaru_total = 0
split_list = []

st.title("Receipt Tool")

amount = st.number_input("Item Amount")

eva_boolean = st.checkbox("Eva")
theo_boolean = st.checkbox("Theo")
hikaru_boolean = st.checkbox("Hikaru")

if st.button("Add to Running Total"):
    split_list.append(eva_boolean)
    split_list.append(theo_boolean)
    split_list.append(hikaru_boolean)
    if sum(split_list) == 0:
        st.write("Please select at least one person.")
    else:
        split_amount = amount / sum(split_list)

        if split_list[0] == True:
            eva_total = eva_total + split_amount

        if split_list[1] == True:
            theo_total = theo_total + split_amount

        if split_list[2] == True:
            hikaru_total = hikaru_total + split_amount

        col1, col2, col3 = st.beta_columns(3)
        col1.metric(label="Eva", value="$" + str(eva_total), delta="1.2 °F")
        col2.metric(label="Theo", value="$" + str(theo_total), delta="-8%")
        col3.metric(label="Hikaru", value="$" + str(hikaru_total), delta="4%")