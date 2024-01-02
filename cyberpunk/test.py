
str_1 = '<div>Tulip</div><div>Lily</div><div>Sunflower</div><div>Orchids</div><div>Carnations</div><div>Gerbera Daisies</div><div>Hydrangeas</div><div>Peonies</div><div>Chrysanthemums</div>'

x = str_1.replace('<div>','').split('</div>')
print(x)