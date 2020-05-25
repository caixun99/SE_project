from .forms import DynamicForm,CommentForm
from .models import Dynamic,comment,Category
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404
app_name = "market"

def index(request):
    "主页"
    return render(request, 'community/index.html')

def community(request):
    kinds = Category.objects. order_by('name')
    context = {'kinds':kinds}
    return render(request,'community/community.html',context)

#def category(request):
#    content = {'all_category':Category.objects.all()}
#    return render(request,"community/category.html",content)

#显示动态
def dynamics(request,kind_id):
    """显示所有动态"""
    kind = Category.objects.get(id=kind_id)
    dynamics = kind.belong_set.order_by('publish_time')
    context = {'dynamics': dynamics,'kind':kind}
    return render(request, 'community/dynamics.html', context)
#显示一条动态及其评论
def dynamic(request,dynamic_id):
    dynamic = Dynamic.objects.get(id=dynamic_id)
    comments = dynamic.comment.order_by('publish_time')
    context = {'dynamic': dynamic, 'comments': comments}
    return render(request, 'community/dynamic.html', context)
#发布动态
def new_dynamic(request,kind_id):
    kinds = Category.objects.get(id=kind_id)
    if request.method!='POST':
        form = DynamicForm()
    else:
        form = DynamicForm(request.POST,request.FILES)

        if form.is_valid():
            new_dynamic=form.save(commit=False)
            new_dynamic.publisher=request.user
            new_dynamic.save()
            #form.save()
            return HttpResponseRedirect(reverse('market:dynamics',args=[kind_id]))
    context = {'form':form,'kinds':kinds}
    return render(request,'community/new_dynamic.html',context)
def new_comment(request,dynamic_id):
    dynamic = Dynamic.objects.get(id=dynamic_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.Dynamic = dynamic
            new_entry.publisher = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('market:dynamic', args=[dynamic_id]))

    context = {'dynamic': dynamic, 'form': form}
    return render(request, 'community/new_comment.html', context)
@login_required
def edit_comment(request,comment_id):
    comment1 = comment.objects.get(id=comment_id)
    dynamic = comment1.dynamic
    if comment1.publisher!=request.user:
        raise Http404
    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('market:dynamic', args=[dynamic.id]))

    context = {'comment': comment, 'dynamic': dynamic, 'form': form}
    return render(request, 'community/edit_comment.html', context)
