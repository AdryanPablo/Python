# sixtaxe = \033[style;text;backgroundm

cores = {
    'branco': '\033[0;30m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'magenta': '\033[0;35m',
    'ciano': '\033[0;36m',
    'cinza': '\033[0;37m',
    'brancoNegrito': '\033[1;30m',
    'vermelhoNegrito': '\033[1;31m',
    'verdeNegrito': '\033[1;32m',
    'amareloNegrito': '\033[1;33m',
    'azulNegrito': '\033[1;34m',
    'magentaNegrito': '\033[1;35m',
    'cianoNegrito': '\033[1;36m',
    'cinzaNegrito': '\033[1;37m',
    'limpar': '\033[m',
}

print(f'{cores["cianoNegrito"]}Olá, mundo!')
print(f'{cores["ciano"]}Hello, world!')
