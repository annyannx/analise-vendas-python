import pandas as pd
import matplotlib.pyplot as plt

# 1. CARREGAMENTO DOS DADOS

dados = pd.read_csv("data/vendas.csv")

print("\n===== ANÁLISE DE VENDAS =====\n")

print("Primeiros registros:")
print(dados.head())


# 2. PREPARAÇÃO DOS DADOS

dados["data"] = pd.to_datetime(dados["data"])

dados["faturamento"] = (
    dados["quantidade"] * dados["preco_unitario"]
)


# 3. INDICADORES GERAIS

faturamento_total = dados["faturamento"].sum()
quantidade_total = dados["quantidade"].sum()

produto_mais_vendido = (
    dados.groupby("produto")["quantidade"]
    .sum()
    .idxmax()
)

produto_maior_faturamento = (
    dados.groupby("produto")["faturamento"]
    .sum()
    .idxmax()
)


print("\n===== INDICADORES =====")

print(f"Faturamento total: R$ {faturamento_total:,.2f}")
print(f"Quantidade total vendida: {quantidade_total}")
print(f"Produto com maior quantidade vendida: {produto_mais_vendido}")
print(f"Produto com maior faturamento: {produto_maior_faturamento}")


# 4. FATURAMENTO POR PRODUTO

faturamento_produto = (
    dados.groupby("produto")["faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== FATURAMENTO POR PRODUTO =====")
print(faturamento_produto)



# 5. FATURAMENTO POR CATEGORIA

faturamento_categoria = (
    dados.groupby("categoria")["faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== FATURAMENTO POR CATEGORIA =====")
print(faturamento_categoria)


# 6. GRÁFICO DE FATURAMENTO POR PRODUTO

faturamento_produto.plot(
    kind="bar",
    title="Faturamento por Produto",
    xlabel="Produto",
    ylabel="Faturamento (R$)"
)

plt.tight_layout()
plt.savefig("faturamento_por_produto.png")
plt.show()