# ==============================
#   GESTOR DE TAREAS EN CONSOLA
# ==============================

# 1️⃣ Lista inicial de tareas
tareas = ["Estudiar Python", "Hacer ejercicio", "Leer 20 minutos"]

def mostrar_tareas():
    # 2️⃣ Mostrar todas las tareas actuales
    if not tareas:  # 7️⃣ Validar si la lista está vacía
        print("\n🎉 ¡Todas las tareas completadas!")
    else:
        print("\n📋 TAREAS PENDIENTES:")
        for i, tarea in enumerate(tareas):  # 5️⃣ Recorrer con for
            print(f"{i + 1}. {tarea}")

def agregar_tarea():
    # 3️⃣ Agregar nueva tarea
    nueva = input("✏️ Ingresa la nueva tarea: ")
    tareas.append(nueva)
    print("✅ Tarea agregada correctamente.")

def completar_tarea():
    # 4️⃣ Marcar tarea como completada (eliminarla)
    mostrar_tareas()
    
    if tareas:
        try:
            num = int(input("✔️ Número de tarea completada: "))
            tarea_eliminada = tareas.pop(num - 1)  # 6️⃣ Usar pop() por índice
            print(f"🗑️ Tarea '{tarea_eliminada}' completada y eliminada.")
        except (ValueError, IndexError):
            print("⚠️ Número inválido. Intenta nuevamente.")

# ================
# MENÚ PRINCIPAL
# ================
while True:
    print("\n====== 📝 GESTOR DE TAREAS ======")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        print("\n👋 Cerrando gestor de tareas...")
        if not tareas:
            print("🎉 ¡Todas las tareas completadas!")  # 8️⃣ Mensaje final
        else:
            print("📌 Aún tienes tareas pendientes. ¡Ánimo!")
        break
    else:
        print("❌ Opción inválida. Intenta otra vez.")

