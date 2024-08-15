from django.shortcuts import render, get_object_or_404, redirect
from .models import TextSnippet
from .forms import TextSnippetForm

def create_snippet(request):
    if request.method == 'POST':
        form = TextSnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            return redirect('view_snippet', unique_url=snippet.unique_url)
    else:
        form = TextSnippetForm()
    return render(request, 'create_snippet.html', {'form': form})

def view_snippet(request, unique_url):
    snippet = get_object_or_404(TextSnippet, unique_url=unique_url)
    return render(request, 'view_snippet.html', {'snippet': snippet})
