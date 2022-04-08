#import os
#os.add_dll_directory("C:\\Users\\utilisateur\\anaconda3\\envs\\TEST\\DLLs")
from flask import Flask, redirect, url_for, render_template, request, session, abort
import flask_monitoringdashboard as dashboard

import re
import pandas as pd
from random import randrange
from time import gmtime, strftime
from datetime import datetime
import connect

app = Flask(__name__)
dashboard.config.init_from(file='/config.cfg')
app.config['SECRET_KEY'] = 'adrammalech'

dashboard.bind(app)

@app.route('/',methods=['GET','POST'])
def login():
    try:

        if request.method == "POST":
            session.permanent = True
            user = request.form["Login"]

            form = request.form
            login = form.get("Login")
            password = form.get("Password")
            compare = connect.login(login, password)
            enter_login = compare['identifiant'][0]
            enter_password = compare['password'][0]

            if login != enter_login or password != enter_password:
                return render_template("index.html")
            
            else:	
                session["user"] = user
                return redirect(url_for("user"))
        else:
            if "user" in session:
                return redirect(url_for("user"))
            
        return render_template("index.html")
    
    except:
        return render_template("error.html"), 500





@app.route('/create_account',methods=['GET','POST'])
def account():
    try:

        alerte = ''
        if request.method == 'POST':
            form = request.form
            login = form.get("Login")
            password = form.get("Password")
            confirm = form.get("Confirmation")

            if login == '' or password =='':
                alerte = 'Entrez un identifiant et un mot de passe valides !'
                alerte_color = '#c439399d'
                

            else:
                if len(login) < 8 :
                    alerte = 'Entrez un identifiant valide !'
                    alerte_color = '#c439399d'

                elif password != confirm:
                    alerte = 'Mots de passe saisis invalides !'
                    alerte_color = '#c439399d'

                else:
                    verif = connect.exist_user(login)['identifiant'][0]
                    print(f'verif : {verif}')
                    
                    if str(login) != verif:
                        pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%!*^&+=]).*$"
                        result = re.findall(pattern, password)
                        
                        if (result):
                            connect.create_account(str(login), str(password))
                            alerte = 'Compte créé !'
                            alerte_color = '#0c7cbd85'

                        else :
                            alerte = 'Mots de passe saisis invalides !'
                            alerte_color = '#c439399d'
                    else:
                        alerte = 'Identifiant indisponible'
                        alerte_color = '#c439399d'

            return render_template('create_account.html',  alerte = alerte, login = login, password = password, 
            confirm = confirm, alerte_color = alerte_color)
        
        return render_template('create_account.html', alerte = alerte)

    except:
        return render_template('error.html'), 500




@app.route('/password',methods=['GET','POST'])
def password():
    try:
        
        alerte = ''
        if request.method == 'POST':
            form = request.form
            login = form.get("Login")
            password = form.get("Password")

            if login == '' or password =='':
                alerte = 'Entrez un identifiant et un mot de passe valides !'
                alerte_color = '#c439399d'
                
            else:
                
                if len(login) < 8:
                    alerte = 'Entrez un identifiant et un mot de passe valides !'
                    alerte_color = '#c439399d'

                else:
                    verif = connect.exist_user(login)['identifiant'][0]
                    
                    if str(login) == verif:
                        pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%!*^&+=]).*$"
                        result = re.findall(pattern, password)
                        
                        if (result):
                            connect.update_password(login, password)
                            alerte = 'Mot de passe Changé !'
                            alerte_color = '#0c7cbd85'
                        
                        else :
                            alerte = 'Nouveau mot de passe saisi invalide !'
                            alerte_color = '#c439399d'
                    
                    else:
                        alerte = 'Identifiant incorrect'
                        alerte_color = '#c439399d'

            return render_template('password.html',  alerte = alerte, login = login, password = password, 
            alerte_color = alerte_color)
        
        return render_template('password.html', alerte = alerte)

    except:
        return render_template('error.html'), 500


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        year = [2017, 2018, 2019, 2020]
        month = list(range(1, 13, 1))
        return render_template("access.html", user = user, year = year, month = month)
    
    else:
        return redirect(url_for("login"))




@app.route('/database', methods=['GET','POST'])
def database():
    try:

        if "user" in session:
            user = session["user"]
            
            if request.method == 'POST':
                form = request.form
                year = form.getlist("year")
                year = int(year[0])

                month = form.getlist("month")
                month = int(month[0])

                main = connect.DB_dataset(year, month)
                
                Results = connect.prediction(main)[['msno', 'membership_expire_date', 'propensity_to_churn(%)']]
                nb_msno = len(Results)

                Results9 = Results[:9]
                Results9.columns = ['Identifiant', 'Expiration Abonnement', 'Risque de Partir (%)']
                dico_month = {'Janvier': 1, 'Février': 2, 'Mars': 3, 'Avril': 4, 'Mai': 5, 'Juin': 6, 
                'Juillet': 7, 'Août': 8, 'Septembre': 9, 'Octobre': 10, 'Novembre': 11, 'Décembre': 12}

                for key, value in dico_month.items():
                    if value == month:
                        month_key = key

                list_of_dico = connect.plot(Results)

                data_js = connect.js_csv(Results)
                filename = f'{year}_{month}_Results_Upload.csv'

                return render_template(
                    'database.html', tables = [Results9.to_html(classes ='table', index = False)], year = year,
                    month = month, month_key = month_key, nb_msno = nb_msno, data_js = data_js, 
                    list_of_dico = list_of_dico, filename = filename, user = user)
        
        else:
            return redirect(url_for("login"))
        
    except:
        return render_template("error.html"), 500



@app.route('/importCSV',methods=['GET','POST'])
def importCSV():
    try:

        if "user" in session:
            user = session["user"]
            
            if request.method == 'POST':
                f = request.form['csvfile']
                main = connect.preprocessing(f)
                Results = connect.prediction(main)[['msno', 'membership_expire_date', 'propensity_to_churn(%)']]
                nb_msno = len(Results)

                Results9 = Results[:9]
                Results9.columns = ['Identifiant', 'Expiration Abonnement', 'Risque de Partir (%)']
                list_of_dico = connect.plot(Results)

                Results.columns = ['Identifiant', 'Expiration Abonnement', 'Risque de Partir (%)']
                data_js = connect.js_csv(Results)

                return render_template(
                    'importCSV.html', tables = [Results9.to_html(classes ='table', index = False)],
                    nb_msno = nb_msno, data_js = data_js, list_of_dico = list_of_dico, user = user)
        else:
            return redirect(url_for("login"))
    
    except:
        return render_template("error.html"), 500



@app.route('/user/simulation',methods=['GET','POST'])
def test():
    if "user" in session:
        user = session["user"]
        lists = ['Abonné', 'Désabonné']
        prediction = 0
        target = 0
        color = connect.gradient_color("#b8446b", "#4493b8",101)
        color_pred = color[prediction]
        color_target = color[target]
        img_result = 'arrow-repeat'
        Results = pd.DataFrame(columns=['Informations'])
        target_text = '?'
        prediction_text = '?'

        if request.method == 'POST':
            form = request.form
            Results = simulation(form)[1]
            prediction = simulation(form)[0]
            target = Results.iloc[6][0]
            color_pred = color[prediction]
            
            if target == 0:
                target_text = 'Abonné'
                color_target = color[target]      
            
            elif target == 1:
                target = 100
                target_text = 'Désabonné'
                color_target = color[target]

            if prediction < 50:
                prediction_text = 'Abonné'
            
            else:
                prediction_text = 'Désabonné'

            if target_text != prediction_text:
                img_result = 'down'
            
            else:
                img_result = 'up'


        return render_template('simulation.html', lists = lists, prediction = prediction, 
        color_pred = color_pred, color_target = color_target, tables = [Results[:5].to_html(classes ='table', index = True)], 
        target_text = target_text, prediction_text = prediction_text, img_result = img_result, user = user)

    else:
        return redirect(url_for("login"))

def simulation(form):
   
    is_churn = request.form['is_churn']
    if is_churn == 'Abonné':
        is_churn = 0
    
    elif is_churn == 'Désabonné':
        is_churn = 1
    
    else:
        is_churn = randrange(1)

    dataset = connect.select_sim()
    dataset = dataset.loc[dataset['is_churn'] == is_churn]
    dataset = dataset.sample(n=1)
    Results = dataset[['msno', 'membership_expire_date', 'registration_init_time', 'total_secsSum', 'transaction_count', 'is_cancel', 'is_churn']]
    Results.columns = ['Identifiant', 'Expiration Abonnement', 'Date d\'inscription', 'Ecoutes totales (s)', 'Nombre de Transactions', 'Annulation','Rupture']
    value = [i for i in Results.values]
    Results = pd.DataFrame(value[0], columns = ['Informations'], index = Results.columns.tolist())
    
    prediction = int(connect.process_estimation(dataset))
    return (prediction, Results)




@app.route('/performance',methods=['GET','POST'])
def performance():
    try:

        if "user" in session:
            user = session["user"]
            
            if request.method == 'POST':
                f = request.form['csvfile']
                main = connect.preprocessing(f)
                
                matrix = connect.evaluation(main)[0]
                matrix_color = connect.gradient_color("#3972b3", "#001224", 100)
                Total = matrix.sum()
                TrueN = round((matrix[0][0]/Total)*100, 2)
                matrix_colorTN = matrix_color[int(TrueN)]
                FalseP = round((matrix[0][1]/Total)*100, 2)
                matrix_colorFP = matrix_color[int(FalseP)]
                FalseN = round((matrix[1][0]/Total)*100, 2)
                matrix_colorFN = matrix_color[int(FalseN)]
                TrueP = round((matrix[1][1]/Total)*100, 2)
                matrix_colorTP = matrix_color[int(TrueP)]
                gradient = ["#3972b3", "#001224"]
            
                data_False = connect.evaluation(main)[1]
                data_True = connect.evaluation(main)[2]
                
                loss = round(connect.evaluation(main)[3], 4)
                auc = round(connect.evaluation(main)[4], 4)
                scoreF = round(connect.evaluation(main)[5], 4)
                scoremcc = round(connect.evaluation(main)[6], 4)
                recall = round(connect.evaluation(main)[7], 4)
                precision = round(connect.evaluation(main)[8], 4)
                
                data_curve = list(connect.evaluation(main)[9])

                time = strftime("Evaluation du modèle effectuée le %d-%m-%Y à %H:%M:%S", gmtime())
                data0 = matrix[0][0] + matrix[0][1]
                data1 = matrix[1][0] + matrix[1][1]

                dict_score = {  'Date d\'évaluation': strftime("%d-%m-%Y %H:%M:%S", gmtime()),
                                'Log Loss':loss,
                                'Score AUC':auc,
                                'Score F1':scoreF,
                                'Score MCC':scoremcc,
                                'Recall':recall,
                                'Precision':precision,
                                'True Positive':TrueP,
                                'True Negative':TrueN,
                                'False Positive':FalseP,
                                'False Negative':FalseN,
                                'Nombre d\'instances Test': Total    
                            }

                
                datedB = datetime.now()
                Date = datedB.strftime('%Y-%m-%d %H:%M:%S')
                sauvegarde = pd.DataFrame([[i for i in dict_score.values()]], columns = [i for i in dict_score.keys()])
                sauvegarde = connect.js_csv(sauvegarde)
                
                connect.update_score(Date, loss, auc, scoreF, scoremcc, recall, precision, Total)

                df = connect.export_score()
                date_valuate = df['Date'].tolist()
                hist_loss = df['Log_loss'].tolist()
                hist_AUC = df['Score AUC'].tolist()
                hist_F1 = df['Score F'].tolist()
                hist_MCC = df['Score MCC'].tolist()
                hist_Recall = df['Recall'].tolist()
                hist_Precision = df['Precision'].tolist()

                return render_template(
                    'performance.html', matrix = matrix, TrueN = TrueN, FalseP = FalseP, FalseN = FalseN, 
                    TrueP = TrueP, matrix_colorTN = matrix_colorTN, matrix_colorFP = matrix_colorFP,
                    matrix_colorFN = matrix_colorFN, matrix_colorTP = matrix_colorTP, gradient = gradient,
                    data_False = data_False, data_True = data_True, loss = loss, auc = auc, scoreF= scoreF,
                    scoremcc = scoremcc, recall = recall, precision = precision, time = time,
                    data_curve = data_curve, data0 = data0, data1 = data1, sauvegarde = sauvegarde, 
                    user = user, date_valuate = date_valuate, hist_AUC = hist_AUC, hist_F1 = hist_F1, 
                    hist_MCC = hist_MCC, hist_Recall = hist_Recall, hist_Precision = hist_Precision, 
                    hist_loss = hist_loss)
        else:
            return redirect(url_for("login"))
            
    except:
        return render_template("error.html"), 500




@app.route("/user/information")
def information():
    if "user" in session:
        user = session["user"]
        return render_template('information.html', user = user)
    
    else:
        return redirect(url_for("login"))




@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug = True, port=5051, host='127.0.0.1')