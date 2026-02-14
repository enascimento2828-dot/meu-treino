import streamlit as st

st.set_page_config(page_title="Treino Progressivo", layout="centered")

# Estrutura baseada na sua foto
if 'treinos' not in st.session_state:
    st.session_state.treinos = {
        "FICHA A": [
            {"ex": "ELÍPTICO", "carga": 2, "series": "S", "done": False},
            {"ex": "SUPINO COM HALTER BANCO RETO", "carga": 14, "series": "3x12", "done": False},
            {"ex": "CRUCIFIXO POLIA", "carga": 15, "series": "3x12 ou 15", "done": False},
            {"ex": "ELEVAÇÃO LATERAL POLIA BAIXA", "carga": 5, "series": "3x12-15", "done": False},
            {"ex": "TRICEPS CORDA", "carga": 25, "series": "3x12", "done": False},
            {"ex": "FACE PULL", "carga": 25, "series": "3x15", "done": False},
            {"ex": "PRESS OMBROS HALTERES", "carga": 0, "series": "3x12", "done": False},
            {"ex": "ROTAÇÃO EXTERNA POLIA/ELÁSTICO", "carga": 0, "series": "3x15", "done": False},
            {"ex": "ALONGAMENTO PEITORAL", "carga": 0, "series": "2x30 seg", "done": False},
        ],
        "FICHA B": [], "FICHA C": [], "FICHA D": [], "FICHA E": [], "FICHA F": []
    }

st.title("🏋️ Meu Treino")

ficha = st.selectbox("Escolha a Ficha", list(st.session_state.treinos.keys()))

for i, item in enumerate(st.session_state.treinos[ficha]):
    c1, c2, c3 = st.columns([1, 4, 2])
    with c1:
        item['done'] = st.checkbox("", value=item['done'], key=f"c_{ficha}_{i}")
    with c2:
        texto = f"~~{item['ex']}~~" if item['done'] else f"**{item['ex']}**"
        st.markdown(f"{texto}  \n<small>{item['series']}</small>", unsafe_allow_html=True)
    with c3:
        item['carga'] = st.number_input("Kg", value=int(item['carga']), key=f"w_{ficha}_{i}")

if st.button("Limpar Treino do Dia"):
    for ex in st.session_state.treinos[ficha]:
        ex['done'] = False
    st.rerun()
