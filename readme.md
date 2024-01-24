# Estudando Clean Arch

    Este repositório contem meus estudos e códigos sobre clean arch, através de vídeos, artigos, livros, repositories etc I.A, focando em Flutter (Enquanto ele existir!).
    Lembre-se que este é meu entendimento sobre Clean Arch, e pode variar de acordo com diferentes perspectivas e interpretações.

## Proposal
    - Estudando Proposta de Arquitetura Limpa para o Dart/Flutter desenvolvida pela comunidade Flutterando    
    - [Clean Dart Propasal Github](https://github.com/Flutterando/Clean-Dart)

    - 4 Camadas principais e idependentes
    ---
        - Regras de negócios corporativas
            São as regras mais sensíveis em relação as outras, conhecidas por entidades, são as classes de domínio que encapsulam as regras de negócios, cruciais para o funcionamento do sistema, fica de certa forma isolada das camadas exteriores, pois não deve conhecer(ter acessos) a elas, independentes de qualquer detalhe específico de infraestrtura, interface ou qualquer outra camada externa, pense como em uma construção de uma casa onde temos paredes, telhados,  pisos... e suas características(features).
            
            class Casa {
                int _numQuartos;

                Casa(this._numQuartos) {
                    if (_numQuartos < 0) {
                        throw ArgumentError("O número de quartos não pode ser negativo");
                    }
                }

                int get numQuartos => _numQuartos;

                set numQuartos(int valor) {
                if (valor < 0) {
                    throw ArgumentError("O número de quartos não pode ser negativo");
                }
                _numQuartos = valor;
                }
            }  
    ---   
        - Regras de negócios da aplicação
            Casos de uso(Usecases) são comandos que devem refletir o que o usuário pode fazer na aplicação, devendo conhecer(Acesso) apenas a camada das entidades, maass... pode necessitar acessar uma camada "superior" por meio do principio de inversão de dependências do SOLID. Essa camada seguindo nossa analogia seria algo como a separação da mobília dentro da casa, por exemplo uma TV no seu banheiro.
            class Casa {
  bool temTVNoBanheiro;

  Casa() : temTVNoBanheiro = false;
}

abstract class InstalarTV {
  void call(Casa casa);
}

class InstalarTVNoBanheiro implements InstalarTV {
  @override
  void call(Casa casa) {
    casa.temTVNoBanheiro = true;
  }
}

void main() {
  Casa minhaCasa = Casa();
  InstalarTV instalarTV = InstalarTVNoBanheiro();

  print(minhaCasa.temTVNoBanheiro); // false
  instalarTV(minhaCasa);
  print(minhaCasa.temTVNoBanheiro); // true
}
    ---
        - Adptadores de interface
            Essa camada pode ser dada como uma camada de suporte para camadas mais altas(Usecases), convertendo os dados externos em dados que possuam um formato que cumpra os contratos(Principio de inversão de dependencias) definidos pelas regras de negócios. Na nossa analogia seria como mostrar nossa casa para amigos estrangeiros através de um tradutor(não consegui pensar em nada melhor créditos ao github copilot)
    --- 
        - Frameworks e Drivers (Externos)
            Todas as abstrações das camadas superiores são aproveitadas nessa, na facilidadde do plug and play dos artefatos externos como um BD ou uma interface gráfica, todas as alterações aqui devem ser seguras para as camadas de nível mais alto, na construção de nossa casa seriam como as ferramentas, pregos, colas e etc para a construção da casa.
    --- 
        - Complementos

            -SOLID(Principio de inversão de dependencias)
                D — Dependency Inversion Principle (Princípio da inversão da dependência) 
                    Evitar depedencias diretas entre as camadas de baixo e alto nível, fazendo a comunicação através de abstrações, protegendo o código de alto nível.
                    