from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# open file with pickle
file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        print(request.form)
        mydict = request.form
        fever = int(mydict['fever'])
        age = int(mydict['age'])
        bodyPain = int(mydict['bodyPain'])
        runnyNose = int(mydict['runnyNose'])
        diffBreath = int(mydict['diffBreath'])
    # Code for inference
    #input_features = [102, 1, 12, -1, 0]  # this gives the probablity of % getting the percentage
        input_features = [fever,bodyPain,age,runnyNose,diffBreath]
        infection_prob = clf.predict_proba([input_features])[0][1]
        print(infection_prob)
        return  render_template('show.html',inf = round(infection_prob*100))
    return render_template('index.html')
    # return 'Hello, World!'+str(infection_prob)


if __name__ == '__main__':
    app.run(debug=True)
