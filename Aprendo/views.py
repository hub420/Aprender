import http
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """Home page para Aprendo."""
    return render(request, 'Aprendo/index.html' )

@login_required    
def topics(request):
    """muestra todos los topicos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'Aprendo/topics.html', context)

@login_required  
def topic(request, topic_id):
    """muestra un topico con todas sus entradas"""
    topic = Topic.objects.get(id=topic_id)
    #asegurandose que el topico pertenece a su usuario correspondiente.
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'Aprendo/topic.html', context)

@login_required  
def new_topic(request):
    """agregar un nuevo tema"""
    if request.method != 'POST':
        # No hay datos suministrados crear una forma en blanco.
        form = TopicForm()
    else:
        # POST datos suministrados procesar datos.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('Aprendo:topics')
    
    #Desplega una forma en blanco
    context = {'form': form}
    return render(request, 'Aprendo/new_topic.html', context)

@login_required  
def new_entry(request, topic_id):
    """agregar un nuevo tema a un topic en particular"""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # No hay datos suministrados crear una forma en blanco.
        form = EntryForm()
    else:
        # POST datos suministrados procesar datos.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('Aprendo:topic', topic_id=topic_id)
    
    #Desplega una forma en blanco
    context = {'topic':topic,'form': form}
    return render(request, 'Aprendo/new_entry.html', context)

@login_required  
def edit_entry(request, entry_id):
    """Editar una entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # requerimiento inicial prellenado de la forma con la entrada actual  
        form = EntryForm(instance=entry)
    else:
        # POST datos suministrados procesar datos.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Aprendo:topic', topic_id=topic.id)
    
    context = {'entry':entry ,'topic':topic,'form': form}
    return render(request, 'Aprendo/edit_entry.html', context)

