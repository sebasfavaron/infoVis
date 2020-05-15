import pandas as pd
import matplotlib.pyplot as plt


bataxi = pd.read_csv("./bataxi.csv", sep=',')

q1_cant_viajes = bataxi.groupby('id_taxista').size()  # Sub-tabla 1
q1_duracion_promedio = bataxi.groupby('id_taxista').mean()[['duracion']]  # Sub-tabla 2
q1_duracion_promedio.columns = ['duracion_promedio']
q1 = q1_cant_viajes.to_frame(name='cant_viajes').merge(q1_duracion_promedio, how='outer', on='id_taxista')  # Merge sub-tablas
q1.duracion_promedio /= 60
q1_promedio_por_cant_viajes = q1.groupby('cant_viajes').mean()  # Agrupo taxistas con misma cantidad de viajes y promedio
q1_plot = q1.plot.scatter(x='cant_viajes', 
                          y='duracion_promedio')  # Cada punto es un taxista
q1_agg_plot = q1_promedio_por_cant_viajes.plot(ax=q1_plot, 
    color='orange')  # De la tabla anterior se agrupa por cantidad de viajes a los taxistas y se promedia las duraciones de esos
q1_agg_plot.legend(['Taxistas con igual cantidad de viajes agrupados', 'Un punto por taxista'])
q1_agg_plot.set(xlabel='Cantidad de viajes', 
                ylabel='Duracion promedio de viajes (min)')


q2_tabla = bataxi.groupby('id_taxista').size()
q2_conductor = q2_tabla.idxmax()
q2_valor = q2_tabla.max()
q2_promedio = q2_tabla.mean()
q2 = [q2_conductor, q2_valor, q2_tabla.mean()]


q3_tabla = bataxi.groupby(['id_taxista', 'fecha_inicio']).size()
q3_conductor_dia = q3_tabla.idxmax()
q3_conductor = q3_conductor_dia[0]
q3_dia = q3_conductor_dia[1]
q3_valor = q3_tabla.max()
q3_promedio = q3_tabla.mean()
q3 = [q3_conductor_dia, q3_valor, q3_tabla.mean()]


q4_with_nulls = bataxi.where(bataxi.fecha_inicio != bataxi.fecha_fin)
q4_table = q4_with_nulls[q4_with_nulls.duracion.notnull()][['id_taxista', 
    'fecha_inicio', 'fecha_fin', 'duracion', 'cantidad_pasajeros']]
q4 = q4_table.shape[0]


print('q1. Duracion vs cantidad de viajes. A mas viajes menor duracion?\n\t(Ver grafico)')

print('q2. Maximo de viajes realizados por un conductor?')
print('    \tEl maximo de viajes del 1 de Mayo al 1 de Septiembre de 2017 lo realizo el conductor {} con {} viajes. El promedio de cantidad de viajes en ese tiempo es {:.2f}'.format(q2_conductor, q2_valor, q2_promedio))

print('q3. Maximo de viajes realizados por un conductor en un dia?')
print('    \tEl maximo de viajes en un dia lo realizo el conductor {} en el dia {} con {} viajes. El promedio de cantidad de viajes para un dia cualquiera es {:.2f}'.format(q3_conductor, q3_dia, q3_valor, q3_promedio))

print('q4. Cantidad de viajes trasnoche (que empiecen en un dia y terminen en otro)?')
print('    \tHubieron {} viajes trasnoche del 1 de Mayo al 1 de Septiembre de 2017, o en promedio {:.2f} por dia'.format(q4, q4/123))
plt.show() # q1
