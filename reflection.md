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
I used Claude for this project, and the add-on to have it on VSCode as well.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Cluade swapped the guess logic so a guess higher than the secret number would provide a hint to go lower, and guesses lower would hint the player to go higher. Before this was swapped, and AI fixed this error. I verified through a pytest from Cluade, which stated that is was correclty showing the right outputs, and then running the game once more and trying to make attempts, which verified the fix.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
At first, I selected lines for fixing the bug where a new game does not reset the number of guesses given. I told Claude to move the selected lines into logic_utlis.py and refactor it so the guesses list resets. It made a new function for when we start a new game, and kept the game state previously intact while ensuring the guesses are empty when returned.
I was mainly confused why a new function was made that returned these values, but looking at the code in app.py, Claude ensured that we have a variable that calls the function and its reset values.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
The output was showing not only the expected result that I wanted, but it was correct with the game's logic, so the bug for making guesses was fixed.

The bug was fixed when the problem that I encountered could not be replicated anymore. Making multiple guesses and attempting a New Game always reset the history of guesses from the previous one. No matter how many or little guesses were made, the list reset, so the bug was fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
Pytest was used in which Claude added regression tests in test_game_logic.py to verify the bug of guesses showing the wrong hint. A too high guess was correct if the guess was above the secret number, and a two low one was correct as well.

- Did AI help you design or understand any tests? How?
AI designed these tests in the test_game_logic.py file when I asked it to generate a pytest specific to the bugs fixed. It showed me the lines of code that actually showcase the test, along with running a test on the specific function, and telling me the tests passed. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.