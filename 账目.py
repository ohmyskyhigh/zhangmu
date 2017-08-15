
import pandas as pd
examplePATH = 'example/'

sale = pd.DataFrame(pd.read_excel('销售单.xlsx'))
production = pd.DataFrame(pd.read_excel('生产表.xlsx'))
buy = pd.DataFrame(pd.read_excel('采购单.xlsx'))

example_sale = pd.DataFrame(pd.read_excel(examplePATH+'销售单.xlsx'))
example_production = pd.DataFrame(pd.read_excel(examplePATH+'生产表.xlsx'))
example_buy=pd.DataFrame(pd.read_excel(examplePATH+'采购单.xlsx'))
reference = pd.DataFrame(pd.read_excel(examplePATH+'目录.xlsx'))
storage = pd.DataFrame(pd.read_excel(examplePATH+'库存单.xlsx'))


# In[4]:


saleC = sale.columns
productionC = production.columns
buyC = buy.columns
category = ['日期', '产品名称', '单据类型', '单据编号' '数量', '单价', '金额']


# In[5]:


reference.head()


# In[6]:


class setup(object):
    """this class is to deal with first time setup, login the orgin of every products and resources and their number
    
        Attributes:
            reference: stock template
            
            """
    
    
    
    def reference_dict(reference_df):
        r1 = pd.DataFrame(reference_df[['销售表-商品名称', '销售表-商品起始']]).dropna()
        r2 = pd.DataFrame(reference_df[['原料', '原料起始']]).dropna()
        goods_out = dict(zip(list(r1['销售表-商品名称']),list(r1['销售表-商品起始'])))
        goods_in =  dict(zip(list(r2['原料']),list(r2['原料起始'])))
    
    return goods_in, goods_out


# In[8]:


in_dic, out_dic = reference_dict(reference)


# In[3]:


sale = sale[pd.notnull(sale[saleC[0]])]
sale.head()


# In[10]:


buy = buy[pd.notnull(buy[buyC[0]])]
buy.head()


# In[7]:


production = production[pd.notnull(production[productionC[0]])]
production.head()


# def translation(df, example_df):
#     #first we need to translate chinese in english so that we can modify them easier
#     header = list(df.columns)
#     length = len(header)
#     reference = list(example_df.columns)
#     reference_length = len(reference)
#     header_n = []
#     if length == reference_length:
#         print('pass')
#         #assign new header with english
#         for i in range(length):
#             if header[i] == reference[i]:
#                 nh = str('H'+str(i))
#                 print(nh)
#                 header_n.append(nh)
#                 df = df.rename(columns={header[i]: nh})
#         #create a dictionary for later use
#         header_dic = dict(zip(header_n, header))
#         return header_dic
#     

# In[17]:


production['日期'] = pd.to_datetime(production[productionC[0]], errors='coerce').sort_values()
buy['日期'] = pd.to_datetime(buy[buyC[0]], errors='coerce').sort_values()
sale['日期'] = pd.to_datetime(sale[saleC[0]], errors='coerce').sort_values()


# In[18]:


storage


# In[ ]:


def copy_sb(df_sb, storage, reference):
    storage['日期'] = 
    


# In[87]:


production_date = dict(production[productionC[0]])
buy_date = dict(buy[buyC[0]])
sale_date = dict(buy[buyC[0]])


# In[88]:


def monthly(date):
    #split date by month
    months = {}
    for value in date.values():
        m = value.month
        y = value.year
        time = str(y)+'-'+str(m)
        if time not in list(months.keys()):
            months.update({time: []})
    for idx, d in date.items():
        m = d.month
        y = d.year
        time = str(y)+'-'+str(m)
        for mon in months.keys():
            if mon == time:
                months[mon].append(idx)
    return months
        


# #split the dataframe monthly
# production_date_list = [i for i in production_date.values()]
# production_date_list[0].m = []
# for item in ship.itervalues():
#     if item not in ship_list:
#         ship_list.append(item)

# In[89]:


Pdate = monthly(production_date)
Bdate = monthly(buy_date)
Sdate = monthly(sale_date)


# In[90]:


Pdate


# In[ ]:





# In[ ]:


def sumUp(df, date_dict):
    

