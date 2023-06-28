import pickle
import json
import config
import numpy as np


class RiskAnalytics():
    def __init__(self,  SK_ID_CURR, NAME_CONTRACT_TYPE_x, CODE_GENDER,
       FLAG_OWN_CAR, FLAG_OWN_REALTY, CNT_CHILDREN, AMT_INCOME_TOTAL,
       NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS,REGION_POPULATION_RELATIVE, DAYS_EMPLOYED, DAYS_REGISTRATION,
       DAYS_ID_PUBLISH,REG_CITY_NOT_LIVE_CITY,OBS_30_CNT_SOCIAL_CIRCLE,OBS_60_CNT_SOCIAL_CIRCLE,
       FLAG_DOCUMENT_4, FLAG_DOCUMENT_5, FLAG_DOCUMENT_6, FLAG_DOCUMENT_7, FLAG_DOCUMENT_8, FLAG_DOCUMENT_9,
       FLAG_DOCUMENT_10, FLAG_DOCUMENT_11, FLAG_DOCUMENT_13,FLAG_DOCUMENT_14,FLAG_DOCUMENT_17,
       FLAG_DOCUMENT_20, FLAG_DOCUMENT_21, AMT_REQ_CREDIT_BUREAU_QRT,AMT_REQ_CREDIT_BUREAU_YEAR, AMT_ANNUITY_y,
       NAME_CONTRACT_STATUS, DAYS_DECISION,SELLERPLACE_AREA, DAYS_FIRST_DUE, DAYS_LAST_DUE_1ST_VERSION,
       NFLAG_INSURED_ON_APPROVAL,NAME_TYPE_SUITE_x,NAME_INCOME_TYPE_,NAME_HOUSING_TYPE_,
       ORGANIZATION_TYPE_,NAME_CONTRACT_TYPE_y_,NAME_CASH_LOAN_PURPOSE_,NAME_PAYMENT_TYPE_,CODE_REJECT_REASON_,NAME_TYPE_SUITE_y_,
       NAME_CLIENT_TYPE_,NAME_GOODS_CATEGORY_,NAME_PORTFOLIO_,NAME_PRODUCT_TYPE_,CHANNEL_TYPE_,NAME_SELLER_INDUSTRY_,
       NAME_YIELD_GROUP_,PRODUCT_COMBINATION_):
       self.SK_ID_CURR = SK_ID_CURR
       self.NAME_CONTRACT_TYPE_x = NAME_CONTRACT_TYPE_x
       self.CODE_GENDER = CODE_GENDER
       self.FLAG_OWN_CAR = FLAG_OWN_CAR
       self.FLAG_OWN_REALTY = FLAG_OWN_REALTY
       self.CNT_CHILDREN = CNT_CHILDREN
       self.AMT_INCOME_TOTAL = AMT_INCOME_TOTAL
       self.NAME_EDUCATION_TYPE = NAME_EDUCATION_TYPE
       self.NAME_FAMILY_STATUS = NAME_FAMILY_STATUS
       self.REGION_POPULATION_RELATIVE = REGION_POPULATION_RELATIVE
       self.DAYS_EMPLOYED = DAYS_EMPLOYED
       self.DAYS_REGISTRATION = DAYS_REGISTRATION
       self.DAYS_ID_PUBLISH = DAYS_ID_PUBLISH
       self.REG_CITY_NOT_LIVE_CITY = REG_CITY_NOT_LIVE_CITY
       self.OBS_30_CNT_SOCIAL_CIRCLE = OBS_30_CNT_SOCIAL_CIRCLE
       self.OBS_60_CNT_SOCIAL_CIRCLE = OBS_60_CNT_SOCIAL_CIRCLE
       self.FLAG_DOCUMENT_4 = FLAG_DOCUMENT_4
       self.FLAG_DOCUMENT_5 = FLAG_DOCUMENT_5
       self.FLAG_DOCUMENT_6 = FLAG_DOCUMENT_6
       self.FLAG_DOCUMENT_7 = FLAG_DOCUMENT_7
       self.FLAG_DOCUMENT_8 = FLAG_DOCUMENT_8
       self.FLAG_DOCUMENT_9 = FLAG_DOCUMENT_9
       self.FLAG_DOCUMENT_10 = FLAG_DOCUMENT_10
       self.FLAG_DOCUMENT_11 = FLAG_DOCUMENT_11
       self.FLAG_DOCUMENT_13 = FLAG_DOCUMENT_13
       self.FLAG_DOCUMENT_14 = FLAG_DOCUMENT_14
       self.FLAG_DOCUMENT_17 = FLAG_DOCUMENT_17
       self.FLAG_DOCUMENT_20 = FLAG_DOCUMENT_20
       self.FLAG_DOCUMENT_21 = FLAG_DOCUMENT_21
       self.AMT_REQ_CREDIT_BUREAU_QRT = AMT_REQ_CREDIT_BUREAU_QRT
       self.AMT_REQ_CREDIT_BUREAU_YEAR =AMT_REQ_CREDIT_BUREAU_YEAR
       self.AMT_ANNUITY_y = AMT_ANNUITY_y
       self.NAME_CONTRACT_STATUS = NAME_CONTRACT_STATUS
       self.DAYS_DECISION = DAYS_DECISION
       self.SELLERPLACE_AREA = SELLERPLACE_AREA
       self.DAYS_FIRST_DUE = DAYS_FIRST_DUE
       self.DAYS_LAST_DUE_1ST_VERSION = DAYS_LAST_DUE_1ST_VERSION
       self.NFLAG_INSURED_ON_APPROVAL = NFLAG_INSURED_ON_APPROVAL
       self.NAME_TYPE_SUITE_x = 'NAME_TYPE_SUITE_x_'+  NAME_TYPE_SUITE_x
       self.NAME_INCOME_TYPE_ = "NAME_INCOME_TYPE_" + NAME_INCOME_TYPE_
       self.NAME_HOUSING_TYPE_ = "NAME_HOUSING_TYPE_" + NAME_HOUSING_TYPE_
       self.ORGANIZATION_TYPE_ = "ORGANIZATION_TYPE_" + ORGANIZATION_TYPE_
       self.NAME_CONTRACT_TYPE_y_ = "NAME_CONTRACT_TYPE_y_" + NAME_CONTRACT_TYPE_y_
       self.NAME_CASH_LOAN_PURPOSE_ = "NAME_CASH_LOAN_PURPOSE_" + NAME_CASH_LOAN_PURPOSE_
       self.NAME_PAYMENT_TYPE_ = "NAME_PAYMENT_TYPE_" + NAME_PAYMENT_TYPE_
       self.CODE_REJECT_REASON_ = "CODE_REJECT_REASON_" + CODE_REJECT_REASON_
       self.NAME_TYPE_SUITE_y_ = "NAME_TYPE_SUITE_y_" + NAME_TYPE_SUITE_y_
       self.NAME_CLIENT_TYPE_ = "NAME_CLIENT_TYPE_" + NAME_CLIENT_TYPE_
       self.NAME_GOODS_CATEGORY_ = "NAME_GOODS_CATEGORY_" + NAME_GOODS_CATEGORY_
       self.NAME_PORTFOLIO_ = "NAME_PORTFOLIO_" + NAME_PORTFOLIO_
       self.NAME_PRODUCT_TYPE_ = "NAME_PRODUCT_TYPE_" + NAME_PRODUCT_TYPE_
       self.CHANNEL_TYPE_  = "CHANNEL_TYPE_" +  CHANNEL_TYPE_
       self.NAME_SELLER_INDUSTRY_ = "NAME_SELLER_INDUSTRY_" +NAME_SELLER_INDUSTRY_
       self.NAME_YIELD_GROUP_ = "NAME_YIELD_GROUP_" + NAME_YIELD_GROUP_
       self.PRODUCT_COMBINATION_ = "PRODUCT_COMBINATION_" + PRODUCT_COMBINATION_
    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as file:
            self.model = pickle.load(file)

        with open(config.JSON_FILE_PATH,"r") as file:
            self.json_data = json.load(file)


    def get_riskanalytics(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data["columns"]))   # len(self.json_data["columns"])
        region_index_1 = self.json_data['columns'].index(self.NAME_TYPE_SUITE_x)
        region_index_2 = self.json_data['columns'].index(self.NAME_INCOME_TYPE_)
        region_index_3 = self.json_data['columns'].index(self.ORGANIZATION_TYPE_)
        region_index_4 = self.json_data['columns'].index(self.NAME_CONTRACT_TYPE_y_)
        region_index_5 = self.json_data['columns'].index(self.NAME_CASH_LOAN_PURPOSE_)
        region_index_6 = self.json_data['columns'].index(self.NAME_PAYMENT_TYPE_)
      
        region_index_7 = self.json_data['columns'].index(self.CODE_REJECT_REASON_)
        region_index_8 = self.json_data['columns'].index(self.NAME_TYPE_SUITE_y_)
        
        region_index_9 = self.json_data['columns'].index(self.NAME_CLIENT_TYPE_)
        region_index_10 = self.json_data['columns'].index(self.NAME_GOODS_CATEGORY_)
        region_index_11 = self.json_data['columns'].index(self.NAME_PORTFOLIO_)
        region_index_12 = self.json_data['columns'].index(self.NAME_PRODUCT_TYPE_)
       
        region_index_13 = self.json_data['columns'].index(self.CHANNEL_TYPE_)
        region_index_14 = self.json_data['columns'].index(self.NAME_SELLER_INDUSTRY_)
        region_index_15 = self.json_data['columns'].index(self.NAME_YIELD_GROUP_)
        region_index_16 = self.json_data['columns'].index(self.PRODUCT_COMBINATION_)
        
        
       
        test_array[0] = self.SK_ID_CURR
        test_array[1] = self.json_data["NAME_CONTRACT_TYPE_x"][self.NAME_CONTRACT_TYPE_x]
        test_array[2] = self.json_data["CODE_GENDER"][self.CODE_GENDER]
        test_array[3] = self.json_data["FLAG_OWN_CAR"][self.FLAG_OWN_CAR]
        test_array[4] = self.json_data["FLAG_OWN_REALTY"][self.FLAG_OWN_REALTY]
        test_array[5] = self.CNT_CHILDREN
        test_array[6] = self.AMT_INCOME_TOTAL
        test_array[7] = self.json_data["NAME_EDUCATION_TYPE"][self.NAME_EDUCATION_TYPE]
        test_array[8] = self.json_data["NAME_FAMILY_STATUS"][self.NAME_FAMILY_STATUS]
        test_array[9] = self.REGION_POPULATION_RELATIVE
        test_array[10] = self.DAYS_EMPLOYED
        test_array[11] = self.DAYS_REGISTRATION 
        test_array[12] = self.DAYS_ID_PUBLISH
        test_array[13] = self.REG_CITY_NOT_LIVE_CITY
        test_array[14] = self.OBS_30_CNT_SOCIAL_CIRCLE
        test_array[15] = self.OBS_60_CNT_SOCIAL_CIRCLE
        test_array[16] = self.FLAG_DOCUMENT_4
        test_array[17] = self.FLAG_DOCUMENT_5
        test_array[18] = self.FLAG_DOCUMENT_6
        test_array[19] = self.FLAG_DOCUMENT_7
        test_array[20] = self.FLAG_DOCUMENT_8
        test_array[21] = self.FLAG_DOCUMENT_9
        test_array[22] = self.FLAG_DOCUMENT_10
        test_array[23] = self.FLAG_DOCUMENT_11
        test_array[24] = self.FLAG_DOCUMENT_13
        test_array[25] = self.FLAG_DOCUMENT_14
        test_array[26] = self.FLAG_DOCUMENT_17
        test_array[27] = self.FLAG_DOCUMENT_20
        test_array[28] = self.FLAG_DOCUMENT_21
        test_array[29] = self.AMT_REQ_CREDIT_BUREAU_QRT
        test_array[30] = self.AMT_REQ_CREDIT_BUREAU_YEAR
        test_array[31]= self.AMT_ANNUITY_y         
        test_array[32]= self.json_data["NAME_CONTRACT_STATUS"][self.NAME_CONTRACT_STATUS]      
        test_array[33]= self.DAYS_DECISION       
        test_array[34]=self.SELLERPLACE_AREA   
        test_array[35]=self.DAYS_FIRST_DUE   
        test_array[36]=self.DAYS_LAST_DUE_1ST_VERSION 
        test_array[37]=self.NFLAG_INSURED_ON_APPROVAL
        test_array[region_index_1] = 1
        test_array[region_index_2] = 1
        test_array[region_index_3] = 1
        test_array[region_index_4] = 1
        test_array[region_index_5] = 1
        test_array[region_index_6] = 1
        test_array[region_index_7] = 1
        test_array[region_index_8] = 1
        test_array[region_index_9] = 1
        test_array[region_index_10] = 1
        test_array[region_index_11] = 1
        test_array[region_index_12] = 1
        test_array[region_index_13] = 1
        test_array[region_index_14] = 1
        test_array[region_index_15] = 1
        test_array[region_index_16] = 1



        predict_target = self.model.predict([test_array])
        return predict_target
    


   
