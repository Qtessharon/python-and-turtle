import turtle

#kuya adalah pemanggil new turtle
kuya = turtle.Turtle()
turtle.color('blue')

#kemudian membuat gambar kotak menggunakan for
for i in range(100):
    kuya.forward(20+i * 3)

    #code dibawah ini mempengaruhi gambar sesuai dengan angka sudutnya ex(90)
    kuya.right(457)
