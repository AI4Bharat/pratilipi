from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from video.models import Video
from .serializers import TranscriptSerializer

import requests
import json 

from .models import *
from video.models import Video
from .serializers import TranscriptSerializer

## Utility Functions 
def make_asr_api_call(url, lang):
    try:
        headers = {"Content-Type": "application/json"}
        body = {"url": url, "language": lang}
        request_url = "http://216.48.181.177:5050/transcribe"
        response = requests.post(url=request_url, headers = headers, json = body,verify=False)
        response_data = json.loads(response.content)
        return response_data
    except Exception as e:
        return None

# Define the API views 
@api_view(['GET'])
def create_transcription(request):
    """
    Endpoint to get or generate(if not existing) a transcription for a video
    """
    if "video_id" in dict(request.query_params):
        video_id = request.query_params["video_id"]
        lang = request.query_params["language"]
        transcript = Transcript.objects.filter(video_id__exact = video_id).filter(language=lang)
    else:
        return Response({"message": "missing param : video_id"}, status=status.HTTP_400_BAD_REQUEST)

    if transcript:
        transcript_serializer = TranscriptSerializer(transcript)
        return Response({"data": transcript_serializer.data['payload']}, status=status.HTTP_200_OK)
    else:
        # generate transcript using ASR API
        video = Video.objects.get(pk=video_id)
        transcribed_data = make_asr_api_call(video.url, lang)
        if transcribed_data is not None:
            transcript_obj = Transcript(transcript_type=MACHINE_GENERATED, video=video, language=lang, payload=transcribed_data)
            transcript_obj.save()
            return Response({"data": transcript_obj.payload}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Error while calling ASR API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def retrieve_transcription(request): 
    """
    Endpoint to retrive a transcription for a transcription entry 
    """

    # Check if video_id and language has been passed 
    if "video_id" and "language" in dict(request.query_params):
        video_id = request.query_params["video_id"]
        lang = request.query_params["language"]

        transcript = Transcript.objects.filter(video_id__exact=video_id).filter(language=lang)

        # Check if user has been alloted to this transcript 
        if transcript.user == request.user:
            return Response({"data": transcript.payload}, status=status.HTTP_200_OK)

        else:   
            load_latest_transcript = request.query_params["load_latest_transcript"]
            # Check if the load latest transcript flag is set to true
            if load_latest_transcript == "true":
                return Response({"data": transcript.payload}, status=status.HTTP_200_OK)
            else: 
                return Response({"message": "You are not allowed to load this transcript."}, status=status.HTTP_400_BAD_REQUEST)        
    else:
        return Response({"message": "missing param : video_id or language"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def save_transcription(request):
    """
    Endpoint to save a transcript for a video

    Request body:
    {
        "transcript_id": "",
        "language": "",
        "payload": ""
    }
    """

    # Collect the request parameters
    transcript_id = request.data["transcript_id"]
    language = request.data["language"]
    transcribed_data = request.data["payload"]
    user_id = request.user.id 

    # Retrieve the transcript object 
    try: 
        transcript = Transcript.objects.get(pk=transcript_id)

        # Check if the transcript has a user 
        if transcript.user is None:
            
            # Create a new transcript object with the existing transcript as parent 
            transcript_obj = Transcript(
                transcript_type=MANUALLY_CREATED,
                parent_transcript=transcript,
                video=transcript.video,
                language=language,
                payload=transcribed_data,
                user_id=user_id,
            ) 

            # Save the new transcript object
            transcript_obj.save()
            
            return Response(
                {
                    "data": transcript.payload
                }, 
                status=status.HTTP_200_OK
            )

        else:
            # Update the transcript object with the new payload
            transcript.update(payload=transcribed_data)

    except Transcript.DoesNotExist: 
        return Response({"message": "Transcript Object does not exist Check transcript ID."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_supported_languages(request): 
    """
    Endpoint to get the supported languages for ASR API
    """
    
    # Make a call to the FASTAPI endpoint to get the list of supported languages 
    try: 
        headers = {"Content-Type": "application/json"}
        request_url = "http://216.48.182.174:5000/supported_languages" 
        response = requests.get(url=request_url, headers = headers, verify=False)
        response_data = json.loads(response.content)
        return Response({"data": response_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": "Error while calling ASR API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

## Define the Transcript ViewSet
class TranscriptViewSet(ModelViewSet):
    '''
    API ViewSet for the Transcript model.
    Performs CRUD operations on the Video model.
    Endpoint: /transcript/api/
    Methods: GET, POST, PUT, DELETE
    '''
    queryset = Transcript.objects.all()
    serializer_class = TranscriptSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    