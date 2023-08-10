
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AddPostForm, AddCommentForm
from .models import MyBlogInfo, Category, Comment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect






class Homepage(ListView):
    model = MyBlogInfo
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = MyBlogInfo
    template_name = 'art-detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        the_likes = get_object_or_404(MyBlogInfo, id=self.kwargs['pk'])
        total_likes = the_likes.total_likes()

        # This block of code is used to effect the unlike post in the article details page
        liked = False
        if the_likes.Likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    

class AddPostView(CreateView):
    model = MyBlogInfo
    template_name = 'add_post.html'
    form_class = AddPostForm
    #fields = '__all__'      # form_class and  filds can not be used together

class UpdatePostView(UpdateView):
    model = MyBlogInfo
    template_name = 'update_post.html'
    form_class = AddPostForm

class DeletePostView(DeleteView):
    model = MyBlogInfo
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



def CategoryView(request, cats):
    category_posts = MyBlogInfo.objects.filter(category=cats.replace('-', ' '))   #.replace('-', ' ') is used to slugify url, i.e remove white space
    # Notice that Blogdata was used here and not Category because we also used Category

    return render(request, 'category.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts}) # .title().replace('-', ' ') replaces the - in the caption(coding-tutorial) with empty space


class AddCategoryView(CreateView):
    model = Category

    #form_class = PostForm

    template_name = 'add_category.html'
    fields = '__all__'


def LikeView(request, pk):
    post = get_object_or_404(MyBlogInfo, id=request.POST.get('post_id'))

    
    # The block of code below is for unliking a post
    liked = False
    if post.Likes.filter(id=request.user.id).exists():
        post.Likes.remove(request.user)
        liked = False
    else:
        post.Likes.add(request.user)
        liked = True
        #post.Likes.add(request.user)
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))


class AddCommentView(CreateView):
    model = Comment
    template_name = 'comment.html'
    form_class = AddCommentForm
    
    #fields = '__all__'      # form_class and  filds can not be used together

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')
