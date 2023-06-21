import json
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, CreateView, ListView, DetailView
import openai

from diary.forms import ProfileForm
from diary.models import Post, Calendar, Profile


# 이따
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post_title = post.title
    calendar_data = Calendar.objects.all()

    post.delete()

    return redirect('list')


def item(request):
    dateDay = request.POST.get('dateDay')
    selMonth = request.POST.get('selMonth')
    context = {
        'Day': dateDay,
        'Month': selMonth
    }

    return HttpResponse(json.dumps(context), content_type="application/json")


class PostCreate(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content', 'mood']

    def form_valid(self, form):
        current_user = self.request.user
        data_param = self.request.GET.get('data')
        print(data_param)
        if data_param:
            data_dict = json.loads(data_param)
            date_json = data_dict.get('data')
            calendar_data = json.dumps(date_json)

            form.instance.calendar = calendar_data
            form.instance.author = current_user

            if form.is_valid():
                post = form.save(commit=False)
                post.mood = form.cleaned_data['mood']
                post.user = current_user
                post.date = datetime.strptime(date_json, '%Y-%m-%d').date()
                post.save()

                # Create and save calendar data for the post
                title = form.cleaned_data.get('title')
                data = {
                    'date': date_json,
                    'content': title,
                }
                calendar_data = Calendar(date=data['date'], content=data['content'], post=post)
                calendar_data.user = current_user
                calendar_data.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('calendar')


class PostList(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-pk'
    template_name = 'post_list.html'

    def get_queryset(self):
        print(self.kwargs)
        queryset = super().get_queryset()
        current_user = self.request.user
        if self.kwargs['mood'] == "all":
            queryset = queryset.filter(user=current_user)
        else:
            queryset = queryset.filter(user=current_user, mood=self.kwargs['mood'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['current_user'] = current_user
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        return context


@login_required
def calendar(request):
    current_user = request.user
    calendar_items = Calendar.objects.filter(user=current_user)
    citem_list = []
    for item in calendar_items:
        citem_list.append({
            'date': item.date.strftime("%Y-%m-%d"),
            'content': item.content
        })
    return render(request, 'diary/calendar.html', {'citem_list': citem_list})


@login_required
def update_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'diary/update_profile.html', {'form': form})


@login_required()
def detail_profile(request):

    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # 프로필이 없는 경우 새로운 프로필 생성
        profile = Profile.objects.create(user=request.user)

    context = {
        "profile": profile
    }

    return render(request, 'diary/profile_detail.html', context)

# @csrf_exempt
# def save_event(request):
#     if request.method == 'POST':
#         event_date = request.POST.get('eventDate')
#         event_content = request.POST.get('eventContent')
#
#
#
#     return HttpResponse('잘못된 요청입니다.')
