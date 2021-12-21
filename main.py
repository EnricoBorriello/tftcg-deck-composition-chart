import streamlit as st
st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', True)

import matplotlib.pyplot as plt
import numpy as np



composition = st.container()

with composition:

	st.title('Deck Composition Chart')
	st.markdown("by **Computron's Lab**")

	N = 40
	col_A, col_B, col_C = st.columns(3)

	O = col_A.slider('orange',min_value=0,max_value=N,key='orange-O')
	B = col_A.slider('blue',min_value=0,max_value=N)
	W = col_A.slider('white',min_value=0,max_value=N)
	G = col_A.slider('green',min_value=0,max_value=N)
	K = col_A.slider('black',min_value=0,max_value=N)

	OO = col_A.slider('orange + orange',min_value=0,max_value=N)
	BB = col_A.slider('blue   + blue',min_value=0,max_value=N)
	OB = col_A.slider('orange + blue',min_value=0,max_value=N)
	
	OG = col_A.slider('orange + green',min_value=0,max_value=N)
	BG = col_A.slider('blue + green',min_value=0,max_value=N)
	WG = col_A.slider('white   + green',min_value=0,max_value=N)

	OK = col_B.slider('orange + black',min_value=0,max_value=N)
	KB = col_B.slider('black   + blue',min_value=0,max_value=N)
	WK = col_B.slider('white   + black',min_value=0,max_value=N)
	KG = col_B.slider('black   + green',min_value=0,max_value=N)
	KK = col_A.slider('black   + black',min_value=0,max_value=N)

	OKG = col_B.slider('orange + black + green',min_value=0,max_value=N)
	WOB = col_B.slider('white + orange + blue',min_value=0,max_value=N)
	KKK = col_B.slider('black + black + black',min_value=0,max_value=N)
	OKB = col_B.slider('orange + black + blue',min_value=0,max_value=N)
	KKG = col_B.slider('black + black + green',min_value=0,max_value=N)
	b   = col_B.slider('blank',min_value=0,max_value=N)

	
def icon_color(icon):
    if icon == 'b':
        return 'gainsboro'
    if icon == 'W':
        return 'whitesmoke'
    if icon == 'O':
        return 'orange'
    if icon == 'B':
        return 'dodgerblue'
    if icon == 'G':
        return 'yellowgreen'    
    if icon == 'K':
        return 'dimgray'


    
composition = {
# single icon
	'W':W,'O':O,'B':B,'G':G,'K':K,   
# 2 icons
	'OO':OO,
	'OB':OB,'BB':BB,              
	'OG':OG,'BG':BG,'WG':WG,    
	'OK':OK,'KB':KB,'WK':WK,'KG':KG,'KK':KK,   
# 3 icons  
	'WOB':WOB,
	'OKG':OKG,
	'OKB':OKB,
	'KKK':KKK,
	'KKG':KKG,
#no icons
	'b':b
	}
    
# Preferred Sorting
all_icons = [
'O','B','W','G','K',
'OO',
'BB','OB',
'OG','BG','WG',
'OK','KB','WK','KG','KK',    
'OKG','WOB','KKK','OKB', 'KKG',
'b'
]

# Alternatively, Authomatic Sorting:
#all_icons = composition.keys()
    
icons = []
for i in range(len(all_icons)):
	if composition[all_icons[i]] > 0:
		icons.append(all_icons[i])  

# CHART DEFINITION:

fig, ax = plt.subplots()

#fig.patch.set_visible(False)
ax.axis('off')

ax = plt.axes( [0.25,0.025,0.95,0.95],polar=True)

ax.set_facecolor('gainsboro')

size = sum(composition.values())

# Inner Ring (1st icon, if any)

width = []
theta = []
radii = []
bars = []

for i in range(len(icons)):
	if composition[icons[i]] >= 0:
		wdt = 2*np.pi*composition[icons[i]]/size
		width.append(wdt)
		center = 2*np.pi*sum([composition[icons[j]] for j in range(i)])/size
		shift = wdt/2
		theta.append(center+shift)
		radii.append(1)
		plt.plot([center,center],[1,4],c='white')
		plt.text(center+shift, 3.8, str(composition[icons[i]]),horizontalalignment='center',verticalalignment='center',fontsize=12, color='black')
 
bars1 = plt.bar(theta, radii, width=width, bottom=1)

for i in range(len(icons)):
	bars1[i].set_facecolor(icon_color(icons[i][0]))

    # Middle Ring (2st icon, if any)
    
width = []
theta = []
radii = []
bars = []

for i in range(len(icons)):
	if len(icons[i]) >= 2 and composition[icons[i]] > 0:
		wdt = 2*np.pi*composition[icons[i]]/size
		width.append(wdt)
		center = 2*np.pi*sum([composition[icons[j]] for j in range(i)])/size
		theta.append(center+shift)
		radii.append(1)
        
bars2 = plt.bar(theta, radii, width=width, bottom=2)

icons2 = []
for i in range(len(icons)):
	if len(icons[i]) >= 2 and composition[icons[i]] > 0:
		icons2.append(icons[i])

for i in range(len(icons2)):
	bars2[i].set_facecolor(icon_color(icons2[i][1]))

    # Outher Ring (3rd icon, if any)
    
width = []
theta = []
radii = []
bars = []

for i in range(len(icons)):
	if len(icons[i]) == 3 and composition[icons[i]] > 0:
		wdt = 2*np.pi*composition[icons[i]]/size
		width.append(wdt)
		center = 2*np.pi*sum(
			[composition[icons[j]] for j in range(i)])/size
		shift = wdt/2
		theta.append(center+shift)
		radii.append(1)
        
bars3 = plt.bar(theta, radii, width=width, bottom=3)

icons3 = []

for i in range(len(icons)):
	if len(icons[i]) == 3 and composition[icons[i]] > 0:
		icons3.append(icons[i])

for i in range(len(icons3)):
	bars3[i].set_facecolor(icon_color(icons3[i][2]))

lines, labels = plt.thetagrids([(360./size)*i for i in range(size)], [])
lines, labels = plt.rgrids([1,2,3,4], [])
ax.grid(linewidth=1.4,c='gainsboro')

ax.text(0.5, 0.515, str(size),horizontalalignment='center',verticalalignment='center',fontsize=16, color='black',transform=ax.transAxes )

ax.text(0.5, 0.465, 'cards',horizontalalignment='center',verticalalignment='center',fontsize=9, color='black',transform=ax.transAxes )

col_C.pyplot(fig)










