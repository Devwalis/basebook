import unittest
from unittest.mock import patch

from biblioteca import livros

class TestCadastroLivro(unittest.TestCase):


    def setUp(self):
        self.dados = {
            "usuarios": [],
            "livros": [],
            "emprestimos": [],
            "proximos_ids": {
                "usuario": 1,
                "livro": 1,
                "exemplar": 1,
                "emprestimo": 1,
            },
            
        }


    @patch("biblioteca.livros.storage.salvar")
    def test_cadastrar_livro_sucesso(self, mock_salvar):
        obra, erro = livros.cadastrar(
            self.dados,
            "Clean Code",
            3,

        )

        self.assertIsNone(erro)
        self.assertIsNotNone(obra)
        
        self.assertEqual(obra["id"], 1)
        self.assertEqual(obra["titulo"], "Clean Code")

        self.assertEqual(len(obra["exemplares"]), 3)


        self.assertEqual(obra["exemplares"][0]["id"], 1)
        self.assertEqual(obra["exemplares"][1]["id"], 2)
        self.assertEqual(obra["exemplares"][2]["id"], 3)

        self.assertTrue(obra["exemplares"][0]["disponivel"])
        self.assertIsNone(obra["exemplares"][0]["emprestado_para"])

        mock_salvar.assert_called_once_with(self.dados)


if __name__ == "__main__":
    unittest.main()


