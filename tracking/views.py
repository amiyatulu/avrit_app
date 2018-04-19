from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.sites.shortcuts import get_current_site
from tracking.models import PostForm, Post, Review
from tracking.forms import SignUpForm, ProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import json
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from tracking.tokens import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers



# Create your views here.
def home(request):
    return render(request, 'tracking/home.html')

@login_required
def postSubmission(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            subform = form.save(commit=False)
            subform.user = request.user
            subform.save()
            

            return HttpResponseRedirect(reverse('tracking:postview',kwargs={'pid':subform.id}))
    else:
        form = PostForm()
    return render(request,'tracking/post.html',{'form':form,
                                                       })

@login_required
def postview(request,pid):
    post = get_object_or_404(Post, pk=pid)
    if post.user_id == request.user.id:
        return render(request,'tracking/submissiondetail.html',{"post":post})
    else:
        return render(request,'tracking/pagenotfound.html') 
    
        

@login_required
def ajaxcreatereview(request,pid):
    post = get_object_or_404(Post, pk=pid)
    if post.user_id == request.user.id:
        return render(request,'tracking/pagenotfound.html')
    elif request.method == 'POST' and request.is_ajax():
        data = json.loads(request.body)
        print(data)
        graphics = data.get('graphics')
        concrete = data.get('concrete')
        probing = data.get('probing')
        elaboration = data.get('elaboration')
        solved_problems = data.get('solved_problems')
        practice = data.get('practice')
        originality = data.get('originality')
        errors = data.get('errors')
        deepness = data.get('deepness')
        preciseness = data.get('preciseness')
        cognitive_load = data.get('cognitive_load')
        big_ideas = data.get('big_ideas')
        evidence = data.get('evidence')
        overall_comments = data.get('overall_comments')
        dat_link = data.get('dat_link')
        backup_link = data.get('backup_link')
        if not graphics and not concrete and not probing and not elaboration and not solved_problems and not practice and not originality and not errors and not deepness and not preciseness and not cognitive_load and not big_ideas and not evidence and not overall_comments:
            return render(request,'tracking/pagenotfound.html') 

        else:
            review, created = Review.objects.update_or_create(
                post_id = pid,
                user=request.user,
                defaults={
                "graphics":graphics, "concrete": concrete, "probing": probing, "elaboration": elaboration, "solved_problems": solved_problems, "practice": practice, "originality": originality, "errors": errors, "deepness": deepness, "preciseness": preciseness, "cognitive_load": cognitive_load, "big_ideas": big_ideas, "evidence": evidence, "overall_comments": overall_comments,"dat_link": dat_link, "backup_link": backup_link
                }
                )
            print(created)
            print(review)
        return render(request, 'tracking/viewreview.html', {'review':review, 'pid':pid})


@login_required
def reviewPage(request, pid):
    post = get_object_or_404(Post, id=pid)
    review = Review.objects.filter(post=post)
    userexitsquery = review.filter(user=request.user)
    if userexitsquery:
        userexists = True
    else:
        userexists = False
    print(post.user_id)
    print(request.user.id)
    print(userexists)
    return render(request, 'tracking/reviewpage.html', {'post':post, 'reviewlist':review, 'userexists': userexists})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, prefix="usr")
        profile_form = ProfileForm(request.POST, prefix='loc')
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user._bio = profile_form.cleaned_data['bio']
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('tracking/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('tracking:account_activation_sent')
    else:
        form = SignUpForm(prefix="usr")
        profile_form = ProfileForm(prefix='loc')
    return render(request, 'tracking/signup.html', {'form': form, 'profile_form': profile_form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('tracking:home')
    else:
        return render(request, 'tracking/account_activation_invalid.html')

def account_activation_sent(request):
    return render(request, 'tracking/account_activation_sent.html')


def getReview(request, rid):
    review = get_object_or_404(Review, id=rid)
    data = serializers.serialize("json", [review,] )
    return HttpResponse(data)


def htmlreviewform(request):
    return render(request, 'tracking/review_form.html')