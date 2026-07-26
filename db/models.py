from sqlalchemy import Column, Integer, String, Boolean, Numeric, text, DateTime
from sqlalchemy import ForeignKey, func , Date
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from db.database import Base

class FoodItem(Base):
    __tablename__ = "food_item"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable= False)
    current_quantity = Column(Numeric)
    unit = Column(String)
    sufficient_stock = Column(Boolean, server_default= text("true"), index=True)
    serving_unit = Column(String)
    calories = Column(Numeric)    
    serving_size = Column(Numeric , nullable=True)
    protein_g = Column(Numeric, nullable=True)
    carbs_g = Column(Numeric , nullable=True)
    fat_g = Column(Numeric , nullable=True)
    fiber_g = Column(Numeric , nullable=True)
    sugar_g = Column(Numeric , nullable=True)
    sodium_mg = Column(Numeric , nullable=True)
    
    
class Ingredients(Base):
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key= True)
    name = Column(String, unique=True, nullable=False)
    default_unit = Column(String)
    category = Column(String)
    food_item_id = Column(Integer, ForeignKey("food_item.id"), nullable=True)
    
class Recipes(Base):
    __tablename__ = "recipe"
    id = Column(Integer, primary_key= True)
    name = Column(String, nullable=False)
    instructions = Column(String)
    meal_type = Column(ARRAY(String))
    prep_time = Column(Integer)
    servings = Column(Integer)
    nutrition = Column(JSONB, nullable=True)
    rating = Column(Integer)
    last_used = Column(DateTime(timezone=True), nullable=True)
    times_suggested = Column(Integer, server_default= text("0"))
    times_accepted = Column(Integer, server_default= text("0"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    

class RecipeIngredients(Base):
    __tablename__ = "recipe_ingredient"
    id = Column(Integer, primary_key = True)
    recipes_id = Column(Integer, ForeignKey("recipe.id", ondelete="CASCADE"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredient.id", ondelete="CASCADE"), nullable=False, index=True)
    quantity = Column(Numeric)
    unit = Column(String)
    
class FoodItemPurchases(Base):
    __tablename__ = "food_item_purchases"
    id = Column(Integer, primary_key = True)
    food_item_id = Column(Integer, ForeignKey("food_item.id"), nullable=False, index=True)
    date_purchased = Column(Date, index=True)
    expiration_date = Column(Date, nullable=True)
    quantity_purchased = Column(Numeric)
    unit = Column(String)
    price = Column(Numeric)
    store = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_estimated = Column(Boolean)
    
class MealPlans(Base):
    __tablename__ = "meal_plan"
    id = Column(Integer, primary_key = True)
    week_start = Column(Date)
    week_rating = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    recalc_completed_at = Column(DateTime(timezone=True), nullable=True)
    

class MealPlanEntries(Base):
    __tablename__ = "meal_plan_entries"
    id = Column(Integer, primary_key = True)
    plan_id = Column(Integer, ForeignKey("meal_plan.id", ondelete="CASCADE"), nullable=False, index=True)
    day = Column(Date)
    slot = Column(String)
    recipe_id = Column(Integer, ForeignKey("recipe.id", ondelete="CASCADE"), nullable= False)
    status = Column(String, index=True)
    rejection_note = Column(String, nullable=True)
    suggested_at = Column(DateTime(timezone=True), server_default=func.now())
    decided_at = Column(DateTime(timezone=True), nullable=True)