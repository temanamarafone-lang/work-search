import streamlit as st
import pandas as pd

st.set_page_config(page_title="Поиск компании сотрудника", page_icon="🔍", layout="centered")

@st.cache_data
def load_data():
    file_path = 'Аут сентябрь.xlsx'
    df1 = pd.read_excel(file_path, sheet_name='Лист1')
    df2 = pd.read_excel(file_path, sheet_name='Лист2', header=None)
    df2.columns = ['Исполнитель', 'Головное предприятие']
    return pd.concat([df1, df2], ignore_index=True)

df = load_data()

st.title("🔍 Поиск компании сотрудника")
query = st.text_input("Введите фамилию или ФИО сотрудника:", "")

if query:
    q = query.strip().lower()
    res = df[df['Исполнитель'].astype(str).str.lower().str.contains(q, na=False)]
    
    if res.empty:
        st.warning("Сотрудники с таким именем не найдены в базе.")
    else:
        st.success(f"Найдено совпадений: {len(res)}")
        show_df = res.rename(columns={'Исполнитель': 'ФИО сотрудника', 'Головное предприятие': 'Компания'})
        st.dataframe(show_df, use_container_width=True, hide_index=True)
else:
    st.info("Введите запрос в поле выше для начала поиска.")
