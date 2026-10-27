import streamlit as st import pandas as pd
st.set_page_config(page_title="Поиск компании сотрудника", page_icon="🔍", layout="centered")
@st.cache_data def load_data(): file_path = 'Аут сентябрь.xlsx' df1 = pd.read_excel(file_path, sheet_name='Лист1') df2 = pd.read_excel(file_path, sheet_name='Лист2', header=None) df2.columns = ['Исполнитель', 'Головное предприятие'] full_df = pd.concat([df1, df2], ignore_index=True) return full_df
try: df = load_data() except Exception as e: st.error(f"Не удалось загрузить файл базы данных: {e}") st.stop()
st.title("🔍 Поиск компании сотрудника") st.markdown("Введите фамилию или ФИО (можно частично), чтобы узнать, в какой компании работает сотрудник.")
query = st.text_input("Введите ФИО или фамилию сотрудника:", "")
if query: query_clean = query.strip().lower() mask = df['Исполнитель'].astype(str).str.lower().str.contains(query_clean, na=False) results = df[mask]
if results.empty:
    st.warning("Сотрудники с таким именем не найдены в базе.")
else:
    st.success(f"Найдено совпадений: {len(results)}")
    display_df = results.rename(columns={'Исполнитель': 'ФИО сотрудника', 'Головное предприятие': 'Компания'})
    st.dataframe(display_df, use_container_width=True, hide_index=True)
else: st.info("Введите запрос в поле выше для начала поиска.")
