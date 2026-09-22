import os
import json
import random
from datetime import datetime

DB_PATH = "C:/Users/Administrator/Projects/getlayers-autonomous/data/products.json"

CATEGORIES = ["SaaS", "Fintech", "AI / Tech", "3D Element", "Health / Science", "Portfolio"]
ADJECTIVES = ["Nebula", "Quantum", "Apex", "Vortex", "Horizon", "Prism", "Echo", "Zenith", "Pulse", "Titan"]
NOUNS = ["Matrix", "Flow", "Engine", "Pulse", "Shield", "Core", "Nexus", "Grid", "Vertex", "Wave"]

def load_db():
    if not os.path.exists(DB_PATH):
        return {"templates": [], "scenes": []}
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def generate_autonomous_product():
    db = load_db()
    
    name = f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)}"
    item_id = name.lower().replace(" ", "-")
    category = random.choice(CATEGORIES)
    copies = random.randint(10, 250)
    
    images = [
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1634017839464-5c339ebe3cb4?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80"
    ]
    image = random.choice(images)
    prompt = f"Build a cinematic {category.lower()} web interface for '{name}' featuring high-end dark glassmorphism, responsive layout, and immersive motion."
    
    new_item = {
        "id": item_id,
        "title": name,
        "category": category,
        "copies": copies,
        "image": image,
        "prompt": prompt,
        "created_at": datetime.now().isoformat()
    }
    
    target_list = "scenes" if "Element" in category or "3D" in category else "templates"
    db[target_list].insert(0, new_item)
    
    if len(db[target_list]) > 20:
        db[target_list].pop()
        
    save_db(db)
    print(f"Autonomous Worker: Created new product -> {name} ({category})")

if __name__ == "__main__":
    generate_autonomous_product()
