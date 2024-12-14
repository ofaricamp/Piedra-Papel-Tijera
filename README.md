# Piedra-Papel-Tijera

## 1. Especión del entorno de tareas

Contorno de tarefas | Observable| Axentes | Determinista | Episódico | Estático | Discreto | Coñecido
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
 RPS | Parcialmente | Multiagente | No Deterministico | Secuencial | Estático | Discreto | Conocido |

## **Razonamiento de las carácteristicas del entorno**

#### **Parcialmente observable:**
Considero que es parcialmente observable puesto que nosotros no podemos ver en todo momento lo que ocurre, porque el agente no puede saber que va a sacar el rival hasta que ya lo muestra (que acaba la acción).

#### **Multiagente:**
Considero que se trata de multiagentes dado que en este caso se necesitan al menos 2 agentes como mínimo para poder realizar esta tarea.

#### **No Deterministico:**
Es no deterministico por que tenemos determinada o elegida previamente la acción que ejecutaremos basandonos en la anterior, puwato que aunque nosotros dispongamos de una estrategia, esta no resulta en una verdad absuta y nunca podemos determinar nuestras acciones al 100%.

#### **Secuencial:**
Como se definio previamente en el apartado de **no deterministico** se puede tratar de una entorno secuencial por que no tenemos una acción previamente definida para la siguiente que el agente vaya a realizar.

#### **Estático:**
Digo que es estático porque el estado del mundo no cambia en absoluto despues de que la decisión fue tomada.

#### **Discreto:**
Es discreto porque las posibilidades son limitas al igual que todas las posibles conbinaciones a realizar de las mismas.

#### **Conocido:**
Considero que es conocido puesto que todos los agentes conocen previamente las normas antes de jugar al juego y por tanto no se tiene ninguna información que no conozca ninguno de los agentes.

## 2. Identificacion del tipo de agente y su estructura

El tipo de agente empleado en este proyecto se trata de uno **reactivo basado en un modelo** (situado en el punto 2.4.3 del libro **"Artificial Intelligence a Modern Approach"**).El codigo implementado dispondremos 2 variables globales para que nuestro agente tome decisiones a raiz de lo almacenado en las mismas, estas son **`result`** (donde se guarda el resultado de la partida anterior) y **`last_user_action`** (donde se almacenará el ultimo movimiento realizado por el usuario en caso de que la partida dure mas de 1 ronda).Dispondremos de una clase llamada **`GameComputerResult`** de tipo Enum donde se reflejará de una manera numérica el resultado de la ultima partida realizada, para que nuestro agente elija su acción a raiz de ella. 

#### **Diagrama**
![imagen del esquema](/img/Esquema.png)

Siguiendo la logica de como ganar en RPS, como se explica en el sigueinte video es el razonamiento en el que esta basado mi agente: [Video de lógica del razonamiento](https://www.youtube.com/watch?v=TPz5LFmq5cw "Video de lógica del razonamiento")

[explicación de la lógica empleada en caso de no desear ver el video](#logica)

<div id= 'diagrama'>

### Explicación del diagrama del agente:

+ **Estado: Victoria o Derrota**: De acuerdo con el modelo planteado, será necesario ver cúal fue el desenlace de la partida, ya que sera importante para decidir cual sera la mejor decisión para la siguiente jugada.

+ **Ultima acción realizada por el oponente**: Siendo el elemento fundamental a la hora de dicidir cualquier jugada *(excepto en el caso del Empate)* puesto que es gracias a ella con la que podemos aspirar adelantarnos a la jugada del oponente.

+ **Procesamiento de decisión de movimiento**: Con los elementos anteriores sera en esta parte donde se pondra todo a peso y se hará la elección de la jugada por parte del agente para la siguiente ronda.

<div id= 'logica'>

### Lógica empleada para el agente:
La lógica a emplear es realmente sencilla es estadística pura, por ejemplo como primer movimiento el que tiene más probabilidades de ganar es sacar papel en vez de cualquier otra.

esto solo en el movimiento inicial y a continuación la explicación para cada uno de los 3 posibles casos (aunque los importantes a tener en cuenta son **Victoria y Derrota**):

+ **Victoria:** En caso de que nuestro agente resulte ganador la jugada más óptima es copiar la jugada que acaba de hacer el oponente, puesto que el pensamiento humano nos hace pensar que como usamos algo que ganó repetirlo nos daría más posibilidades de volver a ganr y lo que puede vencer al movimiento que ganaba al nuestro anterior es el que uso nuestro oponente. **Un ejemplo sería que nosotros sacamos PAPEL y el oponente saca PIEDRA, si se usa este razonamiento nuestro oponente sacara TIJERAS para ganarnos, pero si sacamos PIEDRA como el hizo en la ronda anterior es altamente probable que ganemos.**
  
+ **Derrota:** Cuando nuestro agente pierda la ronda seguirá el siguiente razonamiento de acuerdo con la estadistica y siendo con la decisión más óptima la de que el siguiente movimiento sea el que no salio en la ronda anterior. **Un ejemplo es que nuestro oponente saca PAPEL y nosotros sacamos ROCA como el razonamiento humano nos hace pensar como se explico en el razonamiento de *Victoria* por tanto nuestro mejor movimiento seria sacar TIJERAS puesto que así le ganariamos al PAPEL que seguramente vuelva a sacar nuestro rival.**
  
+ **Empate:** El caso del empate se resume en ***dejarlo en manos del destino*** puesto que no hay una estrategia fija o óptima para este caso, a si que nuestro agente debera sacar una de las posibles opciones de manera aleatoria.
  
[Explicación del diagrama del agente:](#diagrama)