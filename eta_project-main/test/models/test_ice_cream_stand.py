import pytest
from src.models.ice_cream_stand import IceCreamStand

class TestIceCreamStand:
    """Classe de teste para a classe IceCreamStand."""

    @pytest.fixture
    def ice_cream_stand(self):
        """Fixture para instanciar um IceCreamStand."""
        return IceCreamStand("Gelateria", "Sorveteria", ["Baunilha", "Chocolate", "Morango"])

    def test_initialization_valid_flavors(self, ice_cream_stand):
        """Testa se a lista de sabores é inicializada corretamente."""
        assert ice_cream_stand.flavors == ["Baunilha", "Chocolate", "Morango"], \
            "A lista de sabores não foi inicializada corretamente."

    def test_initialization_invalid_flavors(self):
        """Testa se o metodo levanta um erro ao receber uma lista inválida."""
        with pytest.raises(ValueError, match="A lista de sabores deve ser uma lista válida."):
            IceCreamStand("Gelateria", "Sorveteria", None)

    def test_flavors_available_with_flavors(self, ice_cream_stand):
        """Testa se a lista de sabores disponíveis é retornada corretamente."""
        expected_output = "No momento temos os seguintes sabores de sorvete disponíveis:\nBaunilha\nChocolate\nMorango"
        assert ice_cream_stand.flavors_available() == expected_output, \
            "A lista de sabores disponíveis não foi retornada corretamente."

    def test_flavors_available_no_flavors(self):
        """Testa o comportamento quando não há sabores disponíveis."""
        stand = IceCreamStand("Gelateria", "Sorveteria", [])
        assert stand.flavors_available() == "Estamos sem estoque atualmente!", \
            "A mensagem para falta de sabores não foi retornada corretamente."

    def test_find_flavor_exists(self, ice_cream_stand):
        """Testa a busca por um sabor existente (case insensitive)."""
        assert ice_cream_stand.find_flavor("baunilha") == "Temos Baunilha no estoque!", \
            "A busca por sabores existentes não funcionou corretamente."

    def test_find_flavor_does_not_exist(self, ice_cream_stand):
        """Testa a busca por um sabor inexistente."""
        assert ice_cream_stand.find_flavor("Pistache") == "Não temos Pistache no momento!", \
            "A mensagem para sabores inexistentes não foi retornada corretamente."

    def test_find_flavor_invalid_input(self, ice_cream_stand):
        """Testa a busca por um sabor com entrada inválida."""
        assert ice_cream_stand.find_flavor(123) == "Erro: O sabor informado deve ser uma string válida.", \
            "A validação para entrada inválida não funcionou corretamente."

    def test_add_flavor_new_flavor(self, ice_cream_stand):
        """Testa a adição de um novo sabor ao estoque."""
        assert ice_cream_stand.add_flavor("Pistache") == "Pistache adicionado ao estoque!", \
            "A adição de um novo sabor não funcionou corretamente."
        assert "Pistache" in ice_cream_stand.flavors, \
            "O novo sabor não foi adicionado ao estoque."

    def test_add_flavor_existing_flavor(self, ice_cream_stand):
        """Testa a tentativa de adicionar um sabor já existente."""
        assert ice_cream_stand.add_flavor("Baunilha") == "Sabor já disponível!", \
            "A validação para sabores duplicados não funcionou corretamente."

    def test_add_flavor_invalid_input(self, ice_cream_stand):
        """Testa a adição de um sabor com entrada inválida."""
        assert ice_cream_stand.add_flavor(123) == "Erro: O sabor informado deve ser uma string válida.", \
            "A validação para entrada inválida ao adicionar sabores não funcionou corretamente."
