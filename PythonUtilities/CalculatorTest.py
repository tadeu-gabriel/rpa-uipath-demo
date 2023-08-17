import time
import pyautogui

def realizar_operacao(op, num1, num2):
    pyautogui.press('win')
    pyautogui.write('calculadora', interval=0.05)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.write(str(num1), interval=0.05)
    pyautogui.press(op)
    pyautogui.write(str(num2), interval=0.05)
    pyautogui.press('enter')
    time.sleep(1)

    resultado = pyautogui.screenshot(region=(1030, 355, 225, 40))
    resultado.save('resultado.png')
    pyautogui.hotkey('alt', 'f4')

    return resultado

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

resultado = realizar_operacao(op, num1, num2)

print(f"O resultado da operação {num1} {op} {num2} é:")
resultado.show()