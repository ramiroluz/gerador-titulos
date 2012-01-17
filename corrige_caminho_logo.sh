#!/usr/bin/env bash
# Corrige o caminho para o logo, isto é necessário pois o editor de vídeos
# Openshot não lida bem com caminhos relativos.
# Para converter/exportar os arquivos para png é possível usar o inkscape
# ou o PHatch, ferramenta gráfica para tratar fotos em lote.

CAMINHO="\/home\/ramiro\/Dropbox\/PythonBrasil\/PythonBrasil6-2010\/arte\/logo.png"
CORRIGIDO="\/home\/ramiro\/python\/gerador-titulos\/logo.png"

PASTA="titulos_csv"
DESTINO="titulos_svg"

for arquivo in $PASTA/*svg ; do
    sed -e "s/$CAMINHO/$CORRIGIDO/g" $arquivo > $DESTINO/${arquivo##*/}
done

