# _FragmentadoBot_
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/andrerogersdev/FragmentadoBot/blob/main/LICENSE) 

# Sobre o projeto

_FragmentadoBot_ é um robô automatizado projetado para atualizar a foto de perfil do usuário no WhatsApp a cada 15 segundos ou mais. Ele funciona utilizando tecnologias de automação como Selenium e PyAutoGUI.

![ImagemFragmentadoBot](https://github.com/andrerogersdev/FragmentadoBot/blob/main/assets/fragmentado_perfil.png)

# Tecnologias Utilizadas
## Back-End
- Python
- selenium
- pyautogui

# Como executar o projeto
## Back-End
Pré-requisitos: 
- Python 3
- ### Instale as bibliotecas
- selenium
- pyautogui
  
## Baixe o projeto
Abra no Editor de códigos

## Faça Alterações
### Altere
- Edge_profile = 'user-data-dir=C:\\Users\\Allya\\AppData\\Local\\MicrosoftEdge\\User\\WhatsPerfil'
  #### Em \\Allya\\ troque para o nome de usuário da sua máquina.

  ### por quê?
  - Essa funcionalidade permite que o selenium salve no seu computador na pasta \\WhatsPerfil os dados do navegador que será automatizado.
  - Após realizar o 1° scan no QR code, o navegador guardará essa informação na pasta \\WhatsPerfil. E com isso, nas próximas vezes em que rodar a aplicação não será necessário passar pelo QrCode Novamente.
  - #### Genial né
### Altere
- pasta_fotos = "C:\\Users\\Allya\\OneDrive\\Documentos\\programacao\\Trocar_Foto_auto\\eu"
  
  Substitua "_C:\\Users\\Allya\\OneDrive\\Documentos\\programacao\\Trocar_Foto_auto\\eu_" pelo caminho da Pasta que contenha as fotos que serão usadas em seu perfil.

## Notas do Autor

Utilize com Moderação

# Autor

andrerogersdev

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andrerogersdev/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/andrerogersdev)
