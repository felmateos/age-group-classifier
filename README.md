<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Exercício Programa de PLN</h3>

  <p align="center">
    👶👧👦 Desvendando padrões na escrita das pessoas, <br />
    descobrindo a faixa etária da pessoa apenas pelo seu texto 👨👩👴
    <br />
    <br />
    <a href="https://github.com/felmateos/age-group-classifier/issues">Report Bug</a>
    ·
    <a href="https://github.com/felmateos/age-group-classifier/issues">Request Feature</a>
  </p>
</div>

<br />

---

Este repositório contém um classificador de texto desenvolvido para identificar a faixa etária associada a determinados textos. O modelo foi treinado utilizando técnicas de processamento de linguagem natural (PLN) e machine learning, com o objetivo de prever a faixa etária de acordo com o conteúdo textual fornecido.

## Git Clone

Para obter uma cópia local deste repositório, utilize o seguinte comando:

```
git clone https://github.com/felmateos/age-group-classifier.git
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Instalação

Antes de começar, certifique-se de ter o ambiente Python configurado. Utilize o seguinte comando para instalar as dependências necessárias:

```
pip install -r requirements.txt
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Métricas

O desempenho do modelo é avaliado por meio das seguintes métricas:

- **Acurácia no Conjunto de Teste (Test Accuracy):** Mede a proporção de classificações corretas em relação ao total de instâncias no conjunto de teste.
  - ### 52.31%
- **Acurácia Média em 10 Folds (Cross Validation):** A acurácia média obtida através de um processo de validação cruzada com 10 folds.
  - ### 51.28%
 
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Matriz de Confusão

A matriz de confusão oferece uma visão detalhada do desempenho do modelo. A imagem abaixo representa a matriz de confusão gerada durante a avaliação do classificador:

![Matriz de Confusão](images/confusion_matrix.png)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Documentos importantes

Na pasta 'docs' estão tanto o relatório, quanto a apresentação do projeto, onde constam informações que podem ser úteis para compreender o que foi feito.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias, relatar problemas ou abrir pull requests.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/felmateos/age-group-classifier.svg?style=for-the-badge
[contributors-url]: https://github.com/felmateos/age-group-classifier/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/felmateos/age-group-classifier.svg?style=for-the-badge
[forks-url]: https://github.com/felmateos/age-group-classifier/network/members
[stars-shield]: https://img.shields.io/github/stars/felmateos/age-group-classifier.svg?style=for-the-badge
[stars-url]: https://github.com/felmateos/age-group-classifier/stargazers
[issues-shield]: https://img.shields.io/github/issues/felmateos/age-group-classifier.svg?style=for-the-badge
[issues-url]: https://github.com/felmateos/age-group-classifier/issues
[license-shield]: https://img.shields.io/github/license/felmateos/age-group-classifier.svg?style=for-the-badge
[license-url]: https://github.com/felmateos/age-group-classifier/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=259
[linkedin-url]: https://linkedin.com/in/felmateos
