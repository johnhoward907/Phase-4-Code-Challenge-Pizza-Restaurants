from .app import create_app, db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

app = create_app()
with app.app_context():
    db.session.query(RestaurantPizza).delete()
    db.session.query(Restaurant).delete()
    db.session.query(Pizza).delete()

    r1 = Restaurant(name="Kiki's Pizza", address="123 Pizza St")
    r2 = Restaurant(name="Papa Dough", address="456 Dough Blvd")

    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Margherita", ingredients="Basil, Tomato, Cheese")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=15, pizza_id=p2.id, restaurant_id=r1.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("✅ Seeded!")
