from django.shortcuts import render
from django.http import HttpResponse
import base64
from io import BytesIO
from PIL import Image
from .forms import TextForm, UploadImageForm

from .utils.utils import *

# Create your views here.

def index(request):
    
    if request.method == "POST":
        
        user_input = TextForm(request.POST)
        
        if user_input.is_valid():
            
            gemini_response = call_text_gemini(user_input)

            # If rate limit reached
            if gemini_response == "api_error":
                error_msg = "We have encountered an error. Please try again shortly."
                return render(request, "latex_converter/index.html", {'error_message': error_msg, 'form': user_input})

            image_b64 = render_latex(gemini_response.replace('\n', ''))

            return render(request, 'latex_converter/index.html', {'gemini_response': gemini_response, 'latex_image': image_b64, "form": TextForm()})

    else:
        user_input = TextForm()

    return render(request, "latex_converter/index.html", {'form': user_input})

def drawer(request):

    if request.method == "POST":

        user_input = request.POST.get("image_data") # Returns string

        if user_input:
            
            # Decode image
            header, encoded = user_input.split(",", 1) # Strip off the "data:image/png;base64," part            
            binary_data = base64.b64decode(encoded) # Decode base64 to binary
            image = Image.open(BytesIO(binary_data)) # Load image into a PIL Image object
            
            gemini_response = call_gemini_api(image)

            # If rate limit reached
            if gemini_response == "api_error":
                error_msg = "We have encountered an error. Please try again shortly."
                return render(request, "latex_converter/drawer.html", {'error_message': error_msg})

            image_b64 = render_latex(gemini_response.replace('\n', ''))

            return render(request, 'latex_converter/drawer.html', {'gemini_response': gemini_response, 'latex_image': image_b64})

    return render(request, "latex_converter/drawer.html")


def uploader(request):

    if request.method == "POST":
        
        user_input = UploadImageForm(request.POST, request.FILES)
        
        if user_input.is_valid():
            
            uploaded_image = request.FILES['image']
            image = Image.open(uploaded_image)

            gemini_response = call_gemini_api(image)

            # If rate limit reached
            if gemini_response == "api_error":
                error_msg = "We have encountered an error. Please try again shortly."
                return render(request, "latex_converter/uploader.html", {'error_message': error_msg})

            image_b64 = render_latex(gemini_response.replace('\n', ''))

            return render(request, 'latex_converter/uploader.html', {'gemini_response': gemini_response, 'latex_image': image_b64, "form": UploadImageForm()})

    else:
        user_input = UploadImageForm()

    return render(request, "latex_converter/uploader.html", {"form": user_input})

def about(request):
    return render(request, 'latex_converter/about.html')

def legal(request):
    return render(request, 'latex_converter/legal.html')

