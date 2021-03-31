Modifiable RPS isn't just a standard rock paper scissors downloadable game. The key word is "modifiable", literally in the name.
Some of the game's appearance can be changed even by someone not knowing code, which includes:
- The names of the items
- The victory messages

If you know Python, then this entire game is in your hands.
There are small sections to get you started, and the rest you will be able to do yourself.

# Before you edit
Modifiable RPS uses special TOML files that contain data for configurable stuff, which include the items and messages.
If you're not acquainted with those, you can get a headstart and learn more with these links:
- https://toml.io/en/v1.0.0 (Official TOML website documentation)
- https://en.wikipedia.org/wiki/TOML (Wikipedia page, contains lots of data)

# Things to use
To use TOML, you need just one thing: An editor. Frankly, you can use any sort of editor that can do 2 things: Read and write files. Even Notepad will work.
Some editors can be Visual Studio Code, Atom, etc if you're a programmer. Of course though, Notepad itself will allow you to do the job properly.

# Editing `items.toml`
`items.toml` is a small file that is 14 lines long. In rock paper scissors, we all know the rules: 3 things that 2 players choose and it is what the outcome depends on.<br>

The file is structured this way:<br>
```toml
[item1]
beats = "item2"
falls_to = "item3"

[item2]
beats = "item3"
falls_to = "item1"

[item3]
beats = "item1"
falls_to = "item3"
```

Every item has its own section. A section is the thing that is surrounded by square brackets ([]) which contains 2 pieces of data:
- Which item does it beat?
- Which item does it lose to?

For example, let's see here:
```toml
[scissors]
beats = "paper"
falls_to = "rock"
```

This section is for scissors. In this section, 2 things are declared:
- Scissors beat paper.
- Scissors lose to rock.

(We don't need to declare with which item does it make a draw with.)<br><br>

These 2 key and value pairs strictly define what item does it beat and lose to. A key and value fair is, in the simplest term, anything that takes this form: `key = value`<br>
The key is the first thing **before** the equals sign, and the value is the second thing after the sign. Each section **must have only** 2 key and value pairs. The keys should be:
- beats
- falls_to
"beats" is the first key, and its value should be the **name of the item's section** that the item beats.<br>
"falls_to" is the second and its value should also the name of an item's section, but this time that item must be what beats the current item.<br>

In a nutshell:
- Each must have its own section (`[section example]`)
- Each section must have the name of the item it is describing
- Each section must have 2 key and value pairs:
    - First key should be "beats", and its value should be the name of the section of the item that it beats.
    - Second should be "falls_to", which is the opposite.

There must be only 3 items. If there is an amount that isn't 3, the game **will** break. Maybe I will change it to include multiple items, not just 3, but for now you must only have 3 items.<br>
**NOTE: IF YOU MODIFY THE ITEMS, YOU MUST CHANGE `messages.toml` FOR THE GAME TO WORK.**

# Editing `messages.toml`
This part is much easier to edit for beginners. The file `messages.toml` contains data for the **messages that display to see what result happens after the 2 items have been picked**.
As we all know, the outcome of the round depends on which items have been chosen (rock and scissors, scissors and paper, paper and paper, rock and paper, etc). The file contains every message that is displayed after finding out the outcome. Like:
- When you choose rock and the AI chooses paper: "The AI's paper goes over your rock."
- You choose scissors and the AI chooses paper: "Your scissors cut the AI's paper."
- You and the AI have the same item: "The items are the same!"
- and etc.

Every message is structured this way (which we will use as a template):<br>
`[the winner]-[the winner's item]-beats-[the loser's item] = "[message here]"`<br>
So, to make a message for when the player's scissors beat rock you do `player-scissors-beats-rock = "Your scissors beat the AI's rock! Somehow..."`<br>
if the player is who won, you enter "player" as the winner that you must put. If the AI won, you enter "ai":

`[the winner]` in the example key and value pair| Who won?
-------------|---------
`player` | The player
`ai` | The AI

Examples include:
Who won? (`[the winner])` | Winner's item | Loser's item | The message | Key and value pair
----------------------- | ------------- | ------------ | ---------- | -------------------
The player (player) | Rock | Scissors | "sample message 1" | `player-rock-beats-scissors = "sample message 1"`
The AI (ai) | Paper | Rock | "sample message 2" | `ai-paper-beats-rock` = "sample message 2"

To find out which name you must put inside `[the winner's item]` and `[the loser's item]`, you simply replace them with the corresponding:
Thing to replace in the template | What to replace it with
-------------------------------- | -----------------------
`[the winner's item]` | The name of the section of the item that won
`[the loser's item]` | The name of the section of the item that lost to the winning item

To make a message for the draws is much easier. There **must be only one message for a draw**, and it's key is just "draw", and the value is anything you want to put.<br>
For example:
- `draw = "There is a draw!"`
- `draw = "Oh wow, no winner!"`
- `draw = "The items are the same."`

# What you should remember
- If you modify one of the `.toml` files, you must modify the other too in a way that fits your modification.
- Every section and key must be **fully in lowercase**. There is a high risk I haven't tested it will break if you use uppercase characters, or anything else that doesn't include lowercase letters.
- Since I have said the above, remember that `.toml` is case sensitive. `key = "value"` is not the same as `Key = "value"`.
- If you are a visual learner, you can try analyzing the files yourself and see what to do.
- There **must** be only 3 items.