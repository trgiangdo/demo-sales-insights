# Sales **Dashboard**{: .color-primary}

<|{Icon('', username)}|button|on_action={lambda s: navigate(s, 'login', force=True)}|class_name=login_button plain|>

<|1 1 1|layout|
<total_sales|
# **Total**{: .color-primary} sales:
### US $ <|{int(data["Total"].sum())}|text|raw|>
|total_sales>

<average_rating|
# Average **Rating**{: .color-primary}:
### <|{round(data["Rating"].mean(), 1)}|text|raw|>
|average_rating>

<average_sale|
# Average **Sales**{: .color-primary}:
### US $ <|{round(data["Total"].mean(), 2)}|text|raw|>
|average_sale>
|>

<center>
<|navbar|lov={[('/Overview', 'Overview'), ('/Analysis', 'Analysis'), ('/Predictions', 'Predictions'), ('/Admin', 'Admin')]}|>
</center>

<|Data|expandable|expanded=False|
<|{data}|table|>
|>