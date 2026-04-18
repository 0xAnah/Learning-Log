from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_log/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_log/topics.html', context)

def topic(request, topic_id):
    """show the chess topic and its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {"topic":topic, "entries":entries}
    return render(request, 'learning_log/topic.html', context)

def new_topic(request):
    """add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_log:topics')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_log/new_topic.html', context)

def new_entry(request, topic_id):
    """add a new entry for a topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # no data created; create blank form 
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            redirect('learning_log:topic', topic_id=topic_id)
        
    # display a blank form
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_log/new_entry.html', context)

def edit_entry(request, entry_id):
    """edit an exisiting entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            redirect('learning_log:topic', topic_id=topic.id)
    
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_log/edit_entry.html', context)