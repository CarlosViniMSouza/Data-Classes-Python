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

### Embora isso não seja muito mais código para escrever, você já pode ver sinais da dor do clichê: classificação e naipe são repetidos três vezes simplesmente para inicializar um objeto. Além disso, se você tentar usar essa classe simples, notará que a representação dos objetos não é muito descritiva, e por alguma razão uma rainha de copas não é o mesmo que uma rainha de copas:

```Python Console
>>> queen_of_hearts = RegularCard('Q', 'Hearts')
>>> queen_of_hearts.rank
'Q'
>>> queen_of_hearts
<__main__.RegularCard object at 0x7fb6eee35d30>
>>> queen_of_hearts == RegularCard('Q', 'Hearts')
False
```

### Parece que as classes de dados estão nos ajudando nos bastidores. Por padrão, as classes de dados implementam um [método .__repr__()](https://realpython.com/operator-function-overloading/) para fornecer uma boa representação de string e um método .__eq__() que pode fazer comparações básicas de objetos. Para a classe RegularCard imitar a classe de dados acima, você precisa adicionar estes métodos também:

```Python
class RegularCard
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)
```

### Neste tutorial, você aprenderá exatamente quais as conveniências que as classes de dados oferecem. Além de boas representações e comparações, você verá:

```
  ° Como adicionar valores padrão aos campos de classe de dados
  ° Como as classes de dados permitem a ordenação de objetos
  ° Como representar dados imutáveis
  ° Como as classes de dados lidam com a herança
```

### Em breve, nos aprofundaremos nesses recursos das classes de dados. No entanto, você pode estar pensando que já viu algo assim antes.

## Alternativas às classes de dados

### Para estruturas de dados simples, você provavelmente já usou uma tupla ou um ditado. Você pode representar a carta dama de copas de uma das seguintes maneiras:

```Python Console
>>> queen_of_hearts_tuple = ('Q', 'Hearts')
>>> queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}
```

### Funciona. No entanto, isso coloca muita responsabilidade em você como programador:

```
  ° Você precisa lembrar que a variável queen_of_hearts_... representa uma carta.

  ° Para a versão de tupla, você precisa lembrar a ordem dos atributos. Escrever ('Spades', 'A') atrapalhará seu programa, mas provavelmente não fornecerá uma mensagem de erro facilmente compreensível.

  ° Se você usar a versão dict, deverá certificar-se de que os nomes dos atributos sejam consistentes. Por exemplo, {'value': 'A', 'suit': 'Spades'} não funcionará como esperado.
```

### Além disso, usar essas estruturas não é ideal:

```Python Console
>>> queen_of_hearts_tuple[0]  # No named access
'Q'
>>> queen_of_hearts_dict['suit']  # Would be nicer with .suit
'Hearts'
```

### Uma alternativa melhor é a [`namedtuple`](https://dbader.org/blog/writing-clean-python-with-namedtuples). Ele tem sido usado há muito tempo para criar pequenas estruturas de dados legíveis. Na verdade, podemos recriar o exemplo de classe de dados acima usando um `namedtuple` como este:

```Python
from collections import namedtuple

NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])
```

### Esta definição de `NamedTupleCard` fornecerá exatamente a mesma saída que nosso exemplo de `DataClassCard` deu:

```Python Console
>>> queen_of_hearts = NamedTupleCard('Q', 'Hearts')
>>> queen_of_hearts.rank
'Q'
>>> queen_of_hearts
NamedTupleCard(rank='Q', suit='Hearts')
>>> queen_of_hearts == NamedTupleCard('Q', 'Hearts')
True
```

### Então, por que se preocupar com classes de dados? Em primeiro lugar, as classes de dados vêm com muito mais recursos do que você viu até agora. Ao mesmo tempo, a `namedtuple` possui alguns outros recursos que não são necessariamente desejáveis. Por design, uma `namedtuple` é uma tupla regular. Isso pode ser visto em comparações, por exemplo:

```Python Console
>>> queen_of_hearts == ('Q', 'Hearts')
True
```
