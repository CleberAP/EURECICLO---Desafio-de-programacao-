# EURECICLO Desafio de programação
<b>Desafio de programação elaborado pela EURECICLO</b>

<h1>Desafio Inicial</h1>
<h3>Desafio: README.md</h3>
<p>Dado um conjunto de garrafas d'água, com volumes de água diferentes entre si, e um galão de água. Crie um algoritmo, na linguagem que achar melhor, para escolher as garrafas a serem utilizadas para encher o galão, de acordo:</p>
<ul>
        <li><b>i.</b> O galão deve ser completamente preenchido com o volume das garrafas;</li>
        <li><b>ii.</b> Procure esvaziar totalmente as garrafas escolhidas;</li>
        <li><b>iii.</b> Quando não for possível esvaziar todas garrafas escolhidas, deixe a menor sobra possível;</li>
        <li><b>iv.</b> utilize o menor número de garrafas possível;</li>
</ul>
<p><b>Resposta:</b></p>
<p>Escrevi um algoritmo com base em algoritmo de enumeração Lexcográfico.</p>
<p>Escrevi 2 arquivos para tratar a inserção de forma diferentes:</b>
<ul>
 <li><b>Algoritmo_Lista:</b> recebe valores e organiza em uma lista.</li>
 <li><b>Algoritmo_Dict:</b> recebe valores e trata as informações em estrutura de dicionário. É útil caso queira identificar o recipiente (garrafa), como por exemplo, com código de registro. Para demonstrar o uso também desenvolvi um Protótipo em linguagem Python v.3.7 com a biblioteca Tkinter.</li>
</ul>
<h5>Sobre o Protótipo</h5>
<p>A aplicação está disponível para rodar através do arquivo "aplicativo.py" (implementei de forma simples num único arquivo, mas pode ser melhorado) e do algoritmo do tipo dict (conforme arquivo "Algorithm_Dict.py") que contem as instruções para tratar os 2 tipos de análises disponibilizados.</p>
<p>Este protótipo foi criado com orientação a objetos, então cada item listado é um objeto (instância) da classe container, arquivo container.py, também disponibilizado.</p>
<ul>
        <li>No menu FILE tem opções para exportar ou importar arquivos *.csv e inserir nas respectivas listas de recipiente principal e de despejo.</li>
        <li>2 frames para registro e exibição:
                <ol>
                        <li>Para registrar Galões, ou outro tipo de recipiente principal onde se deseja despejar e armazenar conteúdo.</li>
                        <li>Para registrar os recipientes que possuem o conteúdo a ser despejado no recipiente principal.</li>
                </ol>
        </li>
        <li>Cada frame tem um botão para adicionar registros nas respectivas listas.</li>
        <li>No canto direito da área de exibição tem 2 botões para dois tipos de análises. :
                <ol>
                        <li><b>Analisar Possibilidades:</b> utiliza toda lista de Recipientes de Despejo e utiliza o algoritmo criado. No final exibe a resposta, melhor opção. <i>Esta é a opção que atende ao desafio proposto pela EURECICLO.</i></li>
                        <li><b>Analisar Selecionados:</b> analisa Recipientes de Despejo selecionados.</li>
                </ol>
                <p>*Para utilizá-los, basta selecionar um Recipiente Principal e os Recipientes de Despejo que se deseja analisar.</p>
        </li>
        <li>2 botões de limpeza para as respectivas listas.</li>
</ul>
<p>Como eu mencionei é um protótipo, então faltam muitos tratamentos para uma aplicação completa.</p>
<p>Também desponibilizei 2 arquivos criados com o protótipo, contendo alguns registros fictícios que podem ser utilizados, como teste.</p>
<p>Experimente importá-los!</p>
<br>
<p>Ou crie outros!</p>
<br>
<p>Espero que o aplicativo (<b>Protótipo</b>) seja útil no aprendizado ou aplicação em algum projeto.
<br>
<hr>
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

