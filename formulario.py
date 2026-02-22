import flet as ft 

def main(page: ft.Page):
    # ---------------- CONFIGURACIÓN ----------------
    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#FDFBE3"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # ---------------- CONTROLES ----------------
    txt_nombre = ft.TextField(
        label="Nombre",
        border_color="#4D2A32",
        width=450
    )

    txt_control = ft.TextField(
        label="Número de control",
        border_color="#4D2A32",
        width=450
    )

    txt_email = ft.TextField(
        label="Email",
        border_color="#4D2A32",
        width=450
    )

    dd_carrera = ft.Dropdown(
        label="Carrera",
        width=215,
        border_color="#4D2A32",
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        width=215,
        border_color="#4D2A32",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
    )

    genero_group = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="Masculino", label="Masculino"),
                ft.Radio(value="Femenino", label="Femenino"),
                ft.Radio(value="Otro", label="Otro"),
            ],
            spacing=30
        )
    )

    txt_resultado = ft.Text("", weight=ft.FontWeight.BOLD)

    # ---------------- FUNCIÓN ENVIAR ----------------
    def enviar_click(e):

        # Validación de campos vacíos
        if (
            not txt_nombre.value or
            not txt_control.value or
            not txt_email.value or
            not dd_carrera.value or
            not dd_semestre.value or
            not genero_group.value
        ):
            txt_resultado.value = "⚠ Por favor completa todos los campos."
            txt_resultado.color = "red"

        # Validación de correo con @
        elif "@" not in txt_email.value:
            txt_resultado.value = "⚠ El correo debe contener el signo @"
            txt_resultado.color = "red"

        else:
            txt_resultado.value = (
                "✅ Registro exitoso:\n"
                f"Nombre: {txt_nombre.value}\n"
                f"Control: {txt_control.value}\n"
                f"Email: {txt_email.value}\n"
                f"Carrera: {dd_carrera.value}\n"
                f"Semestre: {dd_semestre.value}\n"
                f"Género: {genero_group.value}"
            )
            txt_resultado.color = "green"

            # Limpiar campos
            txt_nombre.value = ""
            txt_control.value = ""
            txt_email.value = ""
            dd_carrera.value = None
            dd_semestre.value = None
            genero_group.value = None

        page.update()

    # ---------------- BOTÓN ----------------
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar", color="black"),
        bgcolor=ft.Colors.GREY_500,
        width=450,
        height=50,
        on_click=enviar_click
    )

    # ---------------- CONTENEDOR FORMULARIO ----------------
    formulario = ft.Container(
        width=500,
        padding=30,
        bgcolor="#EFE6C8",
        border_radius=10,
        content=ft.Column(
            [
                txt_nombre,
                txt_control,
                txt_email,
                ft.Row(
                    [dd_carrera, dd_semestre],
                    spacing=20
                ),
                ft.Text("Género:", weight=ft.FontWeight.BOLD),
                genero_group,
                btn_enviar,
                txt_resultado
            ],
            spacing=20
        )
    )

    page.add(formulario)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)