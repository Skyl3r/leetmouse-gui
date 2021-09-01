import PySimpleGUIQt as sg
from ModuleParameter import ModuleParameter

Parameters = {
    "Acceleration": ModuleParameter("Acceleration"),
    "Exponent": ModuleParameter("Exponent"),
    "Sensitivity": ModuleParameter("Sensitivity"),
    "Post Scale X": ModuleParameter("PostScaleX"),
    "Post Scale Y": ModuleParameter("PostScaleY"),
    "Pre Scale X": ModuleParameter("PreScaleX"),
    "Pre Scale Y": ModuleParameter("PreScaleY"),
    "Speed Cap": ModuleParameter("SpeedCap"),
    "Sensitivity Cap": ModuleParameter("SensitivityCap"),
    "Offset": ModuleParameter("Offset"),
    "Scrolls per Tick": ModuleParameter("ScrollsPerTick"),
}

ModeLookup = {
    "Linear": 1,
    "Classic": 2
}

# Special cases
UpdateParameter = ModuleParameter("update")
AccelerationModeParameter = ModuleParameter("AccelerationMode")
AccelerationMode = AccelerationModeParameter.parameterValue
AccelerationModePlainText = "Linear"

# get the acceleration mode to set the combo box
for mode, key in ModeLookup.items():
    print("Comparing " + str(AccelerationMode) + " with " + str(key))
    if str(AccelerationMode) == str(key):
        AccelerationModePlainText = mode

layout = [[sg.Text("LEETMOUSE")], [sg.Text("Mode: "), sg.Combo(["Linear", "Classic"], default_value=AccelerationModePlainText, enable_events=True, key="modecombo")]]

for param in Parameters:
    layout.append([sg.Text(param), sg.InputText(default_text=Parameters[param].parameterValue, key=Parameters[param].parameterName)])

layout.append([sg.Button("Update")])

window = sg.Window(title="leetmouse GUI", layout=layout)

while True:
    event, values = window.read()

    if event == "Update":
        # Update parameters
        for param in Parameters:
            Parameters[param].set(window[Parameters[param].parameterName].get())

        AccelerationModeParameter.set(str(AccelerationMode))

        # Set update flag so LEETMOUSE knows to read changes
        UpdateParameter.set("1")

    if event == "modecombo":
        # Mode was changed
        mode = values["modecombo"]
        # Save change but don't write it yet
        AccelerationMode = ModeLookup[mode]

    if event == sg.WIN_CLOSED:
        break



window.close()