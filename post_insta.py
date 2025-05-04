import streamlit as st
import pandas as pd
import boto3
import random
from io import BytesIO
random_number=random.randint(1,10000)
s3_client = boto3.client('s3',
    aws_access_key_id="AKIAWUM2ZIAICQ3HOERO",
    aws_secret_access_key="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",
    region_name="eu-central-1",
)
image=st.file_uploader("Upload a image", type=["jpg", "png", "jpeg"])

if image is not None:


    st.image(image, caption="Uploaded Image",width=300)
    caption=st.text_input("Caption for insta")

    button=st.button("Upload to Instagram")
    
    if button:
        data = image.read()
        buf = BytesIO(data)
        buf.seek(0)
    
        s3_client.upload_fileobj(
            Fileobj=buf, 
            Bucket='lydiaphoteke', 
            Key=f'st_image{random_number}.jpg',
            ExtraArgs={
                'Metadata': {
                    'caption': caption  }
                     })

        
    
   
    
        st.success("Image uploaded successfully!")

    
