import streamlit as st

def home():
    st.header(":drop_of_blood: PANORAMA DA DOENÇA")

    st.markdown("""
    A diabetes é uma doença metabólica que causa alteração no funcionamento geral do organismo, fazendo com que o indivíduo não tenha capacidade biológica de degradar moléculas de glicose de maneira rápida ou em velocidade constante. Essa degradação ocorre por meio da insulina, hormônio que tem a função de quebrar as moléculas de açúcar, transformando-as em energia para manutenção das células do nosso organismo. 

    Existem dois tipos de diabetes: tipo 1 e tipo 2. A primeira é uma doença autoimune. No entanto, a segunda forma é conhecida como não insulinodependente e acomete, em sua maioria, pessoas com mais de 40 anos que apresentam graus de obesidade. Os sintomas se caracterizam por fome frequente, sede constante, formigamento de membros, visão turva, dentre outros. Suas complicações podem levantar a amputação de membros, cegueira e até a morte.

    Dados da décima edição do Atlas do Diabetes, divulgado pela Federação Internacional de Diabetes (IDF, na sigla em inglês), mostram que 537 milhões de pessoas entre 20 e 79 anos de idade têm diabetes no mundo, alta de 16% em dois anos. Os especialistas da IDF projetam que o número de adultos com a doença pode chegar a 643 milhões em 2030 e a 784 milhões em 2045. A prevalência global da doença atingiu 10,5%, com quase metade (44,7%) sem diagnóstico.
    """)

    st.divider()

    st.header(":dart: OBJETIVO DO TRABALHO")

    st.markdown("""
    Este site é parte integrante do trabalho final da disciplina de Visualização da Informação, ofertada pelo Instituto de Ciências Matemáticas e da Computação da USP de São Carlos. As visualizações aqui apresentadas sao oriundas da base "Pima Indian Diabetes", disponível no [Kaggle](https://www.kaggle.com/datasets/mathchi/diabetes-data-set) e tem como objetivo responder às seguintes hipóteses:

    **1. A obesidade pode aumentar a resistência à insulina e afetar o funcionamento adequado do metabolismo da glicose, predispondo as pessoas ao desenvolvimento de diabetes. Dessa forma, há maior prevalência de diabetes em indivíduos com maior Índice de Massa Corporal (BMI)?**
    
    **2. Diabetes é uma síndrome metabólica, em que a insulina não consegue degradar as moléculas de glicose em velocidade constante, o que torna elevado os índices de açúcar no sangue. Com isso, pode-se afirmar que a glicose (Glucose) deve ser a variável mais significativa no desenvolvimento da doença?**
    
    **3. É sabido que com a idade o corpo vai perdendo a capacidade de produzir insulina ou diminuir a sensibilidade em relação a ela. Com isso, é possível afirmar que a maioria dos pacientes portadores da doença possuem idade (Age) acima dos 40 anos?**
    
    **4. De acordo com a Associação Brasileira para o Estudo da Obesidade e Síndrome Metabólica (ABESO), [os indíviduos são considerados diabéticos quando apresentarem glicemia acima de 126 mg/dL](https://abeso.org.br/qual-o-valor-normal-da-glicemia-saiba-o-que-e-e-como-medir-corretamente/). De acordo com a base de dados, qual intervalo de nível de glicose (Glucose) acomete os pacientes com diabetes?**
    """)

    st.divider()

    st.video("https://youtu.be/RjiqbTLW9_E")