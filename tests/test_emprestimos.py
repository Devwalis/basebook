import unittest
from unittest.mock import patch

from biblioteca import emprestimos

class TestEmprestimo(unittest.TestCase):

    def setUp(self):
        self.dados = {
            "usuarios": [
                {
                    "id": 1,
                    "usuario": "joao",
                    "nome": "Joao Souza",
                    "senha": "senha123",
                    "perfil": "leitor",
                }
            ],

            "livros": [
                {
                    "id": 1,
                    "titulo": "Clean Code",
                    "exemplares":[
                        {
                            "id":1,
                            "disponivel": True,
                            "emprestado_para": None,

                        }
                    ],
                }
            ],
            "emprestimos": [],
            "proximos_ids": {
                "usuario": 2,
                "livro": 2,
                "exemplar": 2,
                "emprestimo": 1,
            }
        }

        self.usuario = self.dados["usuarios"][0]
        self.obra = self.dados["livros"][0]
        self.exemplar = self.obra["exemplares"][0]


    @patch("biblioteca.emprestimos.storage.salvar")
    def test_emprestar_livro_sucesso(self, mock_salvar):

        registro, erro = emprestimos.emprestar(
            self.dados,
            self.usuario,
            self.obra,
            self.exemplar,
        )



        self.assertIsNone(erro)
        self.assertIsNotNone(registro)


        self.assertEqual(registro["id"], 1)
        self.assertEqual(registro["usuario_id"], 1)
        self.assertEqual(registro["livro_id"], 1)
        self.assertEqual(registro["exemplar_id"], 1)

        self.assertIsNotNone(registro["data_emprestimo"])
        self.assertEqual(registro["renovacoes"], 0)

        self.assertFalse(self.exemplar["disponivel"])
        self.assertEqual(self.exemplar["emprestado_para"], 1)

        self.assertEqual(len(self.dados["emprestimos"]), 1)


        mock_salvar.assert_called_once_with(self.dados)


if __name__ == "__main__":
    unittest.main()


