# Princípio de Inversão de Dependência (DIP)

## Definição

O DIP estabelece que módulos de alto nível não devem depender de módulos de baixo nível, mas sim de abstrações. Além disso, tanto módulos de alto nível quanto módulos de baixo nível devem depender de abstrações.

## Benefícios

- **Flexibilidade:** Ao depender de abstrações em vez de implementações concretas, o código se torna mais flexível e extensível. É possível substituir ou modificar facilmente as implementações sem afetar o código existente.
- **Desacoplamento:** O DIP reduz o acoplamento entre os diferentes componentes do sistema, tornando-os mais independentes e isolados. Isso facilita a manutenção e evita efeitos colaterais indesejados.
- **Testabilidade:** O código que segue o DIP é mais fácil de testar, pois é mais simples substituir implementações reais por objetos simulados ou de teste durante os testes unitários.
