import json
from tkinter import messagebox


class LangTextDisplay:
    def __init__(self, file_name='main'):
        self.file_name = file_name

    def check_language_settings(self):
        with open('language/language_config.json', encoding='utf-8') as conf_language:
            self.data = json.load(conf_language)
            conf_language.close()
            return self.data['language']

    def set_lang_text(self, lang_text):
        self.lang_text = lang_text
        self.current_lang = self.check_language_settings()
        with open(f'language/{self.current_lang}/{self.current_lang}-{self.file_name}.json', encoding='utf-8') as lang_file:
            self.data = json.load(lang_file)
            return self.data[self.lang_text]

    def save_language(self, value, frame):
        self.value = value

        language_dict = {'English': 'eng_ENG', 'Polski': 'pl_PL'}
        self.language_setting = open('language/language_config.json', 'r')
        self.json_object = json.load(self.language_setting)
        self.language_setting.close()

        self.json_object['language'] = language_dict[self.value]

        self.language_setting = open('language/language_config.json', 'w')
        json.dump(self.json_object, self.language_setting)
        self.language_setting.close()

        if self.value == 'Polski':
            messagebox.showinfo(
                'UWAGA!', 'Zmiana języka zostanie aktywowana po ponownym uruchomieniu programu')
        if self.value == 'English':
            messagebox.showinfo(
                'WARNING!', 'Language change will be activated after restarting the program')

    def current_language_value(self):
        language_dict = {'eng_ENG': 'English', 'pl_PL': 'Polski'}
        return language_dict[self.check_language_settings()]
