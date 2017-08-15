
	Descripción del problema
	Algo ha ocurrido en el sistema de puntuaciones de nuestro juego online "Epic Invaders XXIII". Un hacker amateur, cabreado por los malos resultados que le han llevado hasta lo más bajo de la tabla, ha "secuestrado" su sistema de puntuaciones. El fichero con las puntuaciones no ha desaparecido aunque el hacker lo ha codificado para que sólo él pueda recuperarlo. Afortunadamente los servicios de inteligencia de "Epic Invaders XXIII" han descubierto algunos datos sobre la codificación utilizada por el hacker que pueden ser útiles para resolver este problema:
	El fichero codificado parece un fichero CSV. Cada línea contiene la puntuación de un usuario.
	La primera columna es el nombre del usuario.
	La segunda columna parecen ser los dígitos del sistema numérico utilizado para codificar la puntuación.
	La tercera columna es la puntuación.
	 
	Puedes ayudarnos a descifrar el fichero?
	 
	 
	Fichero de puntuaciones codificado por el hacker
	Johny,oF8,Fo
	Ka0s,0123456789,23
	SmoKe,01,01100
	S0mbra,oi8,oo
	KamiKaze,54?t,?4?
	TheBest,kju2aq,u2ka
	L0s3r,_- /.!#,# _
	 
	Nota: Los dígitos de los sistemas de numeración siempre están escritos de menor a mayor (ejemplo: "0123456789").



# pass file as an argument 
# python main.py file.csv

# without passing file as an argument 
# it will look for a csv file in the current folder
# python main.py 

# test
# python test_main_unittest.py
  