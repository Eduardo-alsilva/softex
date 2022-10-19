import pandas as pd
df=pd.read_csv("notas_aluno.csv")
media=(df["Nota_1"] + df["Nota_2"])/2
df["media"]= media 
df.loc[df["media"]>=7,"situação"]= "aprovado"
df.loc[df["Faltas"]<=5,"situação"]= "aprovado"
df.loc[df["media"]<7,"situação"]= "reprovado"
df.loc[df["Faltas"]>5,"situação"]= "reprovado"
df.to_csv("alunos_situação.csv")
Maior_faltas=df["Faltas"].max()
Media=df["media"].median()
Maior_media=df["media"].max()
print("O maior numero de faltas foi:" ,Maior_faltas) 
print("A Media foi:" ,Media)
print("E a maior Media foi:",Maior_media)
