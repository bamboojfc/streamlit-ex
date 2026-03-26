import os
import pandas as pd
import requests
import streamlit as st

# def get_backend_url():
#     return os.environ.get("BACKEND", None)

# def classify_image(image, backend):
#     """Send the image to the backend for classification."""
#     predict_url = f"{backend}/classify/"
#     response = requests.post(predict_url, files={"file": image}, timeout=10)
#     if response.status_code == 200:
#         return response.json()
#     return None

# def main() -> None:
#     """Main function of the Streamlit frontend."""
#     backend = get_backend_url()
#     if backend is None:
#         msg = "Backend service not found"
#         raise ValueError(msg)

#     st.title("My Image Classification App :)")
#     st.write("Nannapas B.")

#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
#         image = uploaded_file.read()
#         result = classify_image(image, backend=backend)

#         if result is not None:
#             prediction = result["prediction"]
#             probabilities = result["probabilities"]
#             imagenet_classes = result["imagenet_classes"]

#             # show the image and prediction
#             st.image(image, caption="Uploaded Image")
#             st.write("Prediction:", prediction)

#             # make a nice bar chart
#             data = {
#                 "Class": [imagenet_classes[i] for i in range(len(probabilities))], 
#                 "Probability": probabilities
#             }
#             df = pd.DataFrame(data)
#             df.sort_values(by="Probability", inplace=True, ascending=False)
#             df.set_index("Class", inplace=True)
#             st.bar_chart(df[:10], y="Probability")
#         else:
#             st.write("Failed to get prediction")

# if __name__ == "__main__":
#     main()
    
    
st.title("My Image Classification App :)")