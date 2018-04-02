from django.shortcuts import render, get_object_or_404
from tracking.models import PostForm, Post, Review
from django.http import HttpResponseRedirect
from django.urls import reverse
import json



# Create your views here.

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
def postview(request,pid):
    try:
        post = Post.objects.get(pk=pid)
        if post.user_id != request.user.id:
            return render(request,'tracking/pagenotfound.html')
    except:
        return render(request,'tracking/pagenotfound.html')
    return render(request,'tracking/submissiondetail.html',{"post":post}) 

def ajaxcreatereview(request,pid):
    if request.method == 'POST' and request.is_ajax():
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
        return render(request, 'tracking/createreview.html', {'review':review, 'pid':pid})

def reviewPage(request, pid):
        post = get_object_or_404(Post, id=pid)
        review = Review.objects.filter(post=post)
        return render(request, 'tracking/reviewpage.html', {'post':post, 'review':review})

