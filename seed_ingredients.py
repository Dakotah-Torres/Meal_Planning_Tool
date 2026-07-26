"""
Seed script for the ingredients master list.

Safe to re-run: uses ON CONFLICT (name) DO NOTHING, so running this
multiple times will never create duplicate rows.

Usage:
    uv run python seed_ingredients.py
"""

from sqlalchemy.dialects.postgresql import insert
from db.database import SessionLocal
from db.models import Ingredients

INGREDIENTS = [
    # Produce
    ("Garlic", "clove", "produce"),
    ("Onion", "each", "produce"),
    ("Yellow Onion", "each", "produce"),
    ("Red Onion", "each", "produce"),
    ("Tomato", "each", "produce"),
    ("Roma Tomato", "each", "produce"),
    ("Cherry Tomatoes", "cup", "produce"),
    ("Potato", "each", "produce"),
    ("Sweet Potato", "each", "produce"),
    ("Carrot", "each", "produce"),
    ("Celery", "stalk", "produce"),
    ("Bell Pepper", "each", "produce"),
    ("Red Bell Pepper", "each", "produce"),
    ("Jalapeno", "each", "produce"),
    ("Broccoli", "cup", "produce"),
    ("Cauliflower", "cup", "produce"),
    ("Spinach", "cup", "produce"),
    ("Kale", "cup", "produce"),
    ("Romaine Lettuce", "head", "produce"),
    ("Cucumber", "each", "produce"),
    ("Zucchini", "each", "produce"),
    ("Yellow Squash", "each", "produce"),
    ("Mushroom", "cup", "produce"),
    ("Avocado", "each", "produce"),
    ("Lemon", "each", "produce"),
    ("Lime", "each", "produce"),
    ("Ginger", "tbsp", "produce"),
    ("Cilantro", "cup", "produce"),
    ("Parsley", "cup", "produce"),
    ("Basil", "cup", "produce"),
    ("Green Onion", "stalk", "produce"),
    ("Corn", "ear", "produce"),
    ("Green Beans", "cup", "produce"),
    ("Asparagus", "cup", "produce"),
    ("Banana", "each", "produce"),
    ("Apple", "each", "produce"),
    ("Strawberries", "cup", "produce"),
    ("Blueberries", "cup", "produce"),

    # Protein
    ("Chicken Breast", "lb", "protein"),
    ("Chicken Thigh", "lb", "protein"),
    ("Ground Beef", "lb", "protein"),
    ("Ground Turkey", "lb", "protein"),
    ("Steak", "lb", "protein"),
    ("Pork Chop", "lb", "protein"),
    ("Bacon", "slice", "protein"),
    ("Sausage", "link", "protein"),
    ("Salmon", "lb", "protein"),
    ("Shrimp", "lb", "protein"),
    ("Tilapia", "lb", "protein"),
    ("Tuna", "can", "protein"),
    ("Large Eggs", "each", "protein"),
    ("Tofu", "block", "protein"),
    ("Black Beans", "can", "protein"),
    ("Kidney Beans", "can", "protein"),
    ("Chickpeas", "can", "protein"),
    ("Lentils", "cup", "protein"),

    # Dairy
    ("Whole Milk", "cup", "dairy"),
    ("2% Milk", "cup", "dairy"),
    ("Heavy Cream", "cup", "dairy"),
    ("Butter", "tbsp", "dairy"),
    ("Shredded Cheddar", "cup", "dairy"),
    ("Mozzarella", "cup", "dairy"),
    ("Parmesan", "cup", "dairy"),
    ("Cream Cheese", "oz", "dairy"),
    ("Sour Cream", "cup", "dairy"),
    ("Plain Greek Yogurt", "cup", "dairy"),
    ("Cottage Cheese", "cup", "dairy"),

    # Grains / Pantry
    ("White Rice", "cup", "grains"),
    ("Brown Rice", "cup", "grains"),
    ("Quinoa", "cup", "grains"),
    ("Pasta", "oz", "grains"),
    ("Spaghetti", "oz", "grains"),
    ("Bread", "slice", "grains"),
    ("Flour Tortilla", "each", "grains"),
    ("Corn Tortilla", "each", "grains"),
    ("All-Purpose Flour", "cup", "pantry"),
    ("Sugar", "cup", "pantry"),
    ("Brown Sugar", "cup", "pantry"),
    ("Honey", "tbsp", "pantry"),
    ("Olive Oil", "tbsp", "pantry"),
    ("Vegetable Oil", "tbsp", "pantry"),
    ("Soy Sauce", "tbsp", "pantry"),
    ("Chicken Broth", "cup", "pantry"),
    ("Beef Broth", "cup", "pantry"),
    ("Vegetable Broth", "cup", "pantry"),
    ("Diced Tomatoes", "can", "pantry"),
    ("Tomato Sauce", "can", "pantry"),
    ("Tomato Paste", "tbsp", "pantry"),
    ("Coconut Milk", "can", "pantry"),
    ("Peanut Butter", "tbsp", "pantry"),
    ("Oats", "cup", "pantry"),

    # Seasonings
    ("Salt", "tsp", "seasoning"),
    ("Black Pepper", "tsp", "seasoning"),
    ("Garlic Powder", "tsp", "seasoning"),
    ("Onion Powder", "tsp", "seasoning"),
    ("Paprika", "tsp", "seasoning"),
    ("Cumin", "tsp", "seasoning"),
    ("Chili Powder", "tsp", "seasoning"),
    ("Italian Seasoning", "tsp", "seasoning"),
    ("Oregano", "tsp", "seasoning"),
    ("Red Pepper Flakes", "tsp", "seasoning"),
    ("Cinnamon", "tsp", "seasoning"),
    ("Bay Leaf", "each", "seasoning"),
]


def seed():
    session = SessionLocal()
    try:
        inserted = 0
        for name, default_unit, category in INGREDIENTS:
            stmt = (
                insert(Ingredients)
                .values(name=name, default_unit=default_unit, category=category)
                .on_conflict_do_nothing(index_elements=["name"])
            )
            result = session.execute(stmt)
            if result.rowcount:
                inserted += 1

        session.commit()
        print(f"Seed complete. {inserted} new ingredient(s) inserted out of {len(INGREDIENTS)} defined.")

        total = session.query(Ingredients).count()
        print(f"Total ingredients now in database: {total}")

    except Exception as e:
        session.rollback()
        print(f"Seed failed, rolled back: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    seed()