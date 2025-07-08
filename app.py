iface = gr.Interface(
    fn=predict_price,
    inputs=[gr.Dropdown(cities, label="City"),
            gr.Number(label="Area (sq.ft)"),
            gr.Number(label="No. of Rooms"),
            gr.Dropdown(urbans, label="Urban or Rural")],
    outputs="text",
    title="Indian House Price Predictor",
    description="Predict property price using city, area, number of rooms, and urban/rural status."
)

iface.launch()
