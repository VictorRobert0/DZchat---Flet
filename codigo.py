#Hashzap
#botao de iniciar o chat
# popup para entrar no chat
#quando entrar no chat: (aparece para todo mundo)

    # a mensagem que vc entrou
    # o campo e o botao de enviar mensagem
    # a cada mensagem que vc envia (aparece pra todo mundo)

    # Nome: texto da mensagem


import flet as ft 

def main(pagina):
    
    texto = ft.Text("Techza") 

    chat = ft.Column()


    nome_usuario = ft.TextField(label="Escreve seu nome")


    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo =="mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar a mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", size=12, italic= True, color=ft.colors.DEEP_ORANGE_ACCENT_200))
            
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) 

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto":campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})
        #limpar o campo de mensagem
        campo_mensagem.value = ""
        pagina.update()

        
    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)



    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        #adicionar o chat
        pagina.add(chat)
        #fechar popUP
        popup.open = False
        #remover o botao iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        #criar o campo de mensagem do usuario
        #criar o botao de enviar mensagem do usuario
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.update()







    popup = ft.AlertDialog(open=False, modal=True, title=ft.Text("Bem vindo ao DZtech"), content=nome_usuario, 
    actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],)

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()






    botao_iniciar = ft.ElevatedButton("Iniciar o chat", on_click=entrar_chat),
    


    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER, port= 8000)    