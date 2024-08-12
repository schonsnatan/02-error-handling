LINK_DOC = "docs.python.org/3/library/exceptions.html"

#TypeErros: using str instead of int or float

#Print the type of error:
try:
    resultado = len(3)
    print(resultado)
except TypeError as e:
    print(e)