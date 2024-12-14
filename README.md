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

El tipo de agente empleado en este proyecto se trata de uno **reactivo basado en un modelo** (situado en el punto 2.4.3 del libro **"Artificial Intelligence a Modern Approach"**).El codigo implementado dispondremos 2 variables globales para que nuestro agente tome decisiones a raiz de lo almacenado en las mismas, estas son **result** (donde se guarda el resultado de la partida anterior) y **last_user_action** (donde se almacenará el ultimo movimiento realizado por el usuario en caso de que la partida dure mas de 1 ronda).Dispondremos de una clase llamada **GameComputerResult** de tipo Enum donde se reflejará de una manera numérica el resultado de la ultima partida realizada, para que nuestro agente elija su acción a raiz de ella. 