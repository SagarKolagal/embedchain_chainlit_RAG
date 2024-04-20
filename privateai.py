from embedchain import App

import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    app = App.from_config("config.yaml")
    app.add("D:\Playground\Rag\data", data_type="directory")
    app.collect_metrics = False
    stream: True
    cl.user_session.set("app", app)

@cl.on_message
async def on_message(message: cl.Message):
    app = cl.user_session.get("app")
    msg = cl.Message(content="")
    for chunk in await cl.make_async(app.chat)(message.content):
        await msg.stream_token(chunk)

    await msg.send()
