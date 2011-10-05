#!/usr/bin/env python
# -*- coding=utf-8 -*-

ts21 = 'Thursday, October 21, 2010'
ts21 = '21 de out de 2010 {0} a {1}'
s21 = '''8:00am Credenciamento
9:00am A: Cerimônia de Abertura & Infra-Estrutura DINF C3SL UFPR
9:45am A: Como me tornei um empreendedor pythonista
9:45am B: Desenvolvimento Python com MeeGo
10:30am A: Por que Python?
10:30am B: TI em saúde: um vácuo de mercado e por que Pythonistas já saem na frente
11:15am A: Django Design Patterns
11:15am B: Trading Card Game com Realidade Aumentada
1:30pm Keynote: The Zen of Startups
3:00pm A: Metapython Reciclado
3:00pm B: Python e Segurança da Informação: Desenvolvendo Exploits em Python
3:45pm A: Desenvolvendo Web Services com App Engine
3:45pm B: Python Packaging: Passado, Presente e Futuro
4:30pm A: Python Ágil
4:30pm B: O Universo revelado com Python
5:15pm A: Extraindo dados públicos na marra com Python
5:15pm B: Python em Sistemas Recomendação: A Cobra é Inteligente!
6:00pm Palestras Relâmpago'''
ts22 = 'Friday, October 22, 2010'
ts22 = '22 de out de 2010 {0} a {1}'
s22 = '''9:00am A: Melhorando a performance de projetos Django
9:00am B: Python e as eleições nas mídias sociais: Como ela ajudou a decidir o Futuro do Brasil
9:45am A: CartolaFC 2010: Uma aplicação Python rápida e escalável
9:45am B: Lettuce, BDD fácil e divertido
10:30am A: Iniciando com Test Driven Development em Django
10:30am B: Desenvolvendo macros de OpenOffice.org em Python
11:15am A: Arduino: brincando de eletrônica com Python e hardware livre
11:15am B: Introdução ao Cálculo Numérico usando SciPy
1:30pm Keynote: Comunidad, anarquía y subversión
3:00pm A: Como Fazer Jogos com Python (ou Apresentando a PyGame)
3:00pm B: Potter vs Voldemort: Lições Ofidiglotas da Prática Pythônica
3:45pm A: Por que o futuro do Python só depende dos Pythonistas
3:45pm B: Python + Asterisk: desenvolvendo aplicações de telefonia com StarPy
4:30pm A: Como não programar em Python ou Python Tricks que você ainda não conhecia
4:30pm B: MongoDB e Python: Rompendo a barreira do ORM
5:15pm A: Brasil.Gov: Python Powered EGov
5:15pm B: Django e CMS customizáveis
6:00pm Palestras Relâmpago'''
ts23 = 'Saturday, October 23, 2010'
ts23 = '23 de out de 2010 {0} a {1}'
s23 = '''9:00am A: Criando um ambiente de desenvolvimento Pythônico
9:00am B: Implementação do algoritmo de custo mínimo de Dijkstra em Python para calcular a distância mínima entre cidades
9:45am A: O Zen da programação Python
9:45am B: Orbited: monitoramento em tempo real
10:30am A: Pés na Terra, Cabeça nas Nuvens
10:30am B: Python 3: o que mudou e por que adotar?
11:15am A: Inteligência Computacional com Python
11:15am B: Apontador Web Services (para programdores Python, claro!)
1:30pm Uma Visão do Mundo Ruby
3:00pm A: Escalando aplicações Django
3:00pm B: Desenvolvendo soluções comerciais utilizando Open Source
3:45pm A: Análise de redes sociais usando NetworkX e Google App Engine
3:45pm B: p14p - Python-on-a-Chip: Embarque este você também
4:30pm A: Melhores práticas para o desenvolvimento com Plone 4
4:30pm B: Como utilizar a DAL (Camada de abstração de acesso a dados) do web2py em outros projetos ou frameworks Python
5:15pm A: Visão Computacional aplicada à Robótica com Python e OpenCV
5:15pm B: Code Review simplificado através do ReviewBoard
6:00pm Palestras Relâmpago'''

palestras_from_csv = [('A: Cerim\xc3\xb4nia de Abertura & Infra-Estrutura DINF C3SL UFPR',
  'Luis Carlos Erpen de Bona',
  '21 de out de 2010 09:00 a 09:45'),
 ('A: Como me tornei um empreendedor pythonista',
  'Osvaldo Santana Neto',
  '21 de out de 2010 09:45 a 10:30'),
 ('B: Desenvolvimento Python com MeeGo',
  'Lauro Moura Maranh\xc3\xa3o Neto',
  '21 de out de 2010 09:45 a 10:30'),
 ('A: Por que Python?',
  'Marco Andr\xc3\xa9 Lopes Mendes',
  '21 de out de 2010 10:30 a 11:15'),
 ('B: TI em sa\xc3\xbade: um v\xc3\xa1cuo de mercado e por que Pythonistas j\xc3\xa1 saem na frente',
  'Luciana Tricai Cavalini',
  '21 de out de 2010 10:30 a 11:15'),
 ('A: Django Design Patterns',
  'Andrews Patrick Rocha Medina e Enrico Batista da Luz',
  '21 de out de 2010 11:15 a 12:00'),
 ('B: Trading Card Game com Realidade Aumentada',
  'Thiago Malheiros Porcino',
  '21 de out de 2010 11:15 a 12:00'),
 ('A: The Zen of Startups', 'Leah Culver', '21 de out de 2010 13:30 a 15:30'),
 ('A: Metapython Reciclado',
  'Jo\xc3\xa3o Sebasti\xc3\xa3o de Oliveira Bueno',
  '21 de out de 2010 15:30 a 15:45'),
 ('B: Python e Seguran\xc3\xa7a da Informa\xc3\xa7\xc3\xa3o: Desenvolvendo Exploits em Python',
  'Oscar Isauro Bacelar Marques',
  '21 de out de 2010 15:30 a 15:45'),
 ('A: Desenvolvendo Web Services com App Engine',
  'Rodolpho Eckhardt',
  '21 de out de 2010 15:45 a 16:30'),
 ('B: Python Packaging: Passado, Presente e Futuro',
  'Hugo Lopes Tavares',
  '21 de out de 2010 15:45 a 16:30'),
 ('A: Python \xc3\x81gil',
  'Ramiro Batista da Luz',
  '21 de out de 2010 16:30 a 17:15'),
 ('B: O Universo revelado com Python',
  'Eduardo dos Santos Pereira',
  '21 de out de 2010 16:30 a 17:15'),
 ('A: Extraindo dados p\xc3\xbablicos na marra com Python',
  'Pedro Valente',
  '21 de out de 2010 17:15 a 18:00'),
 ('B: Python em Sistemas Recomenda\xc3\xa7\xc3\xa3o: A Cobra \xc3\xa9 Inteligente!',
  'Marcel Pinheiro Caraciolo',
  '21 de out de 2010 17:15 a 18:00'),
 ('A: Palestras Rel\xc3\xa2mpago', '', '21 de out de 2010 18:00 a 19:00'),
 ('A: Melhorando a performance de projetos Django',
  'Marcos Daniel Petry',
  '22 de out de 2010 09:00 a 09:45'),
 ('B: Python e as elei\xc3\xa7\xc3\xb5es nas m\xc3\xaddias sociais: Como ela ajudou a decidir o Futuro do Brasil',
  'Rafael Jacinto Car\xc3\xadcio da Fons\xc3\xaaca',
  '22 de out de 2010 09:00 a 09:45'),
 ('A: CartolaFC 2010: Uma aplica\xc3\xa7\xc3\xa3o Python r\xc3\xa1pida e escal\xc3\xa1vel',
  'Marcel Nicolay Santos',
  '22 de out de 2010 09:45 a 10:30'),
 ('B: Lettuce, BDD f\xc3\xa1cil e divertido',
  'Gabriel Falc\xc3\xa3o Gon\xc3\xa7alves de Moura',
  '22 de out de 2010 09:45 a 10:30'),
 ('A: Iniciando com Test Driven Development em Django',
  'Adriano Petrich',
  '22 de out de 2010 10:30 a 11:15'),
 ('B: Desenvolvendo macros de OpenOffice.org em Python',
  'Luis Henrique Fagundes',
  '22 de out de 2010 10:30 a 11:15'),
 ('A: Arduino: brincando de eletr\xc3\xb4nica com Python e hardware livre',
  '\xc3\x81lvaro Fernandes de Abreu Justen',
  '22 de out de 2010 11:15 a 12:00'),
 ('B: Introdu\xc3\xa7\xc3\xa3o ao C\xc3\xa1lculo Num\xc3\xa9rico usando SciPy',
  'Egon Hilgenstieler',
  '22 de out de 2010 11:15 a 12:00'),
 ('A: Comunidad, anarqu\xc3\xada y subversi\xc3\xb3n',
  'Facundo Batista',
  '22 de out de 2010 13:30 a 15:30'),
 ('A: Como Fazer Jogos com Python (ou Apresentando a PyGame)',
  'Diego Moreira Guimar\xc3\xa3es e Bernardo Fontes',
  '22 de out de 2010 15:30 a 15:45'),
 ('B: Potter vs Voldemort: Li\xc3\xa7\xc3\xb5es Ofidiglotas da Pr\xc3\xa1tica Pyth\xc3\xb4nica',
  'Rodrigo Dias Arruda Senra',
  '22 de out de 2010 15:30 a 15:45'),
 ('A: Por que o futuro do Python s\xc3\xb3 depende dos Pythonistas',
  'Henrique Bastos',
  '22 de out de 2010 15:45 a 16:30'),
 ('B: Python + Asterisk: desenvolvendo aplica\xc3\xa7\xc3\xb5es de telefonia com StarPy',
  'Rud\xc3\xa1 Porto Filgueiras',
  '22 de out de 2010 15:45 a 16:30'),
 ('A: Como n\xc3\xa3o programar em Python ou Python Tricks que voc\xc3\xaa ainda n\xc3\xa3o conhecia',
  'Henrique Pereira',
  '22 de out de 2010 16:30 a 17:15'),
 ('B: MongoDB e Python: Rompendo a barreira do ORM',
  'S\xc3\xa9rgio Almeida Dias',
  '22 de out de 2010 16:30 a 17:15'),
 ('A: Brasil.Gov: Python Powered EGov',
  'Danilo Freitas - \xc3\x89rico Andrei - Pedro Werneck',
  '22 de out de 2010 17:15 a 18:00'),
 ('B: Django e CMS customiz\xc3\xa1veis',
  'Anderson Santos Silva',
  '22 de out de 2010 17:15 a 18:00'),
 ('A: Palestras Rel\xc3\xa2mpago', '', '22 de out de 2010 18:00 a 19:00'),
 ('A: Criando um ambiente de desenvolvimento Pyth\xc3\xb4nico',
  'Gustavo Guimar\xc3\xa3es Rezende',
  '23 de out de 2010 09:00 a 09:45'),
 ('B: Implementa\xc3\xa7\xc3\xa3o do algoritmo de custo m\xc3\xadnimo de Dijkstra em Python para calcular a dist\xc3\xa2ncia m\xc3\xadnima entre cidades',
  'Luiz Augusto de Mac\xc3\xaado Morais',
  '23 de out de 2010 09:00 a 09:45'),
 ('A: O Zen da programa\xc3\xa7\xc3\xa3o Python',
  'Pedro Werneck',
  '23 de out de 2010 09:45 a 10:30'),
 ('B: Orbited: monitoramento em tempo real',
  'Bruno Gon\xc3\xa7alves Tikami',
  '23 de out de 2010 09:45 a 10:30'),
 ('A: P\xc3\xa9s na Terra, Cabe\xc3\xa7a nas Nuvens',
  'Fl\xc3\xa1vio Code\xc3\xa7o Coelho',
  '23 de out de 2010 10:30 a 11:15'),
 ('B: Python 3: o que mudou e por que adotar?',
  'Rafael Carlos Valverde',
  '23 de out de 2010 10:30 a 11:15'),
 ('A: Intelig\xc3\xaancia Computacional com Python',
  'Jos\xc3\xa9 Alexandre Nalon',
  '23 de out de 2010 11:15 a 12:00'),
 ('B: Apontador Web Services (para programdores Python, claro!)',
  'Carlos Duarte do Nascimento (Chester)',
  '23 de out de 2010 11:15 a 12:00'),
 ('A: Uma Vis\xc3\xa3o do Mundo Ruby',
  'F\xc3\xa1bio Akita',
  '23 de out de 2010 13:30 a 15:30'),
 ('A: Escalando aplica\xc3\xa7\xc3\xb5es Django',
  'Andrews Patrick Rocha Medina',
  '23 de out de 2010 15:30 a 15:45'),
 ('B: Desenvolvendo solu\xc3\xa7\xc3\xb5es comerciais utilizando Open Source',
  'Fabr\xc3\xadcio Nicoletti e Ricardo Lenzi',
  '23 de out de 2010 15:30 a 15:45'),
 ('A: An\xc3\xa1lise de redes sociais usando NetworkX e Google App Engine',
  '\xc3\x89rico Andrei',
  '23 de out de 2010 15:45 a 16:30'),
 ('B: p14p - Python-on-a-Chip: Embarque este voc\xc3\xaa tamb\xc3\xa9m',
  'Alberto Fabiano',
  '23 de out de 2010 15:45 a 16:30'),
 ('A: Melhores pr\xc3\xa1ticas para o desenvolvimento com Plone 4',
  'Dorneles Trem\xc3\xa9a',
  '23 de out de 2010 16:30 a 17:15'),
 ('B: Como utilizar a DAL (Camada de abstra\xc3\xa7\xc3\xa3o de acesso a dados) do web2py em outros projetos ou frameworks Python',
  'Bruno Cezar Rocha',
  '23 de out de 2010 16:30 a 17:15'),
 ('A: Vis\xc3\xa3o Computacional aplicada \xc3\xa0 Rob\xc3\xb3tica com Python e OpenCV',
  'Alex Tercete Matos',
  '23 de out de 2010 17:15 a 18:00'),
 ('B: Code Review simplificado atrav\xc3\xa9s do ReviewBoard',
  'Eduardo Felipe Castegnaro',
  '23 de out de 2010 17:15 a 18:00'),
 ('A: Palestras Rel\xc3\xa2mpago', '', '23 de out de 2010 18:00 a 19:00')]

faltantes = '''9:00am A: Cerimônia de Abertura & Infra-Estrutura DINF C3SL UFPR
9:45am A: Como me tornei um empreendedor pythonista
9:45am B: Desenvolvimento Python com MeeGo
11:15am A: Django Design Patterns
3:45pm A: Desenvolvendo Web Services com App Engine
4:30pm B: O Universo revelado com Python
5:15pm A: Extraindo dados públicos na marra com Python
6:00pm Palestras Relâmpago
9:45am B: Lettuce, BDD fácil e divertido
10:30am A: Iniciando com Test Driven Development em Django
10:30am B: Desenvolvendo macros de OpenOffice.org em Python
11:15am A: Arduino: brincando de eletrônica com Python e hardware livre
11:15am B: Introdução ao Cálculo Numérico usando SciPy
3:00pm A: Como Fazer Jogos com Python (ou Apresentando a PyGame)
3:45pm A: Por que o futuro do Python só depende dos Pythonistas
4:30pm B: MongoDB e Python: Rompendo a barreira do ORM
5:15pm A: Brasil.Gov: Python Powered EGov
6:00pm Palestras Relâmpago
9:00am A: Criando um ambiente de desenvolvimento Pythônico
9:00am B: Implementação do algoritmo de custo mínimo de Dijkstra em Python para
calcular a distância mínima entre cidades
9:45am A: O Zen da programação Python
9:45am B: Orbited: monitoramento em tempo real
11:15am B: Apontador Web Services (para programdores Python, claro!)
3:00pm B: Desenvolvendo soluções comerciais utilizando Open Source
3:45pm A: Análise de redes sociais usando NetworkX e Google App Engine
4:30pm A: Melhores práticas para o desenvolvimento com Plone 4
5:15pm B: Code Review simplificado através do ReviewBoard
6:00pm Palestras Relâmpago
'''

palestrantes = {'An\xc3\xa1lise de redes sociais usando NetworkX e GoogleAppEngine': '\xc3\x89rico Andrei',
 'Aplica\xc3\xa7\xc3\xb5es comerciais em Python': 'Ricardo Francis Reghin',
 'Apontador Web Services (para programdores Python, claro!)': 'Carlos Duarte do Nascimento (Chester)',
 'Aprendendo a programar direito com Coding Dojo': '\xc3\x81lvaro Fernandes de Abreu Justen',
 'Arduino: brincando de eletr\xc3\xb4nica com Python e hardware livre': '\xc3\x81lvaro Fernandes de Abreu Justen',
 'Brasil.Gov: Python Powered EGov': 'Danilo Freitas - \xc3\x89rico Andrei - Pedro Werneck',
 'CartolaFC 2010: Uma aplica\xc3\xa7\xc3\xa3o Python r\xc3\xa1pida e escal\xc3\xa1vel': 'Marcel Nicolay Santos',
 'Code Review simplificado atrav\xc3\xa9s do ReviewBoard': 'Eduardo Felipe Castegnaro',
 'Como Fazer Jogos com Python (ou Apresentando a PyGame)': 'Diego Moreira Guimar\xc3\xa3es e Bernardo Fontes',
 'Como me tornei um empreendedor pythonista': 'Osvaldo Santana Neto',
 'Como n\xc3\xa3o programar em Python ou Python Tricks que voc\xc3\xaa ainda n\xc3\xa3o conhecia': 'Henrique Pereira',
 'Como utilizar a DAL (Camada de abstra\xc3\xa7\xc3\xa3o de acesso a dados) do web2py em outros projetos ou frameworks Python': 'Bruno Cezar Rocha',
 'Criando um ambiente de desenvolvimento Pyth\xc3\xb4nico': 'Gustavo Guimar\xc3\xa3es Rezende',
 'Desenvolvendo Web Services com App Engine': 'Rodolpho Eckhardt',
 'Desenvolvendo macros de OpenOffice.org em Python': 'Luis Henrique Fagundes',
 'Desenvolvendo solu\xc3\xa7\xc3\xb5es comerciais utilizando Open Source': 'Fabr\xc3\xadcio Nicoletti e Ricardo Lenzi',
 'Desenvolvimento Python com MeeGo': 'Lauro Moura Maranh\xc3\xa3o Neto',
 'Dinf & C3SL infra estrutura': 'Luis Carlos Erpen de Bona',
 'Django - The Good Parts': 'Henrique Pereira',
 'Django Design Patterns (Boas pr\xc3\xa1ticas no desenvolvimento com Django)': 'Andrews Patrick Rocha Medina e Enrico Batista da Luz',
 'Django e CMS customiz\xc3\xa1veis': 'Anderson Santos Silva',
 'Escalando Aplica\xc3\xa7oes Django': 'Andrews Patrick Rocha Medina',
 'Extraindo dados p\xc3\xbablicos na marra com Python': 'Pedro Valente',
 'Implementa\xc3\xa7\xc3\xa3o do algoritmo de custo m\xc3\xadnimo de Dijkstra em Python para calcular a dist\xc3\xa2ncia m\xc3\xadnima entre cidades': 'Luiz Augusto de Mac\xc3\xaado Morais',
 'Iniciando com Test Driven Development em Django': 'Adriano Petrich',
 'Integra\xc3\xa7\xc3\xa3o entre Blender e Flash atrav\xc3\xa9s de scripts Python': 'Jos\xc3\xa9 Evaristo Jorge',
 'Intelig\xc3\xaancia Computacional com Python': 'Jos\xc3\xa9 Alexandre Nalon',
 'Introdu\xc3\xa7\xc3\xa3o a programa\xc3\xa7\xc3\xa3o de jogos com Pygame': 'Jo\xc3\xa3o Sebasti\xc3\xa3o de Oliveira Bueno',
 'Introdu\xc3\xa7\xc3\xa3o ao C\xc3\xa1lculo Num\xc3\xa9rico usando SciPy': 'Egon Hilgenstieler',
 'Introdu\xc3\xa7\xc3\xa3o ao Google App Engine': 'Rodolpho Eckhardt',
 'Lettuce, BDD f\xc3\xa1cil e divertido': 'Gabriel Falc\xc3\xa3o Gon\xc3\xa7alves de Moura',
 'Melhorando a performance de projetos Django': 'Marcos Daniel Petry',
 'Melhores pr\xc3\xa1ticas para o desenvolvimento com Plone 4': 'Dorneles Trem\xc3\xa9a',
 'Metapython Reciclado': 'Jo\xc3\xa3o Sebasti\xc3\xa3o de Oliveira Bueno',
 'MongoDB e Python - rompendo a barreira do ORM': 'S\xc3\xa9rgio Almeida Dias',
 'O Universo revelado com Python': 'Eduardo dos Santos Pereira',
 'O Zen da programa\xc3\xa7\xc3\xa3o Python': 'Pedro Werneck',
 'Orbited: monitoramento em tempo real ': 'Bruno Gon\xc3\xa7alves Tikami',
 'Por que Python? 10 raz\xc3\xb5es para aprender Python': 'Marco Andr\xc3\xa9 Lopes Mendes',
 'Por que o futuro do Python s\xc3\xb3 depende dos Pythonistas': 'Henrique Bastos',
 'Potter vs Voldemort: Li\xc3\xa7\xc3\xb5es Ofidiglotas da Pr\xc3\xa1tica Pyth\xc3\xb4nica': 'Rodrigo Dias Arruda Senra',
 'PyCUDA e PyOpenCL: Computa\xc3\xa7\xc3\xa3o Cient\xc3\xadfica de Alta Performance nas GPUs': 'Jonh Edson Ribeiro de Carvalho',
 'Python + Asterisk: desenvolvendo aplica\xc3\xa7\xc3\xb5es de telefonia com StarPy': 'Rud\xc3\xa1 Porto Filgueiras',
 'Python 3: o que mudou e por que adotar?': 'Rafael Carlos Valverde',
 'Python Packaging: Passado, Presente e Futuro': 'Hugo Lopes Tavares',
 'Python e Seguran\xc3\xa7a da Informa\xc3\xa7\xc3\xa3o: Desenvolvendo Exploits em Python': 'Oscar Isauro Bacelar Marques',
 'Python e as elei\xc3\xa7\xc3\xb5es nas m\xc3\xaddias sociais - Como ela ajudou a decidir o Futuro do Brasil': 'Rafael Jacinto Car\xc3\xadcio da Fons\xc3\xaaca',
 'Python em Sistemas Recomenda\xc3\xa7\xc3\xa3o:  A Cobra \xc3\xa9 Inteligente!': 'Marcel Pinheiro Caraciolo',
 'Python \xc3\x81gil': 'Ramiro Batista da Luz',
 'P\xc3\xa9s na Terra, Cabe\xc3\xa7a nas Nuvens': 'Fl\xc3\xa1vio Code\xc3\xa7o Coelho',
 'TI em sa\xc3\xbade: um v\xc3\xa1cuo de mercado e por que Pythonistas j\xc3\xa1 saem na frente': 'Luciana Tricai Cavalini',
 'Trading Card Game com Realidade Aumentada': 'Thiago Malheiros Porcino',
 'Vis\xc3\xa3o Computacional aplicada \xc3\xa0 Rob\xc3\xb3tica com Python e OpenCV': 'Alex Tercete Matos',
 'p14p - Python-on-a-Chip - Embarque este voc\xc3\xaa tamb\xc3\xa9m': 'Alberto Fabiano',
 'web2py: desenvolvimento web com agilidade': '\xc3\x81lvaro Fernandes de Abreu Justen e Bruno Rocha'}

#print(faltantes)
#print(s21)
#print(s22)
#print(s23)
for i in palestrantes.keys():
    print(i)
