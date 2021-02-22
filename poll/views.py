from django.shortcuts import render, get_object_or_404, redirect

from .models import Poll, Option, Vote

def show(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id, status='p')
    response = {
        'poll' : poll,
    }

    return render(request, 'poll/show.dj.html', response)


def submit(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id, status='p')
    
    name = request.POST.get('name')
    selected_option_id = request.POST.get('option')
    
    if not name or not selected_option_id:
        return redirect("poll:show", poll_id)

    vote = Vote()
    vote.poll = poll
    vote.name = name
    vote.option = get_object_or_404(Option, pk=selected_option_id)
    vote.save()

    return redirect("poll:complete", poll_id)


def result(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id, status='p')
    votes = Vote.objects.filter(poll=poll)
    result = {}

    for option in poll.options.all():
        result[option.content] = []

    for vote in votes:
        result[vote.option.content].append(vote.name)

    print(result)
    response = {
        'poll' : poll,
        'result' : result,
    }

    return render(request, 'poll/result.dj.html', response)


def complete(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id, status='p')
    response = {
        'poll' : poll,
    }
    return render(request, 'poll/complete.dj.html', response)
