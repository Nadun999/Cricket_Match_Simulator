def GetTeam(teamName):
    print(GetTeam)
    df = pd.read_excel(
        r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\'+teamName+'\\'+teamName+'.xlsx')
    editable_options = df.iloc[:, :1]
    print(editable_options)
