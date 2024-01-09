import PySimpleGUI as sg


class CheckProgress:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "image": ("IMAGE",),
                "StopFlow": (["Yes", "No"],),
            },
        }

    RETURN_TYPES = ("IMAGE",)

    FUNCTION = "stop"

    CATEGORY = "Example"

    def stop(self, image, StopFlow):
        if StopFlow == "Yes":
            layout = [[sg.Button('Continue'), sg.Button('Stop Flow')]]      
            window = sg.Window('Do you wish to continue?', layout)    
            event, values = window.read()    
            window.close()
            if event == 'Continue':
                print("Continue the flow....")
                return (image,)
            else:
                print("******* STOP  THE  FLOW *******")
                return None
            
        return (image,)
        

NODE_CLASS_MAPPINGS = { "CHECK_PROGRESS": CheckProgress }
NODE_DISPLAY_NAME_MAPPINGS = { "Example": "Check Progress" }
