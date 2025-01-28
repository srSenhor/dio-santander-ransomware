# Desafio da DIO: Criando um *ransomware* na prática

No presente projeto, criei um script em python que realiza a criptografia e descriptografia de um arquivo **.txt** usando a cifra AES.

## Modo de Usar

Para usar o script é bem simples: basta rodá-lo passando o caminho para o arquivo, o modo de uso e a chave.

```powershell
python.exe .\steal_a_file.py .\caminho\para\o\arquivo.txt modo_de_operacao chave
```

### Modo de operação:
- **0**: Encriptação
- **1**: Decriptação

### Chave
**DEVE CONTER 16 CARACTERES E DEVE SER A MESMA TANTO PARA ENCRIPTAR QUANTO DECRIPTAR**