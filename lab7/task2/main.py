from models import ComputerPart, CPU, GPU

part1 = ComputerPart("Kingston", "SSD A400", 50)
part2 = CPU("Intel", "Core i7-12700K", 320, 12)
part3 = GPU("NVIDIA", "RTX 5070", 600, 12)

parts = [part1, part2, part3]

for part in parts:
    print(part)
    print(part.get_info())
    print(part.get_power_info())
    print()