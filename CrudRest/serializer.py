from rest_framework import serializers
from .models import Project
# esto es un serializer
'''para que se usa el serializer
    nos permiten usar el modulo serializer
    
  Los serializadores en Django REST Framework son una parte esencial para trabajar con la biblioteca. 
  Los serializadores permiten convertir datos complejos, como querysets e instancias de modelos,
  en tipos de datos nativos de Python que luego se pueden representar fácilmente en JSON, XML u otros tipos
  de contenido1. También proporcionan deserialización, lo que permite convertir datos analizados en tipos 
  complejos, después de validar los datos entrantes1.

Los serializadores en REST Framework funcionan de manera muy similar a las clases Form y ModelForm de Django1.
Proporcionan una forma poderosa y genérica de controlar la salida de las respuestas, así
como una clase ModelSerializer que proporciona un atajo útil para crear serializadores que trabajan con
instancias de modelos y querysets1.

'''

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','title','description','technology','created')
        read_only_fields=('created',)
        