# EURECICLO---Desafio-de-programacao-
<b>Desafio de programação elaborado pela EURECICLO</b>

<h1>Desafio Inicial</h1>


<h1>Desafio Arquitetura</h1>

<h3>Desafio - arquivo: arquitetura.md</h3>

<p>Descreva como você projetaria um sistema online que atenda as histórias:</p>
 <ul>
    <li>Quero poder enviar arquivos em formato .csv para o sistema, de modo que seja possível baixá-los depois;</li>
    <li>Quero poder ler o conteúdo dos meus arquivos .csv de maneira consolidada na plataforma;</li>
    <li>Quero poder ver a lista dos meus arquivos enviados e poder fazer busca através de filtros e parâmetros;</li>
    <li>Quero poder exportar os dados lidos dos meus arquivos em formato .csv;</li>
    <li>Quero poder enviar por email os dados lidos dos meus arquivos.</li>
</ul>
<p>De maneira simplificada, comente qual é a arquitetura ou design que você considera mais adequados para essa solução?</p>

<p><b>Resposta:</b></p>

<p>O primeiro requisito aduz ao interesse de armazenar arquivo *.csv, caracterizando o envio de diferentes tipos de arquivos CSV, sendo necessário um repositório de arquivos. Assim, é descartada a necessidade de criar entidades, no banco de dados, para cada tipo de arquivo.</p>
<p>Uma página com link(botão) para usuário fazer upload de arquivo através do método POST. Neste deve ser possível escolher arquivo que será submetido ao servidor (upload).</p>
<p>Para exibir a lista dos arquivos, é necessário uma página, ou espaço numa página, que exiba esta listagem, podendo ser visualizada em sua totalidade ou por vínculo de arquivos ao usuário conectado, ou seja, visualizar apenas arquivos submetidos por ele.</p>
<p>Esta visualização pode ocorrer em lista (tags: ul ou ol; dropdown; etc), ou tabelas (tag: table) que possibilita exibir mais informações sobre o arquivo em colunas.</p>
<p>Tanto listas quanto tabelas podem ser escritas no HTML fazendo uso de CSS e Javascript, sendo mais viável o uso de plugins/frameworks como o Bootstrap que possui classes que, entre outras, possibilitam a implementação de filtros de busca em dropdowns, tables, div, etc.</p>
<p>Para visualizar os dados dos arquivos, ao lado do nome, deve ser apresentado um link (botão) que carregue o arquivo e exiba seus dados em uma tabela (tag: table).</p>
<p>O carregamento ocorrerá por "leitura" do arquivo, sendo criado um conjunto de dados (dicionário) e exibido em tabela, através de algoritmo que identifique a estrutura de dados e crie as colunas e preencha os registros do mesmo modo que constam no arquivo original. Neste algoritmo pode ser implementada possibilidade de formatação de exibição dos dados como também alteração.</p>
<p>A exportação pode ocorrer com implementação de "botão" que carregue o arquivo e faça a exportação, sendo que este botão pode estar tanto na exibição dos nomes dos arquivos quanto na tela de exibição dos dados.</p>
<p>Basicamente, para exibição os dados é criado um conjunto de dados (objeto DataTable), no caso um dicionário, que poderá ser convertido/configurado para um arquivo CSV.</p>
<p>O envio por e-mail requer módulos do tipo Simple Mail Transfer Protocol (SMTP), assim é possível definir destino, assunto, texto e anexo que serão utilizados para envio.  Para isso é precio utilizar uma conta de e-mail já existente.</p>
<p>Linguagens de programação como Python possuem bibliotecas que auxiliam neste processo e possibilitam a criação de páginas WEB com uso de frameworks como Django ou Flask, ambos para Python.</p>
<p>No caso do Python pode ser utilizada a biblioteca csv, que possibilita leitura e escrita de arquivos, identificando cabeçalhos e uso de dicionários (DictReader e DictWrite), sendo necessário atentar à versão utilizada pois cada uma pode tratar de forma diferente com dicionários.</p>
<p>Um exemplo é a própria biblioteca csv que nas versões anteriores à 3.8 faziam a leitura dos dicionários com tipo OrderedDict e, a partir desta, o tipo é dict.</p>
<p>A utilização de framework, no caso do Django, visa facilitar a construção do site com os requisitos apresentados. Este framework possibilira manipular um upload de arquivo através de objetos do tipo request. O request.FILES é um dicionário que permite manipular os dados do arquivo, onde cada entrada que recebeu é um objeto UploaderFile. Esta classe foi elaborada para manipulaão de uploads e pode ser personalizada.</p>
<p>Para envio de e-mail, com ou sem anexos, o Django possui o módulo smtplib e "wrappers" para dinamizar o envio do e-mail de modo mais seguro e rápido.</p>

