from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Profile
from .forms import ProfileForm, ProfileSearchForm

@login_required
def profile_detail(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
        profile = user.profile
    else:
        profile = request.user.profile
    
    return render(request, 'profiles/profile_detail.html', {
        'profile': profile,
        'is_owner': profile.user == request.user
    })

@login_required
def profile_list(request):
    search_form = ProfileSearchForm(request.GET)
    profiles = Profile.objects.all()
    
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search')
        department = search_form.cleaned_data.get('department')
        position = search_form.cleaned_data.get('position')
        
        if search_query:
            profiles = profiles.filter(
                Q(full_name__icontains=search_query) |
                Q(user__username__icontains=search_query) |
                Q(department__icontains=search_query) |
                Q(position__icontains=search_query)
            )
        if department:
            profiles = profiles.filter(department__icontains=department)
        if position:
            profiles = profiles.filter(position__icontains=position)
    
    return render(request, 'profiles/profile_list.html', {
        'profiles': profiles,
        'search_form': search_form
    })

@login_required
def profile_edit(request, username=None):
    if username and request.user.username != username:
        return redirect('profiles:detail', username=request.user.username)
    
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profiles:detail', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'profiles/profile_edit.html', {
        'form': form,
        'profile': profile
    })
