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

```Python Console
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
class RegularCard:
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

### Embora isso possa parecer uma coisa boa, essa falta de conhecimento sobre seu próprio tipo pode levar a bugs sutis e difíceis de encontrar, especialmente porque também comparará duas classes de `namedtuple` diferentes:

```Python Console
>>> Person = namedtuple('Person', ['first_initial', 'last_name']
>>> ace_of_spades = NamedTupleCard('A', 'Spades')
>>> ace_of_spades == Person('A', 'Spades')
True
```

### The `namedtuple` also comes with some restrictions. For instance, it is hard to add default values to some of the fields in a `namedtuple`. A `namedtuple` is also by nature immutable. That is, the value of a `namedtuple` can never change. In some applications, this is an awesome feature, but in other settings, it would be nice to have more flexibility:

```Python Console
>>> card = NamedTupleCard('7', 'Diamonds')
>>> card.rank = '9'
AttributeError: can't set attribute
```

### As classes de dados não substituirão todos os usos de `namedtuple`. Por exemplo, se você precisa que sua estrutura de dados se comporte como uma tupla, uma tupla nomeada é uma ótima alternativa!

### Outra alternativa, e uma das [inspirações para classes de dados](https://mail.python.org/pipermail/python-dev/2017-December/151034.html), é o [projeto attrs](http://www.attrs.org/). Com o `attrs` instalado (`pip install attrs`), você pode escrever uma classe de cartão da seguinte forma:

```Python
import attr

@attr.s
class AttrsCard:
    rank = attr.ib()
    suit = attr.ib()
```

### Isso pode ser usado exatamente da mesma maneira que os exemplos `DataClassCard` e `NamedTupleCard` anteriores. O projeto `attrs` é ótimo e suporta alguns recursos que as classes de dados não suportam, incluindo conversores e validadores. Além disso, o `attrs` existe há algum tempo e é suportado no Python 2.7, bem como no Python 3.4 e superior. Contudo, como o `attrs` não faz parte da biblioteca padrão, ele adiciona uma [dependency](https://realpython.com/courses/managing-python-dependencies/) externa aos seus projetos. Por meio de classes de dados, funcionalidades semelhantes estarão disponíveis em todos os lugares.

### Além de `tuple, dict, namedtuple` e `attrs`, existem [muitos outros projetos semelhantes](https://www.python.org/dev/peps/pep-0557/#rationale), incluindo [`type.NamedTuple`](https://docs.python.org/library/typing.html#typing.NamedTuple), [`namedlist`](https://pypi.org/project/namedlist/), [`attrdict`](https://pypi.org/project/attrdict/), [`plumber`](https://pypi.org/project/plumber/) e [`fields`](https://pypi.org/project/fields/). Embora as classes de dados sejam uma ótima nova alternativa, ainda há casos de uso em que uma das variantes mais antigas se encaixa melhor. Por exemplo, se você precisar de compatibilidade com uma API específica esperando tuplas ou precisar de uma funcionalidade não suportada em classes de dados.

## Classes de dados básicos

### Voltemos às classes de dados. Como exemplo, criaremos uma classe `Position` que representará as posições geográficas com um nome, bem como a latitude e a longitude:

```Python
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float
```

### O que torna isso uma classe de dados é o [decorador @dataclass](https://realpython.com/primer-on-python-decorators/) logo acima da definição da classe. Abaixo da `classe Position`: linha, você simplesmente lista os campos que deseja em sua classe de dados. A notação : usada para os campos está usando um novo recurso no Python 3.6 chamado [anotações de variáveis](https://www.python.org/dev/peps/pep-0526/). [Em breve](https://realpython.com/python-data-classes/#type-hints) falaremos mais sobre essa notação e por que especificamos tipos de dados como str e float.

### Essas poucas linhas de código são tudo que você precisa. A nova classe está pronta para uso:

```Python Console
>>> pos = Position('Oslo', 10.8, 59.9)
>>> print(pos)
Position(name='Oslo', lon=10.8, lat=59.9)
>>> pos.lat
59.9
>>> print(f'{pos.name} is at {pos.lat}°N, {pos.lon}°E')
Oslo is at 59.9°N, 10.8°E
```

### Você também pode criar classes de dados da mesma forma que as tuplas nomeadas são criadas. O seguinte é (quase) equivalente à definição de `Position` acima:

```Python
from dataclasses import make_dataclass

Position = make_dataclass('Position', ['name', 'lat', 'lon'])
```

### Uma classe de dados é uma classe regular do Python. A única coisa que o diferencia é que ele tem [métodos básicos de modelo de dados](https://docs.python.org/reference/datamodel.html#basic-customization) como `.__init__(), .__repr__()` e `.__eq__()` implementados para você.

## Valores padrão

### É fácil adicionar valores padrão aos campos de sua classe de dados:

```Python
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0
```

### Isso funciona exatamente como se você tivesse especificado os valores padrão na definição do método `.__init__()` de uma classe regular:

```Python Console
>>> Position('Null Island')
Position(name='Null Island', lon=0.0, lat=0.0)
>>> Position('Greenwich', lat=51.8)
Position(name='Greenwich', lon=0.0, lat=51.8)
>>> Position('Vancouver', -123.1, 49.3)
Position(name='Vancouver', lon=-123.1, lat=49.3)
```

### [Mais tarde](https://realpython.com/python-data-classes/#advanced-default-values), você aprenderá sobre `default_factory`, que oferece uma maneira de fornecer valores padrão mais complicados.

## Dicas de tipo

### Até agora, não fizemos um grande alarido sobre o fato de que as classes de dados suportam a [digitação](https://realpython.com/python-type-checking/) pronta para uso. Você provavelmente notou que definimos os campos com uma dica de tipo: `name: str` diz que o `name` deve ser uma [string de texto](https://realpython.com/python-strings/) (tipo `str`).

### Na verdade, adicionar algum tipo de dica de tipo é obrigatório ao definir os campos em sua classe de dados. Sem uma dica de tipo, o campo não fará parte da classe de dados. No entanto, se você não quiser adicionar tipos explícitos à sua classe de dados, use `digitação.Any`:

```python
from dataclasses import dataclass
from typing import Any

@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42
```

### Embora você precise adicionar dicas de tipo de alguma forma ao usar classes de dados, esses tipos não são impostos em tempo de execução. O código a seguir é executado sem problemas:

```Python Console
>>> Position(3.14, 'pi day', 2018)
Position(name=3.14, lon='pi day', lat=2018)
```

### É assim que a digitação em Python geralmente funciona: [Python é e sempre será uma linguagem tipada dinamicamente](https://www.python.org/dev/peps/pep-0484/#non-goals). Para realmente detectar erros de tipo, verificadores de tipo como o [Mypy](http://mypy-lang.org/) podem ser executados em seu código-fonte.

```
NOTE: para instalar o Mypy, use o comando: 

$ python3 -m pip install mypy
```

## Adicionando métodos

### Você já sabe que uma classe de dados é apenas uma classe regular. Isso significa que você pode adicionar livremente seus próprios métodos a uma classe de dados. Como exemplo, vamos calcular a distância entre uma posição e outra, ao longo da superfície da Terra. Uma maneira de fazer isso é usando [a fórmula de Haversine](https://en.wikipedia.org/wiki/Haversine_formula):

![Haversine_Formula](https://files.realpython.com/media/haversine_formula_150.fb2b87d122a4.png)

### Você pode adicionar um método `.distance_to()` à sua classe de dados assim como você pode fazer com classes normais:

```Python
from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))
```

### Funciona como você esperaria:

```Python Console
>>> oslo = Position('Oslo', 10.8, 59.9)
>>> vancouver = Position('Vancouver', -123.1, 49.3)
>>> oslo.distance_to(vancouver)
7181.784122942117
```

## Classes de dados mais flexíveis

### Até agora, você viu alguns dos recursos básicos da classe de dados: ela oferece alguns métodos de conveniência e você ainda pode adicionar valores padrão e outros métodos. Agora você aprenderá sobre alguns recursos mais avançados, como parâmetros para o decorador `@dataclass` e a função `field()`. Juntos, eles lhe dão mais controle ao criar uma classe de dados.

### Vamos voltar ao exemplo do baralho que você viu no início do tutorial e adicionar uma classe contendo um baralho de cartas enquanto estamos nisso:

```Python
from dataclasses import dataclass
from typing import List

@dataclass
class PlayingCard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[PlayingCard]
```

### Um baralho simples contendo apenas duas cartas pode ser criado assim:

```Python Console
>>> queen_of_hearts = PlayingCard('Q', 'Hearts')
>>> ace_of_spades = PlayingCard('A', 'Spades')
>>> two_cards = Deck([queen_of_hearts, ace_of_spades])
Deck(cards=[PlayingCard(rank='Q', suit='Hearts'),
            PlayingCard(rank='A', suit='Spades')])
```

## Valores padrão avançados

### Digamos que você queira dar um valor padrão ao Deck. Por exemplo, seria conveniente se `Deck()` criasse um [baralho regular (francês)](https://en.wikipedia.org/wiki/French_playing_cards) de 52 cartas de baralho. Primeiro, especifique as diferentes graduações e naipes. Em seguida, adicione uma função `make_french_deck()` que cria uma [lista](https://realpython.com/python-lists-tuples/) de instâncias de `PlayingCard`:

```Python
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]
```

### Por diversão, os quatro naipes diferentes são especificados usando seus [símbolos Unicode](https://en.wikipedia.org/wiki/Playing_cards_in_Unicode).

### Para simplificar as comparações de cartas mais tarde, as fileiras e naipes também são listados em sua ordem usual.

### Em teoria, agora você pode usar esta função para especificar um valor padrão para Deck.cards:

```Python
from dataclasses import dataclass
from typing import List

@dataclass
class Deck:  # Will NOT work
    cards: List[PlayingCard] = make_french_deck()
```

### O especificador `field()` é usado para personalizar cada campo de uma classe de dados individualmente. Você verá alguns outros exemplos mais tarde. Para referência, estes são os parâmetros que `field()` suporta:

```
° default: valor padrão do campo
° default_factory: Função que retorna o valor inicial do campo
° init: Usar campo no método .__init__()? (O padrão é Verdadeiro.)
° repr: Usar campo em repr do objeto? (O padrão é Verdadeiro.)
° compare: Incluir o campo nas comparações? (O padrão é Verdadeiro.)
° hash: Incluir o campo ao calcular hash()? (O padrão é usar o mesmo que para comparar.)
° metadatas: Um mapeamento com informações sobre o campo
```

### No exemplo `Position`, você viu como adicionar valores padrão simples escrevendo `lat: float = 0.0`. No entanto, se você também deseja personalizar o campo, por exemplo, para ocultá-lo no `repr`, você precisa usar o parâmetro `default`: `lat: float = field(default=0.0, repr=False)`. Você não pode especificar `default` e `default_factory`.

### O parâmetro de `metadatas` não é usado pelas próprias classes de dados, mas está disponível para você (ou pacotes de terceiros) anexar informações aos campos. No exemplo `Position`, você pode, por exemplo, especificar que a latitude e a longitude devem ser dadas em graus:

```Python
from dataclasses import dataclass, field

@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})
```

### Os metadados (e outras informações sobre um campo) podem ser recuperados usando a função `fields()` (observe o plural `s`):

```Python Console
>>> from dataclasses import fields
>>> fields(Position)
(Field(name='name',type=<class 'str'>,...,metadata={}),
 Field(name='lon',type=<class 'float'>,...,metadata={'unit': 'degrees'}),
 Field(name='lat',type=<class 'float'>,...,metadata={'unit': 'degrees'}))
>>> lat_unit = fields(Position)[2].metadata['unit']
>>> lat_unit
'degrees'
```

## Classes de dados imutáveis

### Uma das características que definem o `namedtuple` que você viu anteriormente é que ele é [imutável](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747). Ou seja, o valor de seus campos pode nunca mudar. Para muitos tipos de classes de dados, esta é uma ótima ideia! Para tornar uma classe de dados imutável, defina `frozen=True` ao criá-la. Por exemplo, o seguinte é uma versão imutável da classe `Position` que [você viu anteriormente](https://realpython.com/python-data-classes/#basic-data-classes):

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0
```

### Em uma classe de dados congelados, você não pode atribuir valores aos campos após a criação:

```Python Console
>>> pos = Position('Oslo', 10.8, 59.9)
>>> pos.name
'Oslo'
>>> pos.name = 'Stockholm'
dataclasses.FrozenInstanceError: cannot assign to field 'name'
```

### Esteja ciente de que, se sua classe de dados contiver campos mutáveis, eles ainda poderão ser alterados. Isso é verdade para todas as estruturas de dados aninhadas em Python (veja [este vídeo para mais informações](https://www.youtube.com/watch?v=p9ppfvHv2Us)):

```python
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str

@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[ImmutableCard]
```

### Mesmo que tanto `ImmutableCard` quanto `ImmutableDeck` sejam imutáveis, a lista de `cartas` não é. Portanto, você ainda pode alterar as cartas do baralho:

```Python Console
>>> queen_of_hearts = ImmutableCard('Q', '♡')
>>> ace_of_spades = ImmutableCard('A', '♠')
>>> deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
>>> deck
ImmutableDeck(cards=[ImmutableCard(rank='Q', suit='♡'), ImmutableCard(rank='A', suit='♠')])
>>> deck.cards[0] = ImmutableCard('7', '♢')
>>> deck
ImmutableDeck(cards=[ImmutableCard(rank='7', suit='♢'), ImmutableCard(rank='A', suit='♠')])
```

### Para evitar isso, certifique-se de que todos os campos de uma classe de dados imutáveis usem tipos imutáveis (mas lembre-se de que os tipos não são impostos em tempo de execução). O `ImmutableDeck` deve ser implementado usando uma tupla em vez de uma lista.

## Herança

### Você pode subclassificar classes de dados livremente. Como exemplo, estenderemos nosso exemplo de Posição com um campo de país e o usaremos para registrar capitais:

```python
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float

@dataclass
class Capital(Position):
    country: str
```

### Neste exemplo simples, tudo funciona sem problemas:

```Python Console
>>> Capital('Oslo', 10.8, 59.9, 'Norway')
Capital(name='Oslo', lon=10.8, lat=59.9, country='Norway')
```

### O campo de `country` de `Capital` é adicionado após os três campos originais em `Position`. As coisas ficam um pouco mais complicadas se algum campo na classe base tiver valores padrão:

```python
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

@dataclass
class Capital(Position):
    country: str  # Does NOT work
```

### Este código irá travar imediatamente com um `TypeError` reclamando que "o argumento não padrão 'país' segue o argumento padrão". O problema é que nosso novo campo `country` não possui valor padrão, enquanto os campos lon e lat possuem valores padrão. A classe de dados tentará escrever um método `.__init__()` com a seguinte assinatura:

```python
def __init__(name: str, lon: float = 0.0, lat: float = 0.0):
    ...
```

### No entanto, isso não é Python válido. [Se um parâmetro tiver um valor padrão, todos os parâmetros a seguir também deverão ter um valor padrão](https://docs.python.org/reference/compound_stmts.html#function-definitions). Em outras palavras, se um campo em uma classe base tiver um valor padrão, todos os novos campos adicionados em uma subclasse também deverão ter valores padrão.

### Outra coisa a ser observada é como os campos são ordenados em uma subclasse. Começando com a classe base, os campos são ordenados na ordem em que são definidos pela primeira vez. Se um campo é redefinido em uma subclasse, sua ordem não muda. Por exemplo, se você definir `Position` e `Capital` da seguinte forma:

```python
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

@dataclass
class Capital(Position):
    country: str = 'Unknown'
    lat: float = 40.0
```

### Então a ordem dos campos em Capital ainda será nome, lon, lat, país. No entanto, o valor padrão de lat será 40,0.

```Python Console
>>> Capital('Madrid', country='Spain')
Capital(name='Madrid', lon=0.0, lat=40.0, country='Spain')
```

## Otimizando classes de dados

### Vou terminar este tutorial com algumas palavras sobre [slots](https://docs.python.org/reference/datamodel.html#slots). Os slots podem ser usados para tornar as aulas mais rápidas e usar menos memória. As classes de dados não têm sintaxe explícita para trabalhar com slots, mas a maneira normal de criar slots também funciona para classes de dados. (Eles realmente são apenas aulas regulares!)

```python
from dataclasses import dataclass

@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float

@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float
```

### Essencialmente, os slots são definidos usando `.__slots__` para listar as variáveis em uma classe. Variáveis ou atributos não presentes em `.__slots__` não podem ser definidos. Além disso, uma classe de slots pode não ter valores padrão.

### O benefício de adicionar tais restrições é que certas otimizações podem ser feitas. Por exemplo, classes de slots ocupam menos memória, como pode ser medido usando [Pympler](https://pythonhosted.org/Pympler/):

```Python Console
>>> from pympler import asizeof
>>> simple = SimplePosition('London', -0.1, 51.5)
>>> slot = SlotPosition('Madrid', -3.7, 40.4)
>>> asizeof.asizesof(simple, slot)
(440, 248)
```

### Da mesma forma, as classes de slots geralmente são mais rápidas para trabalhar. O exemplo a seguir mede a velocidade de acesso ao atributo em uma classe de dados de slots e uma classe de dados regular usando [timeit](https://docs.python.org/library/timeit.html) da biblioteca padrão.

```Python Console
>>> from timeit import timeit
>>> timeit('slot.name', setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals())
0.05882283499886398
>>> timeit('simple.name', setup="simple=SimplePosition('Oslo', 10.8, 59.9)", globals=globals())
0.09207444800267695
```

### Neste exemplo em particular, a classe de slot é cerca de 35% mais rápida.

## Conclusão e leitura adicional

### As classes de dados são um dos novos recursos do Python 3.7. Com classes de dados, você não precisa escrever código clichê para obter inicialização, representação e comparações adequadas para seus objetos.

### Você viu como definir suas próprias classes de dados, bem como:

```
° Como adicionar valores padrão aos campos em sua classe de dados
° Como personalizar a ordenação de objetos de classe de dados
° Como trabalhar com classes de dados imutáveis
° Como a herança funciona para classes de dados
```

### Se você quiser se aprofundar em todos os detalhes das classes de dados, dê uma olhada no [PEP 557](https://www.python.org/dev/peps/pep-0557/), bem como nas discussões no repositório [GitHub original](https://github.com/ericvsmith/dataclasses/issues?utf8=%E2%9C%93&q=).

### Além disso, vale a pena assistir à palestra de Raymond Hettinger em PyCon 2018 [Dataclasses: The code generator to end all code generators](https://www.youtube.com/watch?v=T-TwcmT6Rcw) vale muito a pena assistir.

### Se você ainda não tem o Python 3.7, há também um [backport de classes de dados para Python 3.6](https://github.com/ericvsmith/dataclasses). E agora, vá em frente e escreva menos código!
