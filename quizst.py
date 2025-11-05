# quiz_streamlit.py
import streamlit as st

st.title("♻️ Quiz: Consumismo, mídia e meio ambiente")
st.markdown("Responda às perguntas abaixo:")

questions = [
    ("O que é o consumismo?", ["Comprar apenas essencial", "Trocar produtos com o vizinho", "Compra excessiva por impulso ou influência", "Reciclar embalagens"], "Compra excessiva por impulso ou influência"), 
    ("O que podemos fazer com roupas que não usamos mais?", ["Jogar fora", "Guardar para na esperança de usar novamente", "Doar, trocar ou reaproveitar", "Comprar roupas novas"], "Doar, trocar ou reaproveitar"),
    ("Como a mídia pode incentivar o cuidado com o planeta?", ["Divulgando campanhas e boas práticas ambientais", "Mostrando apenas propagandas de produtos caros", "Incentivando o consumo exagerado", "Evitando falar sobre meio ambiente"], "Divulgando campanhas e boas práticas ambientais"),
    ("Por que é importante reutilizar e reciclar?", ["Porque está na moda", "Para reduzir o desperdício e proteger a natureza", "Para ter mais lixo", "Para comprar coisas novas"], "Para reduzir o desperdício e proteger a natureza"),
    ("O que significa apoiar uma campanha ambiental nas redes sociais?", ["Curtir apenas porque está na moda", "Compartilhar e incentivar atitudes sustentáveis", "Fazer memes sobre o tema", "Não participar"], "Compartilhar e incentivar atitudes sustentáveis"),
    ("Compartilhar informações sobre reciclagem nas redes é uma boa ação?", ["Sim, ajuda a conscientizar outras pessoas", "Não, não faz diferença", "Só se for pago", "É perda de tempo"], "Sim, ajuda a conscientizar outras pessoas"),
    ("O que podemos fazer para reduzir o uso de plástico no dia a dia?", ["Usar sacolas reutilizáveis e garrafas próprias", "Comprar mais embalagens plásticas", "Jogar o plástico fora em qualquer lugar", "Evitar reciclar"], "Usar sacolas reutilizáveis e garrafas próprias"),
    ("Como o consumo de energia pode ser reduzido em casa?", ["Deixando luzes e aparelhos ligados o tempo todo", "Usando lâmpadas LED e desligando o que não for usado", "Usando vários eletrônicos ao mesmo tempo", "Tomando banhos longos com água quente"], "Usando lâmpadas LED e desligando o que não for usado")
]

# Inicializa estado para respostas e mostrar respostas
if "answers" not in st.session_state:
    st.session_state["answers"] = {}
if "show_answer" not in st.session_state:
    st.session_state["show_answer"] = {}

for i, (q, opts, ans) in enumerate(questions):
    st.subheader(f"Pergunta {i+1}")
    st.write(q)

    # Botões das alternativas (um abaixo do outro)
    for j, opt in enumerate(opts):
        if st.button(opt, key=f"q{i}_opt{j}"):
            st.session_state["answers"][i] = opt
    
    # Mostra seleção atual da pergunta (somente estado "Selecionado")
    selected = st.session_state["answers"].get(i)
    if selected == ans:
        st.success(f"✅ Correto! Você selecionou: **{selected}**")
    elif selected == None:
        st.info("Você ainda não selecionou uma resposta.")
    else:
        st.error(f"❌ Incorreto! Você selecionou: **{selected}**. Resposta correta: **{ans}**")

    st.divider()

# Botão para reiniciar o quiz
if st.button("🔄 Reiniciar Quiz"):
    st.session_state["answers"] = {}
    st.session_state["show_answer"] = {}
    st.rerun()

if st.button("Ver Resultado"):
    score = 0
    for i, (_, _, ans) in enumerate(questions):
        if st.session_state["answers"].get(i) == ans:
            score += 1
    if score > 7:
        st.balloons()
        st.success(f"🎉 Você acertou {score} de {len(questions)}!")
    elif score > 5:
        st.success(f"✅ Parabéns! Você acertou {score} de {len(questions)}!")
    elif score > 1 and score < 8:
        st.warning(f"⚠️ Você acertou {score} de {len(questions)}! Você pode melhorar.")
    else:
        st.error("⚠️ Você não acertou nenhuma questão. Use o botão **MOSTRAR RESPOSTA** em cada questão para aprender as respostas corretas!")