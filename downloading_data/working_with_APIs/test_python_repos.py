# Lucas Garzuze Cordeiro - 24/04/2023
# Utilizar o módulo unittest para testar se o chamado da API deu certo

import requests
import unittest

def make_api_call():
    """Faz o chamado da API do GitHub e armazenar seu resultado"""
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers)
    return r


class ApiTestCase(unittest.TestCase):
    """Testes para o chamado da API do GitHub"""

    def test_status_code(self):
        """Teste para verificar se o chamado deu certo"""
        r = make_api_call()
        self.assertEqual(r.status_code, 200)

    def test_num_repos(self):
        """Testando se retornou o número de repositórios corretamente"""
        r = make_api_call()
        response_dict = r.json()
        repo_dicts = response_dict['items']

        self.assertEqual(len(repo_dicts), 30)

    def test_total_repos(self):
        """Testando se o número total de repositórios é maior que 9 milhões"""
        r = make_api_call()
        response_dict = r.json()

        self.assertGreater(response_dict['total_count'], 9000000)

if __name__ == '__main__':
    unittest.main()