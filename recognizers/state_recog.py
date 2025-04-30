from presidio_analyzer import PatternRecognizer, Pattern
state_recognizer = PatternRecognizer( supported_entity = "IND_STATE",
                                    deny_list= [
                                    # States
                                    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
                                    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
                                    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
                                    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
                                    "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
                                    "West Bengal",
                                    
                                    # Union Territories
                                    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
                                    "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
                                ]
                                    )