def pausa(page, mensaje):
    print(f"\n>>> {mensaje}")
    page.wait_for_timeout(1000)