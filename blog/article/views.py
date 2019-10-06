from django.shortcuts import render


def index(request):
    return render(request, 'article/createArticle.html')


"""class TagCreate(View):
    def get(self, request):
        form = TagForm
        return render(request, 'article/tagCreate.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'article/tagCreate.html', context={'form': bound_form})

"""