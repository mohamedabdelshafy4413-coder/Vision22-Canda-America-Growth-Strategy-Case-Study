import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 North America Growth Strategy', layout='wide')

st.title('Vision22 North America Growth Strategy Case Study')
st.subheader('USA & Canada B2B Market Entry | Pricing Intelligence | Growth Strategy Dashboard')

st.markdown('''
# Strategic Positioning
## Vision22 = B2B Growth Partner for North American Companies

The objective is not selling generic digital marketing services.
Vision22 builds measurable growth systems:
- B2B Lead Generation
- Digital Authority
- Performance Marketing
- Conversion Systems
- Content & Brand Growth
''')

st.divider()

packages = pd.DataFrame([
['B2B Growth Foundation',6000,9000,3000,5000,85,'Entry Strategy'],
['B2B Lead Generation Engine',8000,12000,6000,10000,90,'Main Growth Offer'],
['Digital Authority & Brand Growth',12000,20000,7000,12000,75,'Brand Expansion'],
['Performance Growth System',10000,15000,8000,15000,85,'Revenue Optimization'],
['Complete B2B Growth Department',20000,35000,15000,25000,65,'Enterprise Level']
],columns=['Package','Setup Min','Setup Max','Monthly Min','Monthly Max','Success %','Role'])

st.header('1. Package Intelligence Dashboard')
st.dataframe(packages,use_container_width=True)

fig=px.bar(packages,x='Package',y='Success %',title='Success Probability By Package')
st.plotly_chart(fig,use_container_width=True)

st.header('2. Pricing Position Analysis')

pricing=pd.DataFrame([
['Current Premium Affordable',90,'Strong trust','Recommended'],
['30% Lower Pricing',95,'Faster acquisition while preserving value','Growth Entry Strategy'],
['50% Lower Pricing',97,'Fast sales but positioning risk','Use Carefully']
],columns=['Scenario','Conversion Potential','Market Impact','Recommendation'])

st.table(pricing)

st.info('Strategic recommendation: Vision22 should not compete as a cheap agency. The goal is Premium Affordable positioning: higher quality than freelancers, lower cost than US agencies.')

st.header('3. SWOT Strategic Analysis')

c1,c2,c3,c4=st.columns(4)
with c1:
 st.success('STRENGTHS\n\n- Long marketing experience\n- Integrated solutions\n- Branding + Creative power\n- Cost advantage')
with c2:
 st.warning('WEAKNESSES\n\n- Limited US awareness\n- Need local proof\n- Need stronger case studies')
with c3:
 st.info('OPPORTUNITIES\n\n- Manufacturing\n- B2B SaaS\n- Healthcare\n- Industrial companies')
with c4:
 st.error('THREATS\n\n- Strong US agencies\n- Price competition\n- Wrong positioning')

st.header('4. Market Entry Strategy - First 90 Days')

st.markdown('''
### Phase 1: Authority Building
- Publish B2B Growth Insights
- Create Industry Audits
- Build LinkedIn authority

### Phase 2: Account Based Marketing
- Target 500-1000 companies
- Manufacturing priority
- Decision makers: CEO, Founder, Marketing Director

### Phase 3: Conversion
- Free B2B Growth Audit
- Strategy Call
- Convert to Lead Generation Engine
''')

st.header('5. Email Campaign Performance Simulator')

emails=st.slider('Target Accounts',100,10000,1000)
reply=st.slider('Positive Reply Rate %',1,10,3)
close=st.slider('Closing Rate %',5,50,20)

meetings=int(emails*reply/100)
clients=int(meetings*close/100)

col1,col2,col3=st.columns(3)
col1.metric('Expected Replies',meetings)
col2.metric('Expected Clients',clients)
col3.metric('Potential MRR',f'${clients*7000:,}')

st.header('6. Revenue Growth Scenarios')
revenue=pd.DataFrame([
['Conservative',3,15000],
['Realistic',5,35000],
['Aggressive',10,70000]
],columns=['Scenario','Clients','Monthly Revenue'])

st.dataframe(revenue,use_container_width=True)

fig2=px.line(revenue,x='Clients',y='Monthly Revenue',title='MRR Growth Potential')
st.plotly_chart(fig2,use_container_width=True)

st.header('7. Final Strategic Recommendation')
st.markdown('''
## Priority Order

1. B2B Lead Generation Engine ⭐
2. Performance Growth System ⭐
3. B2B Growth Foundation
4. Digital Authority Growth
5. Complete Growth Department

The fastest path to market reputation:

**Become known as the company that helps North American B2B businesses generate predictable sales opportunities.**
''')
