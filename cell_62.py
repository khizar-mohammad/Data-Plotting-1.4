#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sample_data2 = pd.read_csv("countries.csv")
US = sample_data2[sample_data2.country == 'United States']
South_Africa = sample_data2[sample_data2.country=='South Africa']
plt.plot(US.year,(US.population / US.population.iloc[0] * 100)-100)
plt.plot(South_Africa.year,(South_Africa.population / South_Africa.population.iloc[0] * 100)-100)
plt.legend(["This is US's population growth ","This is South Africa's population growth"])
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()

