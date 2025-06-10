Este projeto tem como objetivo praticar a analise de uma grande quantidade de dados

o dado escolhido foram os de imóveis rurais no Tocantins

No arquivo agrupamento_cidade.py é feito um simples agrupamento e classificação da quantidade de imóveis rurais por cidade, já no arquivo linear_regression.py tem como objetivo nos dizer como as variáveis explicam a área do imóvel (num_area) com base em mod_fiscal e no tipo de imóvel (ind_tipo).

Legenda: MSE (erro quadrático médio) R² (coeficiente de determinação)

mod_fiscal: X A cada 1 unidade a mais de módulo fiscal, a área do imóvel tende a aumentar em X hectares, mantendo o tipo constante.

ind_tipo_IRU: Y Se o imóvel for do tipo IRU, ele tende a ter Y hectares a mais ou a menos do que o tipo de referência (veja abaixo) — mantendo mod_fiscal constante.

ind_tipo_PCT: N Se o imóvel for do tipo PCT, ele tende a ter N hectares a mais ou a menos do que o tipo de referência — mantendo mod_fiscal constante.
