import requests
import json

def get_recipe_suggestions(ingredient, cuisine, diet):
    api_key = "YOUR_API_KEY" # replace with your Spoonacular API key
    url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&query={ingredient}&cuisine={cuisine}&diet={diet}"
    response = requests.get(url)
    data = json.loads(response.text)
    
    if response.status_code == 200:
        results = data["results"]
        if len(results) > 0:
            suggestions = []
            for result in results:
                title = result["title"]
                image = result["image"]
                url = result["sourceUrl"]
                suggestions.append({"title": title, "image": image, "url": url})
            return suggestions
        else:
            return "No recipes found."
    else:
        return "Error retrieving recipe suggestions."

# Example usage
ingredient = "chicken"
cuisine = "italian"
diet = "ketogenic"
suggestions = get_recipe_suggestions(ingredient, cuisine, diet)
print(suggestions)
