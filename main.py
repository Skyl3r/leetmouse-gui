import PySimpleGUIQt as sg
from ModuleParameter import ModuleParameter

Parameters = {
    "Acceleration": ModuleParameter("Acceleration"),
    "Sensitivity": ModuleParameter("Sensitivity"),
    "Post Scale X": ModuleParameter("PostScaleX"),
    "Post Scale Y": ModuleParameter("PostScaleY"),
    "Pre Scale X": ModuleParameter("PreScaleX"),
    "Pre Scale Y": ModuleParameter("PreScaleY"),
    "Speed Cap": ModuleParameter("SpeedCap"),
    "Offset": ModuleParameter("Offset"),
    "Scrolls per Tick": ModuleParameter("ScrollsPerTick"),
}

UpdateParameter = ModuleParameter("update")

layout = [
    [sg.Text("leetmouse GUI")]
]

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

        UpdateParameter.set("1")

    if event == sg.WIN_CLOSED:
        break



window.close()