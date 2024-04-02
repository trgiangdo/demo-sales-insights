<|layout|columns=2 9|gap=50px|
<sidebar|sidebar|
Create and select **scenarios**

<|{selected_scenario}|scenario_selector|>
|sidebar>

<scenario|part|render={selected_scenario}|
# **Prediction**{: .color-primary} page

<|3 5|layout|
<date|
#### Level

A parameter to choose how holidays impact your predictions.

<|{selected_level}|slider|on_change=on_change_params|not continuous|min=70|max=150|>
|date>

<country|
#### **Holiday**{: .color-primary}

Upload the CSV of employee holidays:

<|expandable|title=Holidays|expanded=False|
<|{dn_holiday}|data_node|>
|>

<|{selected_holiday}|file_selector|label=Holiday|on_action=on_change_params|>
|country>
|>

Run your scenario

<|{selected_scenario}|scenario|on_submission_change=on_submission_change|not expanded|>

---------------------------------------

## **Predictions**{: .color-primary} and explorer of data nodes

<|{dn_result}|data_node|>
|scenario>
|>
