from imports import *
from sql_all_logins import *
#from theme import *
from save_cloud_image import *

# Universal functions for full functionality

# universal button clicking manager refer to specific case with lambda
def change_screen(manager, screen_name):
    manager.current = screen_name

def update_button_text_size(instance, value):
    instance.text_size = (instance.width, None)
    instance.texture_update()

# Start of app Screen classes
class welcome(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # screen layout
        root = BoxLayout(orientation="vertical")
        root.add_widget(Label(text="Corporate Office"))

        # login option button
        login_button = Button(text="Login")
        root.add_widget(login_button)

        # create account option button
        create_account_button = Button(text="Sign up")
        root.add_widget(create_account_button)

        # add button options to main screen
        self.add_widget(root)

        # manage the button clicking for universal function
        login_button.bind(on_release=lambda instance: change_screen(self.manager, 'login'))
        create_account_button.bind(on_release=lambda instance: change_screen(self.manager, 'sign_up'))
class login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # screen layout
        root = BoxLayout(orientation="vertical")
        root.add_widget(Label(text="Login"))

        # Input fields for username and password
        self.username_input = TextInput(hint_text="Enter username")
        # password input with initial visibility set to True (masked)
        self.password_input = TextInput(hint_text="Enter password", password=True)

        root.add_widget(self.username_input)
        root.add_widget(self.password_input)

        # submit button for login fields
        submit_button = Button(text="Submit")

        submit_button.bind(on_press=self.submit_login)
        root.add_widget(submit_button)

        # Navigate back to the home screen
        home_button = Button(text="Home")
        root.add_widget(home_button)

        # add options to the main layout
        self.add_widget(root)

        # change screen
        home_button.bind(on_release=lambda instance: change_screen(self.manager, 'welcome'))

    # Actual login magic with response
    def submit_login(self, instance):

        # Perform the login logic
        username = self.username_input.text
        password = self.password_input.text
        response = sql_login(username, password)

        # Create and configure the login status popup
        popup_content = BoxLayout(orientation="vertical")
        popup_label = Label(text="Login Successful" if response in ["user", "admin"] else "Login Failed")

        # Add popup elements to popup main
        popup_content.add_widget(popup_label)

        if response == "user":
            window_name = 'main_page'
        elif response == "admin":
            window_name = 'main_page_admin'
        else:
            window_name = None

        if window_name:
            popup_button = Button(text='Open New Window')
            popup_button.bind(on_press=lambda instance: change_screen(self.manager, window_name))
        else:
            popup_button = Button(text="Close")

        popup_button.bind(on_release=self.close_popup)
        popup_content.add_widget(popup_button)

        # Show the popup
        self.popup = Popup(content=popup_content, title="Login Status", size_hint=(0.4, 0.4))
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()
class sign_up(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # screen layout
        root = BoxLayout(orientation="vertical")
        root.add_widget(Label(text="Sign up"))

        # Input fields for username and password
        self.username_input = TextInput(hint_text="Enter username")
        # password input with initial visibility set to True (masked)
        self.password_input = TextInput(hint_text="Enter password", password=True)
        root.add_widget(self.username_input)
        root.add_widget(self.password_input)

        # submit button for sign in fields
        submit_button = Button(text="Submit")

        submit_button.bind(on_press=self.submit_signin)
        root.add_widget(submit_button)

        # Navigate back to home screen
        home_button = Button(text="Home")
        root.add_widget(home_button)

        # add options to main layout
        self.add_widget(root)

        home_button.bind(on_release=lambda instance: change_screen(self.manager, 'welcome'))
    def submit_signin(self, instance):
        # Perform the login logic
        username = self.username_input.text
        password = self.password_input.text
        response = sql_newlogin(username, password)

        # Create and configure the signup status popup (Case dependant)
        popup_content = BoxLayout(orientation="vertical")
        popup_label = Label(text="Account Creation Successful" if response == 1 else "Creation Failed")
        popup_button = Button(text="Close")
        popup_button.bind(on_press=self.close_popup)

        # Add popup elements to popup main
        popup_content.add_widget(popup_label)
        popup_content.add_widget(popup_button)

        # Make popup and add it to screen
        self.popup = Popup(title="Signin Status", content=popup_content, size_hint=(None, None), size=(400, 200))

        # Open the pop-up
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()

class main_page(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Downloads that happen from cloud if login is successful
        find_and_save()

        # screen layout maybe change this actually to grid layout... or other?
        root = BoxLayout(orientation="vertical")
        root.add_widget(Label(text="MAIN PAGE"))

        # Put sign out and photo option etc. etc.
        signout_button = Button(text='Sign out')
        signout_button.bind(on_press=self.sign_out)
        root.add_widget(signout_button)


        # Scan option (button opens to a camera for qr scan, once detected goes to next screen
        # import this code for this kivy_qr()?
        # pass to mock screen (for the product scanneds interface)

        # Train option (here the photos of items should be within the IBM cloud data base.... in docs with id???)
        #the users json file should be updated to contain list of items trained on (definately a grid layout for this page)
        train_button = Button(text='Train')
        train_button.bind(on_release=lambda instance: change_screen(self.manager, 'train'))
        root.add_widget(train_button)

        # Clean
        # Break
        # General


        self.add_widget(root)

    def sign_out(self, instance):

        # Create and configure the login status popup (case dependant)
        popup_content = BoxLayout(orientation="vertical")

        popup_yes_button = Button(text="sign out")
        popup_yes_button.bind(on_press=lambda instance: change_screen(self.manager, 'welcome'))
        popup_yes_button.bind(on_release=self.close_popup)

        popup_no_button = Button(text="Cancel")
        popup_no_button.bind(on_press=self.close_popup)

        # Add popup elements to popup main
        popup_content.add_widget(popup_yes_button)
        popup_content.add_widget(popup_no_button)

        # Make popup and add it to screen
        self.popup = Popup(title="Are you sure you want to sign out?", content=popup_content, size_hint=(None, None), size=(400, 200))

        # Open the pop-up
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()
class main_page_admin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical")
        root.add_widget(Label(text="MAIN PAGE ADMIN"))

        self.add_widget(root)
class train(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # define screen layout
        root = GridLayout(cols=2)
        root.add_widget(Label(text="Train"))

        # All training option buttons
        root.add_widget(self.create_button_with_background("regular-collar.png", "Standard Collar"))
        root.add_widget(self.create_button_with_background("regular-flap.png", "Flap"))
        root.add_widget(self.create_button_with_background("standard-lining.png", "Standard Lining"))
        root.add_widget(self.create_button_with_background("standing-collar.png", "Standing Collar"))

        # Return button
        return_button = Button(text='Return')
        return_button.bind(on_release=lambda instance: change_screen(self.manager, 'main_page'))
        root.add_widget(return_button)

        # add all root elements to self
        self.add_widget(root)

    # assign the background only if the file exists, else just make plain button... prevents whole code erroring if file doesnt exist
    def create_button_with_background(self, image_path, button_text):
        button = Button(text=button_text)
        button.text = button_text
        # call function to make sure test fits on button
        button.bind(size=lambda instance, value: update_button_text_size(instance, value))

        try:
            # Attempt background image
            button.background_normal = image_path
        except FileNotFoundError:
            # case where the image doesn't exist
            button.background_normal = ''  # empty string for no background

        return button

class CorporateOffice(MDApp):

    def build(self):

        # Change this later into a function to look nice
        self.theme_cls.theme_style = "Dark"

        # Create a screen manager
        sm = ScreenManager()

        # Define and add screens to the screen manager
        screen1 = welcome(name='welcome')
        screen2 = login(name='login')
        screen3 = sign_up(name='sign_up')
        screen4 = main_page(name='main_page')
        screen5 = main_page_admin(name='main_page_admin')
        #screen5 = qr_scanner(name='qr_scanner')
        #screen6 = work_bench(name='work_bench')
        screen7 = train(name='train')
        #screen8 = clean
        #screen9 = break
        #screen10 = general

        sm.add_widget(screen1)
        sm.add_widget(screen2)
        sm.add_widget(screen3)
        sm.add_widget(screen4)
        sm.add_widget(screen5)

        sm.add_widget(screen7)

        return sm

if __name__ == '__main__':

    CorporateOffice().run()