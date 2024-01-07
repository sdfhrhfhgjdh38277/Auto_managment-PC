import flet as ft


def main(page: ft.Page):
    page.title = "Comoda editor"
    page.window_resizable = True
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def pick_result(e: ft.FilePickerResultEvent):
        ...

    pick_dialog = ft.FilePicker(on_result=pick_result)
    page.overlay.append(pick_dialog)
    selected_files = ft.Text("")

    page.add(
        ft.Row(
            [
                ft.Text("Change file", size=15, weight=500),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Change file",
                            icon=ft.icons.UPLOAD_FILE,
                            on_click=lambda _: pick_dialog.pick_files(
                                allow_multiple=False
                            ),
                        )
                    ]
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([]),
    )


ft.app(main)
