# Phase-4-Code-Challenge-Pizza-Restaurants
Pizza Restaurant API (Phase 4 Code Challenge)

A RESTful API built with Flask for managing restaurants, pizzas, and their relationships using a many-to-many join model. This project was developed as part of the Flatiron School Phase 4 Flask code challenge.

---

Project Structure

pizza-api/
├── server/
│ ├── app.py
│ ├── config.py
│ ├── seed.py
│ ├── models/
│ │ ├── restaurant.py
│ │ ├── pizza.py
│ │ └── restaurant_pizza.py
│ ├── controllers/
│ │ ├── restaurant_controller.py
│ │ ├── pizza_controller.py
│ │ └── restaurant_pizza_controller.py
├── migrations/
├── pizza.db
├── README.md

 Setup Instructions

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/your-username/pizza-api.git
cd pizza-api
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

nitialize and Migrate the Database
bash
Copy
Edit
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

3. Seed the Database
bash
Copy
Edit
python -m server.seed

3. Seed the Database
bash
Copy
Edit
python -m server.seed

 GET /restaurants/int:id
Returns a single restaurant and its associated pizzas

Success:

json
Copy
Edit
{
  "id": 1,
  "name": "Kiki's Pizza",
  "address": "123 Pizza St",
  "pizzas": [
    {
      "id": 1,
      "name": "Emma",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    }
  ]
}
Error (404):

json
Copy
Edit
{ "error": "Restaurant not found" }

DELETE /restaurants/int:id
Deletes a restaurant and all associated restaurant-pizzas

Success:

204 No Content

Error (404):

json
Copy
Edit


 GET /pizzas
Returns a list of all pizzas

 POST /restaurant_pizzas
Creates a new association between a pizza and a restaurant

 Validation Rules
RestaurantPizza.price must be between 1 and 30, inclusive.

Missing or invalid data returns a 400 Bad Request with helpful error messages.

Technologies Used
Flask

SQLAlchemy

Flask-Migrate

SQLite

Postman (for testing)

Author
John Howard
GitHub: johnhoward907