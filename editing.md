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

# Introduction

## Editing `items.toml`
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

## Editing `messages.toml`
