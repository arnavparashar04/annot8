import dearpygui.dearpygui as dpg


def main():
    dpg.create_context()
    dpg.create_viewport(title="annot8")
    wid = dpg.get_viewport_client_width()
    hei = dpg.get_viewport_client_height()

    dpg.set_viewport_height(hei)
    dpg.set_viewport_width(wid)
    dpg.set_viewport_clear_color([255, 255, 255])

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
