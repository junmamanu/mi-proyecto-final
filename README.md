# Proyecto final Coder house
Proyecto final desarrollado en conjuto por Juan Manuel Godoy Gandaria y Lorenzo Peña

El proyecto se compone a base de Django ver **4.1.2** y python ver **3.10.6**

# Entrega  proyecto intermedio fecha 27/10/2022

Entra-1 Godoy juna manuel y Lorenzo peña

# Herencias de html

Se utiliza la herencia 
- ubicada en /ejemplot/emplates/ejemplo/base.thml
    ```python
    {% extends 'ejemplo/base.html' %}
    {% block titulo%} Alta nuevo usuario {% endblock %}
    {% block contenido %}
    {  % endblock %}
    ```
- Ubicado en /ejemplot/emplates/ejemplo/base.thml 

# Creacion de models

- importando 
    ```python
    from django.db import models
    ```


- se crean 3 modelos con la classe "familiar"

    ```python
    class Familiar(models.Model):
        nombre = models.CharField(max_length=100)
        direccion = models.CharField(max_length=200)
        numero_pasaporte = models.IntegerField()
    ```
- Ubicado en /ejemplo/models.py
Formulario para insetar datos en las clases "familiar"

- Usando el /ejemplo/templates/ejemplo/alta familiar.htm
- Heredando /ejemplo/templates/ejemplo/base.thml

    ```html
    {% extends 'ejemplo/base.html' %}
    {% block titulo%} Alta nuevo usuario {% endblock %}
    {% block contenido %}

    <form action="/mi-familia/alta" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit">
        </form>

        <h2 style="color:green">{{msg_exito}}</h2>
    {% endblock %}
    ```

Importamos la vista al archivo ejemplo/views.py

- importando 
    ```python
    from ejemplo.forms import Buscar, FamiliarForm
    from django.views import View 
    ```
- Creamos la vista 
    ```python
    class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
    ```
- y por ultimo la ruteamos vamos a ejemplo/urls.py 
Importamos 
    ```python
    from ejemplo.views import AltaFamiliar
    ```
- Luego agregamos al path
```python
    path('mi-familia/alta', AltaFamiliar.as_view())
```
# Formulario para Buscar datos en las clases BD

- Usando el /ejemplo/templates/ejemplo/buscar.htm
- Heredando /ejemplo/templates/ejemplo/base.thml

    ```python
    {% extends 'ejemplo/base.html' %}
    {% block titulo%} Buscar Familiares por nombre {% endblock %}
    {% block contenido %}

    <form action="/mi-familia/buscar" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit">
    </form>

    {% for familiar in lista_familiares %}
        <ul>
            <li> Nombre: {{familiar.nombre}}, Dirección: {{familiar.direccion}}, Pasaporte: {{familiar.numero_pasaporte}}</li>
        </ul>
    {% endfor %}
    {% endblock %}
    ```

- Importamos la vista al archivo ejemplo/views.py
- impotando 
    ```python
    from django.views import View 
    ```

- Agregamos la clase al archivo ejemplo/views.py

    ```python

    class BuscarFamiliar(View):

        form_class = Buscar
        template_name = 'ejemplo/buscar.html'
        initial = {"nombre":""}

        def get(self, request):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form})

        def post(self, request):
            form = self.form_class(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data.get("nombre")
                lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
                form = self.form_class(initial=self.initial)
                return render(request, self.template_name, {'form':form, 
                                                            'lista_familiares':lista_familiares})

            return render(request, self.template_name, {"form": form})

    ```





- bullet
* bullet


```python

aca va codigo python 

Lorem, ipsum dolor sit amet 
consectetur adipisicing elit. 
Commodi maxime iure temporibus? 
Dolores tempore accusamus amet ea praesentium 
corporis libero, in iure, 
cum itaque ex expedita consequuntur adipisci. Libero,
fugit.
```
