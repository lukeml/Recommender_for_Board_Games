from flask import Flask, request, render_template
from make_prediction_nlp import get_described, get_games

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index_nlp.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/describe_game/', methods=['GET', 'POST'])
def desc():

    user_input = request.form['your_description']

    # show user final message
    final_message = get_described(user_input)
    
    return render_template('index_nlp.html',  tables=[final_message.to_html(classes='data')], titles=final_message.columns.values)
    
    
# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/similar_game/', methods=['GET', 'POST'])
def similar():
   
    user_input = request.form['your_index']

    # show user final message
    final_message = get_games(user_input)
    
    return render_template('index_nlp.html',  tables=[final_message.to_html(classes='data')], titles=final_message.columns.values)

 

 

 




if __name__ == '__main__':
    app.run(debug=True)