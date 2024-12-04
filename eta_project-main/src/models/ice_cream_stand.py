from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)

        # Bug: `flavors_list` pode ser None, o que causaria erros ao tentar iterar ou acessar atributos.
        # Correção: Valide se `flavors_list` é uma lista válida.
        if not isinstance(flavors_list, list):
            raise ValueError("A lista de sabores deve ser uma lista válida.")
        self.flavors = flavors_list if flavors_list else []

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            # Bug: Falta de espaçamento ou quebra de linha entre os sabores.
            # Correção: Use `\n` para separar os sabores, melhorando a legibilidade.
            result = "No momento temos os seguintes sabores de sorvete disponíveis:\n"
            result += "\n".join(self.flavors)
            return result
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        # Bug: Falta de validação para garantir que `flavor` seja uma string.
        # Correção: Adicione verificação para evitar erros com tipos inválidos.
        if not isinstance(flavor, str):
            return "Erro: O sabor informado deve ser uma string válida."

        # Bug: Não verifica insensibilidade ao caso, podendo duplicar resultados (ex.: 'Baunilha' e 'baunilha').
        # Correção: Normalize os valores para comparação case insensitive.
        if flavor.lower() in (f.lower() for f in self.flavors):
            return f"Temos {flavor.capitalize()} no estoque!"
        else:
            return f"Não temos {flavor.capitalize()} no momento!"

    def add_flavor(self, flavor):
        """Adiciona o sabor informado ao estoque."""
        # Bug: Falta de validação para garantir que `flavor` seja uma string válida.
        # Correção: Adicione verificação para evitar erros com tipos inválidos.
        if not isinstance(flavor, str):
            return "Erro: O sabor informado deve ser uma string válida."

        # Bug: Não verifica insensibilidade ao caso, permitindo duplicatas visuais (ex.: 'Baunilha' e 'baunilha').
        # Correção: Normalize os valores para evitar duplicatas no estoque.
        flavor = flavor.strip().lower()
        if flavor in (f.lower() for f in self.flavors):
            return "Sabor já disponível!"

        # Correção: Adicione o sabor ao estoque com a formatação correta.
        self.flavors.append(flavor.capitalize())
        return f"{flavor.capitalize()} adicionado ao estoque!"
