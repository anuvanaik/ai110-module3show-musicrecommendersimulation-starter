# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

SimpleMusicRecommender 1.0

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

It recommends song based on the users preferences and it's just for classroom exploration since it only has a small set of music to recommend. Also makes a heavy bias towards genre, and thats what it matters the most to the user.


Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

It scores out of 10 for likeness. Use three catergories: genre, mood, and energy. Genre is 5, mood 3, and energy is 2. Genre is heavily weight. Rates each catergory with energu being a bit different since it accounts for user target energy. It used to be out of 1 which made it less clearer.

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  
It uses a small data set of songs with mood, acoustic, genre, and energy. There are 18 songs in the catalog. Some of the genres there are is lofi, jazz, hip-hop, and more. Some of the moods there are is chill, angry, intense, and more. I didn't use acoustic part for the recommender.
Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

It does give reasonable results and it shows the data much clearly. 


Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 
One weakness I found is that some users will have more advantage then others. People who like lofi or pop have more choices, becaused there is a heavy weight in genre it seems unfair to people whole like hipop or some other genre that has less songs.

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

When I tested the user profile for 

target_energy=5.0 (out of range)
  profile: UserProfile(favorite_genre='metal', favorite_mood='angry', target_energy=5.0, likes_acoustic=False)

It gave me a weird result which one song is scored out of 8 and the rest of the recommendations where scored 0.



1. Case/whitespace mismatch

(Concrete Kingdom is hip-hop song but because the energy matches exactly it provides that top of the list )

2. Nonexistent genre+mood
 
  {genre didn't exist, neither the mood}


3. target_energy=5.0 (out of range)
 
  (energy is out of range so it doesn't contribute anything)


4. target_energy=NaN


(There is no target energy and only relied on genre and mood, so it looked fine on the outside)

5. Perfect-tie cluster (lofi/chill)

  (Since it has a tie it degrades the song to break the tie)
  '''

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  
I would make a better scoring so it provides a clearer scoring result, and I would add more songs to data.
Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience. 

It was much easier compared to the other projects, and I clearly undetsood where I was going with this. The project turned to be simple compared to the other projects.

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
discovered  
- How this changed the way you think about music recommendation apps  
