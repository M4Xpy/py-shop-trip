from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int | float]
    products: dict[str: int]

    def purchase_cost_for(self, client: any) -> list | None:
        total = [0, ""]
        for key, value in client.product_cart.items():
            if key not in self.products:
                return None
            unit_coast = self.products[key]
            cost = value * unit_coast
            total[1] += f"{value} {key}s for {(cost, int(cost)
                                               )[cost.is_integer()]} dollars\n"
            total[0] += cost
        total[1] += f"Total cost is {total[0]} dollars"

        return total