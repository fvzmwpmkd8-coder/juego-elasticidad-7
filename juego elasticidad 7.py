import random

print("========================================")
print("   🕵️ DETECTIVE DE LA ELASTICIDAD")
print("========================================")
print("Resuelve 100 casos económicos.")
print("Usa tus pistas con inteligencia.\n")

nivel = 1
puntos = 0

while nivel <= 100:

    pistas = 3

    # ==============================
    # CREAR CASO
    # ==============================

    print("\n========================================")
    print("🕵️ CASO", nivel, "/ 100")
    print("========================================")

    # Dificultad
    if nivel <= 20:
        dificultad = "🟢 Fácil"
    elif nivel <= 40:
        dificultad = "🟡 Normal"
    elif nivel <= 60:
        dificultad = "🟠 Difícil"
    elif nivel <= 80:
        dificultad = "🔴 Muy difícil"
    else:
        dificultad = "🔥 Experto"

    print("Dificultad:", dificultad)

    # Datos aleatorios
    precio_anterior = random.randint(50, 200)
    precio_nuevo = precio_anterior + random.randint(10, 50)

    cantidad_anterior = random.randint(50, 200)

    porcentaje_precio = (
        (precio_nuevo - precio_anterior)
        / precio_anterior
    ) * 100

    # Hacemos que algunos casos sean claramente elásticos
    tipo = random.choice([
        "elastica",
        "inelastica",
        "unitaria"
    ])

    if tipo == "elastica":
        porcentaje_cantidad = porcentaje_precio * random.uniform(1.5, 2.5)

    elif tipo == "inelastica":
        porcentaje_cantidad = porcentaje_precio * random.uniform(0.3, 0.8)

    else:
        porcentaje_cantidad = porcentaje_precio

    cantidad_nueva = round(
        cantidad_anterior *
        (1 - porcentaje_cantidad / 100)
    )

    print("\n🔎 INFORMACIÓN DEL CASO")
    print("----------------------------")
    print("Precio anterior: $", precio_anterior)
    print("Precio nuevo:   $", precio_nuevo)
    print("Cantidad anterior:", cantidad_anterior)
    print("Cantidad nueva:  ", cantidad_nueva)

    print("\n¿Qué tipo de demanda es?")

    print("\n1. 📈 Elástica")
    print("2. 📊 Inelástica")
    print("3. ⚖️ Unitaria")

    print("\n💡 Escribe 'pista' para recibir una pista.")

    respuesta = input("\nTu respuesta: ").lower()

    # ==============================
    # SISTEMA DE PISTAS
    # ==============================

    while respuesta == "pista":

        if pistas > 0:

            pistas -= 1

            print("\n💡 PISTA", 3 - pistas)

            if pistas == 2:

                print("👉 Primero calcula el porcentaje")
                print("de cambio del precio.")

            elif pistas == 1:

                print("👉 Después calcula el porcentaje")
                print("de cambio de la cantidad.")

            elif pistas == 0:

                print("👉 Divide:")
                print("% cambio de cantidad")
                print("÷")
                print("% cambio de precio")

                print("\nSi el resultado es:")
                print("> 1  → Elástica")
                print("< 1  → Inelástica")
                print("= 1  → Unitaria")

            print("\n💡 Pistas restantes:", pistas)

        else:

            print("\n❌ Ya utilizaste tus 3 pistas.")

        respuesta = input("\nTu respuesta: ").lower()

    # ==============================
    # COMPROBAR RESPUESTA
    # ==============================

    if respuesta in ["1", "elastica", "elástica"]:

        respuesta_usuario = "elastica"

    elif respuesta in ["2", "inelastica", "inelástica"]:

        respuesta_usuario = "inelastica"

    elif respuesta in ["3", "unitaria"]:

        respuesta_usuario = "unitaria"

    else:

        respuesta_usuario = "incorrecta"

    # ==============================
    # RESULTADO
    # ==============================

    if respuesta_usuario == tipo:

        puntos += nivel

        print("\n✅ ¡CASO RESUELTO!")
        print("⭐ Ganaste", nivel, "puntos.")
        print("🏆 Puntos totales:", puntos)

    else:

        print("\n❌ CASO NO RESUELTO")
        
        if tipo == "elastica":
            print("La respuesta era: 📈 ELÁSTICA")

        elif tipo == "inelastica":
            print("La respuesta era: 📊 INELÁSTICA")

        else:
            print("La respuesta era: ⚖️ UNITARIA")

        print("⭐ Puntos totales:", puntos)

    # ==============================
    # SIGUIENTE NIVEL
    # ==============================

    if nivel < 100:

        print("\n🔓 Has avanzado al siguiente nivel.")
        input("Pulsa ENTER para continuar...")

    nivel += 1


# ========================================
# FINAL
# ========================================

print("\n========================================")
print("        🏆 CASO FINALIZADO")
print("========================================")

print("Llegaste al NIVEL 100.")
print("⭐ Puntuación final:", puntos)

if puntos >= 7000:

    print("🔥 ¡ERES UN MAESTRO DE LA ELASTICIDAD!")

elif puntos >= 4000:

    print("👏 ¡Excelente trabajo, detective!")

elif puntos >= 2000:

    print("🧠 ¡Buen trabajo! Sigue investigando.")

else:

    print("💪 Sigue practicando y vuelve a intentarlo.")

print("\n🕵️ Gracias por jugar.")