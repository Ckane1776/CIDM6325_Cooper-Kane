from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BlogPost, Category
from .forms import BlogPostForm, CategoryForm

class BlogPostListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'myblog/blog_view.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  # Get the search query from the request
        if query:
            queryset = queryset.filter(title__icontains=query)  # Filter by title
        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):  # Check if the request is from HTMX
            return render(self.request, 'myblog/partials/blog_list.html', context)
        return super().render_to_response(context, **response_kwargs)

class BlogPostCreateView(PermissionRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'myblog/blog_form.html'
    permission_required = 'myblog.add_blogpost'
    success_url = '/blog/'  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        # Check if there are any categories
        if not Category.objects.exists():
            # Redirect to category creation page if no categories exist
            return redirect(reverse('category_create'))
        return super().dispatch(request, *args, **kwargs)

class BlogPostUpdateView(PermissionRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'myblog/blog_form.html'
    permission_required = 'myblog.change_blogpost'
    success_url = '/blog/'

    def form_valid(self, form):
        if self.request.headers.get('HX-Request'):  # Check if the request is from HTMX
            self.object = form.save()
            return render(self.request, 'myblog/partials/blog_item.html', {'post': self.object})
        return super().form_valid(form)

class BlogPostDeleteView(PermissionRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'myblog/blog_confirm_delete.html'
    permission_required = 'myblog.delete_blogpost'
    success_url = '/blog/'

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'myblog/category_list.html'
    context_object_name = 'categories'

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):  # Check if the request is from HTMX
            return render(self.request, 'myblog/partials/category_list.html', context)
        return super().render_to_response(context, **response_kwargs)

class CategoryCreateView(PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'myblog/category_form.html'
    permission_required = 'myblog.add_category'
    success_url = '/categories/'

class CategoryUpdateView(PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'myblog/category_form.html'
    permission_required = 'myblog.change_category'
    success_url = '/categories/'

class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    model = Category
    template_name = 'myblog/category_confirm_delete.html'
    permission_required = 'myblog.delete_category'
    success_url = '/categories/'

def get_queryset(self):
    queryset = super().get_queryset()
    query = self.request.GET.get('q')  # Get the search query from the request
    if query:
        queryset = queryset.filter(title__icontains=query)  # Filter by title
    return queryset