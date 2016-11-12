from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.views.generic import ListView
from django.views.generic.edit import CreateView


#from photos.models import Post
from .models import Post
from .models import Tag
from .forms import PostForm


def create_post(request):
    if request.method == 'GET':
        form = PostForm()
    elif request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()

            tag_text = form.cleaned_data.get('tag','')
            tags = tag_text.split(',')
            for _tag in tags:
                _tag = _tag.strip()
                tag, _ = Tag.objects.get_or_create(name=_tag, defaults={'name': _tag})
                post.tags.add(tag)

            return redirect('photos:view', pk=post.pk)

    ctx = {
        'form':form,
    }
    return render(request, 'edit_post.html', ctx)

'''Class Based View'''
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'

create_post = PostCreateView.as_view()


def list_posts(request):
    try:
        page = int(request.GET.get('page',1))
    except Exception:
        page = 1
    finally:
        if page < 0:
            page = 1

    per_page = 2

    #start_page = (page - 1) * per_page
    #end_page = page * per_page

    #posts = Post.objects.all().order_by('-created_at', '-pk')[start_page:end_page]
    posts = Post.objects.all().order_by('-created_at', '-pk')

    pg = Paginator(posts, per_page)
    try:
        contents = pg.page(page)
    except PageNotAnInteger:
            contents = pg.page(1)
    except EmptyPage:
        contents = []

    ctx = {
        #'posts': posts,
        'posts': contents,
    }

    return render(request, 'list.html', ctx)

'''Class Baesd View'''
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'list.html'
    paginate_by = 2
    #queryset = Post.objects.order_by('id')

    def get_queryset(self):
        return Post.objects.order_by('id')

list_posts = PostListView.as_view()


def view_post(request, pk):

    post = Post.objects.get(pk=pk)
    ctx = {
        'post': post,
    }
    return render(request, 'view.html', ctx)