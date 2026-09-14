def details(name , *details,**metaData):
    print(f"Name: {name}")
    print("Details:", details)
    print("Metadata:", metaData)

details("Tanveer", 38, 12, is_developer=True,skills=["Python","javascript"], location="India")