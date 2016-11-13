from itertools import chain

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect

from oth.models import Level, UserProfile

def index(request):
    return render(request, 'oth/index.html')

@login_required
def display_level(request, level):
    current_user = request.user.profile
    current_level = current_user.current_level
    if current_level == settings.MAX_LEVELS and current_user.completed:
        return redirect('/finish')

    level_object = get_object_or_404(Level, level_number__exact=int(level))

    if request.method == 'GET':
        if current_user.current_level == int(level):
            return render(request, 'oth/level.html', {'level_object': level_object})
        else:
            return HttpResponseRedirect('/level/%d' % current_level)
    elif request.method == 'POST':
        user_answer = request.POST['answer'].encode('utf-8')

        if level_object.validate_answer(user_answer) and int(current_level) <= int(level):
            current_user.increment_level()
            if int(level) == settings.MAX_LEVELS:
                current_user.completed = True
                current_user.save();
            	return HttpResponseRedirect('/finish')
            return HttpResponseRedirect('/level/%d' % (int(level) + 1))
        return HttpResponseRedirect('/level/%d' % int(level))

@login_required
def display_leaderboard(request):
    user_completed = UserProfile.objects.filter(completed=True).order_by('updated_at')
    users_not_completed = UserProfile.objects.filter(completed=False).order_by('-current_level','updated_at')
    users = list(chain(user_completed,users_not_completed))
    users = zip(range(1,len(users)+1),users)
    return render(request, 'oth/leaderboard.html', {'users': users})

@login_required
def finish(request):
    current_user = request.user.profile
    if current_user.current_level == settings.MAX_LEVELS:    
        return render(request, 'oth/finish.html',{})
    return redirect('/level/%d' % current_user.current_level)    

@login_required
def play(request):
    current_user = request.user.profile
    return redirect('/level/%d' % current_user.current_level)
