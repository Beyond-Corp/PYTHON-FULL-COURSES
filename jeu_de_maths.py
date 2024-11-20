import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 5
questions = NB_QUESTIONS
nombre_points = 0


def poser_question():
    global questions, nombre_points
    for i in range(1, 5):
        print()
        print(f"Question Numero {i} / {NB_QUESTIONS}", )
        nombre1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
        nombre2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
        print(f"Calculez: {nombre2} + {nombre1} = ")
        result_str = input(" ")
        result_int = int(result_str)

        if result_int == nombre1 + nombre2:
            questions = questions - 1
            print(f"bonne reponse il vous reste {questions} questions / {NB_QUESTIONS}")
        else:
            questions = questions-1
            print(f"mauvaise reponse il vous reste {questions} questions / {NB_QUESTIONS}")
        if result_int == nombre1 + nombre2:
         nombre_points = nombre_points + 1



    #         revoir ici stp  et adapte normalement

    print(f"TOTAL POINTS : Vous avez: {nombre_points} / {NB_QUESTIONS}")
    moyenne = float(NB_QUESTIONS/2)
    if nombre_points >= moyenne:
     print(f"Excelent, moyenne: {moyenne}")
    elif nombre_points >=moyenne:
     print(f"Passable , moyenne: {moyenne}")
    else:
     print(f"C'est pas grave mon gars , moyenne: {moyenne}")





poser_question()
