from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


def create_message(request):
    messages.set_level(request, 0)
    messages.add_message(request, messages.ERROR, "In che vazie mobin!")
    messages.info(request, "Info Mobin!", 'high-priority')
    messages.debug(request, "x=Mobin")
    messages.success(request, "Yes Mobin!!")
    messages.warning(request, "Oh Mobin!", extra_tags='high-priority')
    messages.add_message(request, 44, "Akbar!!")
    return HttpResponse("New messages created!")


@api_view(['GET'])
def view_message(request):
    from app5.serializers import MessageSerializer
    storage = messages.get_messages(request)  # Cookie, Session!
    msgs = list(storage)
    msg_serializer = MessageSerializer(msgs, many=True)

    return Response(msg_serializer.data)
