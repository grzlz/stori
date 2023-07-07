from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_lambda_python_alpha as _alambda

)
from constructs import Construct

class StoriCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        resize_lambda = _alambda.PythonFunction(
            self, 'ResizeFunction',
            entry="./lambda/",
            runtime=_lambda.Runtime.PYTHON_3_9,
            index='resize.py',
            handler='resize_function',
        )

        api = apigw.RestApi(self, 'ImageResizeApi',
            rest_api_name='Image Resize',
            description='This service resizes images.'
        )

        resize_image = api.root.add_resource('resizeImage')
        resize_image.add_method('POST', apigw.LambdaIntegration(resize_lambda))
