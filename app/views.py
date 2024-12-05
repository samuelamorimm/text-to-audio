from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from gtts import gTTS
import os
from django.conf import settings
# Create your views here.

@api_view(['POST'])
def text_to_audio(request):
  text = request.data.get('text')

  if not text:
    return JsonResponse({'error': 'Texto não fornecido'}, status=400)
  
  tts = gTTS(text=text, lang='pt')
  caminho_arquivo = os.path.join(settings.MEDIA_ROOT, 'audio.mp3')
  tts.save(caminho_arquivo)

  return JsonResponse({"message": 'Áudio gerado com sucesso', "caminho_arquivo": caminho_arquivo}, status=200)
