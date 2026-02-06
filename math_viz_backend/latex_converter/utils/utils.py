from google import genai
from google.genai import errors 
from django.conf import settings
from PIL import Image
import base64
from io import BytesIO
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')

def call_gemini_api(user_input):
    
    try:

        client = genai.Client(api_key=f"{settings.GEMINI_API_KEY}")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[user_input,
                    ("If the given image is a mathematical text - interpret it properly, convert it to LaTeX, and give me the raw code. If not, return 'Invalid input'\n"
                    "Mathematical text is anything that can be classified as a math expression, equation, formula, or similar\n\n"
                    "Additionally, if the given input includes or requires more than one line of math text or code, also say 'Invalid input', "
                    "Since we can only support one line due to matplotlib's limitations\n\n"
                    "For your output, don't include any explanation or symbols - just raw code. For example, if a user inputted the quadratic formula, you only return this:\n"
                    r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}")],
        )

        return response.text
    
    except errors.APIError as e:

        #return str(e.code)
        return "api_error"

    

def call_text_gemini(user_input):

    try:

        client = genai.Client(api_key=f"{settings.GEMINI_API_KEY}")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(f"{user_input}\n\n"
                    "If the given input above is a mathematical text - interpret it properly, convert it to LaTeX, and give me the raw code. If not, return 'Invalid input'\n"
                    "Mathematical text is anything that can be classified as a math expression, equation, formula, or similar\n\n"
                    "Additionally, if the given input includes or requires more than one line of math text or code, also say 'Invalid input', "
                    "Since we can only support one line due to matplotlib's limitations\n\n"
                    "For your output, don't include any explanation or symbols - just raw code. For example, if a user entered the quadratic formula, you only return this:\n"
                    r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}")
        )

        return response.text
    
    except errors.APIError as e:

        return "api_error"

    
def render_latex(latex_str):

    plt.rcParams.update({
        "mathtext.fontset": "cm",
        "font.family": "serif",
    })

    fig, ax = plt.subplots(figsize=(2, 1))
    ax.text(0.5, 0.5, fr"${latex_str}$", fontsize=20, ha='center', va='center')
    ax.axis('off')

    buffer = BytesIO()
    plt.savefig(buffer, format="png", dpi=100, bbox_inches='tight', transparent=True)
    plt.close()
    buffer.seek(0)

    image_b64 = base64.b64encode(buffer.read()).decode('utf-8')
    return image_b64

def test_api_call(user_input):
    return "api_error"



    
