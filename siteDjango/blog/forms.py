from django.shortcuts import get_object_or_404, render

from blog.models.post import Post
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content',)


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter().order_by("created_at")
    new_comment = None
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    

    return render(
        request, 
        template_name, 
        {
            "post": post, 
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form
        }
    )