from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import PostForm
from django.urls import reverse_lazy
from .models import Post, Category

class RecipeListView(ListView):
    model = Post
    template_name = 'recipes/home.html'
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category', 'All')
        return context

    def get_queryset(self):
        category_name = self.request.GET.get('category')
        if category_name and category_name != 'All':
            return Post.objects.filter(category__name=category_name)
        return Post.objects.all()

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'recipes/detail_post.html'
    context_object_name = 'post'
    login_url = '/login/'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'recipes/create_post.html'
    login_url = '/login/' # Redirect to login if not authenticated

    def form_valid(self, form):
        form.instance.author = self.request.user
        category_new = form.cleaned_data.get('category_new')
        if category_new:
            category, created = Category.objects.get_or_create(name = category_new)
            form.instance.category = category
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs = {"pk" : self.object.pk})
    

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'recipes/update_post.html'
    fields = ['recipe', 'desc', 'image', 'category']
    login_url = '/login/'
    
    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs = {"pk" : self.object.pk})

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'recipes/delete_post.html'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('recipe-home')
    

def About(request):
    return render(request, 'about.html')