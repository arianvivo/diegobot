#!/usr/bin/python3
import praw
import re
import random

# REDDIT ACCOUNT CREDENTIALES
r = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)

subreddit = r.subreddit("fulbo")

frases=["Yo me equivoqué y pagué, pero la pelota no se mancha",
"Se le escapó la tortuga",
"Me cortaron las piernas",
"La pelota no se mancha",
"Pelé debutó con un pibe…  Y le pegó a la jermu",
"Lástima no se le tiene a nadie, maestro",
"Más falso que dólar celeste",
"Me siento más sólo que Kung Fu",
"Les pido que me dejen vivir mi vida. Nunca quise ser un ejemplo",
"Lo espero Segurola y Habana 4310, séptimo piso",
"Fuma debajo del agua",
"Si voy al banco es para sacar plata, fiera",
"Si no me va a contestar, es un botón",
"La droga es un pacman que se come a toda tu familia",
"Para jugar contra Australia nos daban café veloz",
"Es capaz de meterle un supositorio a una liebre",
"La tenés adentro",
"Fui, soy y seré drogadicto",
"Los boludos son como las hormigas, están en todas partes del mundo",
"Si sos puto, bancátela",
"No, eeh, la... eeh... la... mmmmmh..... la... laaaa... eeehhhh... mmmh...",
"Con perdón de las damas, que la sigan chupando",
"Vos también la tenés adentro",
 "No hay que tomarle la leche al gato",
"La gente tiene que entender que Diego no es una máquina de dar felicidad",
"La bronca es mi combustible",
 "Lo único que no soy, es falso",
"Los que me creían muerto, que se jodan",
"Hoy no hablo muchachos. Tengo menos palabras que un telegrama",
"No soy un ejemplo, pero sí un referente"]

# ESPECIAL DIA DE LOS INOCENTES

#frases=["Eu me enganei e paguei, mas a bola não se mancha",
#"Escapou a tartaruga",
#"Cortaram minhas pernas",
#"A bola não se mancha",
#"Pelé estreou com um garoto... E bateu na mulher",
#"Não se tem pena de ninguém, mestre",
#"Mais falso que dólar azul",
#"Me sinto mais sozinho que Kung Fu",
#"Peço que me deixem viver minha vida. Nunca quis ser um exemplo",
#"Eu espero, Segurola e Habana 4310, sétimo andar",
#"Fuma debaixo d'água",
#"Se eu vou ao banco é para sacar grana, fera",
#"Se não vai me responder, é um dedo duro",
#"A droga é um pacman que devora toda a sua família",
#"Para jogar contra a Austrália nos davam café rápido",
#"É capaz de enfiar um supositório numa lebre",
#"Você tem dentro",
#"Fui, sou e serei viciado",
#"Os bobos são como as formigas, estão em todos os lugares do mundo",
#"Se você é viado, aguenta",
#"Não, eeh, a... eeh... a... mmmmmh... a... aaaa... eeehhhh... mmmh...",
#"Com perdão das damas, que continuem chupando",
#"Você também tem dentro",
#"Não se deve tirar o leite do gato",
#"As pessoas precisam entender que Diego não é uma máquina de dar felicidade",
#"A raiva é meu combustível",
#"A única coisa que não sou, é falso",
#"Os que me achavam morto, que se danem",
#"Hoje não falo, pessoal. Tenho menos palavras que um telegrama",
#"Não sou um exemplo, mas sou uma referência"]

sampa="Si a Sampaoli le tirás la pelota, te la devuelve con la mano"
gordo="Ahora que me dijo gordito le voy a meter cuatro goles"
ronaldo="Cristiano Ronaldo hace un gol y te vende un shampoo"


pattern = re.compile(r'maradona', re.IGNORECASE)
pattern2 = re.compile(r'el diego', re.IGNORECASE)
samparegex = re.compile(r'sampaoli', re.IGNORECASE)
gordoregex = re.compile(r'gordito', re.IGNORECASE)
ronaldoregex = re.compile(r'ronaldo', re.IGNORECASE)

def main():
    print("Bot is running...")
    for comment in subreddit.stream.comments(skip_existing=True):
        if pattern.search(comment.body) or pattern2.search(comment.body):
            if samparegex.search(comment.body):
                comment.reply(sampa)
            elif gordoregex.search(comment.body):
                comment.reply(gordo)
            elif ronaldoregex.search(comment.body):
                comment.reply(ronaldo)
            else:
                comment.reply(random.choice(frases))



if __name__ == "__main__":
    main()
