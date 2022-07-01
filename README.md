<h1 align="center">
  :computer: Atividade final - Engenharia de Software II
</h1>
<br>

## :clipboard: Descrição

Respositório para entrega do trabalho final.

OBJETIVO DO TRABALHO
- Estudar o padrão e preparar material explicativo sobre Design Patterns (Padrões de Projeto) que surgiram com a motivação de ajudar a solucionar problemas que ocorrem frequentemente, e se usado com bom senso, podem se tornar ferramentas poderosas para qualquer desenvolvedor de software.


Factory Method:
- Factory Method é um padrão de design criacional que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objeto que será criado.


Sobre o Factory Method
- É um padrão de projeto de criação (lida com a criação de objetos).
- Oculta a lógica de instanciação do código cliente. O método fábrica será responsável por instanciar as classes desejadas.
- É obtido através de herança. O método fábrica pode ser criado ou sobrescrito por subclasses
- Dá flexibilidade ao código cliente permitindo a criação de novas factories sem a necessidade de alterar o código já escrito (OCP)
- Pode usar parâmetros para determinar o tipo dos objetos a serem criados ou os parâmetros a serem enviados aos objetos sendo criados.


CONSEQUÊNCIAS


PONTOS POSITIVOS 
- Você evita um acoplamento rígido entre o criador e os produtos de concreto.
- Princípio de responsabilidade única (single responsability) . Você pode mover o código de criação do produto para um local do programa, facilitando o suporte ao código.
- Princípio Open/Closed . Você pode introduzir novos tipos de produtos no programa sem quebrar o código do cliente existente.


PONTOS NEGATIVOS
- O código pode se tornar mais complicado, pois você precisa introduzir muitas subclasses novas para implementar o padrão. O melhor cenário é quando você está introduzindo o padrão em uma hierarquia existente de classes de criadores.

LINK PARA REFERÊNCIA
- https://refactoring.guru/pt-br/design-patterns/singleton

LINK PARA APRESENTAÇÃO
- https://drive.google.com/drive/folders/143dzcyd67g6A8FihUvl-PUEXtOTe-RgY?usp=sharing

## 💻 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:
- :snake: **Python**


Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

## 🤝 Contribuídores

<a href="https://github.com/AmaroWes"><img src="https://github.com/AmaroWes.png" width="45" height="45"></a> &nbsp;
<a href="https://github.com/R3N4NR"><img src="https://github.com/R3N4NR.png" width="45" height="45"></a> &nbsp;
<a href="https://github.com/GuiRohdes"><img src="https://github.com/GuiRohdes.png" width="45" height="45"></a> &nbsp;
<a href="https://github.com/JonasCouto"><img src="https://github.com/JonasCouto.png" width="45" height="45"></a> &nbsp;
