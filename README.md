# KakasiAPI-Docker α
The API is available at https://romanization.hirameki.me/ using a POST on =input, test with 'curl -X POST -d "input=今日は美しい朝だ！" https://romanization.hirameki.me/'
Will return "konnichiha utsukushi i asa da !"

A API está disponivel em https://romanization.hirameki.me/ usando um POST em =input, teste com 'curl -X POST -d "input=今日は美しい朝だ！" https://romanization.hirameki.me/'
Vai retornar "konnichiha utsukushi i asa da !"

-----------------------
Kakasi HTTP API on Docker

This is the API using the KAKASI software in http made especially for RfAM, it is basically a communicator between http and the program compiled in C.

In a second moment I intend to integrate C with python, or write an API in C to answer the HTTP post without going through the shell.

[Here is a link for docker Image](http://home.hirameki.me/KakasiDocker.tar)

To import this image -> "cat archive.tar |docker import - kakasidocker"
To activate the container -> "docker run -d -u 1000 --name kakasidocker_backend kakasidockerstart.sh prod"
To activate the API -> "docker start kakasidocker_backend"

After that you can give CURL using a POST to get the conversion -> "curl -X POST -d "input=今日は美しい朝だ！" http://[DOCKER IP]/convert"

Extra -> You can check your IP using "docker exec kakasidocker_backend ip a"

-----------------------
Essa e a API usando o software KAKASI em http feita em especial para o RfAM, e basicamente um comunicador entre o http e o programa compilado em C.

Em um segundo momento pretendo integrar o C ao python, ou escrever uma API em C para responder o HTTP post sem passar pelo shell.

[Aqui o link para a imagem docker](http://home.hirameki.me/KakasiDocker.tar)

Para importar essa imagem -> "cat arquivo.tar |docker import - kakasidocker"
Para ativar o container -> "docker run -d -u 1000 --name kakasidocker_backend kakasidockerstart.sh prod"
Para ativar a API -> "docker start kakasidocker_backend "

Após isso você pode dar o CURL usando um POST para obter a conversão -> "curl -X POST -d "input=今日は美しい朝だ！" http://[IP DO DOCKER]/convert"

Extra -> Você pode checar seu IP usando  "docker exec kakasidocker_backend ip a"
