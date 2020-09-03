from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
import scrape_mars

# Create connection variable
#conn = 'mongodb://localhost:27017'
#client =  pymongo.MongoClient(conn)
#db=client.mars_db

# Create an instance of Flask
app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
   mars= mongo.db.collection.find_one()
   return render_template("index.html", mars=mars)

# Route that will trigger the scrape function
@app.route('/scrape')
def scrape():
    # Run the scrape function

    mars=mongo.db.mars
    mars_data=scrape_mars.scrape()
    mars.update(
        {}, 
        mars_data,
        upsert=True)
    return index()    
    #return redirect("/")

    #db.mars_db.insert(scrape_mars.scrape())
    #return jsonify(scrape_mars.scrape())
    # Redirect back to home page
    
    #return "Scrapped Data"

if __name__ == "__main__":
    app.run(debug=True)