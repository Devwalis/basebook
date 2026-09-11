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


	


	@patch("biblioteca.usuarios.storage.salvar")
	def test_cadastro_usuario_sucesso(self, mock_salvar):
		usuario, erro = usuarios.cadastrar(
			self.dados,
			"joao",
			"Joao souza",
			"senha123",
			"leitor",
			)


		self.assertIsNone(erro)
		self.assertIsNotNone(usuario)
		self.assertEqual(usuario["nome"], "Joao souza")
		self.assertEqual(usuario["usuario"], "joao")
		self.assertEqual(usuario["senha"], "senha123")
		self.assertEqual(usuario["perfil"], "leitor")
		self.assertEqual(usuario["id"], 1)
			
		mock_salvar.assert_called_once_with(self.dados)

	@patch("biblioteca.usuarios.storage.salvar")
	def test_cadastrar_usuario_perfil_invalido(self, mock_salvar):
		usuario, erro = usuarios.cadastrar(
			self.dados,
			"joao",
			"Joao souza",
			"senha123",
			"administrador",

		)

		self.assertIsNone(usuario)
		
		self.assertEqual(
			erro,

			"Perfil inválido. Use 'leitor' ou 'bibliotecario'."
		)

		mock_salvar.assert_not_called()
	
			


if __name__ == "__main__":
	unittest.main()


		