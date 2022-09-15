from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
import pandas as pd
import matplotlib.pyplot as plt
In [18]:
data_front = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Front End efficiency')
data_till = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Till Activity Study')


print(data_front)
             Study   Location  Tags        Date     Day  Round  \
0     StGW0710ras3   Stamford   NaN  07/10/2019  Monday  10:47   
1     StGW0710ras3   Stamford   NaN  07/10/2019  Monday  10:47   
2     StGW0710ras3   Stamford   NaN  07/10/2019  Monday  10:47   
3     StGW0710ras3   Stamford   NaN  07/10/2019  Monday  10:47   
4     StGW0710ras3   Stamford   NaN  07/10/2019  Monday  10:52   
...            ...        ...   ...         ...     ...    ...   
3699  LeGW2710ras1  Leicester   NaN  27/10/2019  Sunday  16:11   
3700           NaN        NaN   NaN         NaN     NaN    NaN   
3701           NaN        NaN   NaN         NaN     NaN    NaN   
3702           NaN        NaN   NaN         NaN     NaN    NaN   
3703           NaN        NaN   NaN         NaN     NaN    NaN   

                Role  El Code                                     Elements  \
0      Team Member 1   2534.0                       Serve Customer at Till   
1      Team Member 2   5206.0  Serve Customer at Collections/Click&Collect   
2     Customer Count      5.0                               Customer Count   
3     Customer Count      5.0                               Customer Count   
4      Team Member 1   5174.0            Deal with Store Visit RM / AM etc   
...              ...      ...                                          ...   
3699   Team Member 6   5189.0                       Return Product to Sale   
3700             NaN      NaN                                          NaN   
3701             NaN      NaN                                          NaN   
3702             NaN      NaN                                          NaN   
3703             NaN      NaN                                          NaN   

         Rating   BMS  Qty              Area   Main Category        Category  \
0           100  5.00  1.0             Tills        Customer             NaN   
1           100  5.00  1.0  Collections Desk        Customer             NaN   
2     Not Rated  0.00  1.0  Collections Desk             NVA  Customer Count   
3     Not Rated  0.00  1.0             Tills             NVA  Customer Count   
4           100  5.00  1.0  Collections Desk  Task & Process             NaN   
...         ...   ...  ...               ...             ...             ...   
3699         75  3.75  1.0             Tills  Task & Process             NaN   
3700        NaN   NaN  NaN               NaN             NaN             NaN   
3701        NaN   NaN  NaN               NaN             NaN             NaN   
3702        NaN   NaN  NaN               NaN             NaN             NaN   
3703        NaN   NaN  NaN               NaN             NaN             NaN   

     Notes Unnamed: 16  
0      NaN         NaN  
1      NaN         NaN  
2      NaN         NaN  
3      NaN    Timeslot  
4      NaN     Morning  
...    ...         ...  
3699   NaN   Afternoon  
3700   NaN   Afternoon  
3701   NaN   Afternoon  
3702   NaN   Afternoon  
3703   NaN   Afternoon  

[3704 rows x 17 columns]
In [15]:
print(data_front.head())
          Study  Location  Tags        Date     Day  Round            Role  \
0  StGW0710ras3  Stamford   NaN  07/10/2019  Monday  10:47   Team Member 1   
1  StGW0710ras3  Stamford   NaN  07/10/2019  Monday  10:47   Team Member 2   
2  StGW0710ras3  Stamford   NaN  07/10/2019  Monday  10:47  Customer Count   
3  StGW0710ras3  Stamford   NaN  07/10/2019  Monday  10:47  Customer Count   
4  StGW0710ras3  Stamford   NaN  07/10/2019  Monday  10:52   Team Member 1   

   El Code                                     Elements     Rating  BMS  Qty  \
0   2534.0                       Serve Customer at Till        100  5.0  1.0   
1   5206.0  Serve Customer at Collections/Click&Collect        100  5.0  1.0   
2      5.0                               Customer Count  Not Rated  0.0  1.0   
3      5.0                               Customer Count  Not Rated  0.0  1.0   
4   5174.0            Deal with Store Visit RM / AM etc        100  5.0  1.0   

               Area   Main Category        Category Notes Unnamed: 16  
0             Tills        Customer             NaN   NaN         NaN  
1  Collections Desk        Customer             NaN   NaN         NaN  
2  Collections Desk             NVA  Customer Count   NaN         NaN  
3             Tills             NVA  Customer Count   NaN    Timeslot  
4  Collections Desk  Task & Process             NaN   NaN     Morning  
In [ ]:

In [20]:
pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)
In [21]:
print(data_front.head())
          Study  Location  Tags        Date     Day  Round            Role  \
0  StGW0710ras3  Stamford   NaN  07/10/2019  Monday  10:47   Team Member 1   
1  StGW0710ras3  Stamford   NaN  07/10/2019  Monday  10:47   Team Member 2   
2  StGW0710ras3  Stamford   NaN  07/10/2019  Monday  10:47  Customer Count   
3  StGW0710ras3  Stamford   NaN  07/10/2019  Monday  10:47  Customer Count   
4  StGW0710ras3  Stamford   NaN  07/10/2019  Monday  10:52   Team Member 1   

   El Code                                     Elements     Rating  BMS  Qty  \
0   2534.0                       Serve Customer at Till        100  5.0  1.0   
1   5206.0  Serve Customer at Collections/Click&Collect        100  5.0  1.0   
2      5.0                               Customer Count  Not Rated  0.0  1.0   
3      5.0                               Customer Count  Not Rated  0.0  1.0   
4   5174.0            Deal with Store Visit RM / AM etc        100  5.0  1.0   

               Area   Main Category        Category Notes Unnamed: 16  
0             Tills        Customer             NaN   NaN         NaN  
1  Collections Desk        Customer             NaN   NaN         NaN  
2  Collections Desk             NVA  Customer Count   NaN         NaN  
3             Tills             NVA  Customer Count   NaN    Timeslot  
4  Collections Desk  Task & Process             NaN   NaN     Morning  
In [22]:
data_front.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3704 entries, 0 to 3703
Data columns (total 17 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Study          3700 non-null   object 
 1   Location       3700 non-null   object 
 2   Tags           0 non-null      float64
 3   Date           3700 non-null   object 
 4   Day            3700 non-null   object 
 5   Round          3700 non-null   object 
 6   Role           3700 non-null   object 
 7   El Code        3700 non-null   float64
 8   Elements       3700 non-null   object 
 9   Rating         3700 non-null   object 
 10  BMS            3700 non-null   float64
 11  Qty            3700 non-null   float64
 12  Area           3700 non-null   object 
 13  Main Category  3700 non-null   object 
 14  Category       1067 non-null   object 
 15  Notes          274 non-null    object 
 16  Unnamed: 16    3684 non-null   object 
dtypes: float64(4), object(13)
memory usage: 492.1+ KB
In [25]:
time_spent = data_front.groupby(["Location"]).BMS.sum().reset_index()
In [ ]:

In [26]:
print(time_spent)
        Location      BMS
0      Ashbourne   730.50
1      Bracknell  2893.00
2     Chichester  2316.75
3  Kidderminster   958.25
4      Leicester  2477.50
5       Stamford  1365.50
In [86]:
time_spent.plot(x='Location', y='BMS', style='o')
Out[86]:
<matplotlib.axes._subplots.AxesSubplot at 0x7f78efef7f50>

In [39]:
print(data_till.head())
           Study               Location   Tags        Date      Day      Time  \
0  BrJC1708dots1  Bristol Emerson Green  SAG D  17/08/2021  Tuesday  10:03:26   
1  BrJC1708dots1  Bristol Emerson Green  SAG D  17/08/2021  Tuesday  10:03:33   
2  BrJC1708dots1  Bristol Emerson Green  SAG D  17/08/2021  Tuesday  10:03:37   
3  BrJC1708dots1  Bristol Emerson Green  SAG D  17/08/2021  Tuesday  10:03:40   
4  BrJC1708dots1  Bristol Emerson Green  SAG D  17/08/2021  Tuesday  10:03:48   

             Area                               Task  \
0  Main Till Bank  Till Transaction - Main Till bank   
1  Main Till Bank  Till Transaction - Main Till bank   
2  Main Till Bank  Till Transaction - Main Till bank   
3  Main Till Bank  Till Transaction - Main Till bank   
4  Main Till Bank  Till Transaction - Main Till bank   

                                     Element              UOM     Rating  \
0                          Wait No Customers     Per Occasion  Not Rated   
1  Call Up Next Customer & Start Transaction              NaN        100   
2            Determine Customer Requirements              NaN        100   
3    Request & Process Advantage Card (Chip)              NaN        100   
4       Scan & Bag Item(s) - Number of Items  Number of Items        100   

   Frequency  Obs _Time   BMS  BMs_per_UOM Main Category  Category Notes  \
0          1       0.12  0.00         0.00           NVA       NaN   NaN   
1          1       0.06  0.06         0.06      Customer       NaN   NaN   
2          1       0.06  0.06         0.06      Customer       NaN   NaN   
3          1       0.13  0.13         0.13      Customer       NaN   NaN   
4          2       0.23  0.23         0.12      Customer       NaN     2   

  Timeslot  
0  Morning  
1  Morning  
2  Morning  
3  Morning  
4  Morning  
In [20]:
total_time_till = data_till["BMS"]+data_till["Obs_Time"]
data_till["Total_Time"] = total_time_till
time_spent_till = data_till.groupby(["Location"]).Total_Time.sum().reset_index()
print(time_spent_till)
                   Location  Total_Time
0     Bristol Bradley Stoke   1725.2871
1         Bristol Broadmead   1336.4860
2  Bristol Clifton Queen Rd   1126.7461
3   Bristol Cribbs Causeway    828.4547
4     Bristol Emerson Green   1857.4489
5          Bristol Henleaze    611.6570
In [22]:
plt.scatter(time_spent_till['Location'], time_spent_till['Total_Time'])
plt.gcf().set_size_inches((13, 13)) 
plt.show()

In [23]:
time_spent_till_category = data_till.groupby(["Main Category"]).Total_Time.sum().reset_index()
print(time_spent_till_category)
    Main Category  Total_Time
0        Customer   3159.9237
1             NVA   4053.0127
2  Task & Process    273.1434
In [27]:
plt.scatter(time_spent_till_category['Main Category'], time_spent_till_category['Total_Time'])
plt.gcf().set_size_inches((13, 13)) 
plt.show()

In [57]:
time_spent_front = data_front.groupby(["Location"]).BMS.sum().reset_index()
print(time_spent_front)
        Location      BMS
0      Ashbourne   730.50
1      Bracknell  2893.00
2     Chichester  2316.75
3  Kidderminster   958.25
4      Leicester  2477.50
5       Stamford  1365.50
In [55]:
time_spent_total_till = data_till["BMS"].sum()
print(time_spent_total_till)
1714.3569000000002
In [56]:
time_spent_total_front = data_front["BMS"].sum()
print(time_spent_total_front)
10741.5
In [59]:
ineffective_time = data_till.groupby(["Main Category","Location"]).Obs_Time.sum().reset_index()
print(ineffective_time)
     Main Category                  Location  Obs_Time
0         Customer     Bristol Bradley Stoke    401.14
1         Customer         Bristol Broadmead    275.42
2         Customer  Bristol Clifton Queen Rd    221.27
3         Customer   Bristol Cribbs Causeway    153.35
4         Customer     Bristol Emerson Green    442.99
5         Customer          Bristol Henleaze     87.54
6              NVA     Bristol Bradley Stoke    891.35
7              NVA         Bristol Broadmead    651.11
8              NVA  Bristol Clifton Queen Rd    684.61
9              NVA   Bristol Cribbs Causeway    515.27
10             NVA     Bristol Emerson Green    973.51
11             NVA          Bristol Henleaze    337.17
12  Task & Process     Bristol Bradley Stoke     16.33
13  Task & Process         Bristol Broadmead     67.35
14  Task & Process   Bristol Cribbs Causeway      3.57
15  Task & Process          Bristol Henleaze     49.75
In [70]:
NVA_all_client =ineffective_time[ineffective_time['Main Category']=='NVA']
print(NVA_all_client)
   Main Category                  Location  Obs_Time
6            NVA     Bristol Bradley Stoke    891.35
7            NVA         Bristol Broadmead    651.11
8            NVA  Bristol Clifton Queen Rd    684.61
9            NVA   Bristol Cribbs Causeway    515.27
10           NVA     Bristol Emerson Green    973.51
11           NVA          Bristol Henleaze    337.17
In [72]:
ineffective_time_all_client = NVA_all_client.Obs_Time.sum()
print(ineffective_time_all_client)
4053.0127
In [58]:
ineffective_time_front = data_front.groupby(["Main Category","Location"]).BMS.sum().reset_index()
print(ineffective_time_front)
     Main Category       Location      BMS
0         Customer      Ashbourne   500.00
1         Customer      Bracknell  2410.00
2         Customer     Chichester  1770.00
3         Customer  Kidderminster   785.00
4         Customer      Leicester  1655.00
5         Customer       Stamford  1030.00
6              NVA      Ashbourne     0.00
7              NVA      Bracknell     0.00
8              NVA     Chichester     0.00
9              NVA  Kidderminster     0.00
10             NVA      Leicester    10.00
11             NVA       Stamford     0.00
12  Task & Process      Ashbourne   230.50
13  Task & Process      Bracknell   483.00
14  Task & Process     Chichester   546.75
15  Task & Process  Kidderminster   173.25
16  Task & Process      Leicester   812.50
17  Task & Process       Stamford   335.50
In [ ]:

In [45]:
task_frequency = data_till.groupby(["Task"]).Frequency.sum().reset_index()
print(task_frequency)
                                                Task  Frequency
0  Dot Com Instore pick 2 - Clifton Down, Henleaz...          6
1  Self Check out - Cribbs Only - note customers ...        925
2  Till Transaction - Healthcare Counter - Small ...       2220
3                  Till Transaction - Main Till bank       9584
In [46]:
task_BMS = data_till.groupby(["Task"]).BMS.sum().reset_index()
print(task_BMS)
                                                Task      BMS
0  Dot Com Instore pick 2 - Clifton Down, Henleaz...     1.28
1  Self Check out - Cribbs Only - note customers ...   221.07
2  Till Transaction - Healthcare Counter - Small ...   302.68
3                  Till Transaction - Main Till bank  1189.33
In [47]:
cols_to_use = task_BMS.columns.difference(task_frequency.columns)
In [49]:
dfNew = task_frequency.merge( task_BMS[cols_to_use], left_index=True, right_index=True, how='outer')
In [50]:
print(dfNew)
                                                Task  Frequency      BMS
0  Dot Com Instore pick 2 - Clifton Down, Henleaz...          6     1.28
1  Self Check out - Cribbs Only - note customers ...        925   221.07
2  Till Transaction - Healthcare Counter - Small ...       2220   302.68
3                  Till Transaction - Main Till bank       9584  1189.33
In [52]:
dfNew["Task Rate"] = dfNew["Frequency"]/dfNew["BMS"]
print(dfNew)
                                                Task  Frequency      BMS  \
0  Dot Com Instore pick 2 - Clifton Down, Henleaz...          6     1.28   
1  Self Check out - Cribbs Only - note customers ...        925   221.07   
2  Till Transaction - Healthcare Counter - Small ...       2220   302.68   
3                  Till Transaction - Main Till bank       9584  1189.33   

   Task Rate  
0       4.69  
1       4.18  
2       7.33  
3       8.06  
In [10]:
time_each_category =data_front.groupby(["Location",'Main Category']).BMS.sum().reset_index()
print(time_each_category)
         Location   Main Category      BMS
0       Ashbourne        Customer   500.00
1       Ashbourne             NVA     0.00
2       Ashbourne  Task & Process   230.50
3       Bracknell        Customer  2410.00
4       Bracknell             NVA     0.00
5       Bracknell  Task & Process   483.00
6      Chichester        Customer  1770.00
7      Chichester             NVA     0.00
8      Chichester  Task & Process   546.75
9   Kidderminster        Customer   785.00
10  Kidderminster             NVA     0.00
11  Kidderminster  Task & Process   173.25
12      Leicester        Customer  1655.00
13      Leicester             NVA    10.00
14      Leicester  Task & Process   812.50
15       Stamford        Customer  1030.00
16       Stamford             NVA     0.00
17       Stamford  Task & Process   335.50
In [15]:
cus_classify = data_front.groupby(["Elements","Main Category"]).count()
print(cus_classify)
                                                            Study  Location  \
Elements                                    Main Category                     
Admin at Till                               Task & Process    318       318   
Assist Customer in Store                    Customer          115       115   
Break                                       NVA               137       137   
COSHH - deal with spillage                  Task & Process      2         2   
Customer Count                              NVA              1067      1067   
Deal with Store Visit RM / AM etc           Task & Process      1         1   
Facing Up - away from till area             Task & Process     32        32   
Get Product for Customer                    Customer           44        44   
Not Working                                 NVA                11        11   
Personal Needs                              NVA                14        14   
Product Carry & Collect from car            Customer           13        13   
Replenish Brochures/Catalogues              Task & Process      2         2   
Return Product to Sale                      Task & Process     84        84   
Returns/ Exchanges/ Repairs at Till         Customer           33        33   
Rug Doctor Rental                           Customer            5         5   
Sell to Customer from Display               Customer            2         2   
Serve Customer at Collections/Click&Collect Customer          175       175   
Serve Customer at Till                      Customer         1234      1234   
Serve Customer with DPD parcel              Customer            9         9   
System Delay                                NVA                 2         2   
Talk Not Work                               NVA                16        16   
Talk Work NOTE who and topic                Task & Process     41        41   
Team Briefing 121                           Task & Process      6         6   
Telephone                                   Task & Process     18        18   
Tidy till area                              Task & Process     51        51   
Training                                    Task & Process      4         4   
Wait No Customer                            NVA               264       264   

                                                            Tags  Date   Day  \
Elements                                    Main Category                      
Admin at Till                               Task & Process     0   318   318   
Assist Customer in Store                    Customer           0   115   115   
Break                                       NVA                0   137   137   
COSHH - deal with spillage                  Task & Process     0     2     2   
Customer Count                              NVA                0  1067  1067   
Deal with Store Visit RM / AM etc           Task & Process     0     1     1   
Facing Up - away from till area             Task & Process     0    32    32   
Get Product for Customer                    Customer           0    44    44   
Not Working                                 NVA                0    11    11   
Personal Needs                              NVA                0    14    14   
Product Carry & Collect from car            Customer           0    13    13   
Replenish Brochures/Catalogues              Task & Process     0     2     2   
Return Product to Sale                      Task & Process     0    84    84   
Returns/ Exchanges/ Repairs at Till         Customer           0    33    33   
Rug Doctor Rental                           Customer           0     5     5   
Sell to Customer from Display               Customer           0     2     2   
Serve Customer at Collections/Click&Collect Customer           0   175   175   
Serve Customer at Till                      Customer           0  1234  1234   
Serve Customer with DPD parcel              Customer           0     9     9   
System Delay                                NVA                0     2     2   
Talk Not Work                               NVA                0    16    16   
Talk Work NOTE who and topic                Task & Process     0    41    41   
Team Briefing 121                           Task & Process     0     6     6   
Telephone                                   Task & Process     0    18    18   
Tidy till area                              Task & Process     0    51    51   
Training                                    Task & Process     0     4     4   
Wait No Customer                            NVA                0   264   264   

                                                            Round  Role  \
Elements                                    Main Category                 
Admin at Till                               Task & Process    318   318   
Assist Customer in Store                    Customer          115   115   
Break                                       NVA               137   137   
COSHH - deal with spillage                  Task & Process      2     2   
Customer Count                              NVA              1067  1067   
Deal with Store Visit RM / AM etc           Task & Process      1     1   
Facing Up - away from till area             Task & Process     32    32   
Get Product for Customer                    Customer           44    44   
Not Working                                 NVA                11    11   
Personal Needs                              NVA                14    14   
Product Carry & Collect from car            Customer           13    13   
Replenish Brochures/Catalogues              Task & Process      2     2   
Return Product to Sale                      Task & Process     84    84   
Returns/ Exchanges/ Repairs at Till         Customer           33    33   
Rug Doctor Rental                           Customer            5     5   
Sell to Customer from Display               Customer            2     2   
Serve Customer at Collections/Click&Collect Customer          175   175   
Serve Customer at Till                      Customer         1234  1234   
Serve Customer with DPD parcel              Customer            9     9   
System Delay                                NVA                 2     2   
Talk Not Work                               NVA                16    16   
Talk Work NOTE who and topic                Task & Process     41    41   
Team Briefing 121                           Task & Process      6     6   
Telephone                                   Task & Process     18    18   
Tidy till area                              Task & Process     51    51   
Training                                    Task & Process      4     4   
Wait No Customer                            NVA               264   264   

                                                            El Code  Rating  \
Elements                                    Main Category                     
Admin at Till                               Task & Process      318     318   
Assist Customer in Store                    Customer            115     115   
Break                                       NVA                 137     137   
COSHH - deal with spillage                  Task & Process        2       2   
Customer Count                              NVA                1067    1067   
Deal with Store Visit RM / AM etc           Task & Process        1       1   
Facing Up - away from till area             Task & Process       32      32   
Get Product for Customer                    Customer             44      44   
Not Working                                 NVA                  11      11   
Personal Needs                              NVA                  14      14   
Product Carry & Collect from car            Customer             13      13   
Replenish Brochures/Catalogues              Task & Process        2       2   
Return Product to Sale                      Task & Process       84      84   
Returns/ Exchanges/ Repairs at Till         Customer             33      33   
Rug Doctor Rental                           Customer              5       5   
Sell to Customer from Display               Customer              2       2   
Serve Customer at Collections/Click&Collect Customer            175     175   
Serve Customer at Till                      Customer           1234    1234   
Serve Customer with DPD parcel              Customer              9       9   
System Delay                                NVA                   2       2   
Talk Not Work                               NVA                  16      16   
Talk Work NOTE who and topic                Task & Process       41      41   
Team Briefing 121                           Task & Process        6       6   
Telephone                                   Task & Process       18      18   
Tidy till area                              Task & Process       51      51   
Training                                    Task & Process        4       4   
Wait No Customer                            NVA                 264     264   

                                                             BMS   Qty  Area  \
Elements                                    Main Category                      
Admin at Till                               Task & Process   318   318   318   
Assist Customer in Store                    Customer         115   115   115   
Break                                       NVA              137   137   137   
COSHH - deal with spillage                  Task & Process     2     2     2   
Customer Count                              NVA             1067  1067  1067   
Deal with Store Visit RM / AM etc           Task & Process     1     1     1   
Facing Up - away from till area             Task & Process    32    32    32   
Get Product for Customer                    Customer          44    44    44   
Not Working                                 NVA               11    11    11   
Personal Needs                              NVA               14    14    14   
Product Carry & Collect from car            Customer          13    13    13   
Replenish Brochures/Catalogues              Task & Process     2     2     2   
Return Product to Sale                      Task & Process    84    84    84   
Returns/ Exchanges/ Repairs at Till         Customer          33    33    33   
Rug Doctor Rental                           Customer           5     5     5   
Sell to Customer from Display               Customer           2     2     2   
Serve Customer at Collections/Click&Collect Customer         175   175   175   
Serve Customer at Till                      Customer        1234  1234  1234   
Serve Customer with DPD parcel              Customer           9     9     9   
System Delay                                NVA                2     2     2   
Talk Not Work                               NVA               16    16    16   
Talk Work NOTE who and topic                Task & Process    41    41    41   
Team Briefing 121                           Task & Process     6     6     6   
Telephone                                   Task & Process    18    18    18   
Tidy till area                              Task & Process    51    51    51   
Training                                    Task & Process     4     4     4   
Wait No Customer                            NVA              264   264   264   

                                                            Category  Notes  \
Elements                                    Main Category                     
Admin at Till                               Task & Process         0     92   
Assist Customer in Store                    Customer               0     24   
Break                                       NVA                    0      6   
COSHH - deal with spillage                  Task & Process         0      0   
Customer Count                              NVA                 1067      4   
Deal with Store Visit RM / AM etc           Task & Process         0      0   
Facing Up - away from till area             Task & Process         0      3   
Get Product for Customer                    Customer               0     11   
Not Working                                 NVA                    0      0   
Personal Needs                              NVA                    0      2   
Product Carry & Collect from car            Customer               0      0   
Replenish Brochures/Catalogues              Task & Process         0      2   
Return Product to Sale                      Task & Process         0     13   
Returns/ Exchanges/ Repairs at Till         Customer               0      1   
Rug Doctor Rental                           Customer               0      1   
Sell to Customer from Display               Customer               0      0   
Serve Customer at Collections/Click&Collect Customer               0      5   
Serve Customer at Till                      Customer               0     67   
Serve Customer with DPD parcel              Customer               0      1   
System Delay                                NVA                    0      0   
Talk Not Work                               NVA                    0      1   
Talk Work NOTE who and topic                Task & Process         0      6   
Team Briefing 121                           Task & Process         0      4   
Telephone                                   Task & Process         0      3   
Tidy till area                              Task & Process         0     16   
Training                                    Task & Process         0      0   
Wait No Customer                            NVA                    0     12   

                                                            Unnamed: 16  
Elements                                    Main Category                
Admin at Till                               Task & Process          309  
Assist Customer in Store                    Customer                115  
Break                                       NVA                     137  
COSHH - deal with spillage                  Task & Process            2  
Customer Count                              NVA                    1064  
Deal with Store Visit RM / AM etc           Task & Process            1  
Facing Up - away from till area             Task & Process           32  
Get Product for Customer                    Customer                 44  
Not Working                                 NVA                      11  
Personal Needs                              NVA                      14  
Product Carry & Collect from car            Customer                 13  
Replenish Brochures/Catalogues              Task & Process            2  
Return Product to Sale                      Task & Process           82  
Returns/ Exchanges/ Repairs at Till         Customer                 33  
Rug Doctor Rental                           Customer                  5  
Sell to Customer from Display               Customer                  2  
Serve Customer at Collections/Click&Collect Customer                174  
Serve Customer at Till                      Customer               1230  
Serve Customer with DPD parcel              Customer                  9  
System Delay                                NVA                       2  
Talk Not Work                               NVA                      16  
Talk Work NOTE who and topic                Task & Process           41  
Team Briefing 121                           Task & Process            6  
Telephone                                   Task & Process           18  
Tidy till area                              Task & Process           50  
Training                                    Task & Process            4  
Wait No Customer                            NVA                     264  
