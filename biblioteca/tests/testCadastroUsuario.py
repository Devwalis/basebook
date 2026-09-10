import unittest
from unittest.mock import patch
from biblioteca import usuarios


class TestCadastroUsuario(unittest.TestCase):
	
	def setUp(self):
		self.dados = {
			"usuarios": [],
			"livros": [],
			"emprestimos": [],
			"proximos_ids":{
				"usuario": 1,
				"livro": 1,
				"exemplar": 1,
				"emprestimo": 1,
			},
		}



		def test_cadastro_usuario_sucesso(self):
			usuario, erro = usuarios.cadastrar(
				self.dados,
				"joao",
				"Joao souza",
				"senha123",
				"leitor",
			)


			self.assertIsNone(erro)
			self.assertIsNotNone(usuario)
			self.assertEqual(usuario["nome"], "joão souza")
			self.assertEqual(usuario["usuario"], "joao")
			self.assertEqual(usuario["senha"], "senha123")
			self.assertEqual(usuario["perfil"], "leitor")
			self.assertEqual(usuario["id"], 1)


			mock_salvar.assert_called_once_with(self.dados)


if __name__ == "__main__":
	unittest.main()


		