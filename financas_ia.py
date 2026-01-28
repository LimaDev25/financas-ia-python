import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import re

class FinancasIA:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, valor, descricao, tipo="despesa"):
        # IA SIMPLES: classifica categoria automaticamente
        categoria = self._classificar_categoria(descricao)
        transacao = {
            'data': datetime.now(),
            'valor': valor if tipo == "receita" else -valor,
            'descricao': descricao,
            'categoria': categoria,
            'tipo': tipo
        }
        self.transacoes.append(transacao)
    
    def _classificar_categoria(self, descricao):
        descricao_lower = descricao.lower()
        if any(palavra in descricao_lower for palavra in ['mercado', 'supermercado', 'alimentos']):
            return 'Alimentação'
        elif any(palavra in descricao_lower for palavra in ['netflix', 'spotify', 'prime', 'cinema']):
            return 'Lazer'
        elif any(palavra in descricao_lower for palavra in ['salário', 'freelance']):
            return 'Salário'
        else:
            return 'Outros'
    
    def grafico_gastos(self):
        df = pd.DataFrame(self.transacoes)
        if df.empty:
            print("Sem transações!")
            return
        
        gastos_por_categoria = df[df['valor'] < 0].groupby('categoria')['valor'].sum().abs()
        
        plt.figure(figsize=(10,6))
        gastos_por_categoria.plot(kind='pie', autopct='%1.1f%%')
        plt.title('🧠 Análise Inteligente: Seus Gastos por Categoria')
        plt.ylabel('')
        plt.savefig('analise_gastos.png')
        plt.show()
    
    def previsao_proximos_30dias(self):
        if len(self.transacoes) < 5:
            return "Colete mais dados!"
        
        df = pd.DataFrame(self.transacoes)
        media_diaria = df['valor'].sum() / len(df)
        previsao = media_diaria * 30
        print(f"🔮 Previsão 30 dias: R$ {previsao:.2f}")
        return previsao
    
    def sugestoes_inteligentes(self):
        df = pd.DataFrame(self.transacoes)
        gastos_categoria = df[df['valor'] < 0].groupby('categoria')['valor'].sum().abs()
        
        for cat, valor in gastos_categoria.items():
            if valor > 500:
                print(f"💡 {cat}: Você gastou R${valor:.2f}! Considere reduzir 20%.")

# INTERFACE PRINCIPAL
def main():
    financas = FinancasIA()
    
    while True:
        print("\n=== FINANÇAS IA PYTHON ===")
        print("1. Adicionar Receita\n2. Adicionar Despesa\n3. Gráfico Gastos\n4. Previsão 30 dias\n5. Sugestões IA\n6. Sair")
        
        op = input("Escolha: ")
        
        if op == '1':
            valor = float(input("Valor da receita: "))
            desc = input("Descrição: ")
            financas.adicionar_transacao(valor, desc, "receita")
            
        elif op == '2':
            valor = float(input("Valor da despesa: "))
            desc = input("Descrição: ")
            financas.adicionar_transacao(valor, desc)
            
        elif op == '3':
            financas.grafico_gastos()
            
        elif op == '4':
            financas.previsao_proximos_30dias()
            
        elif op == '5':
            financas.sugestoes_inteligentes()
            
        elif op == '6':
            break

if __name__ == "__main__":
    main()
