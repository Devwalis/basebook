import unittest
from unittest.mock import patch

from biblioteca import devolucoes



class TestDevolucoes(unittest.TestCase):


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
                    "exemplares": [
                        {
                            "id": 1, 
                            "disponivel": False,
                            "emprestado_para": 1,

                        }
                    ],
                }
            ],
            "emprestimos": [
                {
                    "id": 1,
                    "usuario_id": 1,
                    "livro_id": 1,
                    "exemplar_id": 1,
                    "data_emprestimo": "2026-09-11",
                    "data_prevista": "2026-09-18",
                    "data_devolucao": None,
                    "renovacoes": 0,


                }
            ],
            "proximos_ids":{
                "usuario": 2,
                "livro": 2,
                "exemplares": 2,
                "emprestimo": 2,

            },
        }


        self.emprestimo = self.dados["emprestimos"][0]
        self.obra = self.dados["livros"][0]
        self.exemplar = self.obra["exemplares"][0]



    @patch("biblioteca.devolucoes.storage.salvar")
    def test_devolver_emprestimo_ja_devolvido(self, mock_salvar):

        self.emprestimo["data_devolucao"] = "2026-09-11"
        devolvido, erro = devolucoes.devolver(
            self.dados,
            self.emprestimo,
            self.obra,
            self.exemplar,
        )

        self.assertIsNone(devolvido)

        self.assertEqual(
            erro,
            "Empréstimo já devolvido."
        )

        mock_salvar.assert_not_called()

    @patch("biblioteca.devolucoes.storage.salvar")
    def test_devolver_livro_sucesso(self, mock_salvar):

        devolvido, erro = devolucoes.devolver(
            self.dados,
            self.emprestimo,
            self.obra,
            self.exemplar,
        )

        self.assertIsNone(erro)
        self.assertIsNotNone(devolvido)


        self.assertEqual(devolvido["id"], 1)
        self.assertIsNotNone(devolvido["data_devolucao"])

        self.assertTrue(self.exemplar["disponivel"])
        self.assertIsNone(self.exemplar["emprestado_para"])

        mock_salvar.assert_called_once_with(self.dados)


if __name__ == "__main__":
    unittest.main()