import streamlit as st

st.set_page_config(layout="wide")

if "kondisi" not in st.session_state:
    st.session_state.kondisi={'kondisi1': True, 'kondisi2':False, 'kondisi3':False,
                              'kondisi4':False, 'kondisi5':False, 'kondisi6':False}

# ====================================
def materi1():
    st.markdown('''
    <iframe src="https://martin-bernard26.github.io/mediaPBI/materi2.html" style="width:100%;height:4000px"></iframe>
    ''',unsafe_allow_html=True)

def materi2():
    st.markdown('''
    <iframe src="https://martin-bernard26.github.io/mediaPBI/materi3c.html" style="width:100%;height:4000px"></iframe>
    ''',unsafe_allow_html=True)

if st.session_state.kondisi['kondisi1']:
    st.markdown('''
    <iframe src="https://martin-bernard26.github.io/mediaPBI/kover.html" style="width:100%;height:600px"></iframe>
    ''',unsafe_allow_html=True)
def ujianTest():
    st.markdown('''
    <iframe src="https://martin-bernard26.github.io/mediaPBI/tugas.html" style="width:100%;height:600px"></iframe>
    ''',unsafe_allow_html=True)
# =======================================
if st.session_state.kondisi['kondisi2']:
    materi1()
if st.session_state.kondisi['kondisi3']:
    materi2()
if st.session_state.kondisi['kondisi4']:
    ujianTest()
#=============================================
if st.sidebar.button('Beranda'):
    st.session_state.kondisi={'kondisi1': True, 'kondisi2':False, 'kondisi3':False,
                              'kondisi4':False, 'kondisi5':False, 'kondisi6':False}
    st.rerun()

if st.sidebar.button('Kumpulan Tugas dan UTS dan UAS'):
    st.session_state.kondisi={'kondisi1': False, 'kondisi2':False, 'kondisi3':False,
                              'kondisi4':True, 'kondisi5':False, 'kondisi6':False}
    st.rerun()

if st.sidebar.button('Psikologi Pendidikan'):
    st.session_state.kondisi={'kondisi1': False, 'kondisi2':True, 'kondisi3':False,
                              'kondisi4':False, 'kondisi5':False, 'kondisi6':False}
    st.rerun()

if st.sidebar.button('Teori-teori Psikologi Pendidikan'):
    st.session_state.kondisi={'kondisi1': False, 'kondisi2':False, 'kondisi3':True,
                              'kondisi4':True, 'kondisi5':False, 'kondisi6':False}
    st.rerun()
