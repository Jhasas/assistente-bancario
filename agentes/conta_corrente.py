def consultar_saldo(conta_id: str) -> dict:
      """Consulta o saldo atual de uma conta corrente.

      Args:
          conta_id: Identificador unico da conta corrente.

      Returns:
          Dicionario com saldo disponivel e data da consulta.
      """
      # Aqui vai a logica (no nosso caso, dados mock)
      return {
          "status": "success",
          "conta_id": conta_id,
          "saldo_disponivel": 15432.50,
      }

def consultar_extrato(conta_id: str, dias: int) -> dict:
      """Consulta o extrato de uma conta corrente.

      Args:
          conta_id: Identificador unico da conta corrente.
          dias: Numero de dias a consultar.

      Returns:
          Dicionario com extrato da conta corrente.
      """
      # Aqui vai a logica (no nosso caso, dados mock)
      return {
          "status": "success",
          "conta_id": conta_id,
          "transacoes": [
            {
              "data": "2026-03-17",
              "descricao": "Transferencia PIX",
              "valor": 100.00,
            },
            {
              "data": "2026-03-16",
              "descricao": "Transferencia PIX",
              "valor": 200.00,
            },
          ],
      }

def realizar_pix(conta_origem: str, conta_destino: str, valor: float) -> dict:
      """Realiza uma transferencia PIX entre contas.

      Args:
          conta_origem: Conta corrente de origem.
          conta_destino: Conta corrente de destino.
          valor: Valor a ser transferido.

      Returns:
          Dicionario com status da transferencia e dados da operacao.
      """

      # Validação 1: valor precisa ser positivo
      if valor <= 0:
        return {
          "status": "error",
          "mensagem": "O Valor do PIX deve ser positivo",
        }

      # Validação 2: limite diurno
      if valor > 10000:
        return {
          "status": "error",
          "mensagem": "O Valor do PIX excede o limite diurno de R$ 10.000,00",
        }

      # Validação 3: saldo insuficiente
      saldo = consultar_saldo(conta_origem)["saldo_disponivel"]
      if valor > saldo:
        return {
          "status": "error",
          "mensagem": "Saldo insuficiente para realizar o PIX",
        }

      # Sucesso: retorna comprovante
      return {
        "status": "success",
        "conta_origem": conta_origem,
        "conta_destino": conta_destino,
        "valor": valor,
        "data": "2026-03-17",
        "comprovante": "PIX-20260317-ABC123",
        "mensagem": f"PIX de R$ {valor:.2f} para a conta {conta_destino} realizado com sucesso!",
      }