import streamlit as st
import base64
from PIL import Image
from src.cnnClassifier.utils.common import decodeImage
from src.cnnClassifier.pipeline.prediction import PredictionPipeline
import os


# Set up environment variables
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# Initialize the app
st.title("Kidney Tumor Detector App")

# ClientApp class to manage prediction pipeline
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# Instantiate ClientApp
clApp = ClientApp()

# Main app content
st.header("Upload an Image for Prediction")

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Save the uploaded image locally
    with open(clApp.filename, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Predict button
    if st.button("Predict"):
        try:
            # Run prediction pipeline
            result = clApp.classifier.predict()

            # Interactive display of the result
            st.success("Prediction Successful!")
            st.write("### Predicted Results:")

            # Display results based on the type of output
            if isinstance(result, dict):
                for key, value in result.items():
                    st.write(f"- **{key}:** {value}")
            elif isinstance(result, list):
                for idx, value in enumerate(result):
                    st.write(f"- **Prediction {idx + 1}:** {value}")
            else:
                st.write(f"- **Result:** {result}")

        
        except Exception as e:
            st.error(f"Error during prediction: {e}")
else:
    st.info("Please upload an image to start the prediction.")
