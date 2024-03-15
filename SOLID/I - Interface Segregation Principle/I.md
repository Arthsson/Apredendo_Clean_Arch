# Princípio de Segregação de Interface (ISP)

## Definição

O ISP estabelece que uma classe não deve ser forçada a depender de métodos que não utiliza. Em outras palavras, interfaces grandes e genéricas devem ser divididas em interfaces menores e mais específicas, de modo que as classes só precisem implementar os métodos que realmente precisam.

## Benefícios

- **Modularidade:** Dividir interfaces em partes menores permite que as classes dependam apenas dos métodos relevantes para suas responsabilidades, promovendo uma estrutura de código mais modular e coesa.
- **Flexibilidade:** Classes podem implementar apenas as interfaces que são pertinentes às suas necessidades, facilitando a reutilização de código e a introdução de novas funcionalidades.
- **Manutenibilidade:** Interfaces mais específicas tornam mais claro o contrato entre classes, facilitando a compreensão e a manutenção do código ao longo do tempo.
