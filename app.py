import streamlit as st
import streamlit.components.v1 as components



#liste der vars in session state


# mündlich:
# wie kann eine digitale technologie den Besuch eines Museums verändern?


#maybes:
#Python erklären
#

def intro_streamlit():
	st.title('To navigate, use the sidebar to your left (cliking the arrow on the upper left expands it ).') 
	st.title('Click on the three lines at the upper right part of your screen to access the Settings')

def alex_sar_jstor():
	st.write('''
		<https://www.jstor.org/action/doBasicSearch?Query=alexander+sarcophagus&acc=on&wc=on&fc=off&group=none&refreqid=search%3Abdafc6066e6f6e7ad0ac2ff045a153a2&groupefq=WyJjb250cmlidXRlZF9pbWFnZXMiXQ%3D%3D&efqs=eyJjdHkiOlsiWTI5dWRISnBZblYwWldSZmFXMWhaMlZ6Il0sImNsYXNzaWZpY2F0aW9uIjpbXSwiY291bnRyeSI6W10sImNvbGxlY3Rpb25faWRzIjpbXX0%3D&pagemark=eyJwYWdlIjoxLCJzdGFydHMiOnsiSlNUT1JCYXNpYyI6MH19&searchkey=1635365138675>
		''')


st.title('Visiting the Archaeological and the Orient Museum of Istanbul')

def heckel_button():
	st.write('heckel 2006 button')
	heckel = st.button('DOWNLOAD') #for heckel 2006
	if heckel:
		st.write('''
			<https://www.academia.edu/45173283/Heckel_Mazaeus_and_Alexander_Sarcophagus>
			''')


choice = st.sidebar.selectbox('Go to', ['Home', 'Archaeological Museum', 'Ancient Orient Museum', 'Quiz'])


def home():

	intro_streamlit()

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

	if st.button('Plut.Alex. 33.3-33.5'):
		st.write('''
			<https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0007.tlg047.perseus-eng2:33.3-33.5?right=perseus-grc2>''')

	if st.button('Curt. 4.16.1-7'):
		st.write('''
			<https://scaife.perseus.org/reader/urn:cts:latinLit:phi0860.phi001.perseus-lat2:4.16.1-4.16.7?q=alexander&qk=form''')

	st.subheader('II. weiterführende Sekundärliteratur')

	with st.expander('Heckel 2006'):
		st.write('''Waldemar Heckel: "Mazaeus, Callisthenes and the Alexander Sarcophagus". Historia: Zeitschrift für Alte Geschichte (55,4) 2006, 385-396.''')
		st.write('''<http://www.jstor.org/stable/4436826>''')
	# put best image here st.image()

	st.subheader('Varia')

	#with st.expander('+'):
	colc, cold = st.columns(2)
	with colc:
		#st.write('premier groupe imgs')
		st.image('room6.jpg')
	with cold:
		#st.write('deuxieme groupe img')
		st.image('baby_couple.jpg')
	render_3d('head.html')

	with st.expander('more images'):
		st.write('https://commons.wikimedia.org/w/index.php?search=istanbul+archaeology+museum&title=Special:MediaSearch&go=Go&type=image')
	

def render_3d(filename):
	HtmlFile = open(filename, 'r', encoding='utf-8')
	source_code = HtmlFile.read() 
	components.html(source_code)

def orient_mus():
	st.title('Ancient Orient Museum')

	st.subheader('The Ishtar Gate')
	st.image('ishtar.jpg')
	render_3d('gate.html')
	st.subheader('I. Metadaten')

	st.subheader('II. Griechisch-römische Quellen')
	
	if st.button('Hdt. 1.190'):
		st.write('''
			<https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0016.tlg001.perseus-eng2:1.190>''')

	if st.button('Vitr. 1.5.8'):
		st.write('''
			<https://scaife.perseus.org/reader/urn:cts:latinLit:phi1056.phi001.perseus-lat1:1.5.8?q=babylon&qk=form&right=perseus-eng1>''')




	st.subheader('III. weiterführende Sekundärliteratur')

	with st.expander('Pedersén 2018'):
		st.write('''Olof Pedersén: "The Ishtar Gate Area in Babylon. From Old Documents to New Interpretations ina Digital Model". ZOrA (2018, 11), 160-178.''')
		st.write('''<https://www.academia.edu/38545436/The_Ishtar_Gate_Area_in_Babylon_From_Old_Documents_to_New_Interpretations_in_a_Digital_Model>''')

	with st.expander('Poster by Hedegard et al.'):
		st.write('''<https://www.academia.edu/25465550/Babylonian_Blues_Studying_the_blue_and_turquoise_green_glazes_of_the_Ishtar_Gate_and_the_Processional_Way>''')



	

	st.subheader('Varia')
	cola, colb = st.columns(2)
	with cola:
		#st.write('premier groupe imgs')
		st.image('double_sphinx.jpg')
		#st.image('mummy_thebes.jpg')
		#st.image('')
		st.image('knight.jpg')
		#render_3d('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Mummy_in_Istanbul_Archaeological_Museums.jpg/640px-Mummy_in_Istanbul_Archaeological_Museums.jpg')

	with colb:
		#st.write('deuxieme groupe img')
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
		see_url = st.button('+')
		if see_url:
			st.write('Images stem from wikimedia commons:')
			st.write('''<https://commons.wikimedia.org/wiki/Main_Page>''')
			st.write('3d Models stem from Sketchfab')
			st.write('''<https://sketchfab.com/>''')
			#st.session_state.see_url = True

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')


	
def ask_quiz():

	q2_options = ['Hephaestion','Alexander', 'Abdalonymus', 'we do not know']
	q3_options = ['weil Lysipp den Sarkophag als Hofkünstler erstellt hat', 'weil man ihn im Heiligtum des Alexanders gefunden hat', 'weil Attribute des Alexanders eindeutig erkennbar sind', 'weil er dort begraben war']
	q4_options = ['Dareios I.', 'Dareios II.', 'Dareios III.']
	q6_options = ['De ipso autem muro (...)', 'non enim (...)', 'sed ubi sunt (...)']
	answers = [1891, 'Abdalonymus','weil Attribute des Alexanders eindeutig erkennbar sind','Dareios III.', 'babylon', 'non enim (...)', 'house of the Faun','Mušḫuššu']
	q7_options = ['villa dei misteri', 'house of the Faun', 'house of the Vettii', 'house of the prince of Naples']
	q8_options = ['Unicorn', 'Mušḫuššu', 'Chimera', 'Griffin', 'Lamassu']
#eig faslsch nicht lamassu
	with st.form('form_quiz'):
		st.image('ishtar.jpg')
		q8 = st.radio('Wie wird dieses Tier genannt?', q8_options)
		q1 = st.number_input('1. Wann wurde das archäologische Museum gegründet?', 1700)
		q2 = st.radio('2. Wer liegt im Alexander Sarkophag (laut Heckel 2006)', q2_options)
		q3 = st.radio('3. Warum wird der Sarkophag mit Alexander d.G. in Verbindung gebracht?', q3_options)
		q4 = st.radio('4. Welcher Dareios flieht vor Alexander in der Stelle von Plutarch?', q4_options)
		q5 = st.text_input('5. Wo stand das Ischtar-Tor?').lower()
		q6 = st.radio('6. Welcher Satz des Vitruvs lehrt uns möglicherweise etwas über das Ischtar-Tor?', q6_options)
		st.write('''Eine Seite des Alexandersarkophages wird oft mit einer berühmten Schlacht in Verbindung gebracht.\n Eine Mosaik, die diese Schlacht darstellt, wurde in Pompeii gefunden.\n''')
		q7 = st.radio('''7. In welchem Haus?''', q7_options)

		sub = st.form_submit_button('CHECK ANSWERS')
		if sub:
			if [q1,q2,q3,q4,q5,q6,q7,q8] == answers:
				st.balloons()
				st.success('Correct!')
			else:
				st.error('Not quite, try again!') 



#1891

# lisa question:
#st.write('the battle depicted in ___ is probably also to be seen on a mosaic in which house of Pompei?')
#choices:
#house of the faun>correct
#villa dei misteri
#house of the vettii
#house of the golden cupids
#house of the prince of naples

# stefania: 
#st.write('whats the name of the animal depicted on the page')

#lahmassu
#chim(a)era
#gryffin
#unicorn
	


#laut heckel 2006, wer liegt im Alexander Sarkophag:

#warum wird der Sarkophag überhaupt mit Alexander d.G in verbindung gebracht?

#
#

#

#


def main():
	if 'see_url' not in st.session_state:
		st.session_state['see_url'] = False
	if choice == 'Home':
		home()
	elif choice == 'Archaeological Museum':
		archeo_mus()
	elif choice == 'Ancient Orient Museum':
		orient_mus()
	elif choice == 'Quiz':
		ask_quiz()
	else:
		st.error('Something went wrong')
	credits()

main()
