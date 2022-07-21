# with open("books.txt") as file:
#     print(file.read())
# with open("books.txt") as file:
#     for line in file:
#         print(f"моя любимая книга {line}")
# with open("blank.txt","w") as file:
#     file.write("Новый текст")
# with open("blank.txt") as file:
#     print(file.read())


color = "red"
shape = "squeare"

def function():
    shape = "circle"
    global color
    color = "green"
function()
print(color)
print(shape)
