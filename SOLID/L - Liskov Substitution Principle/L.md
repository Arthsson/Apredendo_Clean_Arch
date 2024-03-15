# Princípio da Substituição de Liskov (LSP)

## Definição

O LSP estabelece que objetos de uma classe derivada devem ser capazes de substituir objetos de sua classe base sem interromper o funcionamento do programa. Isso significa que as subclasses devem preservar o contrato estabelecido pela classe base, garantindo que o comportamento esperado do programa não seja afetado.

## Benefícios

- **Flexibilidade:** O LSP permite que novas classes possam ser introduzidas no sistema sem a necessidade de modificar o código existente, tornando-o mais flexível e adaptável a mudanças.
- **Reutilização de código:** As classes que seguem o LSP são mais reutilizáveis, pois podem ser facilmente substituídas por suas superclasses sem introduzir efeitos colaterais indesejados.
- **Manutenibilidade:** Ao garantir que as subclasses preservem o contrato da classe base, o LSP facilita a manutenção do código, reduzindo a probabilidade de erros e simplificando o processo de debug.
