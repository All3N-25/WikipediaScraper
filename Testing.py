from WikiScraper import WikiScraper
import json
from sentence_transformers import SentenceTransformer, util
import torch

Start = "President of the United States"
JSON_Directory  = f"JSON/Wikipedia_{Start}"

testing = WikiScraper(Start)
titles = testing.Scraper()
 
json_string = json.dumps(titles)

#Write the JSON file
with open(JSON_Directory, "w") as json_file:
    json.dump(titles, json_file, indent=4)
    
#Read the JSON file
with open(JSON_Directory, "r") as file:
    data_dict = json.load(file)

keys = data_dict.keys()

#print (keys)

#Compare the keys

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "President"
titles_list = list(keys)
embeddings = model.encode(Start)

query_embedding = model.encode(query, convert_to_tensor=True)
title_embeddings = model.encode(titles_list, convert_to_tensor=True)

cosine_scores = util.cos_sim(query_embedding, title_embeddings)
# shape: [1, N]
scores = cosine_scores.squeeze()  # shape: [N]

probabilities = torch.softmax(scores, dim=0)

best_idx = torch.argmax(probabilities).item()

best_title = titles_list[best_idx]
best_score = scores[best_idx].item()
best_prob = probabilities[best_idx].item()

print("Best match:", best_title)
print("Cosine similarity:", best_score)
print("Probability:", best_prob)

top_k = 5
top_results = torch.topk(probabilities, k=top_k)

for idx, prob in zip(top_results.indices, top_results.values):
    print(
        titles_list[idx],
        "| prob =", round(prob.item(), 4),
        "| cosine =", round(scores[idx].item(), 4)
    )

    
print("success")