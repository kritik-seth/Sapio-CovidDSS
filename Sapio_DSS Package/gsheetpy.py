def connect_dcm(**kwargs):
    """
    Connects to Master Sheet
    
    Arguments required:
    1. 'sheet_name' type str
    2. 'sheet_no' type int
    
    Returns:
    1. gspread.models.Worksheet
    """
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name(kwargs['cred'], scope)
    gc = gspread.authorize(creds)

    
    if 'sheet_name' and 'sheet_no' in kwargs:
        wks = gc.open(kwargs['sheet_name']).get_worksheet(kwargs['sheet_no'])
        return wks
    
    else:
        print('Arguments required:')
        print('1. \'sheet_name\' type str')
        print('2. \'sheet_no\' type int')


def update_url(**kwargs):
    """
    Updates URL of Sheets which are ready 
    
    Arguments required:
    1. 'worksheet' type gspread.models.Worksheet'
    OR
    2. 'sheet_name' type str and 'sheet_no' type int
    
    Optional:
    1. 'status_check' type bool
        
    Returns:
    1. DataFrame
    """
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name(kwargs['cred'], scope)
    gc = gspread.authorize(creds)
    
    if ('worksheet' in kwargs) or ('sheet_name' and 'sheet_no' in kwargs):
        
        cols = [1,2,3]
        
        if 'worksheet' in kwargs:
            url_list = []
            for i in cols:
                url_list.append(kwargs['worksheet'].col_values(i))
        
        elif 'sheet_name' and 'sheet_no' in kwargs:
            wks = gc.open(kwargs['sheet_name']).get_worksheet(kwargs['sheet_no'])
            url_list = []
            for i in cols:
                url_list.append(wks.col_values(i))
                
        url_df = pd.DataFrame(url_list).T      
        url_df.columns = url_df.loc[3]
        url_df = url_df.drop([0,1,2,3,4,5],axis=0)
        
        if 'status_check' in kwargs:
            
            if kwargs['status_check']:
                url_df = url_df.loc[url_df['Status'] == 'Y']
                return url_df
            else:
                return url_df
            
        else:
            return url_df
    
    else:
        print('Arguments required:')
        print('\'worksheet\' type gspread.models.Worksheet')
        print('OR')
        print('\'sheet_name\' type str, \'sheet_no\' type int')
    

def select_region(**kwargs):
    """
    Selects URL based on REGION
    
    Arguments required:
    1. 'region' type str
    2. 'url' type DataFrame
    
    Returns:
    1. DataFrame
    """
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name(kwargs['cred'], scope)
    gc = gspread.authorize(creds)

    
    if 'region' in kwargs:
        region = kwargs['region']
        if 'url' in kwargs:
            url = kwargs['url']
            region_list = list(url['REGION'])
            if region in region_list:
                url = url.loc[url['REGION']==region]
            else:
                print(f'{region} is not present in the list, please check again!')
            
            
        else:
            print('Argument required \'url\' type DataFrame')
    else:
            print('Argument required \'region\' type str')
            
    return url.iat[0,2]
            

def get_url_data(**kwargs):
    """
    Extracts data from URL
    
    Arguments required:
    1. 'url' type str
    2. 'sheet_no' type int
    
    Returns:
    1. DataFrame
    2. gspread.models.Worksheet
    """
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name(kwargs['cred'], scope)
    gc = gspread.authorize(creds)
    
    
    if 'url' and 'sheet_no' in kwargs:
        sht_val = []
        sht = gc.open_by_url(kwargs['url'])
        worksheet = sht.get_worksheet(kwargs['sheet_no'])
        sht_val = worksheet.get_all_values()
        df = pd.DataFrame(sht_val)
        df.columns = df.loc[1]
        df = df.drop([0,1],axis=0)
        return df, worksheet
    
    else:
        print('Arguments required:')
        print('1. \'url\' type str')
        print('2. \'sheet_no\' type int')
        

def get_data_by_column(**kwargs):
    """
    Extracts certain columns from URL data
    
    Arguments required:
    1. 'col' type list and 'worksheet' type gspread.models.Worksheet
    2. 'col' type list, 'url' type str and 'sheet_no' type int
    
    Returns:
    1. DataFrame
    """
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name(kwargs['cred'], scope)
    gc = gspread.authorize(creds)
    
    if 'col' in kwargs:
    
        if 'worksheet' in kwargs:
            col_list = []
            for i in kwargs['col']:
                col_list.append(kwargs['worksheet'].col_values(i))
                sheet_df = pd.DataFrame(col_list).T
                sheet_df.columns = sheet_df.loc[1]
                sheet_df = sheet_df.drop([0,1],axis=0)
            return sheet_df
        
        elif 'url' and 'sheet_no' in kwargs:
            sht_val = []
            sht = gc.open_by_url(kwargs['url'])
            worksheet = sht.get_worksheet(kwargs['sheet_no'])
            col_list = []
            for i in kwargs['col']:
                col_list.append(worksheet.col_values(i))
                sheet_df = pd.DataFrame(col_list).T
                sheet_df.columns = sheet_df.loc[1]
                sheet_df = sheet_df.drop([0,1],axis=0)
            return sheet_df
        
        else:
            print('Arguments required:')
            print('1. \'worksheet\' type gspread.models.Worksheet')
            print('2. \'url\' type str and \'sheet_no\' type int')
            
    else:
        print('Argument required:  \'col\' type list')
        

def get_data(**kwargs):
    """
    Combined data extraction
    
    Arguments required:
    1. 'master_sheet_name' type str
    2. 'master_sheet_no' type int
    3. 'region_name' type str
    4. 'region_sheet_no' type int
    5. 'status_check' type bool
    
    Returns:
    1. DataFrame
    
    """
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name(kwargs['cred'], scope)
    gc = gspread.authorize(creds)
    
    if 'status_check' in kwargs:
        url_df = update_url(sheet_name = kwargs['master_sheet_name'], sheet_no = kwargs['master_sheet_no'],
                            status_check = kwargs['status_check'], cred = kwargs['cred'])
    else:
        url_df = update_url(sheet_name = kwargs['master_sheet_name'], sheet_no = kwargs['master_sheet_no'],
                            cred = kwargs['cred'])
    url = select_region(url = url_df, region = kwargs['region_name'], cred = kwargs['cred'])
    sht, wks_url = get_url_data(url = url, sheet_no = kwargs['region_sheet_no'], cred = kwargs['cred'])
    
    return sht
