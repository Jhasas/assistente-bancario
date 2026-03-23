from google.adk.agents import Agent

def recomendar_investimento(perfil: str, valor: float) -> dict:
      """Recomenda um investimento de acordo com o perfil do investidor.

      Args:
          perfil: Perfil do investidor. Pode ser conservador, moderado ou arrojado.
          valor: Valor a ser investido.

      Returns:
          Dicionario com a lista de recomendacoes de investimento pelo tipo de investidor.
      """
      if perfil == "conservador":
        return {
          "status": "success",
          "investimentos": [
            {
              "nome": "Tesouro Direto",
              "rentabilidade": "5% ao ano",
              "risco": "baixo",
            },
            {
              "nome": "CDI",
              "rentabilidade": "6% ao ano",
              "risco": "baixo",
            },
            {
              "nome": "LCI",
              "rentabilidade": "7% ao ano",
              "risco": "baixo",
            },
          ],
          "mensagem": f"Recomendacao de investimento para perfil conservador. Valor a ser investido: R$ {valor:.2f}",
        }
      elif perfil == "moderado":
        return {
          "status": "success",
          "investimentos": [
            {
              "nome": "CDB",
              "rentabilidade": "10% ao ano",
              "risco": "medio",
            },
            {
              "nome": "Fundos Imobiliários",
              "rentabilidade": "12% ao ano",
              "risco": "medio",
            },
            {
              "nome": "Debentures",
              "rentabilidade": "13% ao ano",
              "risco": "medio",
            },
         ],
          "mensagem": f"Recomendacao de investimento para perfil moderado. Valor a ser investido: R$ {valor:.2f}",
        }
      else:
        return {
          "status": "success",
          "investimentos": [
            {
              "nome": "Acoes",
              "rentabilidade": "15% ao ano",
              "risco": "alto",
            },
            {
              "nome": "Criptomoedas",
              "rentabilidade": "20% ao ano",
              "risco": "alto",
            },
            {
              "nome": "Acoes Internacionais",
              "rentabilidade": "18% ao ano",
              "risco": "alto",
            },
         ],
          "mensagem": f"Recomendacao de investimento para perfil arrojado. Valor a ser investido: R$ {valor:.2f}",
        }

def consultar_carteira(conta_id: str) -> dict:
      """Consulta a carteira de investimentos de um investidor.

      Args:
          conta_id: Identificador unico da conta do investidor.

      Returns:
          Dicionario com carteira de investimentos e data da consulta.
      """
      # Aqui vai a logica (no nosso caso, dados mock)
      return {
          "status": "success",
          "carteira": [
            {
              "investimento": "Tesouro Direto",
              "rentabilidade": "5% ao ano",
              "risco": "baixo",
              "valor": 1000.00,
            },
            {
              "investimento": "CDB",
              "rentabilidade": "8% ao ano",
              "risco": "medio",
              "valor": 2000.00,
            },
            {
              "investimento": "Acoes",
              "rentabilidade": "12% ao ano",
              "risco": "alto",
              "valor": 3000.00,
            },
          ],
          "mensagem": "Carteira de investimentos consultada com sucesso!",
      }

def simular_rendimento(produto: str, valor: float, meses: int) -> dict:
      """Simula o rendimento de um investimento.

      Args:
          produto: Tipo de produto de investimento.
          valor: Valor a ser investido.
          meses: Tempo de investimento em meses.

      Returns:
          Dicionario com simulacao do rendimento.
      """

      if produto == "Tesouro Direto":
        taxa_juros = 0.05
      elif produto == "CDB":
        taxa_juros = 0.08
      elif produto == "Acoes":
        taxa_juros = 0.12
      elif produto == "Criptomoedas":
        taxa_juros = 0.20
      elif produto == "Acoes Internacionais":
        taxa_juros = 0.18
      else:
        taxa_juros = 0.05

      return {
        "status": "success",
        "valor_investido": valor,
        "valor_rendimento": taxa_juros * valor * (meses/12),
        "valor_total": valor + (taxa_juros * valor * (meses/12)),
        "mensagem": f"Simulacao de rendimento de R$ {valor:.2f} em {meses} meses realizada com sucesso!",
      }

agent = Agent(
      model="gemini-2.0-flash",
      name="investment_agent",
      description="Agente especialista em investimentos.",
      instruction="""Voce e o assistente de investimentos do Banco.

  Suas capacidades:
  - Recomendar investimentos por perfil usando a tool recomendar_investimento
  - Consultar carteira de investimentos atual usando a tool consultar_carteira
  - Simular rendimento de produtos usando a tool simular_rendimento

  Regras:
  - SEMPRE pergunte o perfil do investidor (conservador, moderado ou arrojado) antes de recomendar.
  - Ao recomendar, explique brevemente o nivel de risco de cada produto.
  - Na simulacao de rendimento, deixe claro que sao projecoes e nao garantias.
  - Nunca faca promessas de rentabilidade. Use termos como "rentabilidade estimada" ou "projecao".
  - Seja profissional, cordial e objetivo nas respostas.
  - Apresente valores monetarios no formato brasileiro (R$ 1.234,56).
  """,
      tools=[recomendar_investimento, consultar_carteira, simular_rendimento],
  )