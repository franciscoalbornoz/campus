def validar_email(email):
    return "@" in email

def validar_password(password):
    return len(password) <= 10 and len(password) > 0

def ejecutar_test(email, password):
    print("===== TEST LOGIN MiCampus =====")
    print(f"Usuario ingresado: {email}")
    print(f"Contraseña ingresada: {'*' * len(password)}")
    print("--------------------------------")

    email_ok = validar_email(email)
    password_ok = validar_password(password)

    print(f"✔ Formato de usuario (@): {'CORRECTO' if email_ok else 'INCORRECTO'}")
    print(f"✔ Longitud de contraseña (máx 10): {'CORRECTO' if password_ok else 'INCORRECTO'}")
    print("--------------------------------")

    if email_ok and password_ok:
        print("✅ ESTADO LOGIN: ACCESO PERMITIDO")
    else:
        print("❌ ESTADO LOGIN: ACCESO DENEGADO")

if __name__ == "__main__":
    usuario = "a.rosas@alumnos.cl"
    clave = "12345678"
    ejecutar_test(usuario, clave)
