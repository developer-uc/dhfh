from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem, IconRightWidget

KV = '''
BoxLayout:
    orientation: "vertical"

    MDTextField:
        id: task_input
        hint_text: "Enter task"
        size_hint_x: 0.9
        pos_hint: {"center_x": 0.5}

    MDBoxLayout:
        orientation: "horizontal"
        size_hint_y: None
        height: "48dp"

        MDRaisedButton:     # <-- old version caused error
            text: "Add Task"
            on_release: app.add_task()

    ScrollView:
        MDList:
            id: task_list
'''

class TodoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def add_task(self):
        task_text = self.root.ids.task_input.text
        if task_text.strip():
            item = OneLineAvatarIconListItem(text=task_text)
            delete_btn = IconRightWidget(icon="delete", on_release=lambda x: self.delete_task(item))
            item.add_widget(delete_btn)
            self.root.ids.task_list.add_widget(item)
            self.root.ids.task_input.text = ""

    def delete_task(self, task_item):
        self.root.ids.task_list.remove_widget(task_item)


TodoApp().run()
