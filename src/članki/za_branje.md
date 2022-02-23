# Neža #
1. [Context-based email classification model](https://eds-p-ebscohost-com.nukweb.nuk.uni-lj.si/eds/pdfviewer/pdfviewer?vid=1&sid=06c9cdf8-5d82-4b70-ac76-2b562d79f0e9%40redis); april 2016

Abstract: Context-based email classification requires understanding of semantic and structural attributes of email. Most of the research
has focused on generating semantic properties through structural components of email. By viewing emails as events (as a major subset of
class of email), a rich contextual test-bed representation for understanding of the semantic attributes of emails has been devised. The eventbased emails have traditionally been studied based on simple structural properties. In this paper, we present a novel approach by first
representing such class of emails as graphs, followed by heuristically applying graph mining and matching algorithm to pick templates
representing contextual and semantic attributes that help classify emails. The classification templates used three key event classes: social,
personal and professional. Results show that our graph mining and matching supported template-based approach performs consistently well
over event email data set with high accuracy.

> Paziti bo treba na **JEZIK!** 

2. [SPONGY (SPam ONtoloGY): Email Classification UsingTwo-Level Dynamic Ontology](https://www.hindawi.com/journals/tswj/2014/414583/); junij 2014

Abstract: Email is one of common communication methods between people on the Internet. 
However, the increase of email misuse/abuse has resulted in an increasing volume of spam emails over recent years. 
An experimental system has been designed and implemented with the hypothesis that this method would outperform existing techniques, and the experimental results showed that indeed the proposed ontology-based approach improves spam filtering accuracy significantly. 
In this paper, two levels of ontology spam filters were implemented: a first level global ontology filter and a second level user-customized ontology filter. 
The use of the global ontology filter showed about 91% of spam filtered, which is comparable with other methods. The user-customized ontology filter was created based on the specific user’s background as well as the filtering mechanism used in the global ontology filter creation. 
The main contributions of the paper are (1) to introduce an ontology-based multilevel filtering technique that uses both a global ontology and an individual filter for each user to increase spam filtering accuracy and (2) to create a spam filter in the form of ontology, which is user-customized, scalable, and modularized, so that it can be embedded to many other systems for better performance.

> Kako si lahko pomagamo z algoritmi za spam?
> Razmerje med splošnim in individualnim?

3. [Cross-dataset email classification](https://eds-s-ebscohost-com.nukweb.nuk.uni-lj.si/eds/detail/detail?vid=0&sid=e107ccd8-8073-43ba-a75f-ed350d5eba66%40redis&bdata=Jmxhbmc9c2wmc2l0ZT1lZHMtbGl2ZQ%3d%3d#AN=147564849&db=a9h); junij 2020

Abstract: Email is one of the most popular ways of communication. Nevertheless, it is also a potential tool to deceive and fill users with unwanted publicity, which reduces productivity. 
To alleviate such fact, a common solution has been building machine learning models based on the content of emails to automatically separate emails (spam vs ham). In this work, a study of a set of machine learning models and content-based features for the problem of cross-dataset email classification is presented. 
This problem consists in training and testing the models using different datasets; considering the fact that the datasets were collected under different independent setups. 
This has the purpose of simulating future variable or unpredictable conditions in the emails content distributions as could happen in a real setting, where models are trained using emails from a certain period of time, group of users or accounts, but tested with emails from other users or accounts. 
Experiments were conducted with the models and features using different datasets and two setups, same-dataset, and cross-dataset, to show the complexity of the later. 
The performance was evaluated using the Area Under the ROC Curve, a common metric in email classification. The results show interesting insights for the problem.

> Kaj so kriteriji razvrščanja? 
> Na kakšen način analizirati vsebino?
> Uporabni modeli.

4. [Social feature-based enterprise email classification without examining email contents](https://www-sciencedirect-com.nukweb.nuk.uni-lj.si/science/article/pii/S1084804511002256); marec 2012

Abstract: Without imposing restrictions, many enterprises find nonwork-related contents consuming network resources. Business communication over emails thus incurs undesired delays and inflicts damages to businesses, explaining why many enterprises are concerned with the competition to use email services. 
Obviously, enterprises should prioritize business emails over personal ones in their email service. Therefore, previous works present content-based classification methods to categorize enterprise emails into business or personal correspondence. 
Accuracy of these methods is largely determined by their ability to survey as much information as possible. 
However, in addition to decreasing the performance of these methods, monitoring the details of email contents may violate privacy rights that are under legal protection, requiring a careful balance of accurately classifying enterprise emails and protecting privacy rights. 
The proposed email classification method is thus based on social features rather than a survey of emails contents. Social-based metrics are also designed to characterize emails as social features; 
the obtained features are treated as an input of machine learning-based classifiers for email classification. Experimental results demonstrate the high accuracy of the proposed method in classifying emails. 
In contrast with other content-based methods that examine email contents, the emphasis on social features in the proposed method is a promising alternative for solving similar email classification problems.

> Da se izognemo posegom v zasebnost (tj. branju vsebine) --> novi modeli, temeljijo na social feature.

5. [PCA document reconstruction for email classification](https://www-sciencedirect-com.nukweb.nuk.uni-lj.si/science/article/pii/S0167947311003549); marec 2012

Abstract: This paper presents a document classifier based on text content features and its application to email classification. 
We test the validity of a classifier which uses Principal Component Analysis Document Reconstruction (PCADR), where the idea is that principal component analysis (PCA) can compress optimally only the kind of documents–in our experiments email classes–that are used to compute the principal components (PCs), 
and that for other kinds of documents the compression will not perform well using only a few components. Thus, the classifier computes separately the PCA for each document class, and when a new instance arrives to be classified, this new example is projected in each set of computed PCs corresponding to each class, and then is reconstructed using the same PCs. 
The reconstruction error is computed and the classifier assigns the instance to the class with the smallest error or divergence from the class representation. We test this approach in email filtering by distinguishing between two message classes (e.g. spam from ham, or phishing from ham). 
The experiments show that PCADR is able to obtain very good results with the different validation datasets employed, reaching a better performance than the popular Support Vector Machine classifier.

> Konkretna metoda, uporabljali samo za ločevanje med spam in ham.

6. [Multi-Language Spam/Phishing Classification by Email Body Text: Toward Automated Security Incident Investigation](https://www.mdpi.com/2079-9292/10/6/668); marec 2021

Abstract: Spamming and phishing are two types of emailing that are annoying and unwanted,differing by the potential threat and impact to the user. 
Automated classification of these categoriescan increase the users’ awareness as well as to be used for incident investigation prioritizationor automated fact gathering.  
However, currently there are no scientific papers focusing on emailclassification concerning these two categories of spam and phishing emails.  
Therefore this paperpresents a solution,  based on email message body text automated classification into spam andphishing emails. We apply the proposed solution for email classification, written in three languages: English, Russian, and Lithuanian. 
As most public email datasets almost exclusively collect Englishemails, we investigate the suitability of automated dataset translation to adapt it to email classification,written in other languages. 
Experiments on public dataset usage limitations for a specific organizationare executed in this paper to evaluate the need of dataset updates for more accurate classificationresults.

![Figure 1.Workflow diagram of the research. (a) Method selection phase, (b) Multi-language experi-ment phase, (c) Concept-drift experiments phase.](https://user-images.githubusercontent.com/100276495/155415683-3155fdf6-7d15-4c16-a573-05cd9ea9be36.png)

> Klasificirali z: Support vector machine (SVM), random forest (RF), decision tree (DT), naïve Bayes (NB), linear regression (LR), k-nearest neighbors (kNN)
> Pomoje uporaben članek za jezike, ki niso angleščina.

6. [Decision Tree Model for Email Classification](https://ieeexplore-ieee-org.nukweb.nuk.uni-lj.si/document/9390143); konferenca februarja 2021

Abstract: In addition to the undeniable benefits, the development of the Internet has led to many undesirable security effects. 
Spam emails are one of the most challenging issues faced by the Internet users. Spam refers to all emails of unsolicited content that arrive in a user's email box. 
Spam can often lead to network congestion and blocking or even damage to the system for receiving and sending electronic messages. 
Thus, appropriate classification of spam email from legitimate email has become quite important. 
This paper presents a new approach for feature selection and Iterative Dichotomiser 3 (ID3) algorithm designed to generate the decision tree for email classification. 
The experimental results indicate that the proposed model achieves very high accuracy.

> Nek hud algoritem, kaže zelo dobro klasifikacijsko točnost - Iterative Dichotomiser 3 (ID3); morda za uporabiti.
> Vizualizacija ključnih besed v besednem oblaku (prikaz), ki jih mora potem razvrstiti v spam.
> !([Visual representation of important words for spam email](https://user-images.githubusercontent.com/100276495/155417159-fd513dc0-934a-4ee0-bc17-7782bccb8514.png)
