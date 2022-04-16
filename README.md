# Trabalho Ambientes Operacionais

Este repositório contém a descrição e códigos necessários para o trabalho aplicado da disciplina de Ambientes Operacionais.

Utilize o ambiente do curso "AWS Academy Learner Lab - Foundation Services" para fazer o trabalho. |Este ambiente persiste até o fechamento do curso.

## Objetivo

Aplicar os conhecimentos adquiridos na disciplina de Ambientes Operacionais, provisionando recursos na AWS dentro de uma VPC e suas subredes públicas e privadas e criando regras de segurança par acesso aos recursos.

## Grupo

O trabalho deve ser feito em **grupos de até 5 alunos**. 

## Entrega

A entrega deverá ser feita até a data especificada no cronograma. O grupo deverá gravar um vídeo mostrando a solução e entregar uma figura com a arquitetura da solução. Utilize https://app.diagrams.net/ para fazer o desenho da arquitetura. O vídeo deve mostrar evidências de todas as tarefas descritas a seguir. 


## Tarefas

1. Criar uma VPC com as seguintes características:

    1.1. A VPC deve ter 1019 endereços de IPv4 disponíveis 

    1.2. Duas subredes públicas

    1.3. Duas subredes privadas.

    1.4. Cada subrede deve conter 59 endereços de IPv4 disponíveis
    
    1.5. Utilizar duas zonas de disponibilidade diferentes. Uma subrede pública e uma privada deve estar em cada zona de disponibilidade

    1.6 A VPC deve conter um NAT Gateway

    1.7 A VPC deve conter um Internet Gateway

    1.8 A VPC deve conter as tabelas de rotas e associações apropriadas para as subredes
    
2. Criar um bucket S3 com as seguintes características:

    2.1. O bucket deve ser configurado permitir acesso público

    2.2 O bucket deve ser configurado para hospedar um site estático

    2.3 O bucket deve ter a seguinte política de segurança. Troque **NOME_BUCKET** pelo nome do sseu bucket:

    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::NOME_BUCKET/*"
            }
        ]
    }
    ```

   
