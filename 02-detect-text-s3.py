import boto3

# Document
s3BucketName = "textract-console-us-east-2-f03713fa-3502-4fcd-b12e-07cdb460cbdd"
documentName = "impuesto.png"

# Amazon Textract client
textract = boto3.client('textract')

# Call Amazon Textract
response = textract.detect_document_text(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': documentName
        }
    })

#print(response)

# Print detected text
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print ('\033[94m' +  item["Text"] + '\033[0m')
