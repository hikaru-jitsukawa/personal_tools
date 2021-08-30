import streamlit as st

if "eva_total" not in st.session_state:
    st.session_state['eva_total'] = 0
if 'theo_total' not in st.session_state:
    st.session_state['theo_total'] = 0
if 'hikaru_total' not in st.session_state:
    st.session_state['hikaru_total'] = 0

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
            st.session_state.eva_total = (float(st.session_state.eva_total) + split_amount)

        if split_list[1] == True:
            st.session_state.theo_total = (float(st.session_state.theo_total) + split_amount)

        if split_list[2] == True:
            st.session_state.hikaru_total = (float(st.session_state.hikaru_total) + split_amount)

        #st.session_state.eva_total = "{:.2f}".format(st.session_state.eva_total)
        #st.session_state.theo_total = "{:.2f}".format(st.session_state.theo_total)
        #st.session_state.hikaru_total = "{:.2f}".format(st.session_state.hikaru_total)

col1, col2, col3 = st.columns(3)
col1.metric(label="Eva", value="$" + str(st.session_state.eva_total))
col2.metric(label="Theo", value="$" + str(st.session_state.theo_total))
col3.metric(label="Hikaru", value="$" + str(st.session_state.hikaru_total))
