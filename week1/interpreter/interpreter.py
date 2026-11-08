x, y, z = input("Expression: ").split(' ')

float_x = float(x)
float_z = float(z)

calculate = 0.0
match y:
    case '+':
        calculate =  float_x + float_z
    case '-':
        calculate =  float_x - float_z
    case '/':
        calculate =  float_x /  float_z
    case '*':
        calculate =  float_x * float_z

print(calculate)
