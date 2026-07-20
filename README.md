# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Based on streaming services such as spotify and youtube, they score than rank the media that the users click on, and they determine using three main methods such as content based flitering, collaborative flitering and Learned ranking models, as they use the user history and implement into those methods inorder to figure out recommendations. However, for this music recommender the feature that is focused for this project will be content based flitering as it will help to match the songs to user preferences much better.

For each song, there will be type of genre, mood of the song, and the energy of the song. For the user profile, there be preferred genre, mood, and energy that will match certain set of features of songs.


Plan:

Genre is the most consider out all of the three features: mood, energy, and genre. SO it is a much heavier weight and there is bias for it. Match points for genre is 5 and for mood is 3, and energy is 2. For similarity points, its 1.00 - (song energy - user target_energy). The samller the gap the more closer to is to the user target energy.


Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded songs: 18

Top Recommendations
========================================

1. Sunrise City (Score: 9.96/10)
----------------------------------------
  - Genre match: pop
  - Mood match: happy
  - Energy similarity: 0.98 (song=0.82, target=0.8)

2. Gym Hero (Score: 6.74/10)
----------------------------------------
  - Genre match: pop
  - Energy similarity: 0.87 (song=0.93, target=0.8)

3. Rooftop Lights (Score: 4.92/10)
----------------------------------------
  - Mood match: happy
  - Energy similarity: 0.96 (song=0.76, target=0.8)

4. Concrete Kingdom (Score: 2.00/10)
----------------------------------------
  - Energy similarity: 1.00 (song=0.8, target=0.8)

5. Night Drive Loop (Score: 1.90/10)
----------------------------------------
  - Energy similarity: 0.95 (song=0.75, target=0.8)
```

```
Loaded songs: 18
============================================================
1. Case/whitespace mismatch
  profile: UserProfile(favorite_genre='Pop', favorite_mood='Happy', target_energy=0.8, likes_acoustic=False)
------------------------------------------------------------
  1. Concrete Kingdom          score=2.000  (Energy similarity: 1.00 (song=0.8, target=0.8))
  2. Sunrise City              score=1.960  (Energy similarity: 0.98 (song=0.82, target=0.8))
  3. Rooftop Lights            score=1.920  (Energy similarity: 0.96 (song=0.76, target=0.8))
  4. Night Drive Loop          score=1.900  (Energy similarity: 0.95 (song=0.75, target=0.8))
  5. Neon Temple               score=1.840  (Energy similarity: 0.92 (song=0.88, target=0.8))

============================================================
2. Nonexistent genre+mood
  profile: UserProfile(favorite_genre='vaporwave', favorite_mood='euphoric', target_energy=0.9, likes_acoustic=True)
------------------------------------------------------------
  1. Storm Runner              score=1.980  (Energy similarity: 0.99 (song=0.91, target=0.9))
  2. Neon Temple               score=1.960  (Energy similarity: 0.98 (song=0.88, target=0.9))
  3. Gym Hero                  score=1.940  (Energy similarity: 0.97 (song=0.93, target=0.9))
  4. Iron Cathedral            score=1.900  (Energy similarity: 0.95 (song=0.95, target=0.9))
  5. Sunrise City              score=1.840  (Energy similarity: 0.92 (song=0.82, target=0.9))

============================================================
3. target_energy=5.0 (out of range)
  profile: UserProfile(favorite_genre='metal', favorite_mood='angry', target_energy=5.0, likes_acoustic=False)
------------------------------------------------------------
  1. Iron Cathedral            score=8.000  (Genre match: metal; Mood match: angry; Energy similarity: 0.00 (song=0.95, target=5.0))
  2. Sunrise City              score=0.000  (Energy similarity: 0.00 (song=0.82, target=5.0))
  3. Midnight Coding           score=0.000  (Energy similarity: 0.00 (song=0.42, target=5.0))
  4. Storm Runner              score=0.000  (Energy similarity: 0.00 (song=0.91, target=5.0))
  5. Library Rain              score=0.000  (Energy similarity: 0.00 (song=0.35, target=5.0))

============================================================
4. target_energy=NaN
  profile: UserProfile(favorite_genre='pop', favorite_mood='happy', target_energy=nan, likes_acoustic=False)
------------------------------------------------------------
  1. Sunrise City              score=8.000  (Genre match: pop; Mood match: happy; Energy similarity: 0.00 (song=0.82, target=nan))
  2. Gym Hero                  score=5.000  (Genre match: pop; Energy similarity: 0.00 (song=0.93, target=nan))
  3. Rooftop Lights            score=3.000  (Mood match: happy; Energy similarity: 0.00 (song=0.76, target=nan))
  4. Midnight Coding           score=0.000  (Energy similarity: 0.00 (song=0.42, target=nan))
  5. Storm Runner              score=0.000  (Energy similarity: 0.00 (song=0.91, target=nan))

============================================================
5. Perfect-tie cluster (lofi/chill)
  profile: UserProfile(favorite_genre='lofi', favorite_mood='chill', target_energy=0.42, likes_acoustic=True)
------------------------------------------------------------
  1. Midnight Coding           score=10.000  (Genre match: lofi; Mood match: chill; Energy similarity: 1.00 (song=0.42, target=0.42))
  2. Library Rain              score=9.860  (Genre match: lofi; Mood match: chill; Energy similarity: 0.93 (song=0.35, target=0.42))
  3. Focus Flow                score=6.960  (Genre match: lofi; Energy similarity: 0.98 (song=0.4, target=0.42))
  4. Spacewalk Thoughts        score=4.720  (Mood match: chill; Energy similarity: 0.86 (song=0.28, target=0.42))
  5. Dust Bowl Letters         score=2.000  (Energy similarity: 1.00 (song=0.42, target=0.42)) '''
**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:
When I did a weight shift it definetly impacted the songs recommended since genre didn't have much as a heavy impact compared to the other ctaergories when i changed it to a lesser number. It recommended new songs that had a higher score.

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

It has a small catalog and there isn't much songs. There is definetly genres that have more songs then the other genres liek lofi vrs metal. It heavily favors genre.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:
I learned how recommenders use data inorder to make predictions for types of media users like, and there how some methods have certain weakness. No matter how good your recommender is, there will always be a bias. I learned how to crate a scoring system in order to recommend songs to the users. I would definetly change the weights of the scoring on the features to reduce some bias and add more features to make the recommendations more detailed to the user. Ai helped me alot to create the scoring I wanted at first and made adjustments to it.


- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this





