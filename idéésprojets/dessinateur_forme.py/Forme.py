

def rectangle(x: int = 1, y: int = 1, indent: int = 0):
    y -= 1
    space = " "
    high = y * ("\n" + f"{indent * space}" + "|" + (x * " ") + "|")

    return f"""
 {indent*" "}{x*"_"}{high}
{indent * space}{"|" + x*"_" + "|"}
"""
