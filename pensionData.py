'''
Created on 11 Mar 2013

@author: eidahil
'''

class MyPensionData(object):

    def __init__(self, company_pension_contribution, pension_contribution):
        self.set_my_pension_contribution(pension_contribution)
        self.set_company_pension_contribution(company_pension_contribution)

    def set_my_pension_contribution(self, my_pension_contribution):
        self.pension_contribution = my_pension_contribution

    def get_my_pension_contribution(self):
        return self.pension_contribution
    
    def set_company_pension_contribution(self, my_company_pension_contribution):
        self.company_pension_contribution = my_company_pension_contribution

    def get_company_pension_contribution(self):
        return self.company_pension_contribution