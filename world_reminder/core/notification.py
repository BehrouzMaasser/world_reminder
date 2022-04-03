import platform as plt
import os


def notify(title, message):
    if plt.system() == 'Windows':
        from plyer import notification
        notification.notify(
            title=title,
            message=message,
            app_icon=r'core\app_icon.ico',
            timeout=6
        )
    elif plt.system() == 'Darwin':
        os.system(f'''
                        osascript -e 'display notification "{message}" with title "{title}" sound name "Submarine"'
                ''')
    elif plt.system() == 'Linux':
        os.system(f'''
                        notify-send "{message}" "{title}"'
                ''')
