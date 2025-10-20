import machining_formulas as mf
import FreeSimpleGUI as sg
import os

sg.theme('black')
spacer = sg.Text("", size=(5, 1))
spacer2 = sg.Text("", size=(5, 1))

# SFM widgets
sfm_label = sg.Text("Surface Feet Per Minute:")
sfm_tool_diameter_label = sg.Text("Tool Diameter: ")
sfm_tool_diameter = sg.InputText(key='sfm_tool_diameter', size=(20, 20))
sfm_spindle_speed_label = sg.Text("Spindle Speed:")
sfm_spindle_speed = sg.InputText(key='sfm_spindle_speed', size=(20, 20))
sfm_calculate_button = sg.Button("Calculate SFM", key='sfm_calculate')
sfm_result_label = sg.Text("", key='sfm_result', text_color='white')


# RPM/Spindle Speed widgets
rpm_label = sg.Text("RPM/Spindle Speed:")
rpm_tool_diameter_label = sg.Text("Tool Diameter:")
rpm_tool_diameter = sg.InputText(key='rpm_tool_diameter', size=(20, 20))
rpm_spindle_speed_label = sg.Text("Feed Rate:     ")
rpm_spindle_speed = sg.InputText(key='rpm_feed_rate', size=(20, 20))
rpm_calculate_button = sg.Button("Calculate Spindle Speed", key='rpm_calculate')
rpm_result_label = sg.Text("", key='rpm_result', text_color='white')


# Feed Rate Widgets
fr_label = sg.Text("Feed Rate:")
fr_feed_per_tooth_label = sg.Text("Feed Per Tooth:")
fr_feed_per_tooth = sg.InputText(key='fr_feed_per_tooth', size=(20, 20))
fr_spindle_speed_label = sg.Text("Spindle Speed: ")
fr_spindle_speed = sg.InputText(key='fr_spindle_speed', size=(20, 20))
fr_num_teeth_label = sg.Text("Num of Teeth:   ")
fr_num_teeth = sg.InputText(key='fr_num_teeth', size=(20, 20))
fr_calculate_button = sg.Button("Calculate Feed ", key='fr_calculate')
fr_result_label = sg.Text("", key='fr_result', text_color='white')


# Material Removal Rate Widgets
mrr_label = sg.Text("Material Removal Rate:")
mrr_width_of_cut_label = sg.Text("Width of Cut:")
mrr_width_of_cut = sg.InputText(key='mrr_width_of_cut', size=(20, 20))
mrr_depth_of_cut_label = sg.Text("Depth of Cut:")
mrr_depth_of_cut = sg.InputText(key='mrr_depth_of_cut', size=(20, 20))
mrr_feed_rate_label = sg.Text("Feed Rate:   ")
mrr_feed_rate = sg.InputText(key='mrr_feed_rate', size=(20, 20))
mrr_calculate_button = sg.Button("Calculate MRR ", key='mrr_calculate')
mrr_result_label = sg.Text("", key='mrr_result', text_color='white')


left_column_content = [[sfm_label],
                       [sfm_tool_diameter_label, sfm_tool_diameter],
                       [sfm_spindle_speed_label, sfm_spindle_speed],
                       [sfm_calculate_button, sfm_result_label],
                       [spacer],
                       [fr_label],
                       [fr_feed_per_tooth_label, fr_feed_per_tooth],
                       [fr_spindle_speed_label, fr_spindle_speed],
                       [fr_num_teeth_label, fr_num_teeth],
                       [fr_calculate_button, fr_result_label]]

right_column_content = [[rpm_label],
                        [rpm_tool_diameter_label, rpm_tool_diameter],
                        [rpm_spindle_speed_label, rpm_spindle_speed],
                        [rpm_calculate_button, rpm_result_label],
                        [spacer2],
                        [mrr_label],
                        [mrr_width_of_cut_label, mrr_width_of_cut],
                        [mrr_depth_of_cut_label, mrr_depth_of_cut],
                        [mrr_feed_rate_label, mrr_feed_rate],
                        [mrr_calculate_button, mrr_result_label]]

left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)

window = sg.Window('Machine Shop Calculator', layout=[[left_column, right_column]])

# displays window
while True:
    event, values = window.read()
    print(1, f'Event: {event}')
    print(2, f'Values: {values}')

    try:
        match event:
            case "sfm_calculate":
                td = float(values['sfm_tool_diameter'])
                ss = float(values['sfm_spindle_speed'])
                sfm = round(mf.calc_sfm_inches(td, ss),2)
                window['sfm_result'].update(value=f'SFM: {sfm}')

            case "rpm_calculate":
                td = float(values['rpm_tool_diameter'])
                fr = float(values['rpm_feed_rate'])
                rpm = round(mf.calc_rpm_inches(td, fr))
                window['rpm_result'].update(value=f'Spindle Speed: {rpm}')

            case 'fr_calculate':
                fpt = float(values['fr_feed_per_tooth'])
                ss = float(values['fr_spindle_speed'])
                num_of_teeth = float(values['fr_num_teeth'])
                feed_rate = round(mf.calc_feed_rate_inches(fpt, ss, num_of_teeth))
                window['fr_result'].update(value=f'Feed Rate: {feed_rate}')

            case 'mrr_calculate':
                woc = float(values['mrr_width_of_cut'])
                doc = float(values['mrr_depth_of_cut'])
                fr = float(values['mrr_feed_rate'])
                mrr = round(mf.calc_material_removal_rate(woc, doc, fr))
                window['mrr_result'].update(value=f'MRR: {mrr} inches\u00B3',)

            case sg.WIN_CLOSED:
                break
    except ValueError:
        sg.popup("Please enter numbers only.", text_color='Red')
    except ZeroDivisionError:
        sg.popup("Enter a number greater than 0.")







