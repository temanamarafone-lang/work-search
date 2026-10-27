if results.empty:
    st.warning("Сотрудники с таким именем не найдены в базе.")
else:
    st.success(f"Найдено совпадений: {len(results)}")
    display_df = results.rename(columns={'Исполнитель': 'ФИО сотрудника', 'Головное предприятие': 'Компания'})
    st.dataframe(display_df, use_container_width=True, hide_index=True)
