![logo-article](https://files.realpython.com/media/The-Ultimate-Guide-to-Data-Classes-in-Python-3.7_Watermarked.96432fedfe8f.jpg)

## por Geir Arne Hjelle

```
Sumário:

° Alternativas às Classes de Dados

° Classes de dados básicos
  ° Valores padrão
  ° Dicas de tipo
  ° Métodos de adição

° Classes de dados mais flexíveis
  ° Valores padrão avançados
  ° Precisa de Representação?
  ° Comparação de Cartões

° Classes de dados imutáveis

° Herança

° Otimizando Classes de Dados

° Conclusão e Leitura Complementar
```

### Um [recurso novo e empolgante no Python 3.7](https://realpython.com/python37-new-features/) é a classe de dados. Uma classe de dados é uma classe que normalmente contém principalmente dados, embora não haja realmente nenhuma restrição. Ele é criado usando o novo decorador @dataclass, da seguinte forma:

```Python
from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str
```

`NOTE: Este código, assim como todos os outros exemplos neste tutorial, funcionará apenas no Python 3.7 e superior.`

### Uma classe de dados vem com funcionalidades básicas já implementadas. Por exemplo, você pode instanciar, imprimir e comparar instâncias de classes de dados imediatamente:

```Python
>>> queen_of_hearts = DataClassCard('Q', 'Hearts')
>>> queen_of_hearts.rank
'Q'
>>> queen_of_hearts
DataClassCard(rank='Q', suit='Hearts')
>>> queen_of_hearts == DataClassCard('Q', 'Hearts')
True
```

### Compare isso com uma aula normal. Uma classe regular mínima seria algo assim:

```Python
class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
```