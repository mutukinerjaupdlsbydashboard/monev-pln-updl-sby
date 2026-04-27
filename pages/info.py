# INFO
import streamlit as st

# Render Halaman Info
def render_info():
    st.markdown("""
    <div class='page-header'>
        <h3 class='page-subtitle'>ℹ️ Informasi Sistem</h3>
        <p class='page-description'>Detail informasi mengenai Learning Insight</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <h4 style='margin-top: 0; color: #0078d4; margin-bottom: 15px;'>📶 Dashboard Learning Insight</h4>
        <p style='font-size: 0.9rem; line-height: 1.6;'>
            Sistem ini dikembangkan untuk mempermudah proses evaluasi dengan mengklasifikasikan sentimen, indikator, dan keluhan sehingga tim mutu dapat menambahkan file data dan 
            menganalisis data teks secara otomatis untuk memperoleh hasilnya dengan lebih cepat dan akurat.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <h4 style='color:#0078d4; margin-top:0; margin-bottom:18px;'>⚙️ Teknologi Sistem</h4>
        <div style='display:flex; flex-direction:column; gap:12px;'>
            <div style='background:rgba(0,120,212,0.05); padding:14px; border-radius:10px;'>
                <b>🧠 Sistem NLP</b><br>
                <small>
                Sistem NLP dibuat menggunakan algoritma <b>RoBERTa dan IndoBERT. Model yang dibuat memiliki akurasi rata-rata <b>97-99%</b> baik untuk klasifikasi Sentimen, Indikator, dan Keluhan.
                </small>
            </div>
            <div style='background:rgba(0,120,212,0.05); padding:14px; border-radius:10px;'>
                <b>🗂️ Kategori Sentimen, Indikator, dan Keluhan</b><br>
                <small>
                Sistem NLP mengklasifikasikan ulasan ke dalam <b>3</b> kategori sentimen <b>(Positif, Netral, Negatif)</b>, dengan tambahan kategori <b>Invalid</b> untuk kasus 
                tertentu sesuai kebutuhan. Selain itu, terdapat model klasifikasi untuk <b>16 kategori Indikator</b> serta <b>32 kategori Keluhan</b> yang merupakan sub-kategori dari indikator tersebut.
                </small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <h4 style='color: #0078d4; margin-top: 0; margin-bottom: 15px;'>👥 Tim</h4>
        <p><b>Divisi Evaluasi & Pengendalian Mutu dan Kinerja</b><br>PT PLN (Persero) UPDL Surabaya</p>
    </div>
    """, unsafe_allow_html=True)
