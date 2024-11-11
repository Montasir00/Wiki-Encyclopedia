import random
from django.shortcuts import render, redirect
from django.conf import settings
import os
from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, TITLE):
    content = util.get_entry(TITLE)  # Get the content of the entry

    if content is None:
        return render(request, "encyclopedia/error.html", {
            "title": TITLE
        })

    # Convert the Markdown content to HTML
    html_content = markdown2.markdown(content)

    return render(request, "encyclopedia/entry.html", {
        "title": TITLE,
        "content": html_content
    })

def search_results(request):
    query = request.GET.get('q', '')  # Get the search query from the URL
    entries = util.list_entries()
    results = []

    if query:
        # Search for exact match
        if query in entries:
            return redirect('entry_page', TITLE=query)
        
        # Search for partial match (substring match)
        results = [entry for entry in entries if query.lower() in entry.lower()]
    
    return render(request, "encyclopedia/search_results.html", {
        "results": results,
        "query": query
    })

def create_page(request):
    if request.method == "POST":
        title = request.POST.get("title").strip()
        content = request.POST.get("content").strip()
        
        # Check if an entry with this title already exists
        if title.lower() in (entry.lower() for entry in util.list_entries()):
            return render(request, "encyclopedia/create.html", {
                "error": "An entry with this title already exists.",
                "title": title,
                "content": content
            })
        
        # Save the new entry to a Markdown file
        filename = os.path.join(settings.BASE_DIR, 'entries', f"{title}.md")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        
        # Redirect to the new entry's page
        return redirect('entry_page', TITLE=title)
    
    # If GET request, show the form
    return render(request, "encyclopedia/create.html")

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('entry_page', TITLE=random_entry)
