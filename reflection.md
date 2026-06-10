# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- Game looked like a browser window with a bar to type guesses for a random number
- Hints were backwards, inputting numbers higher than the secret number would result in hints showing "Go Higher", numbers lower than the number would show "Go Lower"
- Pressing New Game did not reset our sequence, the secret number changed but the guesses from the last game stayed and I could not make any new guesses
- Difficult did not match what it should be, for example, Normal gave a range to guess from 1 - 100 but Hard was 1 - 50. The question would be if that correctly reflects the diffculty chosen.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 42| Too High hint | Too Low hint was shown| none|
| Pressed New Game button| Guess sequence reset, I could make guesses now| Secret number changed only, previous game's guesses remained, submitting new ones did not have an effect| None|
| guess was outside of allowed range| Error thrown, invalid guess| Guess was treated normally, hint was given | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
