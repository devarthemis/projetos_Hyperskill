## INSTRUÇÃO !

Em geral, ela pega vários parâmetros como principal e juros de um empréstimo,
calcula os valores que o usuário quer saber (por exemplo, pagamento mensal ou
pagamento a maior) e os exibe para o usuário.

O principal é o valor original de dinheiro que você toma emprestado.
O juro é uma cobrança pelo empréstimo desse dinheiro, geralmente calculado
como uma porcentagem do valor principal.

Objetivos
Vamos começar imitando este comportamento:

Peça ao usuário para inserir o principal do empréstimo.

Peça ao usuário para inserir seu pagamento mensal.

Calcule e exiba o número de meses necessários para pagar o empréstimo dividindo o principal
do empréstimo pelo pagamento mensal.

## INSTRUÇÃO 2

O usuário pode saber o valor dos pagamentos mensais e se perguntar quantos meses levará para
pagar o empréstimo. Vamos adicionar essa funcionalidade além do cálculo do pagamento mensal.

Nesta etapa, precisamos pedir para inserir o valor principal do empréstimo como antes.
Então, o usuário deve indicar o que precisa ser calculado (o valor do pagamento mensal
ou o número de meses) e inserir o parâmetro necessário. Depois disso, a calculadora de
empréstimos deve gerar o valor que o usuário deseja saber.

- Formula de pagamento = principal/meses

Você tem que arredondar esse valor para cima e torná-lo 112. Mas por que arredondamos para cima
em vez de arredondar para baixo? Lembre-se de que nenhum pagamento pode ser maior do que o
pagamento mensal fixo. Se o valor do seu pagamento mensal for 111, isso tornaria o último pagamento 112,
o que não é aceitável. Se você fizer um pagamento mensal de 112, o último pagamento será 104, o que é bom.
Você pode calcular o último pagamento da seguinte forma:
- Formula último pagamento = principal - (periodo - 1) * pagamento

Objetivos
O comportamento do seu programa deve ser semelhante a este:

Peça ao usuário para inserir o principal do empréstimo e escolher qual dos dois parâmetros ele deseja calcular:
o número de pagamentos mensais ou o valor do pagamento mensal.

Para realizar mais cálculos, você também terá que solicitar o valor ausente necessário.

Por fim, exiba os resultados para o usuário.

## INSTRUÇÃO 3

Vamos calcular todos os parâmetros do empréstimo. Existem pelo menos dois tipos de empréstimo: aqueles com pagamento
de anuidade e aqueles com pagamento diferenciado. Nesta etapa, você vai calcular apenas o primeiro. O tipo de pagamento
de anuidade consiste em pagar uma quantia fixa de dinheiro em intervalos especificados, por exemplo, a cada mês ou a cada
ano. O valor do pagamento de anuidade é precisamente essa quantia fixa de dinheiro que você precisa pagar em intervalos regulares.

- Pagamento anuidade mensal = a = principal * ((i*(1+i)^n)/(1+i)^n - 1)

Onde:

a = pagamento de anuidade;

Principal = principal do empréstimo;

i = taxa de juros nominal (mensal). Normalmente, é 1/12 da taxa de juros anual e é um valor flutuante, não uma porcentagem.
Por exemplo, se sua taxa de juros anual = 12%, então i = 0,01;

n = número de pagamentos. Geralmente é o número de meses em que os reembolsos serão feitos.

Até agora, neste estágio, você está interessado em quatro valores: o número de pagamentos mensais necessários para pagar o empréstimo,
o valor do pagamento mensal, o principal do empréstimo e os juros do empréstimo. Cada um desses valores pode ser calculado se outros forem conhecidos:

- Principal = a/((i*(1+i)^n)/(1+i)^n - 1)
- n = log1+i(a/a-i*principal)

## INSTRUÇÃO 4 - Adicionando pagamento diferenciado

Faremos isso para o tipo de pagamento em que o principal do empréstimo é reduzido em um valor constante a cada mês. O restante do 
pagamento mensal vai para o pagamento de juros e é gradualmente reduzido ao longo do prazo do empréstimo. Isso significa que o pagamento 
é diferente a cada mês. Vamos dar uma olhada na fórmula:

Dm = P/n + i * (P - (P*(m-1))/n)

Dm -> Pagamento diferenciado;
m -> Mês de pagamento atual

Demais parâmetros seguem como a instrução anterior.
Crie um novo argumento --type, "diff" (diferenciado) e "annuity", deve ser sempre fornecido nas execuções
Caso não seja informado apresente a mensagem "Incorrect parameters"