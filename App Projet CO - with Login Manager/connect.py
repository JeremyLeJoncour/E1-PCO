import pandas as pd
import numpy as np
import mysql.connector
from twilio.rest import Client
from dotenv import load_dotenv

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, roc_auc_score, f1_score, log_loss, matthews_corrcoef, recall_score, precision_score
from sklearn.metrics import precision_recall_curve
import joblib
from colour import Color

# Importation des Fichiers de Modèles et Scaler :
colonnescaler = joblib.load('ProcessModel/ColonnesForScale.joblib')
scaler = joblib.load('ProcessModel/ScalerXGBC_BF.joblib')
colonnesmodel = joblib.load('ProcessModel/ColonnesXGBC_BF.joblib')
classifier = joblib.load('ProcessModel/XGBC_BF.joblib')

# Initialisation Twilio Client Alerte et Environnement :
load_dotenv()
twilio_client = Client()




# Fonction Alerte SMS
def alert(alerte):
    twilio_client.messages.create(
            body=f"Alerte Application : {alerte}",
            from_='+16815252835',
            to='+xxxxxxxxxxx')




def login(login, password):
    config = {
      'user': 'root',
      'password': 'root',
      'host': '127.0.0.1',
      'port': '3307',
      'database': 'authenticator',
      'raise_on_warnings': True,
    }

    # Création du Cursor
    link = mysql.connector.connect(**config)
    cursor = link.cursor(buffered=True)
    
    # Requêtes:
    query = """SELECT User_ID, Password FROM login WHERE login.User_ID = %s AND login.Password = %s"""
    cursor.execute(query, (login, password))
    rows = cursor.fetchall()

    sql = []
    for values in rows :
        sql.append(list(values))

    link.close()

    if len(sql) == 0:
        access = pd.DataFrame([[' ', ' ']], columns = ['identifiant', 'password'])
    
    else:
        access = pd.DataFrame(sql, columns = ['identifiant', 'password'])

    return access




def create_account(new_login, new_password):    
    config = {
      'user': 'root',
      'password': 'root',
      'host': '127.0.0.1',
      'port': '3307',
      'database': 'authenticator',
      'raise_on_warnings': True,
    }

    # Création du Cursor
    link = mysql.connector.connect(**config)
    cursor = link.cursor(buffered=True)
    
    query = """INSERT INTO login (Log_ID, User_ID, Password) VALUES (NULL, %s, %s)"""
    cursor.execute(query, (str(new_login), str(new_password)))
    link.commit()
    link.close()




def exist_user(login):
    login = str(login)
    config = {
      'user': 'root',
      'password': 'root',
      'host': '127.0.0.1',
      'port': '3307',
      'database': 'authenticator',
      'raise_on_warnings': True,
    }

    # Création du Cursor
    link = mysql.connector.connect(**config)
    cursor = link.cursor(buffered=True)
    
    # Requêtes:
    cursor.execute(f"SELECT User_ID FROM login WHERE login.User_ID = '{login}'")
   
    rows = cursor.fetchall()

    sql = []
    for values in rows :
        sql.append(list(values))
    link.close()

    if len(sql) == 0:
        access = pd.DataFrame([['0']], columns = ['identifiant'])
    
    else:
        access = pd.DataFrame(sql, columns = ['identifiant'])
        
    return access




def update_password(login, password):
    login = str(login)
    password = str(password)
    config = {
      'user': 'root',
      'password': 'root',
      'host': '127.0.0.1',
      'port': '3307',
      'database': 'authenticator',
      'raise_on_warnings': True,
    }

    # Création du Cursor
    link = mysql.connector.connect(**config)
    cursor = link.cursor(buffered=True)
    
    # Requêtes:
    cursor.execute(f"UPDATE login SET Password = '{password}' WHERE User_ID = '{login}'")
    link.commit()
    link.close()
    



def DB_dataset(year, month):
    config = {
      'user': 'root',
      'password': 'root',
      'host': '127.0.0.1',
      'port': '3307',
      'database': 'databasekkbox',
      'raise_on_warnings': True,
    }

    # Création du Cursor
    link = mysql.connector.connect(**config)
    cursor = link.cursor(buffered=True)
    
    if month < 10 :
        month = '0'+str(month)
    else :
        pass
    
    # Requêtes:
    query = """SELECT Transactions.payment_method_id, Transactions.payment_plan_days,
    Transactions.plan_list_price,Transactions.actual_amount_paid,Transactions.is_auto_renew,
    Transactions.transaction_date,Transactions.membership_expire_date,Transactions.is_cancel,
    Transactions.transaction_count,Transactions.price_per_day,User.msno 
    FROM transactions JOIN User on Transactions.User_ID = User.User_ID 
    WHERE MONTH(str_to_date(Transactions.membership_expire_date, '%Y-%m-%d')) = %s AND 
    YEAR(str_to_date(Transactions.membership_expire_date, '%Y-%m-%d')) = %s"""
    
    cursor.execute(query, (str(month),str(year)))
    rows_transaction = cursor.fetchall()

    Transactions_sql = []
    for values in rows_transaction :
        Transactions_sql.append(list(values))

    cursor.execute("""SELECT Logs.num_25Sum, Logs.num_50Sum, Logs.num_75Sum, Logs.num_985Sum, 
    Logs.num_100Sum, Logs.num_unqSum, Logs.total_secsSum, Logs.num_25Mean, Logs.num_50Mean, 
    Logs.num_75Mean, Logs.num_985Mean, Logs.num_100Mean, Logs.num_unqMean, Logs.total_secsMean, 
    Logs.count, User.msno FROM Logs JOIN User on Logs.User_ID = User.User_ID""")
    rows_logs = cursor.fetchall()

    Logs_sql = []
    for values in rows_logs :
        Logs_sql.append(list(values))

    cursor.execute("""SELECT Members.city, Members.bd, Members.gender, Members.registered_via, 
    Members.registration_init_time, Members.days_fidelity, User.msno FROM Members 
    JOIN User on Members.User_ID = User.User_ID""")
    rows_members = cursor.fetchall()

    Members_sql = []
    for values in rows_members :
        Members_sql.append(list(values))

    link.close()

    # Transformation en DataFrame:    
    Transactions_sql = pd.DataFrame(Transactions_sql, columns = [
        'payment_method_id', 'payment_plan_days', 
        'plan_list_price', 'actual_amount_paid', 'is_auto_renew', 
        'transaction_date', 'membership_expire_date', 'is_cancel', 
        'transaction_count', 'price_per_day', 'msno'])

    Logs_sql = pd.DataFrame(Logs_sql, columns = [
        'num_25Sum', 'num_50Sum', 'num_75Sum', 'num_985Sum', 'num_100Sum',
        'num_unqSum', 'total_secsSum', 'num_25Mean', 'num_50Mean', 'num_75Mean',
        'num_985Mean', 'num_100Mean', 'num_unqMean', 'total_secsMean', 
        'count', 'msno'])

    Members_sql = pd.DataFrame(Members_sql, columns = [
        'city', 'bd', 'gender', 'registered_via', 'registration_init_time', 
        'days_fidelity', 'msno'])

    main = pd.merge(Transactions_sql, Logs_sql, on='msno', how='inner')
    main = pd.merge(main, Members_sql, on='msno', how='inner')

    bd_list = []
    for i in main['bd']:
        if i == 'inconnu':
            bd_list.append(-1)
        
        else:
            bd_list.append(int(i))

    main['bd'] = bd_list

    return main




def preprocessing(f):
    main = pd.read_csv(f)
    bd_list = []
    for i in main['bd']:
        if i == 'inconnu':
            bd_list.append(-1)
        
        else:
            bd_list.append(int(i))

    main['bd'] = bd_list
    
    return main




def Format_intdate(serie):
    Liste = []
    for i in serie:
        y = i[:4]
        m = i[5:7]
        d = i[8:]
        i = f'{y}{m}{d}'
        i = int(i)
        Liste.append(i)

    return Liste




def prediction(dataset):
    Test = dataset.copy()

    # Suppression des variables temporelles:
    Test = Test.drop(['transaction_date'], axis = 1)
    Test['membership_expire_date'] = Format_intdate(Test['membership_expire_date'])
    Test['registration_init_time'] = Format_intdate(Test['registration_init_time'])

    # Afin d'effectuer un futur encodage:
    Test['city'] = [str(i)+'C' for i in Test.city]
    Test['payment_method_id'] = [str(i)+'P' for i in Test.payment_method_id]
    Test['registered_via'] = [str(i)+'R' for i in Test.registered_via]

    # Encodage:
    Test = pd.concat([Test, pd.get_dummies(Test.gender)], axis = 1)
    Test = pd.concat([Test, pd.get_dummies(Test.payment_method_id)], axis = 1)
    Test = pd.concat([Test, pd.get_dummies(Test.registered_via)], axis = 1)
    Test = pd.concat([Test, pd.get_dummies(Test.city)], axis = 1)

    for feature in colonnescaler:
        if feature not in Test.columns:
            Test[feature]=0

    Test = Test[colonnescaler]
    X_test = Test.drop(['msno','is_churn'], axis = 1)

    # Standardisation des données Test avec le scaler fit sur données d'entrainement pour l'intégration Web
    X_test2 = pd.DataFrame(scaler.transform(X_test.values))
    X_test2.columns = X_test.columns.values
    X_test2.index = X_test.index.values
    X_test = X_test2

    X_test = X_test[colonnesmodel]

    y_pred = classifier.predict(X_test)
    probability = classifier.predict_proba(X_test)
    probability = probability[:,1]

    final_results = Test
    final_results['predictions'] = y_pred
    final_results['membership_expire_date'] = dataset['membership_expire_date']
    final_results["propensity_to_churn(%)"] = probability
    final_results["propensity_to_churn(%)"] = final_results["propensity_to_churn(%)"]*100
    final_results["propensity_to_churn(%)"] = final_results["propensity_to_churn(%)"].astype(int)
    final_results = final_results.sort_values(by=['propensity_to_churn(%)'], ascending = False)

    final_results.index.msno=None
    final_results.head(10)
    
    liste = []
    for i in final_results["propensity_to_churn(%)"]:
        if i <= 25.0:
            i = 'Risque faible'
        
        elif 50.0 >= i > 25.0:
            i = 'Risque modéré'
        
        elif 75.0 >= i > 50.0:
            i = 'Risque élevé'
        
        else:
            i = 'Risque très élevé'
        liste.append(i)
    
    final_results["Risk"] = liste
    final_results = final_results.sort_values(by=['propensity_to_churn(%)'],  ascending = False)
    final_results.set_index(['msno'], inplace = False)
    final_results.index.msno=None
    
    return final_results




def plot(dataset):
    pred25 = len(dataset[dataset['propensity_to_churn(%)']<=25.00])
    
    pred50 = len(dataset[(25.00<dataset['propensity_to_churn(%)']) & 
                                  (dataset['propensity_to_churn(%)']<=50.00)])

    pred75 = len(dataset[(50.00<dataset['propensity_to_churn(%)']) & 
                                  (dataset['propensity_to_churn(%)']<=75.00)])
    
    pred90 = len(dataset[(75.00<dataset['propensity_to_churn(%)']) & 
                                  (dataset['propensity_to_churn(%)']<=90.00)])
    
    pred95 = len(dataset[dataset['propensity_to_churn(%)']>90.00])
    
    name = 'name'
    y = 'y'
    z = 'z'

    list_of_dico = [{name : 'Inférieur à 25%', y : pred25, z : 70},
                    {name : 'Entre 25 et 50%', y : pred50, z : 95}, 
                    {name : 'Entre 50 et 75%', y : pred75, z : 120}, 
                    {name : 'Entre 75 et 90%', y : pred90, z : 155}, 
                    {name : 'Supérieur à 90%', y : pred95, z : 190}]
    
    return list_of_dico




def gradient_color(start_color, end_color, step):
    colors = list(Color(start_color).range_to(Color(end_color),step))
    gradient = []
    colorsrgb = [i.rgb for i in colors]
    for i in colorsrgb:
        tr = list()
        
        for j in i:
            j = int(j*255)
            tr.append(j)
        gradient.insert(0, tuple(tr))

    return gradient


    

def process_estimation(dictionnaire):
    df_estimation = dictionnaire

    # Suppression des variables temporelles:
    df_estimation['membership_expire_date'] = Format_intdate(df_estimation['membership_expire_date'])
    df_estimation['registration_init_time'] = Format_intdate(df_estimation['registration_init_time'])

    # Afin d'effectuer un futur encodage:
    df_estimation['payment_method_id'] = [str(i)+'P' for i in df_estimation.payment_method_id]
    df_estimation['registered_via'] = [str(i)+'R' for i in df_estimation.registered_via]

    # Encodage:
    df_estimation = pd.concat([df_estimation, pd.get_dummies(df_estimation.payment_method_id)],1)
    df_estimation = pd.concat([df_estimation, pd.get_dummies(df_estimation.registered_via)],1)

    for feature in colonnescaler:
        if feature not in df_estimation.columns:
            df_estimation[feature]=0

    df_estimation = df_estimation[colonnescaler]
    X_test = df_estimation
    X_test = df_estimation.drop(['msno','is_churn'], axis = 1)
    
    # Standardisation des données Test avec le scaler fit sur données d'entrainement pour l'intégration Web
    X_test2 = pd.DataFrame(scaler.transform(X_test.values))
    X_test2.columns = X_test.columns.values
    X_test2.index = X_test.index.values
    X_test = X_test2

    X_test = X_test[colonnesmodel]
    
    probability = classifier.predict_proba(X_test)
    probability = round(probability[:,1][0]*100,2)

    return probability




def select_sim():
    dataset = pd.read_csv('Import_demonstration.csv')
    
    return dataset




def js_csv(dataset):
    datajs = dataset.values.tolist()
    
    return datajs




def evaluation(dataset):
    Test = dataset.copy()

    # Suppression des variables temporelles:
    Test = Test.drop(['transaction_date'], 1)
    Test['membership_expire_date'] = Format_intdate(Test['membership_expire_date'])
    Test['registration_init_time'] = Format_intdate(Test['registration_init_time'])

    # Afin d'effectuer un futur encodage:
    Test['city'] = [str(i)+'C' for i in Test.city]
    Test['payment_method_id'] = [str(i)+'P' for i in Test.payment_method_id]
    Test['registered_via'] = [str(i)+'R' for i in Test.registered_via]

    # Encodage:
    Test = pd.concat([Test, pd.get_dummies(Test.gender)],1)
    Test = pd.concat([Test, pd.get_dummies(Test.payment_method_id)],1)
    Test = pd.concat([Test, pd.get_dummies(Test.registered_via)],1)
    Test = pd.concat([Test, pd.get_dummies(Test.city)],1)

    for feature in colonnescaler:
        if feature not in Test.columns:
            Test[feature]=0

    Test = Test[colonnescaler]
    X_test = Test.drop(['msno','is_churn'], axis = 1)
    y_test = Test['is_churn']

    # Standardisation des données Test avec le scaler fit sur données d'entrainement pour l'intégration Web
    X_test2 = pd.DataFrame(scaler.transform(X_test.values))
    X_test2.columns = X_test.columns.values
    X_test2.index = X_test.index.values
    X_test = X_test2

    X_test = X_test[colonnesmodel]

    y_pred = classifier.predict(X_test)
    probability = classifier.predict_proba(X_test)
    probability = probability[:,1]

    matrix = confusion_matrix(y_test, y_pred)

    final_results = Test
    final_results['predictions'] = y_pred
    final_results["propensity_to_churn(%)"] = probability
    final_results["propensity_to_churn(%)"] = final_results["propensity_to_churn(%)"]*100
    final_results["propensity_to_churn(%)"] = final_results["propensity_to_churn(%)"].astype(int)
    final_results = final_results[['predictions', 'propensity_to_churn(%)', 'is_churn']]

    # Faux Négatifs:
    False_Neg = final_results.loc[final_results['is_churn'] == 1]
    False_Neg = False_Neg.loc[final_results['predictions'] == 0]

    # Vrai Positifs:
    True_Pos = final_results.loc[final_results['is_churn'] == 1]
    True_Pos = True_Pos.loc[final_results['predictions'] == 1]

    list_0, list_10,  list_20,  list_30, list_40, list_50 = [],[],[],[],[],[]
    list_60, list_70, list_80,  list_90 = [],[],[],[]

    for i in False_Neg['propensity_to_churn(%)']:
        if  i < 10:
            list_0.append(i)
        if 10 <= i < 20:
            list_10.append(i)
        if 20 <= i < 30:
            list_20.append(i)
        if 30 <= i < 40:
            list_30.append(i)
        if 40 <= i < 50:
            list_40.append(i)
        if 50 <= i < 60:
            list_50.append(i)
        if 60 <= i < 70:
            list_60.append(i)
        if 70 <= i < 80:
            list_70.append(i)
        if 80 <= i < 90:
            list_80.append(i)
        if 90 <= i <= 100:
            list_90.append(i)
            
    data_False = [len(list_0), len(list_10), len(list_20), len(list_30), len(list_40), 
                len(list_50), len(list_60), len(list_70), len(list_80), len(list_90)]

    list_0, list_10,  list_20,  list_30, list_40, list_50 = [],[],[],[],[],[]
    list_60, list_70, list_80,  list_90 = [],[],[],[]

    for i in True_Pos['propensity_to_churn(%)']:
        if  i < 10:
            list_0.append(i)
        if 10 <= i < 20:
            list_10.append(i)
        if 20 <= i < 30:
            list_20.append(i)
        if 30 <= i < 40:
            list_30.append(i)
        if 40 <= i < 50:
            list_40.append(i)
        if 50 <= i < 60:
            list_50.append(i)
        if 60 <= i < 70:
            list_60.append(i)
        if 70 <= i < 80:
            list_70.append(i)
        if 80 <= i < 90:
            list_80.append(i)
        if 90 <= i <= 100:
            list_90.append(i)
            
    data_True = [len(list_0), len(list_10), len(list_20), len(list_30), len(list_40), 
                len(list_50), len(list_60), len(list_70), len(list_80), len(list_90)]

    auc = roc_auc_score(y_test, probability)
    logloss = log_loss(y_test, probability)
    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    mcc = matthews_corrcoef(y_test, y_pred)
    
    curve_precision, curve_recall, _ = precision_recall_curve(y_test, probability)
    data_curve = [[i,j] for i, j in zip(list(curve_precision), list(curve_recall))]

    return (matrix, data_False, data_True, logloss, auc, f1, mcc, recall, precision,
    data_curve)




def update_score(Date, loss, auc, scoreF, scoremcc, recall, precision, Total):
    config = {
            'user': 'root',
            'password': 'root',
            'host': '127.0.0.1',
            'port': '3307',
            'database': 'log_model',
            'raise_on_warnings': True,
            }

    # Création du Cursor
    link = mysql.connector.connect(**config)
    cursor = link.cursor(buffered=True)
    
    # Requêtes:
    query = """INSERT INTO log_model (`Date`, `Log_loss`, `Score AUC`, `Score F1`, 
    `Score MCC`, `Recall`, `Precision`, `Instances`, `ID`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NULL)"""
    values = ((Date), float(loss), float(auc), float(scoreF), float(scoremcc), float(recall), float(precision), int(Total))
    cursor.execute(query, values)
    
    link.commit()
    link.close()




def export_score():
    config = {
            'user': 'root',
            'password': 'root',
            'host': '127.0.0.1',
            'port': '3307',
            'database': 'log_model',
            'raise_on_warnings': True,
            }

    # Création du Cursor
    link = mysql.connector.connect(**config)
    cursor = link.cursor(buffered=True)
    
    # Requêtes:
    cursor.execute("""SELECT * FROM log_model""")
    rows = cursor.fetchall()

    log_model = []
    for values in rows :
        log_model.append(list(values))

    df_model = pd.DataFrame(log_model, columns=['Date','Log_loss', 'Score AUC', 'Score F', 'Score MCC', 'Recall', 'Precision',
                                           'Instances', 'ID'])
    datestr = []
    for i in df_model['Date']:
        convert = i.strftime("%d-%m-%Y")
        datestr.append(convert)
    
    df_model['Date'] = datestr

    link.close()
    
    return df_model
    