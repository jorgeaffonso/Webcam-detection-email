
## What this program does

O programa detecta a presença de um objeto, guarda essa imagem e a envia por email.

O programa começa a armazenar imagens no diretório "images" quando reconhece e coloca o objeto no retângulo.
Quando o objeto sai da imagem se escolhe a imagem central para ser enviada por email. Como:
Se você guardou "x" imagens você pega a imagem do meio (x/2) - index = int(len(all_images)/2).

O programa também inicia um processo paralelo para evitar que quando se está enviando o email ou limpando
o diretório, o programa principal não congele a imagem.

    email_thread = Thread(target=send_email, args=(image_with_obj, ))
    email_thread.daemon = True
    email_thread.start()

    clean_thread = Thread(target=clean_folder)
    clean_thread.daemon = True
    clean_thread.start()