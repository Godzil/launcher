import UI


class Applet(UI.Container):
    """
    Applet are the main "application" running in the environment.
    They are filling the main area between the titlebar and the foot bar.

    When you make your own applet, you have to make it to inherit of that class
    so you have access to all the needed features.

    An applet can provide two other services:
     - A plugin
     - A settings page

    They need to be registered in the applet init function

    The system should not try to create more than one instance of an applet, but
    it is still a good practice to make sure your applet would not crash or create any
    problem if that happen.

    The main widget function (Draw and handle_event) will be run automatically part of the
    main loop of the environment. If you need asynchronous behavious, it is up to your
    applet to create its own thread and manage them.

    An applet should not try to write directly onto the screen, or trying to get access
    to the canvas of other widget which it does not own as thing can change without notice
    on that part and would break your applet.

    An applet can have a transparent background (and it is recommended until you need to control the background.)
    Still you can use the alpha channel to make the (potential) background picture lighter if needed.
    """

    def Draw(self):
        pass

    def handle_event(self):
        pass