import streamlit as st

st.set_page_config(layout="wide")

if "kondisi" not in st.session_state:
    st.session_state.kondisi={'kondisi1': True, 'kondisi2':False, 'kondisi3':False,
                              'kondisi4':False, 'kondisi5':False, 'kondisi6':False,
                              'kondisi7':False,'kondisi8':False,'kondisi9': False}

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
def materi3():
    kolom2 = st.tabs(['Jenjang SMP','Jenjang SMA'])
    with kolom2[0]:
        st.markdown('''
    <iframe src="https://martin-bernard26.github.io/mediaPBI/IntegrasiPsiKur.html" style="width:100%;height:2300px"></iframe>
    ''',unsafe_allow_html=True)
    with kolom2[1]:
        st.markdown('''
    <iframe src="https://martin-bernard26.github.io/mediaPBI/KurikulumSMA.html" style="width:100%;height:2300px"></iframe>
    ''',unsafe_allow_html=True)
def materi4():
    kolom1 = st.tabs(['Materi SD','Materi SMP','Materi SMA'])
    with kolom1[0]:
        st.markdown('''
        <iframe src="https://martin-bernard26.github.io/mediaPBI/materiSD.html" style="width:100%;height:3000px"></iframe>
        ''',unsafe_allow_html=True)
    with kolom1[1]:
        st.markdown('''
        <iframe src="https://martin-bernard26.github.io/mediaPBI/materiSMP.html" style="width:100%;height:2300px"></iframe>
        ''',unsafe_allow_html=True)
    with kolom1[2]:
        st.markdown('''
        <iframe src="https://martin-bernard26.github.io/mediaPBI/materiSMA.html" style="width:100%;height:2300px"></iframe>
        ''',unsafe_allow_html=True)
def materi5():
    st.markdown('''
        <iframe src="https://martin-bernard26.github.io/mediaPBI/kognitif1kur.html" style="width:100%;height:2300px"></iframe>
        ''',unsafe_allow_html=True)
def materi6():
    st.markdown('''
        <iframe src="https://martin-bernard26.github.io/mediaPBI/kurikulumSkr.html" style="width:100%;height:2300px"></iframe>
        ''',unsafe_allow_html=True)
def materi7():
    st.markdown('''
        <iframe src="https://drive.google.com/file/d/1Ni9P3uIN5kW5LEhyKOdO0tBlVzJT7WNx/preview" style="width:100%;height:2300px"></iframe>
        ''',unsafe_allow_html=True)
# =======================================
if st.session_state.kondisi['kondisi2']:
    materi1()
if st.session_state.kondisi['kondisi3']:
    materi2()
if st.session_state.kondisi['kondisi4']:
    ujianTest()
if st.session_state.kondisi['kondisi5']:
    materi3()
if st.session_state.kondisi['kondisi6']:
    materi4()
if st.session_state.kondisi['kondisi7']:
    materi5()
if st.session_state.kondisi['kondisi8']:
    materi6()
if st.session_state.kondisi['kondisi9']:
    materi7()
#=============================================
if st.sidebar.button('Beranda'):
    st.session_state.kondisi={'kondisi1': True, 'kondisi2':False, 'kondisi3':False,
                              'kondisi4':False, 'kondisi5':False, 'kondisi6':False,
                              'kondisi7':False, 'kondisi8':False, 'kondisi9': False}
    st.rerun()

if st.sidebar.button('Kumpulan Tugas dan UTS dan UAS'):
    st.session_state.kondisi={'kondisi1': False, 'kondisi2':False, 'kondisi3':False,
                              'kondisi4':True, 'kondisi5':False, 'kondisi6':False,
                              'kondisi7':False, 'kondisi8':False, 'kondisi9': False}
    st.rerun()

if st.sidebar.button('Psikologi Pendidikan'):
    st.session_state.kondisi={'kondisi1': False, 'kondisi2':True, 'kondisi3':False,
                              'kondisi4':False, 'kondisi5':False, 'kondisi6':False,
                              'kondisi7':False, 'kondisi8':False, 'kondisi9': False}
    st.rerun()

if st.sidebar.button('Teori-teori Psikologi Pendidikan'):
    st.session_state.kondisi={'kondisi1': False, 'kondisi2':False, 'kondisi3':True,
                              'kondisi4':False, 'kondisi5':False, 'kondisi6':False,
                              'kondisi7':False, 'kondisi8':False, 'kondisi9': False}
    st.rerun()
if st.sidebar.button('Materi Bahasa Indonesia'):
    st.session_state.kondisi={'kondisi1': False, 'kondisi2':False, 'kondisi3':False,
                              'kondisi4':False, 'kondisi5':False, 'kondisi6':True,
                              'kondisi7':False, 'kondisi8':False, 'kondisi9': False}
    st.rerun()

if st.sidebar.button('Kurikulum Pembelajaran berdasarkan Psikologi'):
    st.session_state.kondisi={'kondisi1': False, 'kondisi2':False, 'kondisi3':False,
                              'kondisi4':False, 'kondisi5':True, 'kondisi6':False,
                              'kondisi7':False, 'kondisi8':False, 'kondisi9': False}
    st.rerun()
if st.sidebar.button('Kurikulum Pembelajaran berdasarkan Psikologi Kognitif'):
    st.session_state.kondisi={'kondisi1': False, 'kondisi2':False, 'kondisi3':False,
                              'kondisi4':False, 'kondisi5':False, 'kondisi6':False,
                              'kondisi7':True, 'kondisi8':False, 'kondisi9': False}
    st.rerun()
if st.sidebar.button('Kurikulum Bahasa Indonesia saat ini'):
    st.session_state.kondisi={'kondisi1': False, 'kondisi2':False, 'kondisi3':False,
                              'kondisi4':False, 'kondisi5':False, 'kondisi6':False,
                              'kondisi7':False, 'kondisi8':True, 'kondisi9': False}
    st.rerun()
if st.sidebar.button('Soal UAS'):
    st.session_state.kondisi={'kondisi1': False, 'kondisi2':False, 'kondisi3':False,
                              'kondisi4':False, 'kondisi5':False, 'kondisi6':False,
                              'kondisi7':False, 'kondisi8':False, 'kondisi9':True}
    st.rerun()
