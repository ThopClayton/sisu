def onboardingDayPopularityDebug(df):
    '''generates hist of each shit type'''

    df = df[df['Event Name'] == 'Vol Orientatio']
    data = [_.weekday() for _ in df['Event Date']]
    # debuging the date bug where orientation only shows up on like 4 days
    dataDebug = [_ for _ in df['Event Date']]
    print("onboardingDayPopularity:")
    for i in range(len(dataDebug)):
        print(f'{dataDebug[i]}\t{data[i]}')


