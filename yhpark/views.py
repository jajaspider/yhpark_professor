from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from .models import Professor,Notice
from yhpark.pagingHelper import *
from .forms import Notice_Write
from django.utils import timezone

# Create your views here.
def index(request):
    noticelist = Notice.objects.order_by('-id')[0:5]
    return render_to_response('yhpark/index.html',{'noticelist': noticelist})

def notice_write(request):
    if request.method == 'POST':
        form = Notice_Write(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('notice')
    else:
        form = Notice_Write()
    return render(request, 'yhpark/notice_write.html', {'form': form})

def notice(request):
    boardList = Notice.objects.order_by('-id')[0:5]
    return render_to_response('yhpark/notice.html',{'boardList': boardList})

def notice_datail(request,pk):
    boardList = get_object_or_404(Notice, pk=pk)
    return render(request, 'yhpark/notice_datail.html', {'boardList': boardList})
