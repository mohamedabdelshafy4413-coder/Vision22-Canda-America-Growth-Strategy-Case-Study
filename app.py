import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 North America Growth Strategy', page_icon='🚀', layout='wide')

# Premium dashboard styling
st.markdown('''
<style>
.main-header {font-size:42px;font-weight:800;}
.card {padding:20px;border-radius:15px;background:#f7f7f7;}
</style>
''', unsafe_allow_html=True)

st.title('Vision22 North America Growth Strategy Case Study')
st.subheader('USA & Canada B2B Market Entry | Pricing Intelligence | Growth Operating Dashboard')

st.markdown('''
## Strategic Positioning

# Vision22 = B2B Growth Partner for North American Companies

Not a generic digital marketing agency.

Vision22 delivers:
- B2B Lead Generation Systems
- Digital Authority Building
- Performance Growth
- Conversion Optimization
- Content & Brand Systems
''')

st.divider()

packages=pd.DataFrame([
['B2B Growth Foundation',6000,9000,3000,5000,85,'Entry Offer'],
['B2B Lead Generation Engine',8000,12000,6000,10000,90,'Primary Growth Offer'],
['Digital Authority & Brand Growth',12000,20000,7000,12000,75,'Trust Building'],
['Performance Growth System',10000,15000,8000,15000,85,'Revenue Optimization'],
['Complete B2B Growth Department',20000,35000,15000,25000,65,'Enterprise Solution']
],columns=['Package','Setup Min','Setup Max','Monthly Min','Monthly Max','Success %','Strategic Role'])

st.header('Package Intelligence')
st.dataframe(packages,use_container_width=True)

fig=px.bar(packages,x='Package',y='Success %',title='Package Success Probability')
st.plotly_chart(fig,use_container_width=True)

st.header('Pricing Strategy Simulator')

price_cases=pd.DataFrame([
['Current Premium Affordable','Balanced','High trust positioning'],
['30% Lower Price','Higher acquisition speed','Recommended entry adjustment'],
['50% Lower Price','Fast conversion','High brand risk']
],columns=['Scenario','Market Effect','Strategic Evaluation'])

st.table(price_cases)

st.info('Recommendation: Vision22 must remain Premium Affordable. Do not compete as a cheap agency.')

st.header('Price Impact Calculator')
base=st.number_input('Monthly Package Price',value=7000,step=500)

c1,c2,c3=st.columns(3)
c1.metric('Current Price',f'${base:,}')
c2.metric('30% Reduction',f'${base*0.7:,.0f}')
c3.metric('50% Reduction',f'${base*0.5:,.0f}')

st.header('SWOT Analysis')
a,b,c,d=st.columns(4)
with a:
 st.success('STRENGTHS\n\n• Experience\n• Integrated Marketing\n• Creative Capability\n• Competitive Cost')
with b:
 st.warning('WEAKNESSES\n\n• Low US Awareness\n• Need Local Proof\n• Need More Case Studies')
with c:
 st.info('OPPORTUNITIES\n\n• Manufacturing\n• SaaS\n• Healthcare\n• Industrial B2B')
with d:
 st.error('THREATS\n\n• US Agencies\n• Price Competition\n• Wrong Positioning')

st.header('Market Entry Priority')
sector=pd.DataFrame([
['Manufacturing',95],['B2B SaaS',92],['Healthcare',90],['Construction',85],['Professional Services',82]
],columns=['Sector','Opportunity Score'])
st.dataframe(sector,use_container_width=True)
st.plotly_chart(px.bar(sector,x='Sector',y='Opportunity Score'),use_container_width=True)

st.header('Email Campaign Simulator')
accounts=st.slider('Target Accounts',100,10000,1000)
reply=st.slider('Positive Reply Rate %',1,15,5)
close=st.slider('Close Rate %',5,60,20)

responses=int(accounts*reply/100)
clients=max(1,int(responses*close/100))

x,y,z=st.columns(3)
x.metric('Replies',responses)
y.metric('Expected Clients',clients)
z.metric('Potential MRR',f'${clients*7000:,}')

st.header('90 Day Execution Plan')
st.markdown('''
Phase 1:
- Build authority content
- Publish B2B insights
- Create growth audits

Phase 2:
- Target 500-1000 accounts
- Manufacturing first
- CEO/Founder outreach

Phase 3:
- Sales meetings
- Convert to Lead Generation Engine
- Upsell Performance Growth System
''')

st.header('Revenue Scenarios')
rev=pd.DataFrame([
['Conservative',3,15000],
['Realistic',5,35000],
['Aggressive',10,70000]
],columns=['Scenario','Clients','MRR'])
st.dataframe(rev,use_container_width=True)
st.plotly_chart(px.line(rev,x='Clients',y='MRR'),use_container_width=True)

st.success('Final Positioning: Vision22 helps North American B2B companies create predictable sales opportunities through strategic digital growth systems.')
