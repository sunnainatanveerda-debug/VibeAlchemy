
import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


st.markdown(
    """
    <style>
    /* Page background */
    .stApp {
        background: linear-gradient(135deg, #EAF5E9, #DCEEDC);
    }

    /* Page width and spacing */
    .block-container {
        max-width: 1200px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    /* Main title */
    h1 {
        color: #123F2A !important;
        font-size: 46px !important;
        font-weight: 800 !important;
    }

    /* Subtitle and headings */
    h2, h3 {
        color: #145A32 !important;
        font-weight: 700 !important;
    }

    /* General text */
    p, li {
        color: #365C48 !important;
        font-size: 16px;
    }

    /* Input labels */
    .stTextInput label,
    .stSelectbox label {
        color: #14532D !important;
        font-size: 15px !important;
        font-weight: 600 !important;
    }

    /* Input fields */
    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
        border: 1px solid #C8DEC9 !important;
    }

    /* White card containers */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF;
        border: 1px solid #D5E8D8;
        border-radius: 18px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(20, 90, 50, 0.07);
    }

    
    /* Buttons */
    .stButton > button {
        background-color: #14532D !important;
        color: #FFFFFF !important;
        border: 2px solid #14532D !important;
        border-radius: 12px !important;
        padding: 12px 25px !important;
        font-size: 16px !important;
        font-weight: 700 !important;
    }

    .stButton > button p,
    .stButton > button span {
        color: #FFFFFF !important;
    }

    .stButton > button:hover {
        background-color: #0B3D25 !important;
        border-color: #0B3D25 !important;
        color: #FFFFFF !important;
    }


    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="VibeAlchemy",
    page_icon="✨",
    layout="wide",
)

st.title("✨ VibeAlchemy")
st.subheader("Turn Cultural Vibes Into Business Ideas")
st.write(
    "Discover cultural connections for your café, pop-up shop, "
    "dessert business, or small retail brand using Qloo."
)


st.divider()
st.header("Tell us about your business")

business_type = st.selectbox(
    "What are you planning to create?",
    ["Café", "Pop-up shop", "Dessert business", "Small retail brand"],
)
location = st.text_input("Business location", placeholder="Lahore, Pakistan")
audience = st.text_input(
    "Who is your target audience?",
    placeholder="University students aged 18–25",
)
budget = st.selectbox(
    "Approximate starting budget",
    ["Under $500", "$500–$2,000", "$2,000–$5,000", "$5,000+"],
)
vibe = st.selectbox(
    "What atmosphere do you want?",
    [
        "Cozy and relaxed",
        "Modern and minimalist",
        "Creative and artistic",
        "Energetic and social",
        "Elegant and premium",
    ],
)
cultural_anchor = st.text_input(
    "Name a musician, artist, film, food, or brand your audience likes",
    placeholder="Taylor Swift",
)

if st.button("Discover cultural connections", type="primary"):
    api_key = os.getenv("QLOO_API_KEY")

    if not api_key:
        st.error(
            "Qloo API key not found. Check that your .env file exists."
        )

    elif not cultural_anchor.strip():
        st.warning(
            "Please enter a cultural anchor, such as Taylor Swift."
        )

    else:
        with st.spinner("Discovering cultural connections..."):
            try:
                # Step 1: Search for the cultural anchor
                response = requests.get(
                    "https://hackathon.api.qloo.com/search",
                    headers={"X-Api-Key": api_key},
                    params={
                        "query": cultural_anchor.strip(),
                        "take": 5,
                    },
                    timeout=20,
                )

                response.raise_for_status()
                data = response.json()

                # Step 2: Extract search results
                results = data.get("results", [])

                if isinstance(results, dict):
                    results = results.get("entities", [])

                if not results:
                    st.warning("No Qloo search results found.")

                else:
                    # Step 3: Remove duplicate search results
                    unique_results = []
                    seen_entity_ids = set()
                    seen_names = set()

                    for result in results:
                        result_id = result.get("entity_id")
                        result_name = result.get("name", "Unknown")
                        normalized_name = result_name.strip().lower()

                        if (
                            result_id not in seen_entity_ids
                            and normalized_name not in seen_names
                        ):
                            unique_results.append(result)

                            if result_id:
                                seen_entity_ids.add(result_id)

                            seen_names.add(normalized_name)

                    results = unique_results

                    # Step 4: Get the first unique result
                    selected_entity = results[0]
                    entity_id = selected_entity.get("entity_id")
                    entity_name = selected_entity.get("name", "Unknown")

                    if not entity_id:
                        st.warning("Qloo did not return an entity ID.")

                    else:
                        st.success(
                            f"Qloo entity identified: {entity_name}"
                        )

                        # Step 5: Request cultural insights
                        insights_params = {
                            "filter.type": "urn:entity:artist",
                            "signal.interests.entities": entity_id,
                            "take": 5,
                        }

                        insights_response = requests.get(
                            "https://hackathon.api.qloo.com/v2/insights",
                            headers={
                                "X-Api-Key": api_key,
                                "Accept": "application/json",
                            },
                            params=insights_params,
                            timeout=30,
                        )

                        insights_response.raise_for_status()
                        insights_data = insights_response.json()

                        
                        
                        # Step 6: Display business brief
                        st.subheader("Your Business Brief")

                        display_location = location.strip().title()
                        display_anchor = cultural_anchor.strip().title()

                        display_audience = audience.strip()

                        if display_audience.lower() == "student":
                            display_audience = "Students"
                        elif display_audience.lower() == "university student":
                            display_audience = "University students"
                        elif display_audience.lower().startswith("university student aged"):
                            display_audience = display_audience.replace(
                                "university student aged",
                                "university students aged",
                                1
                            )

                        display_budget = budget.replace("$", r"\$").strip()

                        st.write(f"**Business type:** {business_type}")
                        st.write(f"**Location:** {display_location}")
                        st.write(f"**Target audience:** {display_audience}")
                        st.write(f"**Starting budget:** {display_budget}")
                        st.write(f"**Cultural anchor:** {display_anchor}")

                        # Step 7: Display unique search results
                        st.subheader("Qloo Search Results")

                        for result in results:
                            st.write(
                                result.get("name", "Unnamed result")
                            )

                        # Step 8: Display cultural insights
                        st.subheader("Cultural Connections from Qloo")

                        entities = insights_data.get(
                            "results", {}
                        ).get("entities", [])

                        if entities:
                            for entity in entities:
                                properties = entity.get("properties", {})

                                with st.expander(
                                    entity.get("name", "Unknown")
                                ):
                                    st.write(
                                        "**Description:**",
                                        properties.get(
                                            "description", "Not available"
                                        )
                                    )

                                    st.write(
                                        "**Genres:**",
                                        ", ".join(
                                            properties.get(
                                                "primary_genres", []
                                            )
                                        )
                                    )

                                    st.write(
                                        "**Themes:**",
                                        ", ".join(
                                            properties.get(
                                                "lyrical_themes", []
                                            )
                                        )
                                    )

                                    st.write(
                                        "**Known for:**",
                                        properties.get(
                                            "known_for", "Not available"
                                        )
                                    )
                        else:
                            st.warning(
                                "No cultural connections were returned."
                            )

                        
                        # Step 9: Generate a personalized business concept
                        st.divider()

                        st.subheader(f"Your AI {business_type.title()} Concept")

                        # Generate a personalized concept name
                        anchor_name = cultural_anchor.strip().title()

                        if business_type.lower() == "café":
                            concept_name = f"The {anchor_name} Café Studio"
                        elif business_type.lower() == "pop-up shop":
                            concept_name = f"The {anchor_name} Pop-Up"
                        elif business_type.lower() == "dessert business":
                            concept_name = f"The {anchor_name} Dessert Studio"
                        elif business_type.lower() == "small retail brand":
                            concept_name = f"The {anchor_name} Collection"
                        else:
                            concept_name = f"The {anchor_name} Experience"

                        st.markdown("### Concept Name")
                        st.write(concept_name)


                        
                        st.markdown("### Concept Description")

                        first_word = vibe.strip().lower().split()[0]
                        article = "An" if first_word[0] in "aeiou" else "A"

                        st.write(
                            f"{article} {vibe.lower()} {business_type.lower()} in {display_location}, "
                            f"designed for {display_audience.lower()}. With a starting budget of {display_budget}, "
                            f"the concept takes inspiration from {display_anchor} and the "
                            "audience's cultural interests, creating an affordable and "
                            "welcoming experience."
                        )

                        # Step 10: Use Qloo cultural signals
                        cultural_genres = []
                        cultural_themes = []

                        for entity in entities:
                            properties = entity.get("properties", {})
                            cultural_genres.extend(
                                properties.get("primary_genres", [])
                            )
                            cultural_themes.extend(
                                properties.get("lyrical_themes", [])
                            )

                        # Cultural Inspiration
                        st.markdown("### Cultural Inspiration")

                        col1, col2 = st.columns(2)

                        with col1:
                            st.markdown("#### 🎵 Related Genres")
                            if cultural_genres:
                                unique_genres = list(dict.fromkeys(cultural_genres))
                                for genre in unique_genres[:5]:
                                    st.info(genre)
                            else:
                                st.write("No genre information available.")

                        with col2:
                            st.markdown("#### ✨ Cultural Themes")
                            if cultural_themes:
                                unique_themes = list(dict.fromkeys(cultural_themes))
                                for theme in unique_themes[:5]:
                                    st.success(theme)
                            else:
                                st.write("No cultural themes available.")
                                                # Step 11: Business-specific recommended experience
                        st.markdown("### Recommended Experience")

                        if business_type.lower() == "café":
                            if "cozy" in vibe.lower():
                                recommendations = [
                                    "Comfortable seating and warm lighting",
                                    "Affordable coffee and snack options",
                                    "Quiet study-friendly corners",
                                    "Small group gathering spaces",
                                ]
                            elif "modern" in vibe.lower():
                                recommendations = [
                                    "Minimalist furniture and clean interiors",
                                    "Modern coffee counter and menu design",
                                    "Comfortable spaces for studying",
                                    "Instagram-friendly café corners",
                                ]
                            else:
                                recommendations = [
                                    "Attractive café interior",
                                    "Signature drinks and snacks",
                                    "Comfortable customer seating",
                                    "Friendly customer service",
                                ]

                        elif business_type.lower() == "pop-up shop":
                            recommendations = [
                                "Eye-catching temporary shop display",
                                "Creative product presentation",
                                "Interactive customer activities",
                                "Photo-friendly shopping area",
                            ]

                        elif business_type.lower() == "dessert business":
                            recommendations = [
                                "Attractive dessert display",
                                "Elegant and hygienic packaging",
                                "Signature dessert collections",
                                "Gift boxes and special occasion offers",
                            ]

                        elif business_type.lower() == "small retail brand":
                            recommendations = [
                                "Creative product displays",
                                "Consistent brand colors and packaging",
                                "Personalized product collections",
                                "Social-media-friendly product photography",
                            ]

                        else:
                            recommendations = [
                                "Attractive product presentation",
                                "Affordable customer offers",
                                "Friendly customer service",
                                "Social media promotion",
                            ]

                        for recommendation in recommendations:
                            st.write(f"• {recommendation}")

                        # Step 12: Generate business-specific product ideas
                        st.divider()

                        if business_type.lower() == "café":
                            st.subheader("Affordable Café Menu")
                            recommendations_list = [
                                "Classic Coffee — $2",
                                "Iced Coffee — $2.50",
                                "Chocolate Milkshake — $3",
                                "French Fries — $2",
                                "Chicken Sandwich — $3.50",
                                "Chocolate Brownie — $2",
                            ]

                        elif business_type.lower() == "pop-up shop":
                            st.subheader("Pop-Up Shop Product Ideas")
                            recommendations_list = [
                                "Taylor Swift-inspired friendship bracelets",
                                "Creative art prints and posters",
                                "Personalized tote bags",
                                "Handmade bookmarks",
                                "Music-inspired stickers",
                                "Custom gift boxes",
                            ]

                        elif business_type.lower() == "dessert business":
                            st.subheader("Dessert Menu Ideas")
                            recommendations_list = [
                                "Chocolate brownies",
                                "Mini cheesecakes",
                                "Cupcakes with custom toppings",
                                "Chocolate-dipped strawberries",
                                "Cookie gift boxes",
                                "Affordable dessert combo boxes",
                            ]

                        elif business_type.lower() == "small retail brand":
                            st.subheader("Retail Product Ideas")
                            recommendations_list = [
                                "Personalized tote bags",
                                "Minimalist accessories",
                                "Custom notebooks and stationery",
                                "Aesthetic phone cases",
                                "Creative gift items",
                                "Personalized merchandise",
                            ]

                        else:
                            st.subheader("Small Business Ideas")
                            recommendations_list = [
                                "Affordable personalized products",
                                "Creative customer experiences",
                                "Social media promotions",
                                "Student-friendly offers",
                            ]

                        for item in recommendations_list:
                            st.write(f"• {item}")
                        
                        # Step 13: Download Business Concept Report
                        st.divider()
                        st.subheader("Download Your Business Report")

                        report_content = f"""
VIB EALCHEMY - BUSINESS CONCEPT REPORT

BUSINESS BRIEF
Business Type: {business_type}
Location: {display_location}
Target Audience: {display_audience}
Starting Budget: {budget}
Cultural Anchor: {display_anchor}

CONCEPT NAME
{concept_name}

CONCEPT DESCRIPTION
A {vibe.lower()} {business_type.lower()} in {display_location},
designed for {display_audience.lower()}.
Inspired by {display_anchor} and the audience's cultural interests.

CULTURAL CONNECTIONS
{chr(10).join([entity.get("name", "Unknown") for entity in entities])}

RELATED GENRES
{chr(10).join(list(dict.fromkeys(cultural_genres))[:5])}

CULTURAL THEMES
{chr(10).join(list(dict.fromkeys(cultural_themes))[:5])}

RECOMMENDED EXPERIENCE
{chr(10).join(recommendations)}

PRODUCT OR MENU IDEAS
{chr(10).join(recommendations_list)}

Generated by VibeAlchemy
Powered by Qloo cultural insights.
"""

                        st.download_button(
                            label="📥 Download Business Report",
                            data=report_content,
                            file_name="VibeAlchemy_Business_Report.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
    
            except requests.exceptions.RequestException as e:
                st.error(f"Qloo API request failed: {e}")

            except (ValueError, AttributeError, TypeError) as e:
                st.error(f"Could not process Qloo response: {e}")
