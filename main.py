from Simulation import Simulation
import PySimpleGUI as sg

def main():
    # Default parameters
    n = 10000
    alpha = 0.01
    recovery_days = 14
    transmission_rate = 0.015
    fatality_rate = 0.03
    initial_setting = 0.01

    options = ["Run simulation with lockdown (INTERACTIONS = 5)", "Run simulation without lockdown (INTERACTIONS = 60)",
               "View/Modify Parameters", "Exit"]
    mainmenu = [
        [sg.Button("Run simulation with lockdown (INTERACTIONS = 5)")],
        [sg.Button("Run simulation without lockdown (INTERACTIONS = 60)")],
        [sg.Button("View/Modify Parameters")],
        [sg.Button("Exit")],
        [sg.Text("""
                                𝔹𝕪 𝔹𝕣𝕖𝕟𝕕𝕖𝕟 𝕊𝕞𝕚𝕥𝕙
                                        """)]
    ]

    window = sg.Window("COVID-19 Python Simuation", mainmenu)

    while True:
        event, values = window.read()
        if event == options[3] or event == sg.WIN_CLOSED:
            break
        elif event == options[0]:
            Instance = Simulation(5, n, alpha, recovery_days, transmission_rate, fatality_rate, initial_setting)
            days = getDays()
            Instance.simulationGUI(days)
        elif event == options[1]:
            Instance = Simulation(60, n, alpha, recovery_days, transmission_rate, fatality_rate, initial_setting)
            days = getDays()
            Instance.simulationGUI(days)
        elif event == options[2]: # Modify parameters
            parameterGUI = sg.FlexForm('Simulation parameters')  # Declare GUI instance
            layout = [  # Form
                [sg.Text('n', size=(15, 1)), sg.InputText(n)],
                [sg.Text('ALPHA', size=(15, 1)), sg.InputText(alpha)],
                [sg.Text('RECOVERY_DAYS', size=(15, 1)), sg.InputText(recovery_days)],
                [sg.Text('TRANSMISSION_RATE', size=(15, 1)), sg.InputText(transmission_rate)],
                [sg.Text('FATALITY_RATE', size=(15, 1)), sg.InputText(fatality_rate)],
                [sg.Text('INITIAL_SETTING', size=(15, 1)), sg.InputText(initial_setting)],
                [sg.Submit(), sg.Cancel()]
            ]
            button, values = parameterGUI.Layout(layout).Read()  # Read user input
            if button == "Submit":  # If user submitted their results, override parameter values
                n = values[0]
                alpha = values[1]
                recovery_days = values[2]
                transmission_rate = values[3]
                fatality_rate = values[4]
                initial_setting = values[5]
            parameterGUI.close()  # Exit GUI

def getDays():
    layout = [
        [sg.Text('How many days would you like the simulation to run?')],
        [sg.InputText()],
        [sg.Submit()]
    ]
    daysgui = sg.FlexForm("Simulation Length", layout)
    while True:
        button, values = daysgui.read()
        try:
            days = int(values[0])
        except:
            sg.Popup("ERROR", "Value must be an integer")
        else:
            if days<1:
                sg.Popup("ERROR", "Value must be greater than 0")
            else:
                days = int(values[0])
                break
    daysgui.close()
    return days

if __name__ == "__main__":
    main()
