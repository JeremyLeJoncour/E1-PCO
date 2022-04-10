# Etude de l'attrition et stratégie de modélisation
# 1. Contexte
Depuis 2010, les industries ont développé de nouvelles technologies en vue de la demande croissante des consommateurs de streaming, ce processus par lequel la musique multimédia est accessible depuis internet. A ce jour, le streaming représente plus de la moitié des revenus de l'industrie musicale mondiale (Site Web UK. Parliament. 2020).

Des plateformes diverses telles que YouTube Music, Apple Music, Amazon Music ou encore Spotify ont ainsi réussi à s’étendre à travers le monde et à se populariser (Site Web Frandroid. 2021).  Ces services proposent un catalogue de musiques divers et varié, ainsi que d’autres fonctionnalités en rapport (importation de fichiers MP3 des particuliers, écoutes hors-connexion…). Le nombre croissant de services de streaming d’écoute sur cette dernière décennie a élevé le niveau de la concurrence, notamment depuis la démocratisation des smartphones. Afin de maintenir leur compétitivité sur ces marchés concurrentiels, les entreprises (fournisseur de biens ou de services) mettent en application plusieurs stratégies : 
* Acquérir davantage de nouveaux clients 
* Ventes incitatives pour les clients existants
* Augmenter la période de rétention des clients.

L’analyse de la valeur du retour sur investissement a montré que la dernière stratégie semblait la plus rentable et la plus simple à mettre en place (E. Ascarza et al. 2016). Cela montre que fidéliser un client existant coûte bien moins cher que d'en acquérir de nouveaux (SA. Qureshii et al. 2013). Ainsi, les entreprises doivent en général diminuer l’attrition de leurs clients.

Pour une entreprise, le taux d’attrition (communément évoqué sous le terme churn rate) représente le pourcentage de clients perdus sur une période donnée (généralement un an ou un mois) par rapport au nombre total de clients se trouvant dans la base clientèle au début de cette période. A l’inverse, le taux de rétention est la capacité de l’entreprise à garder ses clients durant cette même période donnée. Le taux d’attrition est majoritairement calculé sur une segmentation particulière de la clientèle (par rapport à l’âge, segmentation marketing…).

En d’autres termes, le taux d’attrition résume la capacité de l’entreprise à retenir le client, en le fidélisant grâce à une offre pertinente et une gamme de produits ou de services conçue à cet effet. Il est considéré comme un indicateur de performance clé dans les bonnes décisions stratégiques (Site Web Optimove. 2020). Par extension, il indique la satisfaction client auprès du service. La fidélisation du client est donc cruciale pour la pérennité de l’entreprise. Attirer de nouveaux clients est bien plus coûteux que de conserver les clients actuels. En effet, les utilisateurs habitués aux services que propose l’entreprise sont beaucoup plus susceptibles d'acheter des produits que les nouveaux clients. Une autre étude (Site Web Invespcro. 2021) montrait que la probabilité de vendre un produit à un client actuel s’élève à près de 70 % contre seulement 5 à 20 % pour un nouveau client, renforçant ainsi le choix des entreprises à privilégier des mesures réduisant les phénomènes d’attrition.

<p align="center">
  <img src="Résultats Analyses/schema1.png" />
</p>

Par simplification, il existe deux types de désabonnement.  Le premier est involontaire, par circonstances indépendantes de leur volonté et entraînant un arrêt du service. Par exemple, cela peut être une expiration de la carte bancaire associée à l’offre de l’entreprise. Le deuxième type, le plus fréquent, est le désabonnement actif. 

Trois formes de désabonnement volontaire peuvent être caractérisées et concernent un changement d’intérêt de l’utilisateur pour le service :
* Le client, par perte d’intérêt du type de service ou produit, résilie/se désabonne
* Le client insatisfait passe chez l’entreprise concurrente
* Le client s’abonne à une autre offre commercialisée par la même entreprise, répondant mieux à ses besoins. C’est un phénomène de phagocytage ou cannibalisation des offres. 

Pour le bon maintien de leurs services, les entreprises ont généralement recours à un CRM (système de gestion de la relation client). Ce système joue notamment un rôle central dans le développement de la satisfaction client, de la fidélité et de l'interface principale pour interagir avec ses clients. Les CRM (et leurs solutions SaaS/Cloud) peuvent regrouper un ensemble d'informations sur le client et être utilisées afin de contrer les phénomènes d’attrition et assurer leur fidélité par exemple (Site Web Eudonet. 2018). 

A travers les données provenant de CRM, les entreprises peuvent mettre en place plusieurs stratégies. On retrouve notamment le « win back », une opération marketing qui consiste à reconquérir un client présentant une forte probabilité d’attrition (Site Web Définitions marketing. 2019). Cela peut se faire par appel téléphonique et surtout dans les secteurs d’activités commercialisant. 

En amont, la détection de l’attrition est quant à elle réalisée à partir d’un scoring prédictif. Chaque client se voit attribuer un score en fonction de l’offre choisie et de son comportement vis-à-vis du service utilisé. 

Généralement, ces scores sont définis par les services marketing par une analyse de données plus ou moins complexe, comparant les clients satisfaits du service et des clients déjà désabonnés afin d’en ressortir les aspects défaillants de l’offre et le profil des utilisateurs résilients. Dans cette optique, des processus de modélisation via des algorithmes de Machine Learning (apprentissages supervisés notamment) permettent une détection plus affinée des utilisateurs à fort potentiel d’attrition. La prédiction de ce phénomène est l'un des cas d'usages les plus fréquents de la data-science.

S’appliquant à la plupart des entreprises traitant du désabonnement des clients, de nombreuses solutions ont vu le jour par l’émergence d’outils facilitant la mise en place d’algorithmes performants. De nombreuses plateformes basées sur l’IA telles qu'Akkio, Churnly ou encore Prevision.io, proposent leurs services afin que les entreprises puissent contrôler, dans ce cas précis, les départs clients grâce à des interfaces utilisateurs simples reliées généralement aux bases CRM.

# 2. Modèles utilisés dans la prédiction de l’attrition

Plusieurs travaux de recherche se sont orientés sur l’étude d’algorithmes d’apprentissage supervisé afin de concevoir des modèles de prédiction performants. Les entreprises disposant maintenant d’une grande quantité de données, l’utilisation d'algorithmes de Machine Learning ou de Deep Learning sont envisageables. La détection de l’attrition est en général un problème de classification binaire, comprenant une classe de clients abonnés et de clients désabonnés, le but étant de créer un modèle capable de distinguer les deux types d’utilisateurs dans ce cas spécifique. En les différenciant à travers des variables associés aux clients, les algorithmes entrainés sont capables de prédire sur de nouveaux utilisateurs, leur comportement et leur potentiel désistement de tels services.

Plusieurs algorithmes de classification sont retrouvés dans la littérature pour répondre à ce projet de détection d’attrition. Par exemple, l’équipe de SA. Neslin et al. (2006) présentait dans leur publication diverses approches de modélisation comprenant des méthodes statistiques traditionnelles telles que la **régression logistique**. La régression logistique est un modèle statistique linéaire généralisé utilisant une fonction de lien logistique. Elle établit avant tout la probabilité de réalisation d’une des modalités à prédire (abonnés : 0 / désabonnés : 1). Cette probabilité est modélisée par une courbe sigmoïde d’intervalle 0 à 1.

On y trouve aussi des modèles statistiques non paramétriques comme l’algorithme des **K plus proches voisins** (K-nearest neighbors), des modèles polyvalents qui peuvent être utilisés dans divers secteurs de métier comme dans le cas de prédiction des clients susceptibles de partir (D. Ruta et al. 2006).

Les **algorithmes Naives Bayes**, basés sur le Théorème de Bayes (fondé sur les probabilités conditionnelles), peuvent aussi être employés dans ce genre de problématique (K.K. Mohbey. 2020). Ces ensembles d’algorithmes traitent les caractéristiques indépendamment de l’ensemble des variables à disposition. Cela implique que chaque fonctionnalité soit indépendante, ce qui n’est pas toujours le cas, et en fait sa principale faiblesse (Site Web Mrmint. 2017). 

Les modèles de **support vector machine** (SVM) ont été envisagés dans des travaux de modélisation sur la détection de l’attrition. L’article de ZY. Chen et al. (2012) effectue un état des lieux sur ces types d’algorithmes et suggère des améliorations probantes. Les SVM ont pour principe de générer une frontière séparant les données de différentes catégories. Dans des cas majoritairement non-linéaire, les SVM utilisent des fonctions (« noyaux ») permettant de projeter les données sur une feature space, séparées par un hyperplan. Bien que robuste, les entraînements des SVM sont longs sur des jeux de données volumineux.

Des **modèles décisionnels** peuvent être élaborés pour répondre aux projets luttant contre les phénomènes d’attrition comme les algorithmes simples d’arbre de décision. Ces algorithmes ont montré une certaine fiabilité dans ce genre de classification binaire (S. Höppner et al. 2020). Ils ont pour principe d’effectuer un filtrage de variables par décision. Ces algorithmes sont souvent utilisés sous des méthodes d’ensemble, présentant de meilleures performances dans la classification binaire (K. Coussement, K.W. De Bock.  2013).

Ces **méthodes d’ensemble** permettent d’obtenir un modèle de prédiction (dans ce cas-ci) résultant des prédictions d’algorithmes simples (weak learner ou apprenants faibles à forte variance) confectionnés en amont. L’objectif de tels modèles vise à corriger plusieurs inconvénients comme la complexité et le surapprentissage des arbres décisionnels par exemple. On y trouve notamment les **Forêts d’Arbres décisionnels (Random Forest Classifier)** dans la catégorie des modèles **Bagging** (ou Bootstrap Aggregating). Les algorithmes Bagging créés des estimateurs entraînés en parallèle pour en ressortir une tendance générale.

Une autre catégorie d’ensemble, nommée **Boosting** (comme le modèle AdaBoost), se présente par une succession d’estimateurs qui cherchent à minimiser l’erreur du précédent. Le principe même du Boosting est d’accorder une importance (ou poids) sur les estimateurs ayant un taux d’erreur faible. Les **modèles de Gradient Boosting** et leurs versions alternatives tels que XGBoost (A.K. Ahmad et al. 2019), LightGBM ou CatBoost par exemple, connaissent une certaine popularité dans de nombreuses compétitions Kaggle pour leur efficacité, leur rapidité et leurs performances (Site Web Datascientest. 2020).

Au niveau de l’apprentissage supervisé profond (Deep Learning), plusieurs publications comme celle de l’équipe de Y. Khan et al. (2019) détaillent l’utilisation de **réseaux de neurones artificiels** dans la prédiction des phénomènes d’attritions (notamment dans les entreprises Télécoms). Dans le domaine du Deep Learning, les réseaux de neurones (ANN) s’inspirent de l’infrastructure du système nerveux central humain. Différents types de réseaux existent, spécifiques pour chaque besoin. On y trouve notamment les Perceptrons Multicouches (proactifs ou rétroactifs), ou encore les réseaux Convolutifs (traitant les images).

Généralement, les réseaux sont composés d’au moins deux couches de neurones (entrée et sortie). Ainsi, plus le problème à résoudre est complexe, plus le nombre de couches augmente. A chaque neurone composant ces couches est attribué un “poids synaptique” modulé par des règles d'apprentissage. Il en résulte des connexions neurales plus importantes qui vont orienter la prédiction finale du modèle. Ces modèles peuvent présenter des performances plus élevées que les algorithmes de Machine Learning sur certaines problématiques courantes notamment sur les données séquentielles (C. Gary Mena et al. 2019).

Enfin, d’autres recherches se sont penchées sur des **systèmes hybrides (principe du Stacking)**, combinant différents algorithmes de Machine Learning ou différents modèles ANN pour les rendre collectivement plus performants (Tianpei Xu et al. 2021). La stratégie d'agrégation est réalisée à partir des données en construisant un métamodèle. Ce dernier permet d’attribuer des poids « optimaux » aux différents modèles entraînés en amont.

# 3. Objectifs du Projet
Les phénomènes d’attrition des clients jouent un rôle crucial dans la pérennité de l’entreprise. A travers différentes méthodes de segmentation client, associées aux données des CRM, les services marketing peuvent déterminer la clientèle prédisposée à se désabonner aux services par la mise en place de scores. L’IA peut jouer un rôle important dans ce genre de problématique, notamment par la multitude de modèles existant, et pouvant être adaptés sur les données de l’entreprise mises à disposition.

Le projet de ce présent rapport se propose de construire des modèles prédictifs sur le comportement des utilisateurs (détection des clients à haut potentiel d’attrition) du service de streaming d’écoute KKBOX.

KKBOX est le premier service de streaming musical en Asie, détenant la bibliothèque musicale Asia-Pop la plus complète au monde avec plus de 30 millions de pistes. Ils offrent une version illimitée de leur service à des millions de personnes, soutenue notamment par de la publicité et des abonnements payants. Actuellement, la société utilise des techniques d'analyse de survie pour déterminer la durée de vie résiduelle de chaque abonné.

L’objectif est donc de construire un algorithme qui prédit si un utilisateur se désabonne après l'expiration de son abonnement, à partir des données fournies par KKBOX. Similaire aux services existants de Churn Detection, la future application doit contenir un front affichant un dashboard récapitulatif des données utilisateurs (provenant d’une base de données faisant office de CRM).  Un tableau répertoriant les clients les plus susceptibles de partir sera généré grâce aux résultats fournis par le modèle IA créé.

# 4. Bibliographie

**Ahmad, A.K., Jafar, A. & Aljoumaa, K**. Customer churn prediction in telecom using machine learning in big data platform.  2019.

**Ascarza E, Iyengar R, Schleicher M**. The perils of proactive churn prevention using plan recommendations: evidence from a field experiment. 2016.

**Coussement, K., & De Bock, K. W**. Customer churn prediction in the online gambling industry: The beneficial effect of ensemble learning. 2013.

**Dymitr Ruta , Detlef Nauck, Behnam Azvine**. K Nearest Sequence Method and Its Application to Churn Prediction. 2006.

**K. K. Mohbey**. Employee's Attrition Prediction Using Machine Learning Approaches. 2020.

**Qureshii SA, Rehman AS, Qamar AM, Kamal A, Rehman A**. Telecommunication subscribers’ churn prediction model using machine learning. 2013.

**Scott A. Neslin, Sunil Gupta, Wagner Kamakura, Junxiang Lu, Charlotte H. Mason**. Defection Detection: Measuring and Understanding the Predictive Accuracy of Customer Churn Models. 2006.

**Sebastiaan Höppner, Eugen Stripling, Bart Baesens, Seppe vanden Broucke, Tim Verdonck**. Profit driven decision trees for churn prediction. 2020.

**Zhen-Yu Chen, Zhi-Ping Fan, Minghe Sun**. A hierarchical multiple kernel support vector machine for customer churn prediction using longitudinal behavioral data. 2012.

**Optimove**. Attrition de la clientèle (2020). https://www.optimove.com/resources/learning-center/customer-attrition
UK Parliament MPs on the House of Commons Digital, Culture, Media and Sport Committee. Music streaming must modernise. Is anybody listening? (2021). https://committees.parliament.uk/work/646/economics-of-music-streaming/

**Frandroid**. Quel est le meilleur service de streaming de musique ? (2021). https://www.frandroid.com/android/288776_streaming-musical-offre-choisir

**Définitions marketing**. Win Back  (2019). https://www.definitions-marketing.com/definition/win-back/

**Eudonet**. Qu’est ce qu’un CRM ? (2018). https://fr.eudonet.com/crm/definition-crm/

**Invespcro**. Customer Acquisition Vs.Retention Costs – Statistics And Trends. (2020). https://www.invespcro.com/blog/customer-acquisition-retention/

**Mr. Mint**. Naive Bayes Classifier pour Machine Learning. (2017). https://mrmint.fr/naive-bayes-classifier

# 5. Analyses et Modélisation
### Analyses et Conception du Dataset Résultant

Les jeux de données proviennent d'une compétition Kaggle https://www.kaggle.com/c/kkbox-churn-prediction-challenge présentant de nombreux fichiers CSV d'entrainement et fichiers de soumissions.

**Plusieurs fichiers (Version 2 et 3) sont à disposition comportant des données des utilisateurs jusqu'à 2017. Le but est ici de créer un fichier CSV unique qui sera ensuite intégré dans une base de données relationnelle type MySQL.**

La définition de l'attrition/renouvellement peut être délicate en raison du modèle d'abonnement de KKBox. Étant donné que la majorité de la durée d'abonnement de KKBox est de 30 jours, de nombreux utilisateurs se réabonnent chaque mois. Les champs clés pour déterminer l'attrition/le renouvellement sont *transaction date*, *membership expiration date*, et *is_cancel*. A noter que le champ *is_cancel* indique si un utilisateur annule activement un abonnement. L'annulation de l'abonnement n'implique pas que l'utilisateur s'est désabonné pour de bon. Un utilisateur peut annuler l'abonnement au service en raison d'un changement de plan de service ou pour d'autres raisons. Le critère de "churn" est l'absence d'un nouvel abonnement de service valide dans les 30 jours suivant l'expiration de l'abonnement actuel.

Le nombre d'utilisateurs uniques diffère d'un CSV à l'autre et une étude approfondie sur un Dataset global apporterait des biais dans la proportion d'individus désabonnés/abonnés. Ainsi, les études seront faites individuellement pour chaque CSV Transactions, Membres, Logs avec un merge de Train. De plus, le nombre d'utilisateur global sur les CSV Transactions et Logs est plus élevé que le nombre d'utilisateur unique, indiquant un aspect temporel des informations. Dans le cadre de ce projet, seule la dernière en date pour chaque membre sera pris en compte.

### transactions_v3.csv
Transactions des utilisateurs jusqu'au 28/02/2017.

* **msno**: utilisateur id
* **payment_method_id**: mode de paiement
* **payment_plan_days**: durée de l'abonnement en jours
* **plan_list_price**: en nouveau dollar de Taïwan (NTD)
* **actual_amount_paid**: en nouveau dollar de Taïwan (NTD)
* **is_auto_renew**
* **transaction_date**: format %Y%m%d Dernière transaction au 31/03/2017
* **membership_expire_date**: format %Y%m%d date d'expiration de l'abonnement
* **is_cancel**: si l'utilisateur a annulé ou non l'adhésion à cette transaction

### user_logs_v2.csv
Journaux d'utilisateurs quotidiens décrivant les comportements d'écoute d'un utilisateur. Données collectées jusqu'au 31/03/2017.

* **msno**: utilisateur id
* **date**: format %Y%m%d
* **num_25**: nombre de musique jouées moins de 25 % de la longueur de la chanson
* **num_50**: nombre de musique jouées entre 25 % et 50 % de la longueur de la chanson
* **num_75**:  nombre de musique jouées entre 50 % et 75 % de la longueur de la chanson
* **num_985**:  nombre de musique jouées entre 75 % et 98.5 % de la longueur de la chanson
* **num_100**: nombre de musique jouées sur 98,5% de la durée de la chanson
* **num_unq**: nombre de musique uniques jouées
* **total_secs**:  nombre total de secondes écouté

### members_v3.csv
Informations de l'utilisateur. Notez que tous les utilisateurs de l'ensemble de données ne sont pas disponibles.

* **msno**: utilisateur id
* **city**: ville id
* **bd**: age. Remarque : cette colonne contient des valeurs aberrantes allant de -7000 à 2015.
* **gender**
* **registered_via**: registration method
* **registration_init_time**: format %Y%m%d
* **expiration_date**: format %Y%m%d, pris comme un instantané auquel le member.csv est extrait. Ne représentant pas le comportement de désabonnement réel.

### train_v2.csv
Contenant les identifiants des utilisateurs et s'ils ont quitté les services du site.

* **msno**: utilisateur id
* **is_churn**:  La variable cible. Le taux de désabonnement est défini comme si l'utilisateur n'a pas continué l'abonnement dans les 30 jours suivant l'expiration. is_churn = 1 signifie désabonnement, is_churn = 0 signifie renouvellement.

Une première analyse a été faite sur la Version 1 des CSV avec un ensemble de données beaucoup plus conséquent. L'analyse c'était d'ailleurs portée sur les 8M premières lignes de *user_logs.csv* et *transactions.csv*, des données antérieures à Mars 2017. Du fait de l'importation en base de données, l'étude se concentre uniquement sur l'analyse des données de Mars 2017.

Dans la présente analyse sur les données qui serviront à l'entrainement du futur modèle, la majorité des features ont été étudiées afin d'en mesurer leur impact sur la valeur cible *is_churn*. Ces données features peuvent être de type quantitative comme celles retrouvées sur le journal des utilisateurs *User_logs* regroupant le temps d'écoute et le nombre de musique écouté. Des informations sur les transactions notament à travers *Payment_method_id*, *Plan_list_price*, *Transaction_date* sont aussi présents et mesure en soi l'activité de l'utilisateur au niveau de son abonnement au service. Ces données peuvent être sous forme de Date, de valeurs catégorielles ou quantitative discontinue (ordinalle). Des informations générales sur les membres sont aussi disponibles regroupant *Age*, *Genre*, *Ville*, *date d'enregistrement* et *expiration de l'abonnement*.

Les données sont comparés entre les deux "types de population" : les utilisateurs toujours abonnés et ceux ayant arrêté leur abonnement pour plus d'un mois.

### User Logs :

<p align="center">
  <img src="Résultats Analyses/schema2.png" />
  <img src="Résultats Analyses/graph1.png" />
</p>

Les données de temps d'écoute et du nombre de musiques écoutés par jour sur le mois de Mars pour chaque utilisateur ont été additionnés. Les tests T ont montré des différences fortements significatives (à hauteur d'une erreur alpha à moins de 0,1%) entre les individus ayant stoppé leur abonnement et les individus encore abonnés. Ces variables seraient ainsi des marqueurs de choix afin de déterminer les futurs membres qui arrêteraient leur abonnement.


### Membres :

<p align="center">
  <img src="Résultats Analyses/graph2.png" />
</p>

**City** : La ville 1 est la plus représenté dans le jeu de donnée. La proportion de gens *is_churn* = 0 et *is_churn* = 1 est similaire entre chaque ville, laissant supposé que la ville n'est pas un facteur de choix prépondérant dans la prédiction du futur modèle.

**Age** : Outre les valeurs abérrantes, les membres utilisant ce service sont majoritairement agés de 21 à 30 ans. La proportion d'utilisateur ayant une plus forte propention à quitter ces services sont agés de 10 à 20 ans. La proportion de membres se désabonnant pour plus de 30 jours est similaire dans les autres catégories d'âge.

**Genre** : La part d'utilisateurs qu'ils soient Homme ou Femme quittant les services de streaming est la même. Dans cette première analyse, le genre ne doit pas influencer sur le risque d'attrition.

**Méthode d'enregistrement** : La méthode d'enregistrement 7 est celle privilégiée par la plupart des utilisateurs. La proportion d'individus utilisant cette méthode est moins enclin à partir. A l'inverse, elle est plus importante sur la méthode d'enregistrement 4.

### Transactions :

**ID Méthode de Paiement** : Cette catégorie montre une certaine variabilité dans la proportion d'utilisateur quittant les services. Les clients qui utilisent certaines méthodes de paiement (3, 6, 8, 12, 13, 15, 17, 20, 22, 26, 32, 35) sont plus sujet à partir. La méthode 41 regroupe la plus grande proportion des utilisateurs.

**Plan_list_price** : La proportion d'invidus en fonction de cette catégorie sur *is_churn* présente une grande variabilité. Le prix d'abonnement le plus choisi par les utilisateurs et celui à 149 NTD suivi de 99 NTD.

**Actual_amount_paid** : Comme pour *Plan_list_price*, cette catégorie présente une forte variabilité de proportion entre utilisateurs restant et sortant. Naturellement, les abonnements payés par la plupart des utilisateurs s'élèvent à 149 NTD et 99 NTD. Il existe toutefois des différences de prix (*delta_paid*) entre ces deux variables et peut être du à d'éventuelles remises, ou paiements différés. Cette analyse a été effectuée en amont, lors d'une précédente étude, cependant, cette variable n'a pas été reproduite ici après avoir remarqué des incohérences sur ce dataset.

**Auto_renew et Is_cancel** : Ces variables présentent une corrélation notable respectivement négative et positive sur la propention à ce qu'un utilisateur arrête son abonnement.

### Variables créées :

**Price_per_day** : Les tests statistiques sur cette variable *Prix de l'abonnement à la journée* montre des différences significatives (à hauteur d'une erreur alpha à moins de 0,1%) entre les deux types d'utilisateurs.

**Fidelity_days** : Les utilisateurs désabonnés ont en moyenne été abonnés plus longtemps que ceux étant encore abonnés. Cette analyse est contre-intuitive mais pourrait s'expliquer par un désintérêt croissant des utilisateurs désabonnés au service de la plateforme. Elle peut aussi s'expliquer par des arrêts discontinues de l'abonnement, espaçant davantage l'utilisation des services proposés par la plateforme de streaming. C'est une variable relative avec les informations que dispose le jeu de donnée.

### Incohérences sur Transactions :

Plusieurs anomalies et incohérences ont été détectées sur ce dataset durant l'analyse. Cette variable ne contient pas toutes les dates de transaction de l'utilisateur (arrêt au 31-03-2017). La date d'expiration de l'abonnement sera la seule prise en compte.

### Fusion des CSV

Le dataset fusionné comprendra des informations sur utilisateurs uniques, sur la dernière date de transaction. Dans le cadre de ce projet et en raison de la démonstration qui en découlera sur la partie interface graphique, l'analyse se poursuivra sur un dataset suivant :

<p align="center">
  <img src="Résultats Analyses/schema3.png" />
</p>


## Modélisation
### Démarche de la modélisation

<p align="center">
  <img src="Résultats Analyses/ModelSchema1.jpg" />
  <img src="Résultats Analyses/ModelSchema2.jpg" />
</p>

Dans le cadre de l'analyse, la métrique *Log Loss* a été privilégiée pour évaluer le modèle. Plusieurs algorithmes ont été entrainés et sélectionnés par Cross-Validation. 

<p align="center">
  <img src="Résultats Analyses/graph3.png" />  
</p>

### Tableau d'ensemble :

<p align="center">
  <img src="Résultats Analyses/graph4.png" />
</p>
Après hyperparamétrage sur les 3 meilleurs modèles, XGBoost a été retenu comme mentionné précédemment. 3 modèles XGBoost ont été comparés :

* Modèle sans paramètre
* Modèle optimisé
* Modèle avec Sélection de Variable

<p align="center">
  <img src="Résultats Analyses/Xgboost Feature Importance2.png" />
  <img src="Résultats Analyses/graph5.png" />
  <img src="Résultats Analyses/RPC Comparaison.png" />
  <img src="Résultats Analyses/ROCAUC Comparaison.png" />
  <img src="Résultats Analyses/Matrix Comparaison.png" />
</p>

Une autre statégie a aussi été réalisés en rééquilbrant les classes. Des techniques de Sous-Echantillonnage(Random ou Tomek Links), de Sur-échantillonnage (duplication, SMOTE, ADASYN), de rééchantillonnages hybrides ou encore de modèles Ensemble de samplers ont été envisagées. L'hyperparamétrage Scale Pos Weight de XGBoost a aussi été vérifié.

#### Vu d'ensemble sur Sur-échantillonnage SMOTE:

<p align="center">
  <img src="Résultats Analyses/graph6.png" />
</p>

#### Matrice sur Modèle d'ensembles de samblers Imblearn:

<p align="center">
  <img src="Résultats Analyses/graph7.png" />
</p>

#### XGBoost Scale_pos_weight :
<p align="center">
  <img src="Résultats Analyses/Score_BestFeatures_Nb.png" />
</p>

**Résultats :** 
Le modèle intégré sera finalement le XGBoost Optimisé avec réduction de dimensionnalité. Les graphes suivants montrent la proportion de client en fonction de la probabilité prédictive du modèle. Une probabilité supérieure à 50% classe l'individu comme se désabonnant, et à l'inverse, reste abonné.

<p align="center">
  <img src="Résultats Analyses/Histogram_FPVN.png" />
  <img src="Résultats Analyses/Histogram_VPFN.png" />
</p>

# 6. Base de données

Les données du Dataset Test (séparé en amont avec *Train_Test_split*) ont été exportées en base MySQL, 4 tables représentent les fichiers CSV de la compétition Kaggle :
* User : Identifiant de l'utilisateur
* Members : Informations générales sur l'utilisateur
* Transaction : Informations sur les transactions de l'utilisateur
* Logs : Informations de l'utilisateur au sein de la plateforme de streaming comme le temps d'écoute, le nombre de musiques écoutées.

<p align="center">
  <img src="Résultats Analyses/Design_database.png" />
</p>

# 7. Création de l'application
L'application a été confectionnée sous divers langages et Framework. Le Front a été construit avec HTML5 et CSS3 et le Framework Bootstrap 4. Pour rendre le contenu dynamique, du Javascript a aussi été incorporé, notamment en intégrant les graphiques conçu sous HighCharts. Evidemment, la gestion de la donnée, stocké sur MySQL, a été réalisée sous Python avec le Framework Flask, permettant de faire le lien entre Front et Back-end.

<p align="center">
  <img src="Résultats Analyses/prog.png" />
  <img src="Résultats Analyses/Schema4.png" />
</p>

Le schéma ci-dessus montre la structure de l'application et comment il intéragit avec l'utilisateur :
* **1.** L'utilisateur rentre les informations souhaitées dans le formulaire.
* **2.** Les informations sont traitées via Flask et Python pour envoyer les requêtes conditionnées vers la base de données.
* **3.** Les requêtes sont envoyées via Python MySQL connector.
* **4.** Les données sont récoltées et traitées via Python. Un DataFrame est créé en conséquence pour le passer vers le modèle IA.
* **5.** Le modèle d'intelligence artificielle enregistré en amont sous format Joblib traite les données et renvoie les prédictions. Python met en forme les résultats sous forme d'un tableau.
* **6.** Les résultats sont renvoyés au Front via la connexion Flask-Front.
* **7.** Les Dashboards générés via JS et HighCharts sont affichés sur le support HTML/CSS. Les résultats peuvent être ensuite téléchargés sous format CSV si l'utilisateur le souhaite.

### Pages de connexion
<p align="center">
  <img src="Ressources/page_1.png" />
  <img src="Ressources/page_2.png" />
</p>

### Connexion BDD ou import de Fichiers CSV
<p align="center">
  <img src="Ressources/page_6.png" />
  <img src="Ressources/page_7.png" />
</p>

### Evaluation du modèle
<p align="center">
  <img src="Ressources/page_9.png" />
  <img src="Ressources/page_10.png" />
  <img src="Ressources/page_11.png" />
</p>

### Simulation
<p align="center">
  <img src="Ressources/page_12.png" />
  <img src="Ressources/page_13.png" />
  <img src="Ressources/page_14.png" />
</p>

### Monitoring
<p align="center">
  <img src="Ressources/page_16.png" />
  <img src="Ressources/page_20.png" />
  <img src="Ressources/page_21.png" />
</p>

# 8. Conclusion et Perspectives
Les phénomènes d'Attrition sont l'un des cas courants de la Data-Science. Dans ce projet, le modèle IA est un classificateur binaire entrainé sur des classes aux proportions déséquilibrées. Dépendant des métriques souhaitant vérifier, plusieurs stratégies peuvent être appliquées afin de répondre au besoin de l'entreprise :
* Un modèle avec une classification performante avec une forte probabilité de prédiction : Vérification *Log Loss* et *AUC*.
* Un modèle détectant au maximum les utilisateurs se désabonnant au détriment de l'augmentation de Faux Positifs: Rééquilibrage des classes et vérification des métriques Recall et Precision.

Plusieurs modèles de *Machine Learning* et de *Deep Learning* ont été entrainés afin de trouver le meilleur algorithme possible. XGBoost a été choisi par cette méthode et présente un *Log Loss* de 0.07 et un score *MCC* et *F1* de près de 80%. Ce modèle présente donc des scores satisfaisants en comparaison avec ceux créés durant la compétition Kaggle (Scores *Log Loss* entre 0.1 et 0.07).

Toutefois, le modèle est encore perfectible :
* Le modèle n'a été entrainé que sur le dernier mois des données d'entrainement. Le Dataset fournis durant la compétition Kaggle comportait plusieurs mois/années de données (420 Millions d'instances). La tâche aurait consisté à utiliser un environnement Hadoop, avec le moteur multilingue Spark, prévu pour l'analyse à grande échelle, afin d'avoir une vision plus large sur le comportement des utilisateurs sur la plateforme de Streaming.
* De ce fait, des tendances pourraient en ressortir, amenant à la création de nouvelles variables pertinentes.
* Un hyperparamétrage plus poussé pourrait être concevable, seuls 3 paramètres ont été testés durant la modélisation des algorithmes de *ML* et 4 ANN ont été testés.
* Enfin, une analyse de l'écosystème et l'apport des bénéfices. En créant une nouvelle métrique, le modèle peut différer, mais encore une fois dépendant de l'attente de l'entreprise.

Enfin, le modèle pourrait être utilisé sur des données réelles futurs pour s'assurer de la bonne cohésion des prédictions fournis par notre modèle XGBoost Classifier.
