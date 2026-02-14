import streamlit as st

st.set_page_config(page_title="Treino Progressivo", layout="centered")

# Estrutura com todas as fichas (A até F)
if 'treinos' not in st.session_state:
    st.session_state.treinos = {
        "FICHA A": [
            {"ex": "SUPINO COM HALTER", "carga": 14, "series": "3x12", "done": False},
            {"ex": "CRUCIFIXO POLIA", "carga": 15, "series": "3x12", "done": False},
        ],
        "FICHA B": [], "FICHA C": [], "FICHA D": [], "FICHA E": [], "FICHA F": []
    }

st.title("🏋️ Meu Diário de Treino")

# Menu de seleção de Ficha
ficha = st.selectbox("Selecione o Treino", list(st.session_state.treinos.keys()))

st.subheader(f"📍 {ficha}")

# Mostrar lista de exercícios
for i, item in enumerate(st.session_state.treinos[ficha]):
    c1, c2, c3, c4 = st.columns([1, 4, 2, 1])
    with c1:
        item['done'] = st.checkbox("", value=item['done'], key=f"ch_{ficha}_{i}")
    with c2:
        # Fica riscado se marcar o check
        texto = f"~{item['ex']}~" if item['done'] else f"*{item['ex']}*"
        st.markdown(f"{texto}  \n<small>{item['series']}</small>", unsafe_allow_html=True)
    with c3:
        item['carga'] = st.number_input("Kg", value=int(item['carga']), key=f"w_{ficha}_{i}")
    with c4:
        if st.button("❌", key=f"del_{ficha}_{i}"):
            st.session_state.treinos[ficha].pop(i)
            st.rerun()

st.divider()

# Adicionar novo exercício na ficha selecionada
with st.expander("➕ Adicionar Exercício"):
    n_nome = st.text_input("Nome do Exercício")
    n_serie = st.text_input("Séries/Repetições")
    if st.button("Salvar na Ficha"):
        if n_nome:
            st.session_state.treinos[ficha].append({"ex": n_nome.upper(), "carga": 0, "series": n_serie, "done": False})
            st.rerun()
