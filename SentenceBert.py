from sentence_transformers import SentenceTransformer, util
import torch

model = SentenceTransformer("all-MiniLM-L6-v2")
    
probabilities = None

def bestMatch(query: str, titles: list) -> int:
    global probabilities
    
    #Get the embeddings of the Query and Titles
    query_embeddings = model.encode(query, convert_to_tensor=True)
    titles_embeddings = model.encode(titles, convert_to_tensor=True)
    
    #Get the cosine scores
    cosine_scores = util.cos_sim(query_embeddings, titles_embeddings)
    #Shape [1, N]
    scores = cosine_scores.squeeze()
    #Get the Probability
    probabilities = torch.softmax(scores, dim=0)
    #Get the index
    best_idx = torch.argmax(probabilities).item()
    
    return best_idx

def bestProb():
    return probabilities.max().item()