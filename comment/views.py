from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from .models import Comment
from .forms import CommentForm

# 新建的urls要在总urls里面添加设置
# 得到前端传递的值
def update_comment(request):
    '''
    # 处理完给前端返回一个页面  重定向(不跳转到新的页面,回到原来的页面)
    referer = request.META.get('HTTP_REFERER', reverse('home'))

    # 数据检查
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message': '用户未登录', 'referer_to': referer})
    text = request.POST.get('text', '').strip()  # 去重空格
    if text == '':  # 前端判断不可信原则(容易被绕过) 所以后台这里还是要进行判断
        return render(request, 'error.html', {'message': '评论内容为空', 'referer_to': referer})
    try:
        content_type = request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))  # from传递都是str类型的 强制转换一下
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except Exception as e:
        return render(request, 'error.html', {'message': '评论X对象不存在', 'referer_to': referer})

    # 检查通过,保存数据
    comment = Comment()
    comment.user = request.user
    comment.text = text
    # 等同于Blog.objects.get(pk=object_id)
    comment.content_object = model_obj
    comment.save()
    return redirect(referer)
    '''

    referer = request.META.get('HTTP_REFERER', reverse('home'))
    comment_form = CommentForm(request.POST, user=request.user)

    if comment_form.is_valid():
        # 检查通过,保存数据
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        # 等同于Blog.objects.get(pk=object_id)
        comment.content_object = comment_form.cleaned_data['content_object']
        comment.save()
        return redirect(referer)
    else:
        return render(request, 'error.html', {'message': comment_form.errors, 'redirect_to': referer})
