from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateGroupForm, JoinGroupForm, MessageForm
from .models import Group, Message
import random
import string
from .utils import generate_random_username

def home(request):
   
    groups = Group.objects.all()  # Fetch all groups from the database
    return render(request, 'home.html', {'groups': groups})

def create_group(request):
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            group_id = ''.join(random.choices(string.digits, k=6))

            # Create group
            group = Group.objects.create(group_id=group_id, topic=topic)

            # Generate and store username in session
            username = generate_random_username()
            request.session['username'] = username

            return redirect('view_group', group_id=group.group_id)  # 👈 Redirect to group after creation
    else:
        form = CreateGroupForm()

    return render(request, 'create_group.html', {'form': form})

def join_group(request):
    if request.method == 'POST':
        form = JoinGroupForm(request.POST)
        if form.is_valid():
            group_id = form.cleaned_data['group_id']
            username = form.cleaned_data['username']
            try:
                group = Group.objects.get(group_id=group_id)
                request.session['username'] = username
                return redirect('view_group', group_id=group_id)
            except Group.DoesNotExist:
                form.add_error('group_id', 'Group not found.')
    else:
        form = JoinGroupForm()
    return render(request, 'join_group.html', {'form': form})

def view_group(request, group_id):
    group = get_object_or_404(Group, group_id=group_id)
    messages = Message.objects.filter(group=group).order_by('created_at')
    username = request.session.get('username')

    if not username:
        return redirect('join_group')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.group = group
            message.anon_name = username
            message.save()
            return redirect('view_group', group_id=group_id)
    else:
        form = MessageForm()

    return render(request, 'group.html', {
        'group': group,
        'messages': messages,
        'form': form,
    })
