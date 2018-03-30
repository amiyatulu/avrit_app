from django.shortcuts import render, get_object_or_404
from tracking.models import PostForm, Post, Review
from django.http import HttpResponseRedirect
from django.urls import reverse



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
	if request.POST and request.is_ajax():
		graphics = request.POST['graphics']
		concrete = request.POST['concrete']
		probing = request.POST['probing']
		elaboration = request.POST['elaboration']
		solved_problems = request.POST['solved_problems']
		practice = request.POST['practice']
		originality = request.POST['originality']
		typo_errors = request.POST['typo_errors']
		deepness = request.POST['deepness']
		comprehensible = request.POST['comprehensible']
		overall_comments = request.POST['overall_comments']
		dat_link = request.POST['dat_link']
		if not graphics and not concrete and not probing and not elaboration and not solved_problems and not practice and not originality and not typo_errors and not deepness and not comprehensible and not overall_comments:
			return render(request,'tracking/pagenotfound.html')	
		else:
			review = Review(submission_id=pid, user=request.user, graphics=graphics, concrete=concrete, probing=probing, elaboration=elaboration, solved_problems=solved_problems, practice=practice, originality=originality, typo_errors=typo_errors, deepness=deepness, comprehensible=comprehensible, overall_comments=overall_comments)
			review.save()
		return render(request, 'tracking/createreview.html', {'review':review, 'pid':pid})

def reviewPage(request, pid):
	    post = get_object_or_404(Post, id=pid)
	    review = Review.objects.filter(post=post)
	    return render(request, 'tracking/reviewpage.html', {'post':post, 'review':review})

