import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(page_title="Views Reality: The fastest growing real estate marketplace company in America!", page_icon="🏡", layout="wide")

# ---Header-----------------------------------------------------------------------------------------------------
current_directory = os.getcwd()
st.header("Views Realty🏡👀")
# Get the current working directory
current_directory = os.getcwd()

# Specify the file name
file_name = "views_logo.jpg"

# Create the absolute path
absolute_path = os.path.join(current_directory, file_name)

# Open the image using PIL
image = Image.open(absolute_path)

# Display the image using st.image
st.image(image, caption="Views Realty Logo", use_column_width=True)
st.title("Making the perfect view your first person view!")
# ------------------------------------------------------------------------------------------------------------
# House Listing sections
st.write("---")
# Function to initialize or load the property DataFrame
def load_data():
    data = {
        'Address': [],
        'Price': [],
        'Bedrooms': [],
        'Image': [],
        'Description': []  # Add a column for property descriptions
    }
    return pd.DataFrame(data)

# Function to display details of a specific property
def display_property_details(property_data, property_index):
    st.title(f'Details for Property {property_index + 1}')

    # Display main property information
    st.write(f"**Address:** {property_data['Address'][property_index]}")
    st.write(f"**Price:** ${property_data['Price'][property_index]:,.2f}")
    st.write(f"**Bedrooms:** {property_data['Bedrooms'][property_index]}")

    # Display main property image as a clickable thumbnail using st.components.html
    for image_url in property_data['Image'][property_index]:
        st.image(image_url, use_column_width=True, caption="Click to view more details")

    # Show additional details
    st.subheader("Additional Details")
    st.write(property_data['Description'][property_index])

# ---------------------------------------------------------------------------------------------------------------------
# Main function to run the Streamlit app
def main():
    st.title('Real Estate Property Listings:')
    st.write("---")

    # Display 5 properties with images
    property_info = [
        {
            'Address': '123 Main St. San Francisco, CA 94105',
            'Price': 1000000,
            'Bedrooms': 4,
            'Image': [
                '1house.jpg',  
                'house_1_2.jpg',
                'house_1_3.jpg',
                'house_1_4.jpg',
                'house_1_5.jpg'
            ],
            'Description': "A masterpiece of architectural finesse, this 4-bedroom haven in San Francisco radiates charm and luxury. Nestled in a coveted neighborhood, the sun-drenched living areas showcase high ceilings and bespoke fixtures, framing the city skyline. The gourmet kitchen is a culinary enthusiast's dream, adorned with premium finishes. The bedrooms, bathed in natural light, offer a serene retreat, while the master suite boasts a spa-inspired bathroom and a private balcony with panoramic views. The meticulously landscaped backyard oasis beckons, providing a sanctuary of relaxation amid the vibrant urban landscape."
        },    #---------------------------------------------------------------------------------------------
        {
             'Address': '156 Graham Rd. San Francisco, CA 94105',
             'Price': 3500000,
             'Bedrooms': 4,
             'Image': [
                 '2house.jpg',  
                 'house_2_2.jpg',
                 'house_2_3.jpg',
                 'house_2_4.jpg',
                 'house_2_5.jpg'
             ],
             'Description': "Nestled in the heart of San Francisco, this stunning 4-bedroom residence epitomizes modern elegance. A seamless blend of classic architecture and contemporary design, the house boasts panoramic views of the iconic cityscape. The spacious living area features floor-to-ceiling windows, allowing natural light to cascade throughout, illuminating the luxurious hardwood floors. The gourmet kitchen is a chef's dream with state-of-the-art appliances and sleek countertops. Four thoughtfully designed bedrooms offer comfort and tranquility, while the master suite includes a private balcony overlooking the Bay Area. The meticulously landscaped backyard oasis provides a perfect retreat, completing this exquisite San Francisco home."
        },       #-------------------------------------------------------------------------------------
        {
            'Address': '124 Bland Rd. San Francisco, CA 94105',
            'Price': 2000000,
            'Bedrooms': 4,
            'Image': [
                '3house.jpg',  
                'house_3_1.jpg',
                'house_3_2.jpg',
                'house_3_3.jpg',
                'house_3_4.jpg'
            ],
            'Description': "A symphony of elegance and modernity, this 4-bedroom residence in San Francisco stands as a testament to refined living. Perched in an exclusive enclave, the home showcases architectural brilliance and panoramic city views. The expansive living spaces boast bespoke details and floor-to-ceiling windows, inviting the outdoors in. The chef's kitchen, adorned with premium appliances, is a culinary masterpiece. The bedrooms, including a lavish master suite with a private balcony, offer a haven of comfort and tranquility. The meticulously landscaped garden, with its al fresco dining area, completes this urban sanctuary, promising a lifestyle of unparalleled luxury."
        },           #---------------------------------------------------------------------------------------------------------
        {
            'Address': '780 Bleeker St. San Francisco, CA 94105',
            'Price': 1600000,
            'Bedrooms': 4,
            'Image': [
                '4house.jpg',  
                'house_4_1.jpg',
                'house_4_2.jpg',
                'house_4_3.jpg'
            ],
            'Description': "Perched on a prestigious San Francisco hillside, this 4-bedroom gem embodies sophistication. With sweeping vistas of the Golden Gate Bridge, the open-concept living space invites relaxation, adorned with bespoke finishes and an artisanal fireplace. The chef's kitchen boasts top-tier appliances, while the master suite exudes opulence with its spa-like bathroom and private terrace. Impeccable design flows seamlessly into the lush garden oasis, offering a tranquil escape within the bustling city."
        },            #---------------------------------------------------------------------------------------------------
        {
            'Address': '411 Laurel Ave. San Francisco, CA 94105',
            'Price': 1800000,
            'Bedrooms': 4,
            'Image': [
                '5house.jpg',  
                'house_5_1.jpg',
                'house_5_2.jpg',
                'house_5_3.jpg'
            ],
            'Description': "Elevated living meets West Coast sophistication in this exquisite 4-bedroom residence in San Francisco. Commanding attention with its sleek design, the home offers an abundance of natural light and unobstructed city views from every angle. The chef's kitchen, equipped with top-of-the-line appliances, is a culinary masterpiece. Four thoughtfully designed bedrooms provide comfort and style, with the master suite featuring a private terrace overlooking the Bay. The meticulously landscaped outdoor space serves as an entertainer's paradise, creating a seamless blend of modern luxury and the quintessential San Francisco lifestyle."
        }
    ]             #-------------------------------------------------------------------------------------------------------

    for property_data in property_info:
        # Display main property information
        st.title(f'Details for Property: {property_data["Address"]}')
        st.write(f"**Address:** {property_data['Address']}")
        st.write(f"**Price:** ${property_data['Price']:,}")
        st.write(f"**Bedrooms:** {property_data['Bedrooms']}")

        # Display all images for the property
        st.subheader("Additional Images")
        for image_url in property_data['Image']:
            st.image(image_url, use_column_width=True, caption="Click to view more details")

        # Show additional details
        st.subheader("Additional Details")
        st.write(property_data['Description'])

if __name__ == '__main__':
    main()
