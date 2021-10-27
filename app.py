import streamlit as st
import streamlit.components.v1 as components



#liste der vars in session state


# mündlich:
# wie kann eine digitale technologie den Besuch eines Museums verändern?


#maybes:
#Python erklären
#

st.title('Visiting the Archaeological and the Orient Museums of Istanbul')


st.write('heckel 2006 button')
heckel = st.button('DOWNLOAD') #for heckel 2006
if heckel:
	st.write('''
		<https://www.academia.edu/45173283/Heckel_Mazaeus_and_Alexander_Sarcophagus>
		''')


choice = st.sidebar.selectbox('Go to', ['Home', 'Archaeological Museum', 'Ancient Orient Museum', 'Quiz'])


def home():
	st.image('main_entrance.jpg')

	st.write('Wiki')
	st.write('''
		<https://en.wikipedia.org/wiki/Istanbul_Archaeology_Museums>''')

	st.write('Description by muze.gen.tr')
	st.write('''
		<https://muze.gen.tr/muze-detay/arkeoloji>''')

	st.write('Description by Turkish Museums')
	st.write('''
		<https://www.turkishmuseums.com/museum/detail/2066-istanbul-archaeological-museums/2066/4>
		''')
	st.write('''
		<https://muze.gen.tr/c7/MysFileLibrary/d14b95a9-a09c-4b57-9fc7-ef690fb7d9a6.pdf>
		''')

	st.write('Statistics')
	st.write('''
		<https://kvmgm.ktb.gov.tr/TR-43336/muze-istatistikleri.html6>
		''')


	st.write('3d visit')
	st.write('''
		<https://sanalmuze.gov.tr/muzeler/ISTANBUL_ARKEOLOJI_MUZELERI/>''')


def archeo_mus():
	st.header('Archaeological Museum')

	st.subheader('Der Alexandersarkophag')
	render_3d('sarco.html')
	#show_source('sarco')

	def show_source(a_string):
		return False
		#if st.session_state('see_url'):
		#	pass

    
	st.subheader('I. Metadaten')
	st.subheader('II. Griechisch-römische Quellen')
	st.subheader('III. weiterführende Sekundärliteratur')

	# put best image here st.image()

	st.subheader('Varia')
	colc, cold = st.columns(2)
	with colc:
		st.write('premier groupe imgs')
		#st.image('')
	with cold:
		st.write('deuxieme groupe img')
		#st.image('')
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
	st.write('''
		Beschreibung:
		Provenienz:
		Datierung:

		''')
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
		#st.image('')
	with colb:
		st.write('deuxieme groupe img')
		#st.image('')

	with st.expander('more images'):
		st.write('https://commons.wikimedia.org/w/index.php?search=istanbul+ancient+orient+museum&title=Special:MediaSearch&go=Go&type=image')
	


def credits():
	col1, col2 = st.columns(2)
	with col1:
		st.write('made by Audric Wannaz and powered by Streamlit')
	with col2:
		st.image('unibas.png', width=60)
	with st.expander('more:'):
		st.write('All used media are under a (CC BY-SA 4.0) license or equivalent')
		see_url = st.button('Display url of all media?')
		if see_url:
			st.session_state.see_url = True

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')


	


	

	


	
	

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
