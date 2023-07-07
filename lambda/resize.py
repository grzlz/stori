import base64
import io
from PIL import Image

def resize_function(event, context):
    try:
        # The image is expected to be base64-encoded
        image_data = event['body']
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        # Resize the image
        width, height = image.size
        image = image.resize((width // 2, height // 2))

        # Convert the image back to base64
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")
        buffer.seek(0)
        resized_image_data = base64.b64encode(buffer.read())

        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'image/jpeg' },
            'body': resized_image_data.decode('utf-8'),
            'isBase64Encoded': True
        }
    except Exception as e:
        print(f'Error: {str(e)}')
        return {
            'statusCode': 500,
            'body': str(e)
        }