html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>my final project</title>
     <style>
    
    </style>
</head>
<body>

    <h1>My Information</h1>
    <p>Name: Aya ayman al ardah </p>
    <p>Email: aya.alardah25@icloud.com</p>
    <p>Phone: 0776097732</p>
    <p>Address: jijjen, irbid, jordan</p>
    <p>University: Philadelphia unversirty</p>
    <p>Field of Study: Cyber secuirty</p>
    <p>My ambition is to become a professional Ethical Hacker</p>
    <img src="pic.jpg" width=700 height=700></img>
</body>
</html>
"""

file_name = "your_information_page.html"


with open(file_name, "w") as html_file:
    html_file.write(html_content)

print(f"HTML page '{file_name}' has been created with your information.")