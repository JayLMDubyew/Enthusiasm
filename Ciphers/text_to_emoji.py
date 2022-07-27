
##: (JayLMDubyew) JLMW - 2022
##TBD: edge cases for plurality and possessiveness

def to_emoji(plaintext):
    converted = ""
    emojilist = {
        "smile":"🙂",
        "hello":"👋",
        "hi":"👋",
        "bye":"👋",
        "goodbye":"👋",
        ":)":"🙂",
        "love":"😍",
        "done":"⌛",
        "eyes":"👀",
        "looking":"👀",
        "look":"👀",
        "see":"👀",
        "stare":"👀",
        "staring":"👀",
        "stares":"👀",
        "page":"📄",
        "pages":"📄",
        "veggie":"🥬",
        "vegetable":"🥬",
        "write":"✍️",
        "writing":"✍️",
        "wrote":"✍️ ",
        "happy":"😁",
        "great":"😁",
        "kiss":"😘",
        "say":"🗣️",
        "speak":"🗣️",
        "said":"🗣️",
        "tell":"🗣️",
        "kissing":"😘",
        "xoxo":"😘",
        "star":"⭐",
        "sparkle":"✨",
        "stars":"✨",
        "shine":"✨",
        "shiny":"✨",
        "rosy":"🌹",
        "rose":"🌹",
        "pizza":"🍕",
        "moon":"🌝",
        "song":"🎼",
        "sun":"🌞",
        "fire":"🔥",
        "burn":"🔥",
        "firework":"🎆",
        "fireworks":"🎆",
        "dance":"💃",
        "dancing":"💃",
        "candy":"🍬",
        "sweet":"🍯",
        "honey":"🍯",
        "tractor":"🚜",
        "sexy":"😘",
        "wow":"🤩",
        "ew":"🤢",
        "tea":"🫖",
        "chicken":"🐔",
        "farmer":"🧑‍🌾",
        "hot":"🥵",
        "cold":"🥶",
        "yay":"🥳"
    }

    plaintext = plaintext.replace("\n"," \n")
    for word in plaintext.split(" "):
        converted += emojilist.get(word.lower(), word) + " "
    print(converted)
    return converted


lyrics = """Head underwater and they tell me
To breathe easy for a while
The breathing gets harder, even I know that

Made room for me, it's too soon to see
If I'm happy in your hands
I'm unusually hard to hold on to

Blank stares at blank pages
No easy way to say this
You mean well, but you make this hard on me

I'm not gonna write you a love song
'Cause you asked for it, 'cause you need one
You see, I'm not gonna write you a love song
'Cause you tell me it's make or break in this
If you're on your way
I'm not gonna write you to stay
If all you have is leavin', I'ma need a better reason
To write you a love song today"""

print(f"Original text: \n {lyrics} \n Converted Text: \n {to_emoji(lyrics)}")