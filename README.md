# PPC1 - Cálculo Numérico Aplicado

## 📌 Descrição

Este projeto implementa o método de Runge-Kutta de quarta ordem (RK4) para resolver numericamente a equação diferencial que descreve o movimento de uma partícula esférica em um fluido viscoso.

---

## 📐 Problema

A equação diferencial adimensional resolvida é:

dv*/dt* = (1 - v* - (3/8)Re (v*)²) / St

onde:
- St: número de Stokes
- Re: número de Reynolds

---

## ⚙️ Método Numérico

Foi utilizado o método de Runge-Kutta de 4ª ordem (RK4), um método explícito com erro global da ordem de O(h⁴), garantindo boa precisão numérica.

---

## 📊 Análises Realizadas

### 1. Validação (Re → 0)

Comparação da solução numérica com a solução analítica:

v*(t) = 1 - exp(-t/St)

Resultado: excelente concordância entre as curvas.

---

### 2. Refinamento Temporal

Foram utilizados diferentes passos de tempo:
- h = 0.5
- h = 0.1
- h = 0.01

Resultado: quanto menor o passo, maior a precisão da solução.

---

### 3. Efeito do Número de Reynolds

Foram analisados diferentes valores:
- Re = 0.0
- Re = 0.5
- Re = 1.0
- Re = 2.0

Resultado: aumento do Re provoca desvio em relação ao regime de Stokes.

---

## ▶️ Como Executar

1. Certifique-se de ter Python instalado
2. Instale as dependências:

```bash
pip install numpy matplotlib
