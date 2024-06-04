from app import create_app

app = create_app()

# Pass the required route to the decorator
@app.route("/")
def index(): 
    return "Homepage for Website"
    
if __name__ == '__main__':
    app.run(debug=True)
