import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle
import os

app = Flask(__name__)
pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)


@app.route('/')
def home():
    return render_template('predict.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            Stall_no = float(request.form['Stall_no'])
            Market_Category = float(request.form['Market_Category'])
            Loyalty_customer = float(request.form['Loyalty_customer'])
            Product_Category = float(request.form['Product_Category'])
            Grade = float(request.form['Grade'])
            Demand = float(request.form['Demand'])
            Discount_avail = float(request.form['Discount_avail'])
            charges_1 = float(request.form['charges_1'])
            charges_2 = float(request.form['charges_2'])
            Maximum_price = float(request.form['Maximum_price'])
            pred_args = [Stall_no, Market_Category, Loyalty_customer, Product_Category, Grade, Demand, Discount_avail,
                         charges_1, charges_2, Maximum_price]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1, -1)
            model_prediction = model.predict(pred_args_arr)
            model_prediction = round(float(model_prediction), 2)
        except ValueError:
            return "Please check if the values are entered correctly"

    return render_template('predict.html', prediction_text='selling price would be {}'.format(model_prediction))

    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)


if __name__ == "__main__":
    #if os.environ['ENVIRONMENT'] == 'production':
        app.run(debug=True)
