import streamlit as st
import streamlit.components.v1 as components



#liste der vars in session state


# mündlich:
# wie kann eine digitale technologie den Besuch eines Museums verändern?


#maybes:
#Python erklären
#

def alex_sar_jstor():
	st.write('''
		<https://www.jstor.org/action/doBasicSearch?Query=alexander+sarcophagus&acc=on&wc=on&fc=off&group=none&refreqid=search%3Abdafc6066e6f6e7ad0ac2ff045a153a2&groupefq=WyJjb250cmlidXRlZF9pbWFnZXMiXQ%3D%3D&efqs=eyJjdHkiOlsiWTI5dWRISnBZblYwWldSZmFXMWhaMlZ6Il0sImNsYXNzaWZpY2F0aW9uIjpbXSwiY291bnRyeSI6W10sImNvbGxlY3Rpb25faWRzIjpbXX0%3D&pagemark=eyJwYWdlIjoxLCJzdGFydHMiOnsiSlNUT1JCYXNpYyI6MH19&searchkey=1635365138675>
		''')


st.title('Visiting the Archaeological and the Orient Museums of Istanbul')

def heckel_button():
	st.write('heckel 2006 button')
	heckel = st.button('DOWNLOAD') #for heckel 2006
	if heckel:
		st.write('''
			<https://www.academia.edu/45173283/Heckel_Mazaeus_and_Alexander_Sarcophagus>
			''')


choice = st.sidebar.selectbox('Go to', ['Home', 'Archaeological Museum', 'Ancient Orient Museum', 'Quiz'])


def home():
	st.image('main_entrance.jpg')

	if st.button('Wiki'):
		st.write('''
			<https://en.wikipedia.org/wiki/Istanbul_Archaeology_Museums>''')


		

	if st.button('Description by Turkish Museums Websites'):
		st.write('''
			<https://muze.gen.tr/muze-detay/arkeoloji>''')

		st.write('''<http://en.istanbul.gov.tr/museums-of-istanbul-istanbul-archaeological-museums>''')

		st.write('''
			<https://www.turkishmuseums.com/museum/detail/2066-istanbul-archaeological-museums/2066/4>
			''')
		st.write('''
			<https://muze.gen.tr/c7/MysFileLibrary/d14b95a9-a09c-4b57-9fc7-ef690fb7d9a6.pdf>
			''')

	if st.button('Statistics'):
		st.write('''
			<https://kvmgm.ktb.gov.tr/TR-43336/muze-istatistikleri.html6>
			''')


	if st.button('3d visit'):
		st.write('''
			<https://sanalmuze.gov.tr/muzeler/ISTANBUL_ARKEOLOJI_MUZELERI/>''')

	st.write('************')

def archeo_mus():
	st.write('************')
	st.title('Archaeological Museum')



	st.subheader('Der Alexandersarkophag')
	render_3d('sarco.html')
	#show_source('sarco')

	if st.button('JSTOR images (VPN may be required)'):
		alex_sar_jstor()

	def show_source(a_string):
		return False
		#if st.session_state('see_url'):
		#	pass

    

	st.subheader('I. Griechisch-römische Quellen')
	st.subheader('II. weiterführende Sekundärliteratur')

	# put best image here st.image()

	st.subheader('Varia')
	colc, cold = st.columns(2)
	with colc:
		st.write('premier groupe imgs')
		st.image('room6.jpg')
	with cold:
		st.write('deuxieme groupe img')
		st.image('baby_couple.jpg')
	render_3d('head.html')

	with st.expander('more images'):
		st.write('https://commons.wikimedia.org/w/index.php?search=istanbul+archaeology+museum&title=Special:MediaSearch&go=Go&type=image')
	

def render_3d(filename):
	HtmlFile = open(filename, 'r', encoding='utf-8')
	source_code = HtmlFile.read() 
	components.html(source_code)

def orient_mus():
	st.header('Ancient Orient Museum')

	st.subheader('The Ishtar Gate')
	st.image('ishtar.jpg')
	render_3d('gate.html')
	st.subheader('I. Metadaten')

	st.subheader('II. Griechisch-römische Quellen')
	
	with st.expander('Cyrus nimmt Babylon ein'):
		st.write('show passage hero')

	with st.expander('Vitruv zu den Ziegeln Babylons'):
		st.write('2 cols source et trad')

	st.subheader('III. weiterführende Sekundärliteratur')

	st.write('digitale rekonstruktion')

	st.subheader('Varia')
	cola, colb = st.columns(2)
	with cola:
		st.write('premier groupe imgs')
		st.image('double_sphinx.jpg')
		#st.image('mummy_thebes.jpg')
		#st.image('')
		st.image('knight.jpg')

	with colb:
		st.write('deuxieme groupe img')
		#st.image('')
		st.image('south_arabian.jpg')
		st.image('hand.jpg')

	with st.expander('more images'):
		st.write('https://commons.wikimedia.org/w/index.php?search=istanbul+ancient+orient+museum&title=Special:MediaSearch&go=Go&type=image')
	


def credits():
	col1, col2 = st.columns(2)
	with col1:
		st.write('made by Audric Wannaz and powered by Streamlit')
	with col2:
		st.image('unibas.png', width=60)
	with st.expander('more:'):
		st.write('All media used in the webapp are under a (CC BY-SA 4.0) license or equivalent')
		see_url = st.button('Display url of all media?')
		if see_url:
			st.session_state.see_url = True

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')


	
def ask_quiz():

# lisa question:

	st.write('the battle depicted in ___ is probably also to be seen on a mosaic in which house of Pompei?')
#choices:
#house of the faun>correct
#villa dei misteri
#house of the vettii
#house of the golden cupids
#house of the prince of naples


# stefania: 

	st.write('whats the name of the animal depicted')

#lahmassu
#chim(a)era
#gryffin
#unicorn
	

	


	
	

def main():
	if 'see_url' not in st.session_state:
		st.session_state['see_url'] = False
	if choice == 'Home':
		home()
	elif choice == 'Archaeological Museum':
		archeo_mus()
	elif choice == 'Ancient Orient Museum':
		orient_mus()
	else:
		st.error('Something went wrong')
	credits()

main()
