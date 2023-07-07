import base64
import requests
from PIL import Image
import io

# Open the image file in binary mode, convert it to base64
with open('test.jpg', 'rb') as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

# Make the POST request to the API Gateway endpoint
# Replace this URL with your API Gateway URL
url = "https://nsat8xqwdj.execute-api.us-west-1.amazonaws.com/prod/resizeImage/"
response = requests.post(url, data=img_base64, headers={'Content-Type': 'text/plain'})

# The response should be a string containing the base64-encoded image data
if response.status_code == 200:
    output_img_base64 = response.text
    output_img_data = base64.b64decode(output_img_base64)

    try:
        # Save the output image
        output_img = Image.open(io.BytesIO(output_img_data))
        output_img.save('output.jpg')
    except Exception as e:
        print(f"Error while opening/saving the output image: {str(e)}")
else:
    print(f"Request failed with status {response.status_code}. Error: {response.text}")




