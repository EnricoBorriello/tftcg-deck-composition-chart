import streamlit as st
st.set_page_config(layout="wide")


import matplotlib.pyplot as plt
import numpy as np
import piechart as pc


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

	st.set_option('deprecation.showPyplotGlobalUse', False)
	chart = pc.deck_comp_chart('/Users/enrico/Desktop/tourn.pdf', 
		O = O,
		B = B,
		W = W,
		G = G,
		K = K,
		OO = OO,
		BB = BB,
		OB = OB,
		OG = OG,
		BG = BG,
		WG = WG,
		OK = OK,
		KB = KB,
		WK = WK,
		KG = KG,
		KK = KK,
		OKG = OKG,
		WOB = WOB,
		KKK = KKK,
		OKB = OKB,
		KKG = KKG,
		b   = b
		)	
	col_C.pyplot(chart)



	

















