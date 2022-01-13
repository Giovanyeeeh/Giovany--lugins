# Slap plugin from https://github.com/ruizlenato/SmudgeLord
# Port for KannaX by fnixdev


import random

from kannax import kannax, Message

@kannax.on_cmd(
    "slap",
    about={
        "header": "slap",
    },
)
async def printer(m: Message):
    if m.reply_to_message:
        try:
            user1 = (
                f"<a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a>"
            )
        except:
            user1 = m.chat.title
        try:
            user2 = f"<a href='tg://user?id={m.reply_to_message.from_user.id}'>{m.reply_to_message.from_user.first_name}</a>"
        except:
            user2 = m.chat.title
        temp = random.choice(TEMPLATE)
        item = random.choice(ITENS)
        hit = random.choice(HIT)
        throw = random.choice(THROW)

        reply = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)

        await m.edit(reply)
    else:
        await m.edit("Bruuuh")

TEMPLATE = [
    "{user1} {hits} {user2} com um {item}.",
    "{user1} {hits} {user2} no rosto com um {item}.",
    "{user1} {hits} {user2} um pouco com um {item}.",
    "{user1} {throws} {item} no {user2}.",
    "{user1} {throws} {item} na cara do {user2} .",
    "{user1} joga um {item} na cabeça do {user2}.",
    "{user1} pensa em bater no {user2} com {item}.",
    "{user1} derruba {user2} e repetidamente o {hits} com {item}.",
    "{user1} pega {item} e {hits} no {user2}.",
    "{user1} amarra {user2} em uma cadeira e {throws} {item}.",
    "{user1} deu um empurrão amigável no {user2} para que ele aprenda a nadar na lava",
  ]

ITENS = [
      "frigideira de ferro fundido",
    "truta grande",
    "taco de beisebol",
    "bastão de cricket",
    "bengala de madeira",
    "unha",
    "penis de borracha",
    "pá",
    "ventilador",
    "um Nokia 3310",
    "torradeira",
    "Laptop da positivo",
    "televisão",
    "caminhão de cinco toneladas",
    "piroca",
    "livro",
    "laptop",
    "televisão antiga",
    "chifre do administrador",
    "um vibrador gigante",
    "galinha de borracha",
    "morcego cravado",
    "extintor de incêndio",
    "litro de 51",
    "pedaço de terra",
    "colméia",
    "pedaço de carne podre",
    "Urso",
    "a mãe do admin"
  ]

THROW = [
  "joga",
  "lança",
  "arremessa",
  ]

HIT = [
    "golpeia",
    "bate",
    "golpeia",
    "esmurra",
    "ataca",
  ]
 
