from win10toast import ToastNotifier
def notify(text):
    toast = ToastNotifier()
    toast.show_toast(
        "Chat-GPT Writer",
        text,
        duration = 20,
        icon_path = "Resources/chatgpt-icon.ico",
        threaded = True,
    )
    return
