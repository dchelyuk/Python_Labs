class Drug:
    drug_type = "pill"

    def __init__(self, name, volume_of_active_substance, weight_in_mg, active_substance_name, max_doses_per_day):
        self.name = name
        self.volume_of_active_substance = volume_of_active_substance
        self.weight_in_mg = weight_in_mg
        self.active_substance_name = active_substance_name
        self.max_doses_per_day = max_doses_per_day

    def __del__(self):
        return

    def __str__(self):
        return f"\nName: {self.name}\n" \
               f"Volume of active substance: {self.volume_of_active_substance}\n" \
               f"Weight in mg: {self.weight_in_mg}\n" \
               f"Active substance name: {self.active_substance_name}\n" \
               f"Maximum allowed doses per day: {self.max_doses_per_day}\n"

    @staticmethod
    def get_drug_type():
        return Drug.drug_type


def main():
    drug1 = Drug("Ibuprofen", 100, 300, "Ibuprom", 3)
    drug2 = Drug("Nurofen", 20, 200, "Nurom", 20)
    drug3 = Drug("Validol", 50, 400, "Validol", 10)

    print(drug1, drug2, drug3)


if __name__ == "__main__":
    main()
