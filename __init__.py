from mycroft import MycroftSkill, intent_file_handler


class SystemCommands(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('commands.system.intent')
    def handle_commands_system(self, message):
        self.speak_dialog('commands.system')


def create_skill():
    return SystemCommands()

