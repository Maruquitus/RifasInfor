# Rifas Infor
Projeto que eu fiz para automatizar o processo de prestação de contas de uma rifa virtual da minha sala.
A prestação é feita por meio de um formulário do Google Forms, conectado com uma interface web no pythonanywhere.

## Códigos
### gerador.py
Responsável por gerar as cartelas dos alunos contidos em pessoas.txt.
<img src="https://github.com/Maruquitus/RifasInfor/assets/58173530/8d4ed756-b822-428c-9e18-17bf744e05ae" width=600>

### flask_app.py
Recebe os requests enviados pelo formulário e executa a função de atualização do planilha.py.

### planilha.py
Código que atualiza as informações da planilha de acordo com as novas respostas do formulário.

## Imagens
### Formulário
![image](https://github.com/Maruquitus/RifasInfor/assets/58173530/e8fd2fdf-3896-4da1-a2e6-93fffb6131b8)

### Código do AppsScript
![image](https://github.com/Maruquitus/RifasInfor/assets/58173530/2951a46e-6e17-4db8-9b52-87ffb1ce05cd)

### Respostas do formulário
Planilha que serve como entrada de dados do código.
![image](https://github.com/Maruquitus/RifasInfor/assets/58173530/47fdb68c-a7a8-49d1-b3a4-28a3efe0291c)

### Finanças
Visualização financeira da venda das rifas, atualizada automaticamente.
![image](https://github.com/Maruquitus/RifasInfor/assets/58173530/4e54adc8-c144-4010-b463-b081e10fb2a4)

### Cartelas
Visualização individual da venda por aluno, também atualizada de forma automática.
![image](https://github.com/Maruquitus/RifasInfor/assets/58173530/384a73f4-f7fd-434d-8852-8b2e7ce8f5ac)

