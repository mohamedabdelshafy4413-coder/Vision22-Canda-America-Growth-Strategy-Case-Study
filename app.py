import streamlit as st
import pandas as pd

st.set_page_config(page_title='Vision22 North America Growth Strategy Case Study', layout='wide')

st.title('Vision22 North America Growth Strategy Case Study')
st.subheader('USA & Canada B2B Market Entry | Pricing | Packages | SWOT Analysis')

st.markdown('''
## Positioning
Vision22 is positioned as a **B2B Growth Partner for North American Companies**.
The focus is not selling generic digital marketing services, but building growth systems:
- Lead Generation
- Digital Authority
- Performance Marketing
- Conversion Systems
''')

packages=pd.DataFrame([
['B2B Growth Foundation','$6K-$9K','$3K-$5K/mo','85%'],
['B2B Lead Generation Engine','$8K-$12K','$6K-$10K/mo','90%'],
['Digital Authority & Brand Growth','$12K-$20K','$7K-$12K/mo','75%'],
['Performance Growth System','$10K-$15K','$8K-$15K/mo','85%'],
['Complete B2B Growth Department','$20K-$35K','$15K-$25K/mo','65%']
],columns=['Package','Setup Price','Monthly Retainer','Success Opportunity'])

st.header('Package Strategy')
st.dataframe(packages,use_container_width=True)

st.header('Pricing Sensitivity Analysis')
pricing=pd.DataFrame([
['Current Premium Affordable Price','Balanced positioning','High trust'],
['30% Lower Price','Higher conversion potential','Maintain premium image'],
['50% Lower Price','Faster entry','Risk of weak positioning']
],columns=['Scenario','Impact','Risk'])
st.table(pricing)

st.header('SWOT Analysis')
col1,col2=st.columns(2)
with col1:
 st.success('Strengths\n\n- Long marketing experience\n- Integrated marketing capability\n- Strong creative production\n- Competitive global pricing')
 st.warning('Weaknesses\n\n- Limited North American awareness\n- Need more US case studies\n- Need local trust signals')
with col2:
 st.info('Opportunities\n\n- Manufacturing\n- B2B SaaS\n- Healthcare\n- Industrial companies')
 st.error('Threats\n\n- US agencies competition\n- Price competition\n- Wrong positioning')

st.header('90 Day Market Entry Plan')
st.write('''
1. Target 500-1000 high value B2B accounts.\n
2. Use B2B Growth Audit as entry offer.\n
3. Focus outreach on Manufacturing, SaaS and Healthcare.\n
4. Convert leads into Lead Generation Engine and Performance Growth System.\n''')

st.header('Revenue Scenarios')
rev=pd.DataFrame([
['Conservative','3 clients','$15K MRR'],
['Realistic','5 clients','$35K MRR'],
['Strong Execution','8 clients','$64K MRR']
],columns=['Scenario','Clients','Expected Revenue'])
st.table(rev)
