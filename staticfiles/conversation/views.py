from django.shortcuts import render,get_object_or_404, redirect
from market.models import Product
from .models import Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required

@login_required
def new_conversation(request,item_pk):
    item=get_object_or_404(Product,pk=item_pk)

    if item.seller == request.user:
        return redirect('dashboard:index')
    
    conversations=Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form=ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation=Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.seller)
            conversation.save()
            
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            return redirect(conversation_message.get_absolute_url())
    else:
        form=ConversationMessageForm()
    return render(request,'conversation/new.html',{'form':form,'item':item})

@login_required
def inbox(request):
    conversations=Conversation.objects.filter(members__in=[request.user.id])
    return render(request,'conversation/inbox.html',{'conversations':conversations})       



@login_required
def detail(request,pk):
        conversation=Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
        if request.method == 'POST':
             form=ConversationMessageForm(request.POST)
             if form.is_valid():
                  conversation_message=form.save(commit=False)
                  conversation_message.conversation=conversation
                  conversation_message.created_by=request.user
                  conversation_message.save()

                  conversation.save()

                  return redirect('conversation:detail', pk=pk)
             
        else:
           form=ConversationMessageForm()
        context={'conversation':conversation,'form':form}
        return render(request,'conversation/detail.html', context)

