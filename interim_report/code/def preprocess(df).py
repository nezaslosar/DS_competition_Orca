def preprocess(df):
    
    #SPREMENI NaN V CLASS "BREZ"
    df = df.fillna("Nedefinirano_polje")
    #VRŽI IZ DF VSE, KI IMAJO CLASS "BREZ"
    df = df.loc[~df["class"].str.contains("Nedefinirano_polje")]
    
    #VRŽI VEN MAILE BREZ VSEBINE
    df = df.loc[~df["content"].str.contains("Nedefinirano_polje")]
    
    #Vrži ven "unnamed
    df = df.drop(columns=["Unnamed: 0"])
    
    #REMOVING WEBSITES FROM STRINGS
    #df['tokenized'] = df['tokenized'].apply(lambda x: re.sub(r'^https?:\/\/.*[\r\n]*', '', x))
    df['tokenized'] = df['content'].apply(lambda x: re.sub(r"(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*", '', x))

    #REMOVING EMAIL ADRESSES FROM STRINGS USING REGEX
    df['tokenized'] = df['tokenized'].apply(lambda x: re.sub('\S*@\S*\s?', '' , x))
    
    #LOWER-CASING NO_STOPWORDS COLUMN
    df["tokenized"] = df["tokenized"].str.lower()
    
    #STRIPPING NO_STOPWORD COLUMN
    df["tokenized"] = df["tokenized"].apply(lambda x: x.strip())
 
    #REMOVING PUNCTUATION
    df['tokenized'] = df['tokenized'].apply(lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ' , x))

    #REMOVING DIGITS 
    df['tokenized'] = df['tokenized'].apply(lambda x: re.sub('[\d]', "" , x))
    
    #REMOVING SINGLE CHARACTERS 
    df['tokenized'] = df['tokenized'].apply(lambda x: re.sub(r"\b[a-zA-Z]\b", "" , x))
    
    #REMOVING WORDS LONGER THAN 16 CHARACTERS FROM 
    df['tokenized'] = df['tokenized'].apply(lambda x: re.sub(r'\b\w{16,100}\b', "" , x))

    #REMOVING WORDS 1-2 CHARACTERS FROM 
    df['tokenized'] = df['tokenized'].apply(lambda x: re.sub(r'\b\w{1,2}\b', "" , x))

    #DETERMINE SLOVENE STOPWORDS
    slo_stopwords = stopwords.words("slovene")
    all_stopwords = slo_stopwords + add_stopwords 
    
    #REMOVE STOPWORDS FROM SLOVENE BASE
    df['tokenized'] = df['tokenized'].apply(lambda x: ' '.join([word for word in x.split() if word not in (all_stopwords)]))
    
    df = df.replace(r'^\s*$', np.NaN, regex=True)
    
    #SPREMENI NaN V - post-classla - "Nedefinirano polje"
    df = df.fillna("Nedefinirano_polje")
    #VRŽI VEN MAILE BREZ VSEBINE - post-classla
    df = df.loc[~df["tokenized"].str.contains("Nedefinirano_polje")]
    
    df.reset_index(drop=True, inplace=True)
    
    #KLASLA
    df["tokenized"] = df["tokenized"].apply(lambda x: klasla(x))
    
    
    return df