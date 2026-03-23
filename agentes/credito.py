from google.adk.agents import Agent

def simular_emprestimo(valor: float, parcelas: int, tipo: str) -> dict:
      """Simula um emprestimo.

      Args:
          valor: Valor do emprestimo.
          parcelas: Numero de parcelas.
          tipo: Tipo de emprestimo. Pode ser pessoal, consignado ou imobiliario. A taxa de juros varia de acordo com o tipo de emprestimo.

      Returns:
          Dicionario com simulacao do emprestimo.
      """
      taxa_juros = 0.018 # 1.8% ao mes
      if tipo == "consignado":
        taxa_juros = 0.012 # 1.2% ao mes
      elif tipo == "imobiliario":
        taxa_juros = 0.009 # 0.9% ao mes

      valor_total = valor * (1 + taxa_juros * parcelas)
      valor_parcela = valor_total / parcelas

      return {
        "status": "success",
        "valor_total": valor_total,
        "taxa_juros": taxa_juros * parcelas,
        "valor_parcela": valor_parcela,
        "mensagem": f"Simulacao de emprestimo de R$ {valor:.2f} em {parcelas}x de R$ {valor_parcela:.2f} realizada com sucesso!",
      }

def consultar_limite(conta_id: str) -> dict:
      """Consulta o limite disponivel de uma conta corrente.

      Args:
          conta_id: Identificador unico da conta corrente.

      Returns:
          Dicionario com limite disponivel e data da consulta.
      """
      # Aqui vai a logica (no nosso caso, dados mock)
      return {
          "status": "success",
          "limite_total": 50000.00,
          "limite_disponivel": 15432.50,
          "limite_utilizado": 34567.50,
          "mensagem": f"Limite disponivel de R$ {15432.50:.2f} para emprestimo.",
      }

def consultar_status_proposta(proposta_id: str) -> dict:
      """Consulta o status de uma proposta de emprestimo.

      Args:
          proposta_id: Identificador unico da proposta.

      Returns:
          Dicionario com status da proposta e data da consulta.
      """
      # Aqui vai a logica (no nosso caso, dados mock)
      return {
          "status": "success",
          "proposta_id": proposta_id,
          "status_proposta": "aprovada",
          "data_aprovacao": "2026-03-17",
          "valor_aprovado": 15432.50,
          "mensagem": f"Proposta de emprestimo de R$ {15432.50:.2f} aprovada com sucesso!",
      }

agent = Agent(
      model="gemini-2.0-flash",
      name="credit_agent",
      description="Agente especialista em analise de credito.",
      instruction="""Voce e o assistente de credito do Banco.

  Suas capacidades:
  - Simular emprestimos (pessoal, consignado, imobiliario) usando a tool simular_emprestimo
  - Consultar limite de credito disponivel usando a tool consultar_limite
  - Consultar status de propostas existentes usando a tool consultar_status_proposta

  Regras:
  - Ao simular emprestimo, apresente claramente: valor total, taxa de juros, valor da parcela e numero de parcelas.
  - Se o cliente nao especificar o tipo de emprestimo, pergunte se e pessoal, consignado ou imobiliario.
  - Sempre alerte o cliente sobre o custo total do emprestimo (valor total - valor solicitado = juros pagos).
  - Seja profissional, cordial e objetivo nas respostas.
  - Apresente valores monetarios no formato brasileiro (R$ 1.234,56).
  """,
      tools=[simular_emprestimo, consultar_limite, consultar_status_proposta],
  )